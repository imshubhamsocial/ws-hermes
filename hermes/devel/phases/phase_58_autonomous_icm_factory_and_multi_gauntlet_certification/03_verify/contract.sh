#!/usr/bin/env bash
# Phase 58 Deterministic Verification Contract (GDR36 Master Certification)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
cd "$PROJECT_ROOT"

echo "[Phase 58] 1/7 Verifying Upstream .hermes/hermes-agent Submodule Purity..."
git -C /var/home/imshubhamsocial/.hermes/hermes-agent diff --quiet
git -C /var/home/imshubhamsocial/.hermes/hermes-agent status --porcelain | grep -q "^" && exit 1 || true

echo "[Phase 58] 2/7 Executing 8-Point ICM Walk Test & Static Link Validator..."
python3 _tools/hermes_icm_validator.py

echo "[Phase 58] 3/7 Verifying icm-architect Skill Registration..."
test -f skills/icm-architect/SKILL.md

echo "[Phase 58] 4/7 Auditing Gauntlet A (3D Voxel FPS & 20 Hz Netcode)..."
bash benchmarks/gauntlet_a_voxel_fps/contract.sh

echo "[Phase 58] 5/7 Auditing Gauntlet B (3-Stage ICM Splatbox CV Pipeline)..."
python3 _tools/hermes_stage_runner.py --stage-dir stages/01-probe --gate-mode autonomous --verify-only
python3 _tools/hermes_stage_runner.py --stage-dir stages/02-controller --gate-mode autonomous --verify-only
python3 _tools/hermes_stage_runner.py --stage-dir stages/03-execute --gate-mode autonomous --verify-only
bash benchmarks/gauntlet_b_splatbox/contract.sh

echo "[Phase 58] 6/7 Auditing Gauntlet C (3D WebGL Aquarium & Buoyancy)..."
bash benchmarks/gauntlet_c_aquarium/contract.sh

echo "[Phase 58] 7/7 Verifying RTX 3050 Hardware Quiescence & Ledger Integrity..."
if systemctl --user is-active --quiet hermes-llama-server.service; then
    python3 _tools/check_vram_limit.py --mode active --max-active 5800.0
else
    python3 _tools/check_vram_limit.py --mode quiescent --max-quiescent 100.0
fi
python3 -m json.tool phases/status_ledger.json > /dev/null

echo "[PASS] Phase 58 Autonomous ICM Software Factory & Multi-Gauntlet Suite Certified (Exit 0)."
