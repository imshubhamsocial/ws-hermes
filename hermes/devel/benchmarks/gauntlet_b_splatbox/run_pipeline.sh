#!/usr/bin/env bash
# Deterministic 3-Stage ICM Compiler Pipeline for Gauntlet B (TUI Enabled)
set -euo pipefail

BENCH_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

for stage in 01-probe 02-controller 03-execute; do
  echo "===================================================="
  echo "[ICM COMPILER] Executing Fresh Context: ${stage}"
  echo "===================================================="
  cd "${BENCH_DIR}/stages/${stage}"
  export HERMES_QUERY="/icm-stage-compiler Execute the stage contract in CONTEXT.md and verify its audit gate."
  hermes chat \
    --oneshot \
    --in "${BENCH_DIR}/stages/${stage}" \
    -s icm-stage-compiler \
    --toolsets 'terminal,file,browser,vision' \
    --accept-hooks \
    --yolo \
    --max-turns 8 \
    -q "${HERMES_QUERY}"
done

echo "===================================================="
echo "[ICM COMPILER] Running Multi-Stage Audit Grader"
echo "===================================================="
cd "${BENCH_DIR}" && bash ./contract.sh
