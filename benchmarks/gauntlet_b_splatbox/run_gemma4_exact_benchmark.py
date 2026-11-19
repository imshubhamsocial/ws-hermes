import json, os, subprocess, sys, time; from pathlib import Path
BENCH = Path(__file__).resolve().parent; OUT = BENCH / "output"; sys.path.insert(0, str(OUT))
sys.path.insert(0, str(BENCH)); from splatbox_agent import run_splatbox_match; from video_composer import compose_split

def ensure_chrome():
    for _ in range(5):
        if subprocess.run("curl -sf http://127.0.0.1:9222/json/version", shell=True, capture_output=True).returncode == 0: return
        subprocess.run(["bash", str(BENCH / "launch_chrome.sh")]); time.sleep(1)

def ensure_server():
    if subprocess.run("curl -sf http://127.0.0.1:8138/health", shell=True, capture_output=True).returncode != 0:
        subprocess.run(["bash", str(BENCH / "server_manager.sh"), "start"], check=True)

def run_gemma():
    OUT.mkdir(exist_ok=True); (BENCH / "stages/03-execute/output").mkdir(parents=True, exist_ok=True)
    ensure_server()
    vram = subprocess.check_output("nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits", shell=True, text=True).split()[0] + " MiB"
    sp = subprocess.run(["python3", str(BENCH.parents[1] / "_tools/benchmark_speed.py"), "120", "0.2", "0.95"], capture_output=True, text=True)
    print(f"[gemma4_exact] Speed: {sp.stdout.strip()}")
    raw_vid, fin_vid = OUT / "raw_splatbox_gemma4_exact.mp4", OUT / "splatbox_gemma4_exact.mp4"
    os.environ["RECORD_VIDEO_PATH"], os.environ["PROOF_VIDEO_NAME"] = str(raw_vid), fin_vid.name
    for f in [OUT / "telemetry.json", BENCH / "stages/03-execute/output/telemetry.json", raw_vid]: f.unlink(missing_ok=True)
    ensure_chrome(); res = run_splatbox_match(); sc = res.get("score", 0)
    compose_split(raw_vid, fin_vid, "Google Gemma 4 Exact 4B (MTP)", "128k (TurboQuant MTP)", vram, sc)
    (OUT / "telemetry_gemma4_exact.json").write_text(Path(OUT / "telemetry.json").read_text())
    subprocess.run(["bash", str(BENCH / "contract.sh")], check=True)
    print(f"\n=== [GEMMA 4 EXACT BENCHMARK COMPLETE: Score={sc}, VRAM={vram}] ===")

if __name__ == "__main__": run_gemma()
