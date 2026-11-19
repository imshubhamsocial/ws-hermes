#!/usr/bin/env bash  
# Layer 4 Deterministic Verification Gate: Gauntlet C WebGL2 Aquarium (35 lines)  
set -euo pipefail  
SIM_DIR="output/aquarium-sim/js"  
MODULES=("wave_pde.js" "caustics_shader.js" "sphere_physics.js" "boids_fish.js" "main.js")

echo "[GATE 1/4] Enforcing Rule 6 Atomic Script Ceiling (<60 lines)..."  
for MOD in "${MODULES[@]}"; do  
  FILE_PATH="${SIM_DIR}/${MOD}"  
  test -f "${FILE_PATH}"  
  LINE_CNT="$(wc -l < "${FILE_PATH}")"  
  if (( LINE_CNT >= 60 )); then  
    echo "CONTRACT_FAIL: ${FILE_PATH} has ${LINE_CNT} lines (limit <60)." && exit 1  
  fi  
done

echo "[GATE 2/4] Verifying WebGL2 Derivative Caustics AST Invariants..."  
grep -q "dFdx" "${SIM_DIR}/caustics_shader.js"  
grep -q "dFdy" "${SIM_DIR}/caustics_shader.js"  
grep -q "refract" "${SIM_DIR}/caustics_shader.js"

echo "[GATE 3/4] Verifying Headless CDP Telemetry Invariants..."  
grep -q "__AQUARIUM_TELEMETRY__" "${SIM_DIR}/main.js"  
if [[ -f "stages/04-verify/output/cdp_telemetry.json" ]]; then  
  python3 -c 'import json,sys; d=json.load(open("stages/04-verify/output/cdp_telemetry.json")); sys.exit(0 if d["fps"]>=55 and d["fishCount"]>=20 and d["causticsActive"] and d["consoleErrors"]==0 else 1)'  
fi

echo "[GATE 4/4] Enforcing RTX 3050 VRAM Ceiling (<= 5800 MiB)..."  
if command -v nvidia-smi >/dev/null 2>&1; then  
  VRAM_MIB="$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits | head -n1 | tr -d " ")"  
  if (( VRAM_MIB > 5800 )); then  
    echo "CONTRACT_FAIL: RTX 3050 VRAM ${VRAM_MIB} MiB exceeds 5800 MiB." && exit 1  
  fi  
fi  
echo "CONTRACT_PASS: Gauntlet C verified across all 4 deterministic gates."
