# Stage 02 Contract: Workspace Topology & Module Contracts (02-scaffold)

## Inputs

| Source | File/Location | Section/Scope | Why |
| :--- | :--- | :--- | :--- |
| Stage 01 Brief | ../01-spec/output/concepts_brief.md | All | Certified 4 mathematical regimes and module scopes |
| Conventions | _config/conventions.md | All | Atomic < 60 line ceiling and ASD-STE100 active prose |
| Hardware Ceilings | _config/hardware_ceilings.md | All | RTX 3050 <= 5800.0 MiB discrete memory limit |

## Process Steps

1. Scaffold module topology for `output/aquarium-sim/js/` and contract path `benchmarks/gauntlet_c_aquarium/contract.sh`.
2. Define interface signatures and atomic line bounds for the 5 WebGL2 modules:
   - `wave_pde.js`: Class `WavePDESolver` (< 60 lines)
   - `caustics_shader.js`: Functions `buildCausticsProgram` and GLSL sources (< 60 lines)
   - `sphere_physics.js`: Class `BuoyantSphere` (< 60 lines)
   - `boids_fish.js`: Class `BoidsFlock` (< 60 lines)
   - `main.js`: Function `startAquariumSimulation` with `__AQUARIUM_TELEMETRY__` (< 60 lines)
3. Emit topology manifest `output/topology_manifest.json` and scaffold report.
4. Verify stage structure using `~/.hermes/skills/icm/icm-stage-compiler/scripts/verify_stage.py`.

## Outputs

| Artifact | Target Path | Verification |
| :--- | :--- | :--- |
| Topology Manifest | output/topology_manifest.json | verify_stage.py |
| Scaffold Report | output/scaffold_report.md | verify_stage.py |

## Check

Run python3 -m json.tool output/topology_manifest.json and verify all 5 modules exist.
