#!/usr/bin/env bash
# Turnkey Triple-Model Benchmark Runner for Gauntlet B (Qwen Q5, Qwen Q6, Dory k=2)
set -euo pipefail
BENCH_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${BENCH_DIR}"

echo "=========================================================="
echo "Starting Hermes Agent OS Gauntlet B Triple-Model Suite"
echo "Target Models: Qwen3.5 Q5_K_M (256k), Qwen3.5 Q6_K (128k), Dory (256k, k=2)"
echo "Hardware Bound: NVIDIA RTX 3050 Laptop GPU (<= 5,800 MiB)"
echo "=========================================================="

cleanup() {
    echo "[TRAP] Cleaning up background benchmark daemons..."
    "${BENCH_DIR}/server_manager.sh" stop 2>/dev/null || true
    pkill -f "remote-debugging-port=9222" 2>/dev/null || true
}
trap cleanup EXIT INT TERM

python3 "${BENCH_DIR}/run_triple_model_suite.py"

echo "=========================================================="
echo "Gauntlet B Triple-Model Benchmark Suite Finished."
echo "Master Showcase: ${BENCH_DIR}/output/hermes_gauntlet_b_triple_showcase.mp4"
echo "=========================================================="
