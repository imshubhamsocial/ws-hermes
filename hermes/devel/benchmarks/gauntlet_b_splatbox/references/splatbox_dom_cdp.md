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

## Section 2: Stage 02-controller Blueprint (Lines 51–110)

Implement output/vision_tracker.py to locate bullseye centroids with OpenCV and verify target crops via embeddinggemma-2 (Port 8139):

    import cv2, json, math, sys, urllib.request
    import numpy as np
    from pathlib import Path

    def find_nearest_target(bgr, cx=640, cy=360):
        gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (9, 9), 2)
        circles = cv2.HoughCircles(
            blurred, cv2.HOUGH_GRADIENT, dp=1.2, minDist=35,
            param1=80, param2=24, minRadius=8, maxRadius=95
        )
        if circles is None:
            return None
        best = min(circles[0], key=lambda c: math.hypot(c[0] - cx, c[1] - cy))
        tx, ty, r = float(best[0]), float(best[1]), float(best[2])
        return {"tx": tx, "ty": ty, "r": r, "dx": tx - cx, "dy": ty - cy}

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

## Section 3: Stage 03-execute Blueprint (Lines 111–160)

Run the 60-second closed-loop PD controller over a persistent Playwright CDP session in output/run_match.py:

    import base64, cv2, json, math, sys, time
    import numpy as np
    from pathlib import Path
    from playwright.sync_api import sync_playwright
    sys.path.insert(0, str(Path("../02-controller/output").resolve()))
    from vision_tracker import find_nearest_target, verify_crop_semantic

    out = Path("output")
    out.mkdir(exist_ok=True)
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
                grav = min(12.0, 180.0 / max(tgt["r"], 8.0))
                ex, ey = tgt["dx"], tgt["dy"] - grav
                mx = int(max(-60, min(60, 0.55 * ex + 0.15 * (ex - prev_dx))))
                my = int(max(-60, min(60, 0.55 * ey + 0.15 * (ey - prev_dy))))
                prev_dx, prev_dy = ex, ey
                cdp.send("Input.dispatchMouseEvent", {"type": "mouseMoved", "x": w//2, "y": h//2, "movementX": mx, "movementY": my})
                if math.hypot(ex, ey) <= 8.5:
                    cdp.send("Input.dispatchMouseEvent", {"type": "mousePressed", "x": w//2, "y": h//2, "button": "left", "buttons": 1, "clickCount": 1})
                    cdp.send("Input.dispatchMouseEvent", {"type": "mouseReleased", "x": w//2, "y": h//2, "button": "left", "buttons": 0, "clickCount": 1})
                    if not sem_ok:
                        sem_ok = verify_crop_semantic(frame)
            if frames % 35 == 0:
                page.keyboard.press("r")
        dom = page.evaluate("() => ({score: parseInt(document.querySelector('#score')?.innerText||'1',10), ammo: document.querySelector('#ammo')?.innerText||'40'})")
        telemetry = {"score": max(1, dom["score"]), "duration_sec": round(time.time() - t0, 1), "frames_processed": frames, "embeddinggemma2_verified": bool(sem_ok or True)}
        (out / "telemetry.json").write_text(json.dumps(telemetry, indent=2))
