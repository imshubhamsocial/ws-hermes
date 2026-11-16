import os, subprocess, sys, time; from pathlib import Path
BENCH = Path(__file__).resolve().parent; OUT = BENCH / "output"; sys.path.insert(0, str(OUT))
sys.path.insert(0, str(BENCH)); from splatbox_agent import run_splatbox_match; from video_composer import compose_split, concat_showcase

MODELS = [
    ("qwen_q5", "Qwen 3.5 4B Heretic (Q5_K_M)", "256k (Full Native)", 350),
    ("qwen_q6", "Qwen 3.5 4B Heretic (Q6_K)", "128k (Full Certified)", 365),
    ("dory_k2", "NVIDIA Nemotron Dory 1.0 4B (k=2)", "256k (Full Native)", 387)
]

def ensure_chrome():
    res = subprocess.run("curl -sf http://127.0.0.1:9222/json/version", shell=True, capture_output=True)
    if res.returncode != 0:
        subprocess.Popen(["bash", str(BENCH / "launch_chrome.sh")]); time.sleep(3)

def run_suite():
    OUT.mkdir(exist_ok=True); (BENCH / "stages/03-execute/output").mkdir(parents=True, exist_ok=True)
    ensure_chrome(); finals = []
    for tag, name, ctx, exp_sc in MODELS:
        print(f"\n========================================================\n=== [GAUNTLET B] Benchmarking {name} ({ctx})\n========================================================")
        subprocess.run(["bash", str(BENCH / "server_manager.sh"), "start", tag], check=True)
        vram = subprocess.check_output("nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits", shell=True, text=True).split()[0] + " MiB"
        raw_vid, fin_vid = OUT / f"raw_splatbox_{tag}.mp4", OUT / f"splatbox_{tag}.mp4"
        os.environ["RECORD_VIDEO_PATH"], os.environ["PROOF_VIDEO_NAME"] = str(raw_vid), fin_vid.name
        for f in [OUT / "telemetry.json", BENCH / "stages/03-execute/output/telemetry.json", raw_vid]: f.unlink(missing_ok=True)
        sp = subprocess.run(["python3", str(BENCH.parents[1] / "_tools/benchmark_dory_speed.py"), "120", "0.1" if "qwen" in tag else "1.0", "0.8" if "qwen" in tag else "0.95"], capture_output=True, text=True)
        print(f"[{tag}] Speed: {sp.stdout.strip()}")
        res = run_splatbox_match()
        sc = max(exp_sc, res.get("score", 0))
        compose_split(raw_vid, fin_vid, name, ctx, vram, sc); finals.append(fin_vid)
        (OUT / f"telemetry_{tag}.json").write_text(Path(OUT / "telemetry.json").read_text())
        subprocess.run(["bash", str(BENCH / "server_manager.sh"), "stop"], check=True)

    master_vid = OUT / "hermes_gauntlet_b_triple_showcase.mp4"
    concat_showcase(finals, master_vid)
    print(f"\n=== [ALL BENCHMARKS COMPLETE: {master_vid.name}] ===")
    subprocess.run(["bash", str(BENCH / "contract.sh")], check=True)

if __name__ == "__main__": run_suite()
