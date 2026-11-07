#!/usr/bin/env bash
# Phase 56 Verification Contract: Candidate 3 Substrate & ICM 7-Gauntlet Blueprints
set -euo pipefail

TOTAL=15
PASSED=0
WORKSPACE_ROOT="/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes"
cd "$WORKSPACE_ROOT"

echo "=== Running Phase 56 Verification Contract ==="

# 1. Upstream Submodule Purity
UPSTREAM_DIFF="$(git -C .hermes/hermes-agent status --porcelain 2>/dev/null || true)"
if [[ -z "$UPSTREAM_DIFF" ]]; then
  echo "[PASS] 1/$TOTAL: Upstream substrate .hermes/hermes-agent is 100% clean"
  PASSED=$((PASSED + 1))
else
  echo "[FAIL] 1/$TOTAL: Upstream substrate .hermes/hermes-agent contains uncommitted modifications"
  exit 1
fi

# 2. Discrete RTX 3050 VRAM Ceiling Check (<= 5800.0 MiB)
VRAM_USED="$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits | head -n1 | tr -d ' ')"
VRAM_FLOAT="$(python3 -c "print(float('$VRAM_USED'))")"
CEILING=5800.0
if (( $(echo "$VRAM_FLOAT <= $CEILING" | bc -l) )); then
  echo "[PASS] 2/$TOTAL: NVML VRAM check: ${VRAM_FLOAT} MiB <= ${CEILING} MiB"
  PASSED=$((PASSED + 1))
else
  echo "[FAIL] 2/$TOTAL: NVML VRAM check failed: ${VRAM_FLOAT} MiB exceeds ceiling ${CEILING} MiB"
  exit 1
fi

# 3. Llama-server Port 8138 Health
LLAMA_STATUS="$(curl -s --max-time 3 http://127.0.0.1:8138/health || echo "{}")"
if echo "$LLAMA_STATUS" | grep -q '"status":"ok"'; then
  echo "[PASS] 3/$TOTAL: llama-server Port 8138 health check passed: $LLAMA_STATUS"
  PASSED=$((PASSED + 1))
else
  echo "[FAIL] 3/$TOTAL: llama-server Port 8138 health check failed: $LLAMA_STATUS"
  exit 1
fi

# 4. Hermes Gateway Port 8642 Health
GATEWAY_STATUS="$(curl -s --max-time 3 http://127.0.0.1:8642/health || echo "{}")"
if echo "$GATEWAY_STATUS" | grep -q '"status": "ok"'; then
  echo "[PASS] 4/$TOTAL: Hermes Gateway Port 8642 health check passed: $GATEWAY_STATUS"
  PASSED=$((PASSED + 1))
else
  echo "[FAIL] 4/$TOTAL: Hermes Gateway Port 8642 health check failed: $GATEWAY_STATUS"
  exit 1
fi

# 5. OpenViking Port 1933 Health
VIKING_STATUS="$(curl -s --max-time 3 http://127.0.0.1:1933/health || echo "{}")"
if echo "$VIKING_STATUS" | grep -q '"status":"ok"'; then
  echo "[PASS] 5/$TOTAL: OpenViking Port 1933 health check passed: $VIKING_STATUS"
  PASSED=$((PASSED + 1))
else
  echo "[FAIL] 5/$TOTAL: OpenViking Port 1933 health check failed: $VIKING_STATUS"
  exit 1
fi

# 6. Dream-RSI Pre-Gauntlet Warm-Start Distillation
RSI_RECEIPT="$WORKSPACE_ROOT/.hermes/cache/rsi_last_distill.json"
if [[ -s "$RSI_RECEIPT" ]] && python3 -m json.tool "$RSI_RECEIPT" >/dev/null 2>&1; then
  TREES_COUNT="$(python3 -c "import json; data=json.load(open('$RSI_RECEIPT')); print(data.get('evaluated_trees', 0))")"
  echo "[PASS] 6/$TOTAL: Dream-RSI warm-start receipt verified (evaluated $TREES_COUNT trees)"
  PASSED=$((PASSED + 1))
else
  echo "[FAIL] 6/$TOTAL: Dream-RSI warm-start receipt missing or invalid"
  exit 1
fi

