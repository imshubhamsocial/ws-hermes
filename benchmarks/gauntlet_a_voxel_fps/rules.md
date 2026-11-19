# Procedural Rules: Gauntlet A — Voxel Paintball FPS Multiplayer

> 1. **Modular Directory Separation**:
   * server/server.js: Express static host + ws.WebSocketServer authoritative game loop.
   * client/index.html & client/css/style.css: Canvas mount, #crosshair, #score, #ammo, #fps, and click-to-play #overlay (Sunwood-ai-labs/threejs-voxel-frontier HUD layout).
   * client/js/engine/voxel_world.js: Generates a 32x16x32 voxel arena with cover bunkers using THREE.InstancedMesh and exposes splatVoxel(voxelIndex, hexColor).
   * client/js/engine/camera_fps.js: Handles PointerLockControls, WASD + Jump physics, and AABB voxel collision detection.
   * client/js/engine/paintball.js: Spawns sphere projectiles, advances ballistic step, and renders decal/voxel color changes.
   * client/js/net/socket_sync.js: Manages ws://127.0.0.1:8080 JSON packets (join, state, shoot, splat, hit).
> 2. **Headless Multi-Client Self-Test**: Before finishing, start node server/server.js in the background, run a Node.js verification test connecting two concurrent WebSocket clients that exchange move and shoot packets, verify the splat broadcast, and cleanly terminate the background server PID.
> 3. **Two-Strike Tabu**: If a bind or module import fails twice, inspect port occupancy (ss -tlnp) or ES module import maps before retrying.
