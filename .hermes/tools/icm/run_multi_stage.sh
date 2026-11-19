#!/usr/bin/env bash
set -euo pipefail
WORKSPACE_ROOT="${1:-.}"
VERIFY_SCRIPT="${HOME}/.hermes/skills/icm/icm-stage-compiler/scripts/verify_stage.py"
python3 "${WORKSPACE_ROOT}/_tools/egm_goldfish_gate.py" "${WORKSPACE_ROOT}/stages/01-spec/CONTEXT.md"
for STAGE_DIR in "${WORKSPACE_ROOT}"/stages/[0-9][0-9]-*; do
  STAGE_NAME="$(basename "${STAGE_DIR}")"
  echo "=== [ICM RUNNER] Starting Clean Session for ${STAGE_NAME} ==="
  python3 "${VERIFY_SCRIPT}" "${STAGE_DIR}"
  hermes chat --oneshot -q \
    "Read ${STAGE_DIR}/CONTEXT.md. Load only declared inputs. Write outputs to ${STAGE_DIR}/output/."
  if [[ -x "${STAGE_DIR}/contract.sh" ]]; then
    bash "${STAGE_DIR}/contract.sh"
  fi
  echo "=== [ICM RUNNER] Stage ${STAGE_NAME} Verified & Context Wiped ==="
done
echo "PIPELINE_COMPLETE: All ICM stages compiled in ${WORKSPACE_ROOT}."
