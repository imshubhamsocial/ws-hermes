# Stage Contract: Gauntlet A — Voxel Paintball FPS Multiplayer

## Inputs
* Workspace Root Map: ../../AGENTS.md
* Hard Operational Bounds: ./invariants.md
* Procedural Execution Order: ./rules.md
* Upstream Voxel & Netcode Schemas: ./references.md

## Process
> 1. Read ./invariants.md, ./rules.md, and ./references.md to load the upstream Sunwood-ai-labs/threejs-voxel-frontier and nickyvanurk/voidfall schemas.
> 2. Initialize output/voxel-paintball-app/package.json with express, ws, and three dependencies and install via npm install.
> 3. Implement the authoritative WebSocket server in output/voxel-paintball-app/server/server.js (Port 8080, 20 Hz tick loop, room registry, projectile ballistics, and voxel splat broadcast).
> 4. Implement the Three.js client in output/voxel-paintball-app/client/ (index.html, css/style.css, js/main.js, js/engine/voxel_world.js, js/engine/camera_fps.js, js/engine/paintball.js, js/net/socket_sync.js).
> 5. Execute bash ./contract.sh to verify server startup, multi-client WebSocket handshake, paintball hit synchronization, and AST completeness.

## Outputs
* Application Directory: output/voxel-paintball-app/
* Verification Receipt: output/status.json

## Check
* Run bash ./contract.sh and confirm exit code 0 with all assertions passing.
