#!/usr/bin/env bash
# Turnkey Side-by-Side Live Showcase: Hermes TUI (Left) + Splatbox (Right)
set -euo pipefail

BENCH_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${BENCH_DIR}"

# 1. Verify Local Model Server on Port 8138
if ! curl -sf http://127.0.0.1:8138/health >/dev/null 2>&1; then
  echo "Starting Gemma 4 Exact daemon on Port 8138..."
  systemctl --user start llama-server.service
  sleep 4
fi

# 2. Launch Chrome on Right Half (960x1080 at x=960, y=0)
flatpak-spawn --host flatpak run com.google.ChromeDev \
  --remote-debugging-port=9222 \
  --user-data-dir="/tmp/hermes_chrome_debug" \
  --window-position=960,0 \
  --window-size=960,1080 \
  "https://splatbox.alexdiaz.fyi/" >/tmp/chrome_showcase.log 2>&1 &

sleep 2

# 3. Launch Konsole with Hermes TUI on Left Half (960x1080 at x=0, y=0)
flatpak-spawn --host /usr/bin/konsole \
  --qwindowgeometry 960x1080+0+0 \
  --workdir "${BENCH_DIR}" \
  -e bash -c '
    echo "=== [HERMES AGENT OS: LIVE GAUNTLET B TESTBED] ==="
    echo "GPU VRAM: $(nvidia-smi --query-gpu=memory.used --format=csv,noheader) | Display: Wayland eDP-1"
    echo "Starting interactive Hermes TUI with icm-architect..."
    hermes chat --provider local-llama -m gemma-4-E4B-it-qat-exact --skills icm-architect -t "terminal,file,browser,vision"
  ' &

echo "=== [SHOWCASE READY] ==="
echo "Left:  Konsole (Hermes Agent OS TUI)"
echo "Right: Google Chrome (Splatbox 3D Game on Port 9222)"
