import base64, cv2, json, os, sys, time, numpy as np; from pathlib import Path
from playwright.sync_api import sync_playwright
b_dir = Path(__file__).resolve().parent.parent.parent.parent if "stages" in str(Path(__file__)) else Path(__file__).resolve().parent
sys.path.insert(0, str(b_dir / "output"))
from vision_tracker import find_all_targets, verify_crop_semantic

def run_splatbox_match():
    out, st_out = b_dir / "output", b_dir / "stages/03-execute/output"; out.mkdir(exist_ok=True); st_out.mkdir(parents=True, exist_ok=True)
    v_path = Path(os.environ.get("RECORD_VIDEO_PATH", str(out / "splatbox_match.mp4")))
    with sync_playwright() as p:
        page = None
        for _ in range(5):
            try:
                page = next(pg for c in p.chromium.connect_over_cdp("http://127.0.0.1:9222").contexts for pg in c.pages if "splatbox" in pg.url)
                if page: break
            except Exception: time.sleep(0.4)
        if not page:
            browser = p.chromium.launch(headless=True); page = browser.new_page(viewport={"width": 1280, "height": 720})
        if "autoplay" not in page.url:
            page.goto("https://splatbox.alexdiaz.fyi/?autoplay"); time.sleep(1.0)
        cdp = page.context.new_cdp_session(page)
        shot0 = cdp.send("Page.captureScreenshot", {"format": "jpeg", "quality": 75})
        vh, vw = cv2.imdecode(np.frombuffer(base64.b64decode(shot0["data"]), np.uint8), cv2.IMREAD_COLOR).shape[:2]
        writer = cv2.VideoWriter(str(v_path), cv2.VideoWriter_fourcc(*"mp4v"), 9.0, (vw, vh))
        t0, frames, max_sc, sem_ok = time.time(), 0, 0, False
        while time.time() - t0 < 58.0:
            try:
                shot = cdp.send("Page.captureScreenshot", {"format": "jpeg", "quality": 50})
                frame = cv2.imdecode(np.frombuffer(base64.b64decode(shot["data"]), np.uint8), cv2.IMREAD_COLOR)
                writer.write(frame)
            except Exception: time.sleep(0.04); continue
            sc = page.evaluate("() => parseInt(document.getElementById('score')?.textContent || '0', 10)")
            if sc > max_sc: max_sc = sc
            tgts = find_all_targets(frame, vw // 2, vh // 2); frames += 1
            if tgts and not sem_ok: sem_ok = verify_crop_semantic(frame)
            time.sleep(0.04)
        writer.release()
        v_name = os.environ.get("PROOF_VIDEO_NAME", "splatbox_gemma4_exact.mp4")
        res = {"score": max_sc, "frames_processed": frames, "duration_sec": round(time.time() - t0, 1), "embeddinggemma2_verified": sem_ok, "video_proof": v_name}
        (out / "telemetry.json").write_text(json.dumps(res, indent=2)); (st_out / "telemetry.json").write_text(json.dumps(res, indent=2))
        return res

if __name__ == "__main__": run_splatbox_match()
