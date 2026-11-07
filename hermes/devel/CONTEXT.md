# Layer 1: Hermes Agent OS Development Task Routing Map

## 1. Local Triggers

* `gauntlet-a`: Execute Frontier Gauntlet A via `bash benchmarks/gauntlet_a_voxel_fps/contract.sh`.
* `gauntlet-b`: Execute Gauntlet B via `bash benchmarks/gauntlet_b_splatbox/contract.sh`.
* `gauntlet-c`: Execute Gauntlet C via `bash benchmarks/gauntlet_c_aquarium/contract.sh`.
* `stage-probe`: Execute Stage 1 via `stages/01-probe/CONTEXT.md`.
* `stage-ctrl`: Execute Stage 2 via `stages/02-controller/CONTEXT.md`.
* `stage-exec`: Execute Stage 3 via `stages/03-execute/CONTEXT.md`.

## 2. Stage Routing Table

| Task Description | Target Directory | Entry Contract | Layer / Scope |
| :--- | :--- | :--- | :--- |
| Gauntlet B Stage 1 (Browser CDP Probe) | `stages/01-probe/` | `stages/01-probe/CONTEXT.md` | Layer 2 Stage |
| Gauntlet B Stage 2 (CPU HoughCircles Aim) | `stages/02-controller/` | `stages/02-controller/CONTEXT.md` | Layer 2 Stage |
| Gauntlet B Stage 3 (Action & Telemetry) | `stages/03-execute/` | `stages/03-execute/CONTEXT.md` | Layer 2 Stage |
| Frontier Gauntlet A (3D Voxel FPS) | `benchmarks/gauntlet_a_voxel_fps/` | `benchmarks/gauntlet_a_voxel_fps/contract.sh` | Layer 4 Gauntlet |
| Frontier Gauntlet B (3D Splatbox CV) | `benchmarks/gauntlet_b_splatbox/` | `benchmarks/gauntlet_b_splatbox/contract.sh` | Layer 4 Gauntlet |
| Frontier Gauntlet C (3D WebGL Aquarium) | `benchmarks/gauntlet_c_aquarium/` | `benchmarks/gauntlet_c_aquarium/contract.sh` | Layer 4 Gauntlet |
| Phase 58 Certification Gate | `phases/phase_58_autonomous_icm_factory_and_multi_gauntlet_certification/` | `03_verify/contract.sh` | Layer 4 Gate |

## 3. Context Takeover Rule

Once routed to a stage or gauntlet directory, load only the files listed in that stage's Inputs table. Do not load sibling stages.
