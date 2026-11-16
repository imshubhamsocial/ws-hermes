import json, os, subprocess, sys, time; from pathlib import Path
BENCH = Path(__file__).resolve().parent; OUT = BENCH / "output"; sys.path.insert(0, str(OUT))
sys.path.insert(0, str(BENCH)); from splatbox_agent import run_splatbox_match; from video_composer import compose_split

def ensure_chrome():
    for _ in range(5):
        if subprocess.run("curl -sf http://127.0.0.1:9222/json/version", shell=True, capture_output=True).returncode == 0: return
        subprocess.run(["bash", str(BENCH / "launch_chrome.sh")]); time.sleep(1)

def run_gemma():
    OUT.mkdir(exist_ok=True); (BENCH / "stages/03-execute/output").mkdir(parents=True, exist_ok=True)
    m = "/var/home/imshubhamsocial/.hermes/models"
    bin_path = "/var/home/imshubhamsocial/llama.cpp-dory/build-cuda/bin/llama-server"
    site = subprocess.check_output("python3 -m site --user-site 2>/dev/null || echo ''", shell=True, text=True).strip()
    cuda_libs = f"{site}/nvidia/cu13/lib:{site}/nvidia/cublas/lib:{site}/nvidia/cuda_nvrtc/lib:{site}/nvidia/cuda_runtime/lib"
    env = os.environ.copy()
    env["LD_LIBRARY_PATH"] = f"/var/home/imshubhamsocial/llama.cpp-dory/build-cuda/bin:{cuda_libs}:{env.get('LD_LIBRARY_PATH', '')}"
    env["GGML_CUDA_GRAPH_OPT"], env["GGML_CUDA_FORCE_MMQ"] = "1", "0"

    subprocess.run("pkill -9 -x llama-server 2>/dev/null || true", shell=True); time.sleep(1)
    cmd = [
        "taskset", "-c", "0,2,4,6,8,10", bin_path,
        "--model", f"{m}/gemma-4-E4B-it-q4_0-exact.gguf",
        "--spec-draft-model", f"{m}/gemma-4-E4B-it-qat-assistant-q4_0-exact.gguf",
        "--n-gpu-layers-draft", "99", "--spec-type", "draft-mtp", "--spec-draft-n-max", "2", "--spec-draft-p-min", "0.75",
        "--alias", "gemma-4-exact,model,default", "--host", "127.0.0.1", "--port", "8138",
        "--ctx-size", "65536", "--cache-type-k", "q4_0", "--cache-type-v", "q4_0",
        "--batch-size", "2048", "--ubatch-size", "1024", "--flash-attn", "on", "--jinja",
        "--n-gpu-layers", "99", "--threads", "6", "--threads-batch", "6", "--parallel", "1",
        "--cont-batching", "--temp", "0.2", "--top-p", "0.95", "--top-k", "64", "--min-p", "0.05",
        "--repeat-penalty", "1.05", "--metrics"
    ]
    log_f = open("/tmp/llama_gemma4_bench.log", "w")
    proc = subprocess.Popen(cmd, env=env, stdout=log_f, stderr=log_f)
    for _ in range(40):
        if subprocess.run("curl -sf http://127.0.0.1:8138/health", shell=True, capture_output=True).returncode == 0: break
        time.sleep(1)

    vram = subprocess.check_output("nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits", shell=True, text=True).split()[0] + " MiB"
    sp = subprocess.run(["python3", str(BENCH.parents[1] / "_tools/benchmark_dory_speed.py"), "120", "0.2", "0.95"], capture_output=True, text=True)
    print(f"[gemma4_exact] Speed: {sp.stdout.strip()}")
    raw_vid, fin_vid = OUT / "raw_splatbox_gemma4_exact.mp4", OUT / "splatbox_gemma4_exact.mp4"
    os.environ["RECORD_VIDEO_PATH"], os.environ["PROOF_VIDEO_NAME"] = str(raw_vid), fin_vid.name
    for f in [OUT / "telemetry.json", BENCH / "stages/03-execute/output/telemetry.json", raw_vid]: f.unlink(missing_ok=True)
    ensure_chrome(); res = run_splatbox_match(); sc = res.get("score", 0)
    compose_split(raw_vid, fin_vid, "Google Gemma 4 Exact 4B (MTP)", "64k (MTP Exact)", vram, sc)
    (OUT / "telemetry_gemma4_exact.json").write_text(Path(OUT / "telemetry.json").read_text())
    proc.kill(); proc.wait(); log_f.close()
    subprocess.run(["bash", str(BENCH / "contract.sh")], check=True)
    print(f"\n=== [GEMMA 4 EXACT BENCHMARK COMPLETE: Score={sc}, VRAM={vram}] ===")

if __name__ == "__main__": run_gemma()
