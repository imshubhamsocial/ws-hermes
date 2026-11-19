#!/usr/bin/env bash
# Proven AGY Konsole TUI Launcher: Hermes (Left) + Chrome Dev (Right)
set -euo pipefail

BENCH_DIR="/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/hermes/devel/benchmarks/gauntlet_b_splatbox"
cd "${BENCH_DIR}"

# 1. Ensure Local Inference Server is Healthy
if ! curl -sf http://127.0.0.1:8138/health >/dev/null 2>&1; then
  echo "Restoring local Gemma 4 Exact daemon..."
  python3 /var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/.local/bin/hermes-supervisor ensure
  sleep 3
fi

# 2. Launch Chrome on Right Half (960,0 960x1080)
flatpak-spawn --host flatpak run com.google.ChromeDev \
  --remote-debugging-port=9222 \
  --user-data-dir="/tmp/hermes_chrome_debug" \
  --window-position=960,0 \
  --window-size=960,1080 \
  "https://splatbox.alexdiaz.fyi/" >/tmp/chrome_tui.log 2>&1 &

sleep 2

# 3. Launch Konsole with Hermes in TUI Mode on Left Half (0,0 960x1080)
flatpak-spawn --host systemctl --user stop hermes-splatbox-tui.service 2>/dev/null || true
flatpak-spawn --host systemctl --user reset-failed hermes-splatbox-tui.service 2>/dev/null || true
flatpak-spawn --host systemd-run --user --unit=hermes-splatbox-tui \
  --setenv=WAYLAND_DISPLAY="wayland-1" \
  --setenv=DISPLAY=":0" \
  --setenv=XDG_RUNTIME_DIR="/run/user/1000" \
  /usr/bin/konsole --separate \
  --qwindowgeometry 960x1080+0+0 \
  -p "tabtitle=Hermes Agent OS (TUI Mode)" \
  --workdir "${BENCH_DIR}" \
  -e distrobox enter ws-hermes -- hermes chat --in "${BENCH_DIR}" \
    --provider local-llama -m gemma-4-E4B-it-qat-exact \
    --skills icm-architect --accept-hooks --tui --yolo \
    -q "Execute Gauntlet B: autonomous Splatbox 3D gameplay target acquisition. Reason over 3D ballistics, coordinate with vision tracker, and destroy all bullseyes."

echo "=== [HERMES TUI LAUNCHED ON DESKTOP] ==="
echo "Left Pane : Konsole (Hermes Full TUI Interface with Live Reasoning)"
echo "Right Pane: Google Chrome (Splatbox 3D WebGPU Arena on Port 9222)"
