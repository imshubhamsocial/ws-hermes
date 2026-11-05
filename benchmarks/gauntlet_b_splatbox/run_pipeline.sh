#!/usr/bin/env bash
# Deterministic 3-Stage ICM Compiler Pipeline for Gauntlet B (TUI Enabled)
set -euo pipefail

BENCH_DIR="/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/benchmarks/gauntlet_b_splatbox"

for stage in 01-probe 02-controller 03-execute; do
  echo "===================================================="
  echo "[ICM COMPILER] Executing Fresh TUI Context: ${stage}"
  echo "===================================================="
  cd "${BENCH_DIR}/stages/${stage}"
  export HERMES_TUI_QUERY="/icm-stage-compiler Execute the stage contract in CONTEXT.md and verify its audit gate."
  hermes --tui \
    --in "${BENCH_DIR}/stages/${stage}" \
    --toolsets 'terminal,file,browser,vision' \
    --accept-hooks \
    --yolo \
    --max-turns 6 \
    -q "${HERMES_TUI_QUERY}"
done

echo "===================================================="
echo "[ICM COMPILER] Running Multi-Stage Audit Grader"
echo "===================================================="
cd "${BENCH_DIR}" && bash ./contract.sh
