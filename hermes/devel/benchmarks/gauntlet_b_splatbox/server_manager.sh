#!/usr/bin/env bash
# Modular Server Manager for Gauntlet B Triple-Model Benchmark Suite
set -euo pipefail
ACTION="${1:-stop}"; MODE="${2:-qwen_q5}"
BIN="/var/home/imshubhamsocial/llama.cpp-dory/build-cuda/bin/llama-server"
MODELS="/var/home/imshubhamsocial/.hermes/models"
SITE_PKG="$(python3 -m site --user-site 2>/dev/null || echo "${HOME}/.local/lib/python3.14/site-packages")"
CUDA_LIBS="${SITE_PKG}/nvidia/cu13/lib:${SITE_PKG}/nvidia/cublas/lib:${SITE_PKG}/nvidia/cuda_nvrtc/lib:${SITE_PKG}/nvidia/cuda_runtime/lib"
export LD_LIBRARY_PATH="/var/home/imshubhamsocial/llama.cpp-dory/build-cuda/bin:${CUDA_LIBS}:${LD_LIBRARY_PATH:-}"
export GGML_CUDA_GRAPH_OPT=1 GGML_CUDA_FORCE_MMQ=1

stop_srv() {
    pkill -9 -x llama-server 2>/dev/null || true
    for _ in {1..15}; do ! curl -sf http://127.0.0.1:8138/health >/dev/null 2>&1 && break || sleep 0.5; done
    for _ in {1..20}; do [[ $(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits 2>/dev/null || echo 0) -lt 500 ]] && break || sleep 0.5; done
    echo "[SERVER] Stopped. Quiescent VRAM: $(nvidia-smi --query-gpu=memory.used --format=csv,noheader)"
}

start_srv() {
    stop_srv
    local m_path="" ctx="262144" ngl="24" flags=()
    case "${MODE}" in
        qwen_q5)
            m_path="${MODELS}/Qwen3.5-4B-heretic-Q5_K_M.gguf"; ctx="262144"; ngl="99"
            flags=(--no-kv-offload --temp 0.1 --top-p 0.80 --top-k 30 --min-p 0.05 --repeat-penalty 1.05 --jinja
                   --spec-type ngram-mod --spec-ngram-mod-n-min 8 --spec-ngram-mod-n-match 12 --spec-ngram-mod-n-max 32) ;;
        qwen_q6)
            m_path="${MODELS}/Qwen3.5-4B-heretic-Q6_K.gguf"; ctx="262144"; ngl="99"
            flags=(--no-kv-offload --temp 0.1 --top-p 0.80 --top-k 30 --min-p 0.05 --repeat-penalty 1.05 --jinja
                   --spec-type ngram-mod --spec-ngram-mod-n-min 8 --spec-ngram-mod-n-match 12 --spec-ngram-mod-n-max 32) ;;
        dory_k2)
            m_path="${MODELS}/dory-heretic-q5_k_m.gguf"; ctx="262144"; ngl="72"
            flags=(--no-kv-offload --temp 1.0 --top-p 0.95 --top-k 0 --min-p 0.0 --repeat-penalty 1.0 --jinja --reasoning on
                   --override-kv "dory.num_loops=int:2,dory.recurrent_kv_cache_mode=str:last_loop"
                   --spec-type ngram-mod --spec-ngram-mod-n-min 8 --spec-ngram-mod-n-match 12 --spec-ngram-mod-n-max 32) ;;
        *) echo "Unknown mode: ${MODE}" && exit 1 ;;
    esac
    echo "[SERVER] Starting ${MODE} (Ctx: ${ctx}, NGL: ${ngl})..."
    taskset -c 0-5 "${BIN}" --model "${m_path}" --alias "model,default" --host 127.0.0.1 --port 8138 \
        --ctx-size "${ctx}" --cache-type-k q4_0 --cache-type-v q4_0 --batch-size 512 --ubatch-size 256 \
        --flash-attn on --no-context-shift --n-gpu-layers "${ngl}" --threads 6 --threads-batch 6 --parallel 1 \
        --cont-batching --metrics "${flags[@]}" >"/tmp/llama_${MODE}.log" 2>&1 &
    for _ in {1..40}; do curl -sf http://127.0.0.1:8138/health >/dev/null 2>&1 && break || sleep 1; done
    curl -sf http://127.0.0.1:8138/health >/dev/null 2>&1 || { echo "[ERROR] Server failed to start"; exit 1; }
    echo "[SERVER] Online: ${MODE} | VRAM: $(nvidia-smi --query-gpu=memory.used --format=csv,noheader)"
}

[[ "${ACTION}" == "start" ]] && start_srv || stop_srv