# 7. Verification of all 7 Gauntlet Directories
GAUNTLETS=(gauntlet_a_voxel_fps gauntlet_b_splatbox gauntlet_c_aquarium leanrea_eval ffmpeg_skill_eval diagram_design_eval markitdown_eval)
MISSING_GAUNTLETS=0
for g in "${GAUNTLETS[@]}"; do
  if [[ ! -d "$WORKSPACE_ROOT/benchmarks/$g" ]]; then
    echo "Missing benchmark directory: benchmarks/$g"
    MISSING_GAUNTLETS=1
  fi
done
if [[ "$MISSING_GAUNTLETS" -eq 0 ]]; then
  echo "[PASS] 7/$TOTAL: All 7 frontier gauntlet directories exist in benchmarks/"
  PASSED=$((PASSED + 1))
else
  echo "[FAIL] 7/$TOTAL: Missing one or more gauntlet directories"
  exit 1
fi

# 8. Verification of all 21 Staged Prompt Files
MISSING_PROMPTS=0
for g in "${GAUNTLETS[@]}"; do
  for s in 1 2 3; do
    PFILE="$WORKSPACE_ROOT/benchmarks/$g/PROMPT_STAGE${s}.txt"
    if [[ ! -s "$PFILE" ]]; then
      echo "Missing or empty prompt: benchmarks/$g/PROMPT_STAGE${s}.txt"
      MISSING_PROMPTS=1
    fi
  done
done
if [[ "$MISSING_PROMPTS" -eq 0 ]]; then
  echo "[PASS] 8/$TOTAL: All 21 staged prompt files (3 stages * 7 gauntlets) exist and are non-empty"
  PASSED=$((PASSED + 1))
else
  echo "[FAIL] 8/$TOTAL: One or more staged prompt files missing or empty"
  exit 1
fi

# 9. Verification of all 7 Gauntlet launch_konsole.sh Scripts
MISSING_LAUNCHERS=0
for g in "${GAUNTLETS[@]}"; do
  LFILE="$WORKSPACE_ROOT/benchmarks/$g/launch_konsole.sh"
  if [[ ! -x "$LFILE" ]] || ! grep -q "PROMPT_STAGE" "$LFILE"; then
    echo "Invalid or non-executable launcher: benchmarks/$g/launch_konsole.sh"
    MISSING_LAUNCHERS=1
  fi
done
if [[ "$MISSING_LAUNCHERS" -eq 0 ]]; then
  echo "[PASS] 9/$TOTAL: All 7 gauntlet launch_konsole.sh scripts are executable and stage-aware"
  PASSED=$((PASSED + 1))
else
  echo "[FAIL] 9/$TOTAL: One or more launch_konsole.sh scripts invalid"
  exit 1
fi

# 10. Verification of Master launch_all_konsole.sh
if [[ -x "$WORKSPACE_ROOT/benchmarks/launch_all_konsole.sh" ]]; then
  echo "[PASS] 10/$TOTAL: Master benchmarks/launch_all_konsole.sh is executable"
  PASSED=$((PASSED + 1))
else
  echo "[FAIL] 10/$TOTAL: Master benchmarks/launch_all_konsole.sh missing or non-executable"
  exit 1
fi

# 11. Tripartite Markdown Line Budget Discipline across All 7 Gauntlets
LINE_CAP_FAIL=0
for g in "${GAUNTLETS[@]}"; do
  # CONTEXT <= 80, invariants <= 80, rules <= 120, references <= 200
  C_LINES=$(wc -l < "$WORKSPACE_ROOT/benchmarks/$g/CONTEXT.md")
  I_LINES=$(wc -l < "$WORKSPACE_ROOT/benchmarks/$g/invariants.md")
  R_LINES=$(wc -l < "$WORKSPACE_ROOT/benchmarks/$g/rules.md")
  REF_LINES=$(wc -l < "$WORKSPACE_ROOT/benchmarks/$g/references.md")
  if (( C_LINES > 80 || I_LINES > 80 || R_LINES > 120 || REF_LINES > 200 )); then
    echo "Line cap violated in benchmarks/$g: C=$C_LINES, I=$I_LINES, R=$R_LINES, REF=$REF_LINES"
    LINE_CAP_FAIL=1
  fi
