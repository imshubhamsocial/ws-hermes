#!/usr/bin/env bash
# Master Gauntlet Konsole Launcher (ICM 3-Stage Pipeline)
set -euo pipefail

BASE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Available Gauntlets:"
echo "  1) gauntlet_a_voxel_fps   (Multiplayer Voxel FPS with WebSockets)"
echo "  2) gauntlet_b_splatbox    (Autonomous Splatbox Browser Gaming via CDP)"
echo "  3) gauntlet_c_aquarium    (3D WebGL Aquarium Simulation)"
echo "  4) leanrea_eval           (leanrea Zero-MCP Reverse Engineering)"
echo "  5) ffmpeg_skill_eval      (ffmpeg-skill Local Video Editor SPEC)"
echo "  6) diagram_design_eval    (diagram-design Editorial HTML+SVG)"
echo "  7) markitdown_eval        (microsoft/markitdown Document Ingestion)"
echo "  all) Launch all 7 gauntlets for a given stage"
echo ""

read -rp "Enter gauntlet selection [1-7 or all]: " choice
read -rp "Enter stage to launch [1-3, default 1]: " stage_choice
STAGE="${stage_choice:-1}"

case "$choice" in
  1) bash "$BASE/gauntlet_a_voxel_fps/launch_konsole.sh" "$STAGE" ;;
  2) bash "$BASE/gauntlet_b_splatbox/launch_konsole.sh" "$STAGE" ;;
  3) bash "$BASE/gauntlet_c_aquarium/launch_konsole.sh" "$STAGE" ;;
  4) bash "$BASE/leanrea_eval/launch_konsole.sh" "$STAGE" ;;
  5) bash "$BASE/ffmpeg_skill_eval/launch_konsole.sh" "$STAGE" ;;
  6) bash "$BASE/diagram_design_eval/launch_konsole.sh" "$STAGE" ;;
  7) bash "$BASE/markitdown_eval/launch_konsole.sh" "$STAGE" ;;
  all)
    for g in gauntlet_a_voxel_fps gauntlet_b_splatbox gauntlet_c_aquarium leanrea_eval ffmpeg_skill_eval diagram_design_eval markitdown_eval; do
      bash "$BASE/$g/launch_konsole.sh" "$STAGE" &
      sleep 1
    done
    ;;
  *) echo "Unknown option $choice" ;;
esac
