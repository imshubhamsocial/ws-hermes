# Gauntlet C: 3D WebGL Aquarium Simulation Testbed

## 1. Identity and Task Routing

You operate inside `gauntlet_c_aquarium`. This is a 4-stage Interpretable Context Methodology (ICM) benchmark pipeline verifying WebGL2 differential area caustics, dual-framebuffer wave PDE ping-pong, and rigid sphere buoyancy.

| Objective / Task | Location | Purpose |
| :--- | :--- | :--- |
| Stage 1: Socratic Spec | `stages/01-spec/` | Mathematical regimes & Goldfish review gate |
| Stage 2: Topology Scaffolding | `stages/02-scaffold/` | Module contract signatures & line limits |
| Stage 3: Atomic Synthesis | `stages/03-implement/` | 5 atomic JavaScript modules (<60 lines) |
| Stage 4: POSIX & CDP Verification | `stages/04-verify/` | Headless Chromium 60 FPS verification |
| Benchmark Contract | `./contract.sh` | Deterministic 4-gate verification suite |

## 2. Shared References (Layer 3 Factory)

- Invariants: `../_config/invariants.md` (VRAM <= 5,800 MiB, Port 8138)
- Schemas: `../../shared/shader_conventions.md` (GLSL dFdx/dFdy area ratio)
- Ceilings: `../_config/hardware_ceilings.md` (Discrete GPU memory limits)

## 3. Compiler Rules

1. Bounded Context: When compiling a stage, launch Hermes with `--in stages/<stage>` so context loads only the local `CONTEXT.md`.
2. Relative Paths Only: Never hardcode `/var/home/...`. Use exact relative paths from the current stage.
3. Atomic Modules: Every JavaScript module in `output/aquarium-sim/js/` must be strictly under 60 lines.
4. Clamped Buoyancy: Strictly clamp submerged volume to 0.0 when ds <= 0.0 and (4/3)*PI*r^3 when ds >= 2r.
