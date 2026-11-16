#!/usr/bin/env bash
# Automated Multi-Model Benchmark Suite
set -euo pipefail
DIR="/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/hermes/devel/_tools"

test_model() {
    local mode="$1" temp="$2" top_p="$3"
    echo "=========================================================="
    echo "Testing Model: ${mode} (Temp: ${temp}, Top_P: ${top_p})"
    echo "=========================================================="
    pkill -9 -x llama-server 2>/dev/null || true
    sleep 2

    "${DIR}/run_model_server.sh" "${mode}" 65536 >"/tmp/${mode}.log" 2>&1 &
    local s_pid=$!

    for _ in {1..30}; do
        if curl -sf http://127.0.0.1:8138/health >/dev/null 2>&1; then
            break
        fi
        sleep 1
    done

    local vram
    vram="$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits) MiB"
    echo "Active VRAM: ${vram}"

    python3 "${DIR}/benchmark_dory_speed.py" 200 "${temp}" "${top_p}"

    kill -9 "${s_pid}" 2>/dev/null || true
    pkill -9 -x llama-server 2>/dev/null || true
    sleep 2
}

test_model "dory2" 1.0 0.95
test_model "dory4" 1.0 0.95
test_model "gemma_heretic" 0.2 0.95
test_model "gemma_exact" 0.2 0.95
echo "ALL MODEL BENCHMARKS COMPLETED."
