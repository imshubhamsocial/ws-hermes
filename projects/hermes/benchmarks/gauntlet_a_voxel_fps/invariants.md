# Hard Invariants: Gauntlet A — Voxel Paintball FPS Multiplayer

> 1. **Zero Stubs or Placeholders**: Every file in server/ and client/ must be 100% implemented. Comments such as // TODO or // implement later are strictly forbidden.
> 2. **Instanced Voxel Rendering**: Voxel chunks MUST use THREE.InstancedMesh (mrdoob/three.js) with per-instance color attributes (instanceColor) so paintball splats recolor voxel blocks dynamically in a single GPU draw call at 60 FPS.
> 3. **Authoritative WebSocket Netcode**: The Node.js server MUST use websockets/ws on Port 8080 following nickyvanurk/voidfall authoritative state broadcasting (20 Hz server tick, 60 Hz client interpolation).
> 4. **PointerLock First-Person Controls**: Camera rotation MUST use PointerLockControls with relative mouse deltas, WASD movement, Space jump, and gravity (g = -24.0 m/s^2).
> 5. **Parabolic Paintball Ballistics**: Projectiles must follow 3D parabolic trajectories and recolor hit voxel instances + award player score upon impact.
> 6. **Hardware & Port Isolation**: Bind HTTP/WS strictly to 127.0.0.1:8080. Never modify files outside benchmarks/gauntlet_a_voxel_fps/output/.
> 7. **Active Context Budget**: Keep initial stage context strictly between 2,000 and 8,000 tokens.
