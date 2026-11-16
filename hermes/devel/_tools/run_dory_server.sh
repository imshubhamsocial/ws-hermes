#!/usr/bin/env bash
# Deterministic Dory Server Launcher with Dynamic Loop Selection & NVIDIA Upstream Spec
set -euo pipefail

LOOPS="${1:-2}"
CTX="${2:-65536}"
SERVER_DIR="/var/home/imshubhamsocial/llama.cpp-dory/build-cuda/bin"
SERVER_BIN="${SERVER_DIR}/llama-server"
MODEL="/var/home/imshubhamsocial/.hermes/models/dory-heretic-q5_k_m.gguf"

SITE_PACKAGES="$(python3 -m site --user-site 2>/dev/null || echo "${HOME}/.local/lib/python3.14/site-packages")"
CUDA_LIBS="${SITE_PACKAGES}/nvidia/cu13/lib:${SITE_PACKAGES}/nvidia/cublas/lib:${SITE_PACKAGES}/nvidia/cuda_nvrtc/lib:${SITE_PACKAGES}/nvidia/cuda_runtime/lib"
export LD_LIBRARY_PATH="${SERVER_DIR}:${CUDA_LIBS}:${LD_LIBRARY_PATH:-}"
export GGML_CUDA_GRAPH_OPT=1 GGML_CUDA_FORCE_MMQ=1

echo "Starting Dory Server (Loops: ${LOOPS}, Context: ${CTX}, NVIDIA Upstream Sampling)..."

exec taskset -c 0-5 "${SERVER_BIN}" \
    --model "${MODEL}" \
    --alias "dory,nemotron-dory,nemotron-3.5-bolt-e4b,gemma-4-exact,google/gemma-4-E4B-it" \
    --host 127.0.0.1 --port 8138 \
    --ctx-size "${CTX}" \
    --cache-type-k q4_0 --cache-type-v q4_0 \
    --batch-size 2048 --ubatch-size 1024 \
    --flash-attn on \
    --no-context-shift \
    --reasoning on \
    --jinja \
    --n-gpu-layers 99 \
    --threads 6 --threads-batch 6 --parallel 1 --cont-batching \
    --temp 1.0 --top-p 0.95 --top-k 0 --min-p 0.0 \
    --repeat-penalty 1.0 --presence-penalty 0.0 \
    --override-kv "dory.num_loops=int:${LOOPS},dory.recurrent_kv_cache_mode=str:last_loop" \
    --spec-type ngram-mod --spec-ngram-mod-n-min 8 --spec-ngram-mod-n-match 12 --spec-ngram-mod-n-max 32 \
    --metrics
