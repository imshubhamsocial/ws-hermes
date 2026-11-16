#!/usr/bin/env bash
# Deterministic Qwen Q5 Server Launcher with Speculative Drafter
set -euo pipefail

CTX="${1:-8192}"
PORT="${2:-8138}"
SERVER_DIR="/var/home/imshubhamsocial/llama.cpp-dory/build-cuda/bin"
SERVER_BIN="${SERVER_DIR}/llama-server"
TARGET_MODEL="/var/home/imshubhamsocial/.hermes/models/qwen2.5-coder-3b-instruct-q5_k_m.gguf"
DRAFT_MODEL="/var/home/imshubhamsocial/.hermes/models/qwen2.5-coder-0.5b-instruct-q4_0.gguf"

SITE_PACKAGES="$(python3 -m site --user-site 2>/dev/null || echo "${HOME}/.local/lib/python3.14/site-packages")"
CUDA_LIBS="${SITE_PACKAGES}/nvidia/cu13/lib:${SITE_PACKAGES}/nvidia/cublas/lib:${SITE_PACKAGES}/nvidia/cuda_nvrtc/lib:${SITE_PACKAGES}/nvidia/cuda_runtime/lib"
export LD_LIBRARY_PATH="${SERVER_DIR}:${CUDA_LIBS}:${LD_LIBRARY_PATH:-}"
export GGML_CUDA_GRAPH_OPT=1 GGML_CUDA_FORCE_MMQ=1

echo "Starting Qwen Q5 Server on Port ${PORT} (Context: ${CTX})..."

DRAFT_FLAGS=()
if [[ -f "${DRAFT_MODEL}" ]]; then
    DRAFT_FLAGS=(--model-draft "${DRAFT_MODEL}" --n-gpu-layers-draft 99 --draft-max 4 --draft-min 2)
else
    DRAFT_FLAGS=(--spec-type ngram-mod --spec-ngram-mod-n-min 8 --spec-ngram-mod-n-match 12 --spec-ngram-mod-n-max 32)
fi

exec taskset -c 0-5 "${SERVER_BIN}" \
    --model "${TARGET_MODEL}" \
    "${DRAFT_FLAGS[@]}" \
    --alias "qwen,qwen-q5,qwen2.5-coder,model" \
    --host 127.0.0.1 --port "${PORT}" \
    --ctx-size "${CTX}" \
    --cache-type-k q4_0 --cache-type-v q4_0 \
    --batch-size 2048 --ubatch-size 1024 \
    --flash-attn on \
    --no-context-shift \
    --jinja \
    --n-gpu-layers 99 \
    --threads 6 --threads-batch 6 --parallel 1 --cont-batching \
    --temp 0.1 --top-p 0.80 --top-k 30 --min-p 0.05 \
    --repeat-penalty 1.05 --presence-penalty 0.0 \
    --metrics
