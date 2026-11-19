# Stage 01 Contract: Socratic Specification & PDE Intent Scoping (01-spec)

## Inputs

| Source | File/Location | Section/Scope | Why |
| :--- | :--- | :--- | :--- |
| Mathematical Physics Specification | docs/research/GDR40/Output/GDR40 Chronological Blueprint Reorganization.md | Section 7.1 | 14 certified governing equations across 4 discrete physical regimes |
| Hardware Ceilings | _config/hardware_ceilings.md | All | Enforce RTX 3050 <= 5800.0 MiB and Intel iGPU Wayland offload |
| Conventions | _config/conventions.md | All | Atomic < 60 line modular scripts and ASD-STE100 active prose |

## Process Steps

1. Structure the 14 governing equations into exactly 4 decoupled mathematical regimes plus 1 WebGL2 orchestrator:
   - Regime A (wave_pde.js, 40 lines): 2D Damped Wave PDE solved via explicit leapfrog finite-difference stencil on a 256x256 RGBA32F texture (0.25 MiB state, CFL^2 = 0.22 <= 0.5 von Neumann stability).
   - Regime B (caustics_shader.js, 37 lines): Analytical vector Snell's law refraction (eta = 0.7501875) projected onto floor plane y = -1.0 with screen-space dFdx/dFdy differential area ratio.
   - Regime C (sphere_physics.js, 35 lines): Single buoyant sphere (R=0.18, rho_s=650.0) with closed-form spherical-cap submerged volume V_sub(d) = (pi*d^2/3)*(3R - d), quadratic drag, and symplectic Euler integration.
   - Regime D (boids_fish.js, 49 lines): Exactly N=24 autonomous fish boids with separation, velocity alignment, centroid cohesion, obstacle repulsion, and velocity clamping [0.15, 0.55].
   - Orchestrator (main.js, 43 lines): 60 FPS WebGL2 render loop exporting window.__AQUARIUM_TELEMETRY__.
2. Enforce discrete VRAM allocation bounds: Total simulation texture and buffer memory is under 10.0 MiB; inference server uses ~5,053.0 MiB; total discrete VRAM remains under 5,065.0 MiB (safety ceiling: 5,800.0 MiB).
3. Validate atomic line ceilings: All 5 JavaScript modules in output/aquarium-sim/js/ contain strictly between 35 and 49 lines each (all < 60 lines).
4. Run _tools/egm_goldfish_gate.py to verify zero BLOCKER findings across Comprehension, Design Critic, and Readiness lenses.

## Outputs

| Artifact | Location | Format | Verification |
| :--- | :--- | :--- | :--- |
| Goldfish Review Report | stages/01-spec/output/goldfish_review_report.json | JSON | egm_goldfish_gate.py status PASS |
| Concepts Brief | stages/01-spec/output/concepts_brief.md | Markdown | verify_stage.py |

## Verification & Check

* Verification: python3 _tools/egm_goldfish_gate.py stages/01-spec/CONTEXT.md
* Check: [x] status == PASS in stages/01-spec/output/goldfish_review_report.json; [x] missing_sections == []; [x] zero BLOCKER findings.
