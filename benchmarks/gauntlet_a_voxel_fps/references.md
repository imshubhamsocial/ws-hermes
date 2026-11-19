# Layer 3 Reference Schemas: Gauntlet A (Upstream GitHub Grounding)

## 1. Upstream Repository Mapping
* **Voxel Arena & HUD**: https://github.com/Sunwood-ai-labs/threejs-voxel-frontier (Three.js + Vite, 5 block palettes, center #crosshair, bottom hotbar 1-5, top-right #fps counter).
* **Multiplayer Netcode**: https://github.com/nickyvanurk/voidfall (Node.js + ws authoritative server loop, client sequence numbers seq, snapshot interpolation).
* **Rendering & WS Primitives**: https://github.com/mrdoob/three.js (InstancedMesh, PointerLockControls, Raycaster) and https://github.com/websockets/ws.

## 2. WebSocket Wire Protocol Schema (nickyvanurk/voidfall Pattern)
* **Client -> Server (input)**: `{"type": "input", "seq": 42, "pos": [x, y, z], "rot": [yaw, pitch], "keys": {"w": true, "a": false, "s": false, "d": false, "space": false}}`
* **Client -> Server (shoot)**: `{"type": "shoot", "seq": 43, "origin": [x, y, z], "dir": [dx, dy, dz], "color": "#F538A0", "weapon": 1}`
* **Server -> Clients (snapshot @ 20 Hz)**: `{"type": "snapshot", "tick": 1024, "players": {"id1": {"pos": [x,y,z], "rot": [yaw,pitch], "score": 3, "hp": 100, "ack": 43}}, "projectiles": [...]}`
* **Server -> Clients (splat)**: `{"type": "splat", "voxelKey": "12,1,15", "instanceId": 412, "color": "#F538A0", "shooterId": "id1", "targetId": "id2"}`

## 3. Instanced Voxel Splat Pattern (mrdoob/three.js)
* Initialize `const mesh = new THREE.InstancedMesh(boxGeo, mat, maxVoxels);`
* Populate `mesh.setMatrixAt(i, dummy.matrix)` and `mesh.setColorAt(i, baseColor)`.
* On splat event: `mesh.setColorAt(instanceId, new THREE.Color(hexColor)); mesh.instanceColor.needsUpdate = true;`
