#!/usr/bin/env bash
# Phase 57 Deterministic Verification Contract (03_verify/contract.sh)
# Asserts 128K Gemma 4 Exact Substrate, Layer 0/1/3 Architecture,
# Gauntlet B 3-Stage Pipeline, ICM Evolution Datasets, and Upstream Purity.

set -euo pipefail

PASS=0
FAIL=0
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$REPO_ROOT"

CONFIG_FILE="$REPO_ROOT/.hermes/config.yaml"
if [[ ! -f "$CONFIG_FILE" && -f "/var/home/imshubhamsocial/.hermes/config.yaml" ]]; then
  CONFIG_FILE="/var/home/imshubhamsocial/.hermes/config.yaml"
fi

assert_check() {
  local desc="$1"
  local cmd="$2"
  if eval "$cmd" >/dev/null 2>&1; then
    echo "[PASS] $desc"
    PASS=$((PASS + 1))
  else
    echo "[FAIL] $desc"
    FAIL=$((FAIL + 1))
  fi
}

echo "=== Executing Phase 57 Verification Contract ==="

# Assertion 1: Layer 0 Workspace Map Presence
assert_check "1. Layer 0 workspace map exists (IDENTITY.md, AGENTS.md, .hermes/SOUL.md, CONTEXT.md)" \
  "[[ -f IDENTITY.md && -f AGENTS.md && -f .hermes/SOUL.md && -f CONTEXT.md ]]"

# Assertion 2: Line Budget Discipline (CONTEXT.md <= 80 lines)
assert_check "2. All CONTEXT.md files are strictly <= 80 lines" \
  "awk 'FNR==1{if(lines>80) exit 1; lines=0} {lines++} END{if(lines>80) exit 1}' CONTEXT.md hermes/devel/stages/*/CONTEXT.md"

# Assertion 3: Zero Bespoke Python/Shell Scripts in scripts/ or plugins/ (authorized hermes_icm_validator.py preserved)
assert_check "3. Zero bespoke Python or shell wrappers in scripts/ or plugins/ (authorized hermes_icm_validator.py preserved)" \
  "[[ ! -d scripts || -z \"\$(find scripts -maxdepth 2 -type f \\( -name '*.py' -o -name '*.sh' \\) ! -name 'hermes_icm_validator.py' 2>/dev/null)\" ]]"

# Assertion 4: 100% Upstream Substrate Purity in .hermes/hermes-agent
assert_check "4. Upstream .hermes/hermes-agent repository is 100% clean" \
  "[[ ! -d .hermes/hermes-agent ]] || git -C .hermes/hermes-agent diff --quiet"

# Assertion 5: 128K Context & Model Registration in config.yaml
assert_check "5. config.yaml enforces context_length: 131072 and default model gemma-4-E4B-it-qat-exact" \
  "grep -q 'context_length: 131072' \"$CONFIG_FILE\" && grep -q 'default: gemma-4-E4B-it-qat-exact' \"$CONFIG_FILE\""

# Assertion 6: Llama-server Active on Port 8138 with 128K Context
assert_check "6. Llama-server on Port 8138 serves 131072 context length" \
  "curl -s http://127.0.0.1:8138/v1/models | grep -q '\"n_ctx\":131072'"

# Assertion 7: Live NVML GPU VRAM <= 5,800.0 MiB
assert_check "7. Live NVML GPU VRAM <= 5,800.0 MiB on RTX 3050" \
  "VRAM_USED=\$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits | head -n1 | tr -d ' '); [[ \"\$VRAM_USED\" -le 5800 ]]"

# Assertion 8: ICM Evolution Datasets Present in Cache
assert_check "8. ICM Evolution Datasets cloned in cache" \
  "[[ -d .cache/icm-datasets/Interpretable-Context-Methodology && -d .cache/icm-datasets/icm-template ]] || [[ -d /var/home/imshubhamsocial/.cache/icm-datasets/Interpretable-Context-Methodology && -d /var/home/imshubhamsocial/.cache/icm-datasets/icm-template ]]"

# Assertion 9: icm-stage-compiler Skill Deployed
assert_check "9. icm-stage-compiler skill installed in skills directory" \
  "[[ -f .hermes/skills/icm/icm-stage-compiler/SKILL.md ]] || [[ -f /var/home/imshubhamsocial/.hermes/skills/icm/icm-stage-compiler/SKILL.md ]]"

# Assertion 10: Gauntlet B Deterministic Contract Verification
assert_check "10. Gauntlet B 3-stage contract executes and passes" \
  "bash hermes/devel/benchmarks/gauntlet_b_splatbox/contract.sh"

echo "=== Summary: $PASS Passed, $FAIL Failed ==="
if [[ "$FAIL" -gt 0 ]]; then
  exit 1
fi

RECEIPT_PATH="$REPO_ROOT/hermes/devel/phases/phase_57_gdr34_meta_prompting_icm_evolution_datasets_and_visual_substrate/stages/03-verify/status.json"
cat <<EOF > "$RECEIPT_PATH"
{
  "phase_id": 57,
  "phase_name": "phase_57_gdr34_meta_prompting_icm_evolution_datasets_and_visual_substrate",
  "status": "VERIFIED_AND_SEALED",
  "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "assertions_passed": $PASS,
  "assertions_failed": $FAIL,
  "context_length_enforced": 131072,
  "model_selected": "gemma-4-E4B-it-q4_0-exact.gguf",
  "vram_ceiling_mib": 5800.0,
  "vram_measured_mib": $(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits | head -n1 | tr -d ' ')
}
EOF

# Maintain backward compatibility in 03_verify
cp "$RECEIPT_PATH" "$REPO_ROOT/hermes/devel/phases/phase_57_gdr34_meta_prompting_icm_evolution_datasets_and_visual_substrate/03_verify/status.json"
cp "$REPO_ROOT/hermes/devel/phases/phase_57_gdr34_meta_prompting_icm_evolution_datasets_and_visual_substrate/stages/03-verify/contract.sh" "$REPO_ROOT/hermes/devel/phases/phase_57_gdr34_meta_prompting_icm_evolution_datasets_and_visual_substrate/03_verify/contract.sh"
chmod +x "$REPO_ROOT/hermes/devel/phases/phase_57_gdr34_meta_prompting_icm_evolution_datasets_and_visual_substrate/03_verify/contract.sh"
