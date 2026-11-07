# Layer 1: Workspace Task Routing Map

## 1. Keyword Triggers

* setup: Run workspace onboarding or verify directory scaffolding via python3 hermes/devel/_tools/hermes_icm_validator.py.
* status: Inspect pipeline completion state across hermes/devel/stages/*/output/check.md and hermes/devel/phases/status_ledger.json.
* walk-test: Execute the cold 8-point ICM Walk Test via python3 hermes/devel/_tools/hermes_icm_validator.py.
* icm-sync: Audit relative links and regenerate context graphs via python3 -I hermes/devel/_tools/links.py . --skip docs --skip phases --skip benchmarks --skip skills.
* quiesce: Stop hermes-llama-server.service and verify GPU VRAM <= 100 MiB via python3 hermes/devel/_tools/check_vram_limit.py --mode quiescent.

## 2. Task Routing Table

| User Objective / Task Description | Target Directory | Entry Contract / Script | Layer / Scope |
| :--- | :--- | :--- | :--- |
| Enter Hermes Agent OS Development Track | `hermes/devel/` | `hermes/devel/CONTEXT.md` | Layer 2 Track |
| Execute Gauntlet B Stage 1 (Browser CDP Probe) | `hermes/devel/stages/01-probe/` | `hermes/devel/stages/01-probe/CONTEXT.md` | Layer 2 Stage |
| Execute Gauntlet B Stage 2 (CPU HoughCircles Aim) | `hermes/devel/stages/02-controller/` | `hermes/devel/stages/02-controller/CONTEXT.md` | Layer 2 Stage |
| Execute Gauntlet B Stage 3 (Action & Telemetry) | `hermes/devel/stages/03-execute/` | `hermes/devel/stages/03-execute/CONTEXT.md` | Layer 2 Stage |
| Run or audit Frontier Gauntlet A (3D Voxel FPS) | `hermes/devel/benchmarks/gauntlet_a_voxel_fps/` | `benchmarks/gauntlet_a_voxel_fps/contract.sh` | Layer 4 Gauntlet |
| Run or audit Frontier Gauntlet B (3D Splatbox CV) | `hermes/devel/benchmarks/gauntlet_b_splatbox/` | `benchmarks/gauntlet_b_splatbox/contract.sh` | Layer 4 Gauntlet |
| Run or audit Frontier Gauntlet C (3D WebGL Aquarium) | `hermes/devel/benchmarks/gauntlet_c_aquarium/` | `benchmarks/gauntlet_c_aquarium/contract.sh` | Layer 4 Gauntlet |
| Access Hermes Project Track Shelf | `hermes/` | `hermes/CONTEXT.md` | Layer 2 Shelf |
| Design or restructure a workspace using ICM | `hermes/devel/skills/icm-architect/` | `hermes/devel/skills/icm-architect/SKILL.md` | Layer 3 Skill |
| Compile a single ICM stage with KV cache isolation | `hermes/devel/_tools/` | `hermes/devel/_tools/hermes_stage_runner.py` | Layer 3 Tool |
| Audit Phase 58 and seal the master status ledger | `hermes/devel/phases/phase_58_autonomous_icm_factory_and_multi_gauntlet_certification/` | `03_verify/contract.sh` | Layer 4 Gate |
| Check system invariants, ports, and VRAM limits | `hermes/devel/_config/` | `hermes/devel/_config/invariants.md` | Layer 3 Config |

## 3. Context Takeover Rule

Once routed to a target stage or benchmark directory, read that directory's local CONTEXT.md and load only the files specified in its Inputs table. Do not load sibling stage folders.
