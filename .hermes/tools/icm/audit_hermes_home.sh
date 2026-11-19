#!/usr/bin/env bash
# Native Hermes Substrate Hygiene & Rule 9 Purity Auditor (26 lines)
set -euo pipefail
HERMES_HOME="${HOME}/.hermes"
UPSTREAM_REPO="${HERMES_HOME}/hermes-agent"

echo "[AUDIT 1/4] Verifying Rule 9 Upstream Substrate Purity..."
if [[ -d "${UPSTREAM_REPO}/.git" ]]; then
  DIRTY="$(git -C "${UPSTREAM_REPO}" status --porcelain)"
  [[ -z "${DIRTY}" ]] || { echo "FAIL: Dirty upstream ${UPSTREAM_REPO}"; exit 1; }
fi

echo "[AUDIT 2/4] Verifying Isolated Profile Fleet (.no-bundled-skills)..."
for BOT in icm-planner icm-scaffolder icm-migrator icm-auditor; do
  test -f "${HERMES_HOME}/profiles/${BOT}/.no-bundled-skills"
  test -f "${HERMES_HOME}/profiles/${BOT}/SOUL.md"
done

echo "[AUDIT 3/4] Enforcing <60 Line Atomic Ceiling on Custom ICM Scripts..."
for SCR in "${HERMES_HOME}"/tools/icm/*.{py,sh} "${HERMES_HOME}"/skills/icm/*/scripts/*.py; do
  [[ -f "${SCR}" ]] || continue
  (( $(wc -l < "${SCR}") < 60 )) || { echo "FAIL: >=60 lines in ${SCR}"; exit 1; }
done

echo "[AUDIT 4/4] Running Custom ICM Skill Unit Tests..."
python3 -m unittest discover -s "${HERMES_HOME}/skills/icm/icm-stage-compiler/tests" -p "test_*.py"
