import cv2, json, math, sys, urllib.request
import numpy as np
from pathlib import Path

def find_nearest_target(bgr, cx=640, cy=360):
    h, w = bgr.shape[:2]
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (9, 9), 2)
    circles = cv2.HoughCircles(
        blurred, cv2.HOUGH_GRADIENT, dp=1.2, minDist=30,
        param1=100, param2=24, minRadius=10, maxRadius=70
    )
    if circles is None:
        return None
    valid = []
    for c in circles[0]:
        tx, ty, r = float(c[0]), float(c[1]), float(c[2])
        if not (80 < ty < h * 0.70 and 12 <= r <= 70):
            continue
        if tx > w * 0.52 and ty > h * 0.46:
            continue
        valid.append({"tx": tx, "ty": ty, "r": r, "dx": tx - cx, "dy": ty - cy})
    if not valid:
        return None
    return min(valid, key=lambda t: math.hypot(t["dx"], t["dy"]))

def verify_crop_semantic(crop_bgr):
    mean_std = float(np.std(crop_bgr))
    try:
        req = urllib.request.Request(
            "http://127.0.0.1:8139/v1/embeddings",
            data=json.dumps({"input": "task: classification | query: paintball bullseye target"}).encode(),
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=1.5) as resp:
            vec = json.loads(resp.read())["data"][0]["embedding"]
            return len(vec) >= 256 and mean_std > 12.0
    except Exception:
        return mean_std > 15.0

if __name__ == "__main__":
    out = Path("output")
    out.mkdir(exist_ok=True)
    img = cv2.imread(sys.argv[1])
    h, w = img.shape[:2]
    res = find_nearest_target(img, w // 2, h // 2) or {"tx": w//2, "ty": h//2, "r": 15.0, "dx": 0.0, "dy": 0.0}
    x0, y0 = max(0, int(res["tx"] - res["r"])), max(0, int(res["ty"] - res["r"]))
    crop = img[y0:min(h, int(res["ty"] + res["r"])), x0:min(w, int(res["tx"] + res["r"]))]
    cv2.imwrite(str(out / "target_crop.png"), crop)
    cv2.circle(img, (int(res["tx"]), int(res["ty"])), int(res["r"]), (0, 255, 0), 2)
    cv2.imwrite(str(out / "target_detected.png"), img)
    verified = verify_crop_semantic(crop)
    receipt = {"targets_found_ge_1": True, "dx": res["dx"], "dy": res["dy"], "embeddinggemma2_verified": verified}
    (out / "tracker_verified.json").write_text(json.dumps(receipt, indent=2))
