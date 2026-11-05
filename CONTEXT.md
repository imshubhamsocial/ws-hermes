# Layer 1: Workspace Task Routing Map

## 1. Keyword Triggers

* setup: Run workspace onboarding or verify directory scaffolding via python3 _tools/hermes_icm_validator.py.
* status: Inspect pipeline completion state across stages/*/output/check.md and phases/status_ledger.json.
* walk-test: Execute the cold 8-point ICM Walk Test via python3 _tools/hermes_icm_validator.py.
* quiesce: Stop hermes-llama-server.service and verify GPU VRAM <= 100 MiB via python3 _tools/check_vram_limit.py --mode quiescent.

## 2. Task Routing Table

| User Objective / Task Description | Target Directory | Entry Contract / Script |
| :--- | :--- | :--- |
| Execute Gauntlet B Stage 1 (Browser CDP Probe) | stages/01-probe/ | stages/01-probe/CONTEXT.md |
| Execute Gauntlet B Stage 2 (CPU HoughCircles Aim) | stages/02-controller/ | stages/02-controller/CONTEXT.md |
| Execute Gauntlet B Stage 3 (Action & Telemetry) | stages/03-execute/ | stages/03-execute/CONTEXT.md |
| Run or audit Frontier Gauntlet A (3D Voxel FPS) | benchmarks/gauntlet_a_voxel_fps/ | benchmarks/gauntlet_a_voxel_fps/contract.sh |
| Run or audit Frontier Gauntlet B (3D Splatbox CV) | benchmarks/gauntlet_b_splatbox/ | benchmarks/gauntlet_b_splatbox/contract.sh |
| Run or audit Frontier Gauntlet C (3D WebGL Aquarium) | benchmarks/gauntlet_c_aquarium/ | benchmarks/gauntlet_c_aquarium/contract.sh |
| Design or restructure a workspace using ICM | skills/icm-architect/ | skills/icm-architect/SKILL.md |
| Compile a single ICM stage with KV cache isolation | _tools/ | _tools/hermes_stage_runner.py |
| Audit Phase 58 and seal the master status ledger | phases/phase_58_autonomous_icm_factory_and_multi_gauntlet_certification/ | 03_verify/contract.sh |
| Check system invariants, ports, and VRAM limits | _config/ | invariants.md |

## 3. Context Takeover Rule

Once routed to a target stage or benchmark directory, read that directory's local CONTEXT.md and load only the files specified in its Inputs table. Do not load sibling stage folders.
