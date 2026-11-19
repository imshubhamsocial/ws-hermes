#!/usr/bin/env bash
set -euo pipefail
PROFILES=("icm-planner" "icm-scaffolder" "icm-migrator" "icm-auditor")
for BOT in "${PROFILES[@]}"; do
  hermes profile create "${BOT}" --no-skills --no-alias
  mkdir -p "${HOME}/.hermes/profiles/${BOT}/memories"
done
hermes profile describe icm-planner --text "Pre-coding Socratic spec interviewer and Goldfish gate controller."
hermes profile describe icm-scaffolder --text "Greenfield 5-layer ICM workspace generator and contract compiler."
hermes profile describe icm-migrator --text "Brownfield AST 5-bucket repository classifier and refactorer."
hermes profile describe icm-auditor --text "Read-only deterministic ICM token, line-ceiling, and substrate auditor."
mkdir -p "${HOME}/.hermes/tools/icm"
for BOT in "${PROFILES[@]}"; do
  test -f "${HOME}/.hermes/profiles/${BOT}/.no-bundled-skills"
done
echo "PROVISION_PASS: All 4 isolated ICM profiles initialized with zero bundled skills."