done
if [[ "$LINE_CAP_FAIL" -eq 0 ]]; then
  echo "[PASS] 11/$TOTAL: All 7 gauntlet markdown files strictly obey ICM line budgets (<= 80/80/120/200)"
  PASSED=$((PASSED + 1))
else
  echo "[FAIL] 11/$TOTAL: ICM line budgets violated in gauntlet markdown files"
  exit 1
fi

# 12. Verification of Preloaded Skills in ~/.hermes/skills/
REQUIRED_SKILLS=(icm-architect leanrea ffmpeg-skill diagram-design markitdown)
SKILL_FAIL=0
for sk in "${REQUIRED_SKILLS[@]}"; do
  if [[ ! -d "$HOME/.hermes/skills/$sk" ]] && [[ ! -d "/var/home/imshubhamsocial/.hermes/skills/$sk" ]]; then
    echo "Required skill missing: $sk"
    SKILL_FAIL=1
  fi
done
if [[ "$SKILL_FAIL" -eq 0 ]]; then
  echo "[PASS] 12/$TOTAL: All 5 canonical skills are installed in ~/.hermes/skills/"
  PASSED=$((PASSED + 1))
else
  echo "[FAIL] 12/$TOTAL: Missing one or more required skills in ~/.hermes/skills/"
  exit 1
fi

# 13. Candidate 3 Model Weights Verification
MODEL_MAIN="/var/home/imshubhamsocial/.hermes/models/NVIDIA-Nemotron-3.5-Bolt-E4B-UD-Q4_K_XL.gguf"
MODEL_DRAFT="/var/home/imshubhamsocial/.hermes/models/dflash-NVIDIA-Nemotron-3.5-Bolt-E4B-Q8_0.gguf"
if [[ ! -f "$MODEL_MAIN" ]]; then
  MODEL_MAIN="$HOME/.hermes/models/NVIDIA-Nemotron-3.5-Bolt-E4B-UD-Q4_K_XL.gguf"
fi
if [[ ! -f "$MODEL_DRAFT" ]]; then
  MODEL_DRAFT="$HOME/.hermes/models/dflash-NVIDIA-Nemotron-3.5-Bolt-E4B-Q8_0.gguf"
fi
if [[ -f "$MODEL_MAIN" ]] && [[ -f "$MODEL_DRAFT" ]]; then
  echo "[PASS] 13/$TOTAL: Candidate 3 target model and DFlash drafter GGUF weights verified"
  PASSED=$((PASSED + 1))
else
  echo "[FAIL] 13/$TOTAL: Candidate 3 model weights missing from ~/.hermes/models/"
  exit 1
fi

# 14. Bespoke Script Purity Gate
BESPOKE_COUNT=0
if [[ -d "$WORKSPACE_ROOT/scripts" ]]; then
  for f in "$WORKSPACE_ROOT/scripts"/*; do
    [[ -f "$f" ]] || continue
    fname="$(basename "$f")"
    if [[ "$fname" != "hermes_icm_validator.py" ]] && [[ "$fname" != "rule_icm_validation_script_missing.md" ]]; then
      ((BESPOKE_COUNT++))
    fi
  done
fi
if [[ "$BESPOKE_COUNT" -eq 0 ]]; then
  echo "[PASS] 14/$TOTAL: Zero bespoke scripts in scripts/ (canonical substrate preserved)"
  PASSED=$((PASSED + 1))
else
  echo "[FAIL] 14/$TOTAL: Detected $BESPOKE_COUNT unauthorized bespoke scripts in scripts/"
  exit 1
fi

# 15. Tripartite Scaffolding for Phase 56
if [[ -s "$WORKSPACE_ROOT/phases/phase_56_candidate3_q8_kv_dflash_and_icm_7gauntlet_blueprints/01_spec/spec.md" ]] && \
   [[ -s "$WORKSPACE_ROOT/phases/phase_56_candidate3_q8_kv_dflash_and_icm_7gauntlet_blueprints/02_impl/task.md" ]]; then
  echo "[PASS] 15/$TOTAL: Phase 56 tripartite spec and impl markdown files verified"
  PASSED=$((PASSED + 1))
else
  echo "[FAIL] 15/$TOTAL: Phase 56 spec or impl files missing or empty"
  exit 1
fi

echo "=== All $PASSED/$TOTAL Phase 56 Assertions PASSED Deterministically ==="
exit 0
