# Gauntlet A: Voxel Paintball FPS Multiplayer Testbed

## 1. Identity and Task Routing

You operate inside `gauntlet_a_voxel_fps`. This is a single-stage Interpretable Context Methodology (ICM) benchmark pipeline verifying authoritative 3D multiplayer WebSocket netcode, instanced voxel rendering, and parabolic paintball physics.

| Objective / Task | Location | Purpose |
| :--- | :--- | :--- |
| Single-Pass Compilation | `CONTEXT.md` | Authoritative server & Three.js client contract |
| Benchmark Contract | `./contract.sh` | Deterministic netcode & compilation gate |
| Visual Telemetry | `output/` | Rendered screenshots and execution receipts |

## 2. Shared References (Layer 3 Factory)

- Invariants: `../../_config/invariants.md` (Port 8080, 20 Hz tick loop)
- Schemas: `../../shared/netcode_protocol.md` (WebSocket sync protocol)
- Blueprint: `references/game-specs.md` (Voxel world & weapon specifications)

## 3. Compiler Rules

1. Bounded Context: When compiling this benchmark, launch Hermes with `--in benchmarks/gauntlet_a_voxel_fps` so context loads only the local `CONTEXT.md`.
2. Relative Paths Only: Never hardcode `/var/home/...`. Use exact relative paths from this directory.
3. Atomic Modules: Every script in `output/` must be strictly under 60 lines.
4. Authoritative Netcode: Server must enforce 20 Hz tick loop and handle all hit detection.
