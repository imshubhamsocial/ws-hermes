#!/usr/bin/env bash
set -euo pipefail

BENCH_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
UNIT_NAME="hermes-gauntlet-b-icm-compiler"

/usr/bin/distrobox-host-exec systemctl --user stop "${UNIT_NAME}.service" 2>/dev/null || true
/usr/bin/distrobox-host-exec systemctl --user reset-failed "${UNIT_NAME}.service" 2>/dev/null || true

MODE="${1:-remediate}"

if [[ "$MODE" == "pipeline" ]]; then
  CMD="bash '${BENCH_DIR}/run_pipeline.sh'"
  TAB="Gauntlet B - 3-Stage Pipeline"
else
  CMD="cd '${BENCH_DIR}' && PROMPT_TEXT=\$(cat '${BENCH_DIR}/PROMPT_REMEDIATION.txt') && export HERMES_TUI_QUERY=\"\$PROMPT_TEXT\" && hermes chat --in '${BENCH_DIR}' --accept-hooks --yolo -s icm-architect --toolsets 'terminal,file,browser,vision' --max-turns 25 -q \"\$PROMPT_TEXT\" --tui -v"
  TAB="Gauntlet B - Remediation"
fi

/usr/bin/distrobox-host-exec systemd-run --user --unit="${UNIT_NAME}" \
  --setenv=DISPLAY="${DISPLAY:-:0}" \
  --setenv=WAYLAND_DISPLAY="${WAYLAND_DISPLAY:-wayland-1}" \
  --setenv=XDG_RUNTIME_DIR="/run/user/1000" \
  konsole --separate --hold -p "tabtitle=${TAB}" \
  -e distrobox enter ws-hermes -- bash -c "${CMD}"
