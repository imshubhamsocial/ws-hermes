#!/usr/bin/env bash
# Hermes TUI Konsole Launcher for Gauntlet A - Voxel Paintball (ICM 3-Stage Pipeline)
set -euo pipefail
WORKSPACE_DIR="/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/benchmarks/gauntlet_a_voxel_fps"
UNIT="hermes-gauntlet-a-voxel-fps"
SKILL="icm-architect"

STAGE="${1:-}"
if [[ -z "$STAGE" ]]; then
  if [[ -t 0 ]]; then
    echo "Select Stage to launch for Gauntlet A (Voxel Paintball):"
    echo "  1) Stage 1: Specification, Dependency Installation & Authoritative Server (max-turns 12)"
    echo "  2) Stage 2: Modular Three.js Voxel Engine, FPS Physics & Netcode Client (max-turns 12)"
    echo "  3) Stage 3: Fresh Verification Gate, Two-Client WebSocket Smoke Test & Sealing (max-turns 10)"
    echo "  4) Stage 4: Runtime Browser Remediation & Zero Console Errors (max-turns 12)"
    read -rp "Enter selection [1-4, default 4]: " choice
    STAGE="${choice:-4}"
  else
    STAGE="4"
  fi
fi

case "$STAGE" in
  1)
    PROMPT_FILE="$WORKSPACE_DIR/PROMPT_STAGE1.txt"
    MAX_TURNS=12
    STAGE_LABEL="Stage 1 (Spec & Server)"
    ;;
  2)
    PROMPT_FILE="$WORKSPACE_DIR/PROMPT_STAGE2.txt"
    MAX_TURNS=12
    STAGE_LABEL="Stage 2 (Modular Client)"
    ;;
  3)
    PROMPT_FILE="$WORKSPACE_DIR/PROMPT_STAGE3.txt"
    MAX_TURNS=10
    STAGE_LABEL="Stage 3 (Verification & Sealing)"
    ;;
  4|remediate)
    PROMPT_FILE="$WORKSPACE_DIR/PROMPT_REMEDIATION.txt"
    MAX_TURNS=12
    STAGE_LABEL="Stage 4 (Runtime Browser Remediation)"
    ;;
  *)
    echo "Invalid stage: $STAGE. Choose 1, 2, 3, or 4."
    exit 1
    ;;
esac

echo "Resetting any previous $UNIT systemd unit..."
/usr/bin/distrobox-host-exec systemctl --user reset-failed "$UNIT.service" 2>/dev/null || true
/usr/bin/distrobox-host-exec systemctl --user stop "$UNIT.service" 2>/dev/null || true

echo "Launching Gauntlet A - $STAGE_LABEL inside Konsole window on desktop..."
/usr/bin/distrobox-host-exec systemd-run --user --unit="$UNIT" \
  --setenv=WAYLAND_DISPLAY="wayland-0" \
  --setenv=DISPLAY=":0" \
  --setenv=XDG_RUNTIME_DIR="/run/user/1000" \
  konsole --separate --hold \
    -p "tabtitle=Gauntlet A - $STAGE_LABEL" \
    -e distrobox enter ws-hermes -- /bin/bash -l -c "
      cd '$WORKSPACE_DIR' && \
      echo '=== Starting Hermes TUI Session for Gauntlet A - $STAGE_LABEL ===' && \
      PROMPT_TEXT=\"\$(cat '$PROMPT_FILE')\" && \
      export HERMES_TUI_QUERY=\"\$PROMPT_TEXT\" && \
      hermes chat --in '$WORKSPACE_DIR' --accept-hooks -s '$SKILL' --max-turns $MAX_TURNS -q \"\$PROMPT_TEXT\" --tui -v
    "

echo "Spawned $UNIT.service ($STAGE_LABEL) on host desktop."
