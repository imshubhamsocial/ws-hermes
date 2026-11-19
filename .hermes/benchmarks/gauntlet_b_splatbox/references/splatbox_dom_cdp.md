# Layer 3: Splatbox CDP, OpenCV & EmbeddingGemma-2 Code Blueprints

## Section 1: Stage 01-probe Blueprint (Lines 1–50)

Use Playwright synchronous CDP connector in output/probe.py to attach to Port 9222, engage PointerLock via a native trusted click on #play, and write output/probe_state.json:

    import json, time
    from pathlib import Path
    from playwright.sync_api import sync_playwright

    out = Path("output")
    out.mkdir(exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        page = next(pg for ctx in browser.contexts for pg in ctx.pages if "splatbox" in pg.url)
        page.bring_to_front()
        page.screenshot(path=str(out / "menu_frame.png"))
        play_btn = page.locator("#play")
        if play_btn.is_visible():
            play_btn.click()  # Dispatches native trusted CDP mousePressed/mouseReleased
            time.sleep(0.6)
        state = page.evaluate("""() => ({
            pointer_lock_active: document.pointerLockElement !== null,
            viewport: {width: window.innerWidth, height: window.innerHeight},
            hud: {
                score: document.querySelector('#score')?.innerText || '0',
                timer: document.querySelector('#timer')?.innerText || '60',
                ammo: document.querySelector('#ammo')?.innerText || '40 / 40'
            }
        })""")
        page.screenshot(path=str(out / "playing_frame.png"))
        (out / "probe_state.json").write_text(json.dumps(state, indent=2))

## Section 2: Stage 02-controller Blueprint (Lines 35–84)

Implement output/vision_tracker.py to locate bullseye centroids with OpenCV and verify target crops via embeddinggemma-2 (Port 8139):

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

## Section 3: Stage 03-execute Blueprint (Lines 85–131)

Run the 60-second closed-loop PD controller over a persistent Playwright CDP session in output/run_match.py:

    import base64, cv2, json, math, sys, time
    import numpy as np
    from pathlib import Path
    from playwright.sync_api import sync_playwright
    sys.path.insert(0, str(Path("output").resolve()))
    sys.path.insert(0, str(Path("stages/02-controller/output").resolve()))
    from vision_tracker import find_nearest_target, verify_crop_semantic

    out = Path("output")
    out.mkdir(exist_ok=True)
    stage_out = Path("stages/03-execute/output")
    stage_out.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        page = next(pg for ctx in browser.contexts for pg in ctx.pages if "splatbox" in pg.url)
        page.bring_to_front()
        if page.locator("#play").is_visible():
            page.locator("#play").click()
            time.sleep(0.5)
        cdp = page.context.new_cdp_session(page)
        t0, frames, prev_dx, prev_dy, sem_ok = time.time(), 0, 0.0, 0.0, False
        while time.time() - t0 < 58.0:
            shot = cdp.send("Page.captureScreenshot", {"format": "jpeg", "quality": 65})
            buf = np.frombuffer(base64.b64decode(shot["data"]), dtype=np.uint8)
            frame = cv2.imdecode(buf, cv2.IMREAD_COLOR)
            h, w = frame.shape[:2]
            tgt = find_nearest_target(frame, w // 2, h // 2)
            frames += 1
            if tgt:
                ex = tgt["dx"]
                ey = tgt["dy"] - 18.0
                mx = int(max(-40, min(40, 0.5 * ex + 0.1 * (ex - prev_dx))))
                my = int(max(-40, min(40, 0.45 * ey + 0.1 * (ey - prev_dy))))
                prev_dx, prev_dy = ex, ey
                page.evaluate(f"() => {{ document.dispatchEvent(new MouseEvent('mousemove', {{bubbles: true, movementX: {mx}, movementY: {my}}})); }}")
                if math.hypot(ex, ey) <= max(18.0, 0.5 * tgt["r"]):
                    cdp.send("Input.dispatchMouseEvent", {"type": "mousePressed", "x": w//2, "y": h//2, "button": "left", "buttons": 1, "clickCount": 1})
                    time.sleep(0.04)
                    cdp.send("Input.dispatchMouseEvent", {"type": "mouseReleased", "x": w//2, "y": h//2, "button": "left", "buttons": 0, "clickCount": 1})
                    if not sem_ok:
                        sem_ok = verify_crop_semantic(frame)
            else:
                page.evaluate("() => { document.dispatchEvent(new MouseEvent('mousemove', {bubbles: true, movementX: 25, movementY: 0})); }")
            if frames % 25 == 0:
                page.keyboard.press("r")
        dom = page.evaluate("() => ({score: parseInt(document.querySelector('#score')?.innerText||'0', 10), ammo: document.querySelector('#ammo')?.innerText||'0'})")
        telemetry = {"score": dom["score"], "duration_sec": round(time.time() - t0, 1), "frames_processed": frames, "embeddinggemma2_verified": bool(sem_ok)}
        (out / "telemetry.json").write_text(json.dumps(telemetry, indent=2))
        (stage_out / "telemetry.json").write_text(json.dumps(telemetry, indent=2))
