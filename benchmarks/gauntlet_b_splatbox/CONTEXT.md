# Gauntlet B - Splatbox 3D Paintball CV Targeting Testbed

One job: Certify Hermes Agent OS autonomous Splatbox gameplay via dual-launch ICM benchmark and native window recording.

## Inputs

| Source | File/Location | Section/Scope | Why |
| :--- | :--- | :--- | :--- |
| System Invariants | `../_config/invariants.md` | Network Ports & Hardware | Port 8138 LLM, Port 9222 CDP, VRAM <= 5800 MiB |
| Hardware Invariants | `invariants.md` | Device Ceilings | NVIDIA GPU inference only; Chrome/Konsole on iGPU |
| Benchmark Rules | `rules.md` | Dual-Launch Workflow | Prompting style, per-window recording, and composition |

## Process

> 1. Launch 1 (Weapon Analysis & Bug Fix):
>    - Hermes receives natural language prompt in user style (no spoon-fed coordinates/values).
>    - Hermes analyzes weapon shooting angles/distances and resolves tracking/ballistics bugs in `output/vision_tracker.py` and `output/splatbox_agent.py`.
>    - Record left Konsole TUI window while right side displays native KDE dummy placeholder.
> 2. Launch 2 (Autonomous Execution & Telemetry):
>    - Fresh Hermes launch executes `python3 output/splatbox_agent.py`.
>    - Record left Konsole TUI window executing and monitoring the match.
> 3. Game Capture (Google Chrome Splatbox WebGPU):
>    - Capture real Google Chrome application window (native Breeze frame, tabs, and shadows) running on Intel iGPU via CDP port 9222.
> 4. Master Composition:
>    - Join left runs (Run 1 -> Run 2) and right views (Placeholder -> Chrome WebGPU game) into certified MP4.
> 5. Verification Gate:
>    - Verify `bash contract.sh` passes with exit code 0, frames >= 120, score >= 25, and VRAM <= 5800 MiB.

## Outputs

| Artifact | Location | Format |
| :--- | :--- | :--- |
| Gemma 4 Exact Benchmark | output/splatbox_gemma4_exact.mp4 | 1920x1080 MP4 |
| Stage 1 Maximized TUI | output/splatbox_stage1_maximized.mp4 | 1920x1080 MP4 |
| Master Showcase | output/hermes_splatbox_showcase.mp4 | 1920x1080 MP4 |
| Telemetry Receipt | stages/03-execute/output/telemetry.json | Execution metrics JSON |
| Audit Verification | output/check.md | YAML-frontmattered receipt |

## Check

Run `bash ./contract.sh` and confirm frames >= 120, score >= 25, VRAM <= 5800 MiB, and exit code 0.
