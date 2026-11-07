# Layer 1: Workspace Task Routing Map

## 1. Keyword Triggers

* setup: Run workspace onboarding or verify directory scaffolding via python3 _tools/hermes_icm_validator.py.
* status: Inspect pipeline completion state across stages/*/output/check.md and phases/status_ledger.json.
* walk-test: Execute the cold 8-point ICM Walk Test via python3 _tools/hermes_icm_validator.py.
* icm-sync: Audit relative links and regenerate context graphs via python3 -I _tools/links.py . --skip docs --skip phases --skip benchmarks --skip skills.
* quiesce: Stop hermes-llama-server.service and verify GPU VRAM <= 100 MiB via python3 _tools/check_vram_limit.py --mode quiescent.

## 2. Task Routing Table

| User Objective / Task Description | Target Directory | Entry Contract / Script | Layer / Scope |
| :--- | :--- | :--- | :--- |
| Execute Project 1 (Hermes) Stage 1 (Browser CDP Probe) | `stages/01-probe/` | `stages/01-probe/CONTEXT.md` | Layer 2 Stage |
| Execute Project 1 (Hermes) Stage 2 (CPU HoughCircles Aim) | `stages/02-controller/` | `stages/02-controller/CONTEXT.md` | Layer 2 Stage |
| Execute Project 1 (Hermes) Stage 3 (Action & Telemetry) | `stages/03-execute/` | `stages/03-execute/CONTEXT.md` | Layer 2 Stage |
| Run or audit Project 1 Gauntlet A (3D Voxel FPS) | `benchmarks/gauntlet_a_voxel_fps/` | `benchmarks/gauntlet_a_voxel_fps/contract.sh` | Layer 4 Gauntlet |
| Run or audit Project 1 Gauntlet B (3D Splatbox CV) | `benchmarks/gauntlet_b_splatbox/` | `benchmarks/gauntlet_b_splatbox/contract.sh` | Layer 4 Gauntlet |
| Run or audit Project 1 Gauntlet C (3D WebGL Aquarium) | `benchmarks/gauntlet_c_aquarium/` | `benchmarks/gauntlet_c_aquarium/contract.sh` | Layer 4 Gauntlet |
| Access Multi-Project Shelf (Project 2+) | `projects/` | `projects/CONTEXT.md` | Layer 2 Shelf |
| Design or restructure a workspace using ICM | `skills/icm-architect/` | `skills/icm-architect/SKILL.md` | Layer 3 Skill |
| Compile a single ICM stage with KV cache isolation | `_tools/` | `_tools/hermes_stage_runner.py` | Layer 3 Tool |
| Audit Phase 58 and seal the master status ledger | `phases/phase_58_autonomous_icm_factory_and_multi_gauntlet_certification/` | `03_verify/contract.sh` | Layer 4 Gate |
| Check system invariants, ports, and VRAM limits | `_config/` | `_config/invariants.md` | Layer 3 Config |

## 3. Context Takeover Rule

Once routed to a target stage or benchmark directory, read that directory's local CONTEXT.md and load only the files specified in its Inputs table. Do not load sibling stage folders.
