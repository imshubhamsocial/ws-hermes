---
name: voxel-fps-game-dev
description: Build a voxel FPS multiplayer game with websockets.
---
# Voxel FPS Game Development Workflow

This skill guides the construction of a complete, production-ready voxel FPS multiplayer game, grounding the voxel arena and HUD in `Sunwood-ai-labs/threejs-voxel-frontier` and the authoritative Node.js + `ws` server in `nickyvanurk/voidfall`.

## Procedure
1. **Context Review:** Read `CONTEXT.md`, `invariants.md`, `rules.md`, and `references.md` to establish constraints and preferences.
2. **Client Implementation:** Implement client-side logic (`VoxelWorld`, `CameraFPS`, `Paintball`) using Three.js, ensuring physics (WASD + jump, gravity: -24.0 m/s^2) and networking (`socket_sync.js`) are integrated.
3. **Server Implementation:** Implement the authoritative Node.js + `ws` server on Port 8080, ensuring a 20Hz snapshot tick, client seq/ack prediction, and parabolic ballistics.
4. **Verification Script:** Create `contract.sh` to automate the live two-client WebSocket synchronization test.
5. **Execution & Verification:** Run `bash contract.sh` from the project root to verify live synchronization.
6. **Finalization:** Write `output/status.json` upon successful verification (exit code 0 and receipt file).

## Pitfalls
* **File Overwrite:** Always read existing files (`read_file`) before attempting `write_file` to prevent refusal errors.
* **Verification Setup:** Before running `contract.sh`, verify system dependencies (e.g., use `ss -tlnp | grep 8080` instead of `nc -z 127.0.0.1 8080` if `nc` is missing) and ensure the `workdir` is correctly set in the `terminal` call.
* **State Tracking:** Track multi-step work using `todo_list` and reference code as `path:line` instead of pasting whole files.

## References
references/game-specs.md: Critical Context (Port 8080, Tick Rate 20Hz, Gravity -24.0 m/s^2, Arena 32x16x32).
