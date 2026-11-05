#!/usr/bin/env bash
# Hermes TUI Konsole Launcher for Gauntlet F - diagram-design Visualizer (ICM 3-Stage Pipeline)
set -euo pipefail
WORKSPACE_DIR="/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/benchmarks/diagram_design_eval"
UNIT="hermes-gauntlet-f-diagram"
SKILL="icm-architect,diagram-design"

STAGE="${1:-}"
if [[ -z "$STAGE" ]]; then
  if [[ -t 0 ]]; then
    echo "Select Stage to launch for Gauntlet F (diagram-design Visualizer):"
    echo "  1) Stage 1: Archetype 01 4px Grid Geometry & Complexity Spec (max-turns 10)"
    echo "  2) Stage 2: Editorial HTML + Inline SVG Synthesis (max-turns 10)"
    echo "  3) Stage 3: XML DOM & 4px Grid Geometry Verification (max-turns 8)"
    read -rp "Enter selection [1-3, default 1]: " choice
    STAGE="${choice:-1}"
  else
    STAGE="1"
  fi
fi

case "$STAGE" in
  1)
    PROMPT_FILE="$WORKSPACE_DIR/PROMPT_STAGE1.txt"
    MAX_TURNS=10
    STAGE_LABEL="Stage 1 (Grid Layout Spec)"
    ;;
  2)
    PROMPT_FILE="$WORKSPACE_DIR/PROMPT_STAGE2.txt"
    MAX_TURNS=10
    STAGE_LABEL="Stage 2 (HTML & SVG Synthesis)"
    ;;
  3)
    PROMPT_FILE="$WORKSPACE_DIR/PROMPT_STAGE3.txt"
    MAX_TURNS=8
    STAGE_LABEL="Stage 3 (Verification & Sealing)"
    ;;
  *)
    echo "Invalid stage: $STAGE. Choose 1, 2, or 3."
    exit 1
    ;;
esac

echo "Resetting any previous $UNIT systemd unit..."
/usr/bin/distrobox-host-exec systemctl --user reset-failed "$UNIT.service" 2>/dev/null || true
/usr/bin/distrobox-host-exec systemctl --user stop "$UNIT.service" 2>/dev/null || true

echo "Launching Gauntlet F - $STAGE_LABEL inside Konsole window on desktop..."
/usr/bin/distrobox-host-exec systemd-run --user --unit="$UNIT" \
  --setenv=WAYLAND_DISPLAY="wayland-0" \
  --setenv=DISPLAY=":0" \
  --setenv=XDG_RUNTIME_DIR="/run/user/1000" \
  konsole --separate --hold \
    -p "tabtitle=Gauntlet F - $STAGE_LABEL" \
    -e distrobox enter ws-hermes -- /bin/bash -l -c "
      cd '$WORKSPACE_DIR' && \
      echo '=== Starting Hermes TUI Session for Gauntlet F - $STAGE_LABEL ===' && \
      PROMPT_TEXT=\"\$(cat '$PROMPT_FILE')\" && \
      export HERMES_TUI_QUERY=\"\$PROMPT_TEXT\" && \
      hermes chat --in '$WORKSPACE_DIR' --accept-hooks -s '$SKILL' --max-turns $MAX_TURNS -q \"\$PROMPT_TEXT\" --tui -v
    "

echo "Spawned $UNIT.service ($STAGE_LABEL) on host desktop."
