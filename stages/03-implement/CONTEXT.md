# Stage 03 Contract: Atomic Module Production (03-implement)

## Inputs

| Source | File/Location | Section/Scope | Why |
| :--- | :--- | :--- | :--- |
| Topology Manifest | stages/02-scaffold/output/topology_manifest.json | All | Verified module specifications and path bindings |
| Blueprint Reorganization | docs/research/GDR40/Output/GDR40 Chronological Blueprint Reorganization.md | Section 7.2-7.6 | Certified Code Blocks 14 through 18 |
| Conventions | _config/conventions.md | All | Atomic < 60 line ceiling and ASD-STE100 active prose |

## Process Steps

1. Synthesize all five atomic WebGL2 modules in `output/aquarium-sim/js/`:
   - `wave_pde.js` (Code Block 14, 40 lines): 2D Damped wave equation leapfrog stencil.
   - `caustics_shader.js` (Code Block 15, 37 lines): Snell's law refraction and floor projection.
   - `sphere_physics.js` (Code Block 16, 35 lines): Spherical-cap submerged buoyancy and drag.
   - `boids_fish.js` (Code Block 17, 48 lines): 3D Reynolds boids with obstacle avoidance.
   - `main.js` (Code Block 18, 43 lines): 60 FPS loop exporting `__AQUARIUM_TELEMETRY__`.
2. Ensure each module strictly contains under 60 lines.
3. Emit implementation receipt and summary report in `stages/03-implement/output/`.
4. Verify stage structure using `~/.hermes/skills/icm/icm-stage-compiler/scripts/verify_stage.py stages/03-implement`.

## Outputs

| Artifact | Target Path | Verification |
| :--- | :--- | :--- |
| Implementation Receipt | stages/03-implement/output/implementation_receipt.json | verify_stage.py |
| Module Summary | stages/03-implement/output/module_summary.md | verify_stage.py |
