# Layer 1: Benchmark Suite Routing Table (benchmarks/)

## 1. Intent-to-Directory Routing Matrix

| Benchmark Track | Directory | Modality / Domain | Primary Contract |
| :--- | :--- | :--- | :--- |
| Gauntlet A | `gauntlet_a_voxel_fps/` | 3D Netcode, 20 Hz Tick, WebSocket sync | `gauntlet_a_voxel_fps/contract.sh` |
| Gauntlet B | `gauntlet_b_splatbox/` | CV Aim-Assist, Chrome CDP, PointerLock | `gauntlet_b_splatbox/contract.sh` |
| Gauntlet C | `gauntlet_c_aquarium/` | WebGL2 GPGPU Wave PDE, Snell Refraction | `gauntlet_c_aquarium/contract.sh` |
| Diagram Design | `diagram_design_eval/` | Procedural SVG/HTML architecture diagrams | `diagram_design_eval/contract.sh` |
| FFmpeg Skill | `ffmpeg_skill_eval/` | Audio/video transcode & media assembly | `ffmpeg_skill_eval/contract.sh` |
| AST-Grep | `ast_grep_eval/` | Structural code search & AST rewriting | `ast_grep_eval/CONTEXT.md` |
| GAIA Agent | `gaia/` | Multi-modal reasoning & browser action | `gaia/CONTEXT.md` |
| LeanREA | `leanrea_eval/` | Formal verification & proof scaffolding | `leanrea_eval/contract.sh` |
| MarkItDown | `markitdown_eval/` | Multi-modal document ingestion & GFM | `markitdown_eval/contract.sh` |
| Tau-Bench | `tau_bench/` | Policy-driven multi-turn customer DB | `tau_bench/CONTEXT.md` |

## 2. Global Substrate Invariants

* Hardware Ceilings: `../_config/hardware_ceilings.md` (RTX 3050 <= 5800.0 MiB VRAM).
* Network & Port Invariants: `../_config/invariants.md` (llama-server: 8138, Chrome CDP: 9222).
* Coding & Script Ceiling: `../_config/conventions.md` (Strictly < 60 lines per script).

## 3. Automation Targets

* Run All Gauntlets: `make run-all-gauntlets` from the workspace root.
* Launch Multi-Konsole View: `bash benchmarks/launch_all_konsole.sh`.
