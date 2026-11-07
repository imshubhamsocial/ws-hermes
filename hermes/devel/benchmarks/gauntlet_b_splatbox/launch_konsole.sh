#!/usr/bin/env bash
set -euo pipefail

BENCH_DIR="/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/benchmarks/gauntlet_b_splatbox"
UNIT_NAME="hermes-gauntlet-b-icm-compiler"

/usr/bin/distrobox-host-exec systemctl --user stop "${UNIT_NAME}.service" 2>/dev/null || true
/usr/bin/distrobox-host-exec systemctl --user reset-failed "${UNIT_NAME}.service" 2>/dev/null || true

/usr/bin/distrobox-host-exec systemd-run --user --unit="${UNIT_NAME}" \
  --setenv=DISPLAY="${DISPLAY:-:0}" \
  --setenv=WAYLAND_DISPLAY="${WAYLAND_DISPLAY:-wayland-0}" \
  --setenv=XDG_RUNTIME_DIR="/run/user/1000" \
  konsole --separate --hold -p "tabtitle=Gauntlet B - 3-Stage ICM Compiler" \
  -e distrobox enter ws-hermes -- bash -c "${BENCH_DIR}/run_pipeline.sh"
