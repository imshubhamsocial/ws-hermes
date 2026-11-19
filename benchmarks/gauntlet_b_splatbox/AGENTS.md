# Gauntlet B: Splatbox 3D CV Targeting Testbed

## 1. Identity and Task Routing

You operate inside `gauntlet_b_splatbox`. This is a 3-stage Interpretable Context Methodology (ICM) benchmark pipeline verifying closed-loop 3D WebGPU target acquisition and weapon actuation.

| Objective / Task | Location | Purpose |
| :--- | :--- | :--- |
| Stage 1: DOM & PointerLock | `stages/01-probe/` | Attach to CDP port 9222 and verify pointer lock |
| Stage 2: Vision & Semantics | `stages/02-controller/` | Full-screen target detection & embedding verification |
| Stage 3: Live 60s Match | `stages/03-execute/` | Closed-loop AI reflex snap & score destruction |
| Benchmark Contract | `./contract.sh` | Deterministic multi-stage audit gate |
| Browser Arena | `./launch_chrome.sh` | Launch isolated Google Chrome on port 9222 |

## 2. Shared References (Layer 3 Factory)

- Invariants: `../../_config/invariants.md` (VRAM <= 5,800 MiB, Port 9222)
- Schemas: `../../shared/vision_schemas.md` (Centroid ballistics, HSV masking)
- Blueprint: `references/splatbox_dom_cdp.md` (CDP dispatch protocols)

## 3. Compiler Rules

1. Bounded Context: When compiling a stage, launch Hermes with `--in stages/<stage>` so context loads only the local `CONTEXT.md`.
2. Relative Paths Only: Never hardcode `/var/home/...`. Use exact relative paths from the current stage.
3. Atomic Modules: Every script in `output/` must be strictly under 60 lines.
4. Level Horizon Invariant: Keep `movementY: 0` to preserve camera horizon lock and prevent grass/sky clipping.
