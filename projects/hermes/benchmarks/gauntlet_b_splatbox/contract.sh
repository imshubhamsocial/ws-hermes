#!/usr/bin/env bash
set -euo pipefail

BENCH_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
S1="${BENCH_DIR}/stages/01-probe/output/probe_state.json"
S2="${BENCH_DIR}/stages/02-controller/output/tracker_verified.json"
S3="${BENCH_DIR}/stages/03-execute/output/telemetry.json"

echo "=== [Gauntlet B: Splatbox 3-Stage ICM Contract Verification] ==="

# 1. Verify Hardware VRAM Invariant (<= 5800 MiB)
VRAM_USED=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits | head -n 1 | tr -d ' ')
if [ "${VRAM_USED}" -gt 5800 ]; then
  echo "[FAIL] Hardware VRAM ceiling breached: ${VRAM_USED} MiB > 5800 MiB"
  exit 1
fi
echo "[PASS] Hardware VRAM within invariant: ${VRAM_USED} MiB <= 5800 MiB"

# 2. Verify Stage 1 Gate
jq -e '.pointer_lock_active == true' "${S1}" > /dev/null
echo "[PASS] Stage 01-probe certified: PointerLock active."

# 3. Verify Stage 2 Gate
jq -e '.targets_found_ge_1 == true' "${S2}" > /dev/null
echo "[PASS] Stage 02-controller certified: Closed-loop target centroid verified."

# 4. Verify Stage 3 Match Telemetry (Zero Fake Green)
jq -e '.score > 0 and .duration_sec >= 55 and .frames_processed >= 120 and .embeddinggemma2_verified == true' "${S3}" > /dev/null
SCORE=$(jq -r '.score' "${S3}")
FRAMES=$(jq -r '.frames_processed' "${S3}")
echo "[PASS] Stage 03-execute certified: Score=${SCORE}, Frames=${FRAMES}."
echo "=== [CERTIFIED: GAUNTLET B 100% PASS] ==="
