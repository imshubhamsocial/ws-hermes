#!/usr/bin/env bash
# Deterministic Multi-Model Upstream Server Launcher
set -euo pipefail

MODE="${1:-gemma_exact}"; CTX="${2:-65536}"; NGL="99"; BATCH="2048"; UBATCH="1024"
[[ "${MODE}" == gemma* && -z "${2:-}" ]] && CTX="65536"
[[ "${MODE}" == dory* ]] && { NGL="48"; BATCH="512"; UBATCH="256"; }
SERVER_DIR="/var/home/imshubhamsocial/llama.cpp-dory/build-cuda/bin"; SERVER_BIN="${SERVER_DIR}/llama-server"
SITE_PACKAGES="$(python3 -m site --user-site 2>/dev/null || echo "${HOME}/.local/lib/python3.14/site-packages")"
CUDA_LIBS="${SITE_PACKAGES}/nvidia/cu13/lib:${SITE_PACKAGES}/nvidia/cublas/lib:${SITE_PACKAGES}/nvidia/cuda_nvrtc/lib:${SITE_PACKAGES}/nvidia/cuda_runtime/lib"
export LD_LIBRARY_PATH="${SERVER_DIR}:${CUDA_LIBS}:${LD_LIBRARY_PATH:-}" GGML_CUDA_GRAPH_OPT=1 GGML_CUDA_FORCE_MMQ=0

BASE_FLAGS=(
    --host 127.0.0.1 --port 8138
    --ctx-size "${CTX}"
    --cache-type-k q4_0 --cache-type-v q4_0
    --batch-size "${BATCH}" --ubatch-size "${UBATCH}"
    --flash-attn on --reasoning on --jinja
    --n-gpu-layers "${NGL}" --threads 6 --threads-batch 6 --parallel 1
    --cont-batching --metrics
)

case "${MODE}" in
    dory2)
        exec taskset -c 0-5 "${SERVER_BIN}" \
            --model "/var/home/imshubhamsocial/.hermes/models/dory-heretic-q5_k_m.gguf" \
            --alias "dory,model,gemma-4-E4B-it-qat-exact" "${BASE_FLAGS[@]}" --no-context-shift \
            --temp 1.0 --top-p 0.95 --top-k 0 --min-p 0.0 --repeat-penalty 1.0 \
            --override-kv "dory.num_loops=int:2,dory.recurrent_kv_cache_mode=str:last_loop" \
            --spec-type ngram-mod --spec-ngram-mod-n-min 8 --spec-ngram-mod-n-match 12 --spec-ngram-mod-n-max 32
        ;;
    dory4)
        exec taskset -c 0-5 "${SERVER_BIN}" \
            --model "/var/home/imshubhamsocial/.hermes/models/dory-heretic-q5_k_m.gguf" \
            --alias "dory,model,gemma-4-E4B-it-qat-exact" "${BASE_FLAGS[@]}" --no-context-shift \
            --temp 1.0 --top-p 0.95 --top-k 0 --min-p 0.0 --repeat-penalty 1.0 \
            --override-kv "dory.num_loops=int:4,dory.recurrent_kv_cache_mode=str:last_loop" \
            --spec-type ngram-mod --spec-ngram-mod-n-min 8 --spec-ngram-mod-n-match 12 --spec-ngram-mod-n-max 32
        ;;
    gemma_heretic)
        exec taskset -c 0-5 "${SERVER_BIN}" \
            --model "/var/home/imshubhamsocial/.hermes/models/gemma-4-heretic-q4_k_m.gguf" \
            --alias "gemma-heretic,model" "${BASE_FLAGS[@]}" \
            --temp 0.2 --top-p 0.95 --top-k 64 --min-p 0.05 --repeat-penalty 1.05
        ;;
    gemma_exact)
        exec taskset -c 0,2,4,6,8,10 "${SERVER_BIN}" \
            --model "/var/home/imshubhamsocial/.hermes/models/gemma-4-E4B-it-q4_0-exact.gguf" \
            --spec-draft-model "/var/home/imshubhamsocial/.hermes/models/gemma-4-E4B-it-qat-assistant-q4_0-exact.gguf" \
            --n-gpu-layers-draft 99 --spec-type draft-mtp \
            --spec-draft-n-max 2 --spec-draft-p-min 0.75 \
            --alias "gemma-4-E4B-it-qat-exact,gemma-4-exact,model,default" "${BASE_FLAGS[@]}" \
            --temp 0.2 --top-p 0.95 --top-k 64 --min-p 0.05 --repeat-penalty 1.05
        ;;
    *)
        echo "Unknown mode: ${MODE}" && exit 1
        ;;
esac
