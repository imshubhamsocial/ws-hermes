# Shared Reference: Multiplayer Netcode Protocol (Gauntlet A)

## Protocol Invariants
- Transport: WebSocket on Port 8080.
- Broadcast Frequency: 20 Hz fixed tick loop (50 ms interval).
- Client Packet Schema: Supports `data.type || data.t`.
- Handshake Sequence: Server sends `join` / `WELCOME` on connection with client ID.
- Position Broadcast: Serialized x, y, z positions with interpolation.
- Voxel Splat Broadcast: Position, color hex, and voxel mutation type.
