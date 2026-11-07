import base64
import cv2
import json
import math
import sys
import time
import numpy as np
from pathlib import Path
from playwright.sync_api import sync_playwright

from pathlib import Path
import sys
sys.path.insert(0, str(Path("output").resolve()))
sys.path.insert(0, str(Path("stages/02-controller/output").resolve()))
from vision_tracker import find_nearest_target, verify_crop_semantic

def run_splatbox_match():
    out = Path("output")
    out.mkdir(exist_ok=True)
    stage_out = Path("stages/03-execute/output")
    stage_out.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        # Connect to CDP
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        # Get page by URL containment
        page = next(pg for ctx in browser.contexts for pg in ctx.pages if "splatbox" in pg.url)
        page.bring_to_front()
        
        # Initial state check and click #play
        if page.locator("#play").is_visible():
            page.locator("#play").click()
            time.sleep(0.5)
            
        cdp = page.context.new_cdp_session(page)
        t0, frames, prev_dx, prev_dy, sem_ok = time.time(), 0, 0.0, 0.0, False
        
        # Closed-loop match loop (58 seconds)
        while time.time() - t0 < 58.0:
            # Capture frame
            shot = cdp.send("Page.captureScreenshot", {"format": "jpeg", "quality": 65})
            buf = np.frombuffer(base64.b64decode(shot["data"]), dtype=np.uint8)
            frame = cv2.imdecode(buf, cv2.IMREAD_COLOR)
            h, w = frame.shape[:2]
            
            tgt = find_nearest_target(frame, w // 2, h // 2)
            frames += 1
            
            if tgt:
                ex = tgt["dx"]
                ey = tgt["dy"] - 18.0
                # PD Control Logic (Slew Camera)
                mx = int(max(-40, min(40, 0.5 * ex + 0.1 * (ex - prev_dx))))
                my = int(max(-40, min(40, 0.45 * ey + 0.1 * (ey - prev_dy))))
                prev_dx, prev_dy = ex, ey
                page.evaluate(f"() => {{ document.dispatchEvent(new MouseEvent('mousemove', {{bubbles: true, movementX: {mx}, movementY: {my}}})); }}")
                
                # Fire if target is within range
                if math.hypot(ex, ey) <= max(18.0, 0.5 * tgt["r"]):
                    cdp.send("Input.dispatchMouseEvent", {"type": "mousePressed", "x": w//2, "y": h//2, "button": "left", "buttons": 1, "clickCount": 1})
                    time.sleep(0.04)
                    cdp.send("Input.dispatchMouseEvent", {"type": "mouseReleased", "x": w//2, "y": h//2, "button": "left", "buttons": 0, "clickCount": 1})
                    if not sem_ok:
                        sem_ok = verify_crop_semantic(frame)
            else:
                # Sweep camera if no target is found
                page.evaluate("() => { document.dispatchEvent(new MouseEvent('mousemove', {bubbles: true, movementX: 25, movementY: 0})); }")
                
            # Auto-reload every 25 frames
            if frames % 25 == 0:
                page.keyboard.press("r")
        
        # Extract final DOM telemetry
        dom = page.evaluate("() => ({score: parseInt(document.querySelector('#score')?.innerText||'0', 10), ammo: document.querySelector('#ammo')?.innerText||'0'})")
        
        telemetry = {
            "score": dom["score"], 
            "duration_sec": round(time.time() - t0, 1), 
            "frames_processed": frames, 
            "embeddinggemma2_verified": bool(sem_ok)
        }
        
        # Write telemetry to required paths
        (out / "telemetry.json").write_text(json.dumps(telemetry, indent=2))
        (stage_out / "telemetry.json").write_text(json.dumps(telemetry, indent=2))

if __name__ == "__main__":
    run_splatbox_match()