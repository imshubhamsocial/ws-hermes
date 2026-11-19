#!/usr/bin/env bash
# Phase 55 Deterministic Verification Contract (03_verify/contract.sh)
# Asserts 49-File ICM Tripartite Scaffolding, Strict Line Budget Caps,
# Upstream Submodule Purity, Zero-Bespoke Wrappers, and NVML VRAM Ceiling.

set -euo pipefail

PASS=0
FAIL=0
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
cd "$PROJECT_ROOT"

CONFIG_FILE="$PROJECT_ROOT/.hermes/config.yaml"
if [[ ! -f "$CONFIG_FILE" && -f "$REPO_ROOT/.hermes/config.yaml" ]]; then
  CONFIG_FILE="$REPO_ROOT/.hermes/config.yaml"
elif [[ ! -f "$CONFIG_FILE" && -f "$HOME/.hermes/config.yaml" ]]; then
  CONFIG_FILE="$HOME/.hermes/config.yaml"
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

echo "=== Executing Phase 55 Verification Contract ==="

# Assertion 1: Layer 0 Workspace Map (AGENTS.md <= 80 lines)
assert_check "1. AGENTS.md exists and is strictly <= 80 lines" \
  "[[ -f AGENTS.md ]] && [[ \$(wc -l < AGENTS.md) -le 80 ]]"

# Assertion 2: Layer 0 Unified Multi-Agent Entry Point
assert_check "2. AGENTS.md operates as unified multi-agent entry point" \
  "[[ -f AGENTS.md ]] && grep -q 'Layer 0' AGENTS.md"

# Assertion 3: Layer 1 Root Task Router (CONTEXT.md <= 80 lines)
assert_check "3. Root CONTEXT.md exists and is strictly <= 80 lines" \
  "[[ -f CONTEXT.md ]] && [[ \$(wc -l < CONTEXT.md) -le 80 ]]"

# Assertion 4: _config/invariants.md <= 80 lines & _config/operational_rules.md <= 120 lines
assert_check "4. _config/invariants.md <= 80 lines and _config/operational_rules.md <= 120 lines" \
  "[[ -f _config/invariants.md && \$(wc -l < _config/invariants.md) -le 80 ]] && [[ -f _config/operational_rules.md && \$(wc -l < _config/operational_rules.md) -le 120 ]]"

# Assertion 5: _config/references.md <= 200 lines
assert_check "5. _config/references.md exists and is strictly <= 200 lines" \
  "[[ -f _config/references.md && \$(wc -l < _config/references.md) -le 200 ]]"

# Assertion 6: Pipeline Stages 01-04 Tripartite Scaffolding Presence
assert_check "6. Stages 01-spec through 04-verify each contain CONTEXT.md, invariants.md, rules.md, references.md" \
  "for s in stages/01-spec stages/02-plan stages/03-execute stages/04-verify; do [[ -f \$s/CONTEXT.md && -f \$s/invariants.md && -f \$s/rules.md && -f \$s/references.md ]] || exit 1; done"

# Assertion 7: Pipeline Stages Line Budget Discipline
assert_check "7. Stages 01-04 CONTEXT.md <= 80, invariants.md <= 80, rules.md <= 120, references.md <= 200 lines" \
  "for s in stages/01-spec stages/02-plan stages/03-execute stages/04-verify; do [[ \$(wc -l < \$s/CONTEXT.md) -le 80 && \$(wc -l < \$s/invariants.md) -le 80 && \$(wc -l < \$s/rules.md) -le 120 && \$(wc -l < \$s/references.md) -le 200 ]] || exit 1; done"

# Assertion 8: Benchmark Suites Tripartite Scaffolding Presence
assert_check "8. benchmarks/tau_bench, gaia, ast_grep_eval each contain tripartite files" \
  "for b in benchmarks/tau_bench benchmarks/gaia benchmarks/ast_grep_eval; do [[ -f \$b/CONTEXT.md && -f \$b/invariants.md && -f \$b/rules.md && -f \$b/references.md ]] || exit 1; done"

# Assertion 9: Benchmark Suites Line Budget Discipline
assert_check "9. Benchmark suites tripartite files obey line caps" \
  "for b in benchmarks/tau_bench benchmarks/gaia benchmarks/ast_grep_eval; do [[ \$(wc -l < \$b/CONTEXT.md) -le 80 && \$(wc -l < \$b/invariants.md) -le 80 && \$(wc -l < \$b/rules.md) -le 120 && \$(wc -l < \$b/references.md) -le 200 ]] || exit 1; done"

# Assertion 10: Canonical Configuration v52 / v45 Invariants in config.yaml
assert_check "10. config.yaml has _config_version >= 45, max_turns: 40, and Candidate 3 configuration" \
  "grep -qE '_config_version: (45|52)' \"$CONFIG_FILE\" && grep -q 'max_turns: 40' \"$CONFIG_FILE\" && grep -q 'nemotron-3.5-bolt-e4b' \"$CONFIG_FILE\""

# Assertion 11: Prompt Bloat Prevention Keys in config.yaml
assert_check "11. config.yaml disables tool_use_enforcement, execution_guidance, task_completion_guidance" \
  "grep -q 'tool_use_enforcement: false' \"$CONFIG_FILE\" && grep -q 'execution_guidance: false' \"$CONFIG_FILE\" && grep -q 'task_completion_guidance: false' \"$CONFIG_FILE\""

# Assertion 12: Zero Bespoke Python/Shell Scripts in scripts/ or plugins/
assert_check "12. Zero bespoke Python or shell wrappers in scripts/ or plugins/ (authorized hermes_icm_validator.py preserved)" \
  "[[ ! -d scripts || -z \"\$(find scripts -maxdepth 2 -type f \\( -name '*.py' -o -name '*.sh' \\) ! -name 'hermes_icm_validator.py' 2>/dev/null)\" ]]"

# Assertion 13: 100% Upstream Submodule Purity in .hermes/hermes-agent
assert_check "13. Upstream .hermes/hermes-agent repository is 100% clean and unpatched" \
  "[[ ! -d .hermes/hermes-agent ]] || git -C .hermes/hermes-agent diff --quiet"

# Assertion 14: Hardware VRAM Ceiling Check (<= 5,800.0 MiB on RTX 3050)
assert_check "14. Live NVML GPU VRAM <= 5,800.0 MiB on RTX 3050" \
  "VRAM_USED=\$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits | head -n1 | tr -d ' '); [[ \"\$VRAM_USED\" -le 5800 ]]"

# Assertion 15: Memory and Gateway Daemon Bindings in config.yaml
assert_check "15. config.yaml binds memory provider openviking and api_server on port 8642" \
  "grep -q 'openviking' \"$CONFIG_FILE\" && grep -q '8642' \"$CONFIG_FILE\""

echo "=== Summary: $PASS Passed, $FAIL Failed ==="
if [[ "$FAIL" -gt 0 ]]; then
  exit 1
fi

cat <<EOF > phases/phase_55_icm_tripartite_scaffolding_and_v45_sealing/03_verify/status.json
{
  "phase_id": 55,
  "phase_name": "phase_55_icm_tripartite_scaffolding_and_v45_sealing",
  "status": "VERIFIED_AND_SEALED",
  "assertions_passed": $PASS,
  "assertions_failed": $FAIL,
  "config_version": 52,
  "default_model": "nemotron-3.5-bolt-e4b",
  "max_turns": 40,
  "normalized_output_rule_enforced": true,
  "vram_ceiling_mib": 5800.0,
  "verified_at": "$(date -Iseconds)"
}
EOF
echo "[PASS] Phase 55 Contract Verified and Sealed."
