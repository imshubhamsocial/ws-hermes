const express = require('express');
const http = require('http');
const WebSocket = require('ws');
const path = require('path');

const PORT = 8080;
const HOST = '127.0.0.1';
const TICK_RATE = 20; // 20 Hz
const TICK_INTERVAL = 1000 / TICK_RATE;
const GRAVITY = -24.0; // m/s^2

// --- State Management ---
let gameState = {
    players: new Map(), // Map<ws, {id, position: {x, y, z}, velocity: {x, y, z}, lastInput: timestamp}>
    voxelSplats: new Map(), // Map<string, {position: {x, y, z}, color: string}>
    tick: 0
};

// --- Server Setup ---
const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

// Serve client files statically
app.use(express.static(path.join(__dirname, '../client')));

// --- Physics and Game Logic ---

/**
 * Updates player positions based on parabolic ballistics.
 * @param {object} player - The player state.
 * @param {number} dt - Delta time (TICK_INTERVAL / 1000).
 */
function updatePhysics(player, dt) {
    // Update velocity: v_new = v_old + a*dt
    player.velocity.y += GRAVITY * dt;

    // Update position: p_new = p_old + v_new*dt
    player.position.x += player.velocity.x * dt;
    player.position.y += player.velocity.y * dt;
    player.position.z += player.velocity.z * dt;
}

/**
 * Runs the authoritative game tick.
 */
function gameTick() {
    gameState.tick++;
    const dt = TICK_INTERVAL / 1000;

    // 1. Process inputs and update physics for all players
    for (const [ws, player] of gameState.players) {
        // In a real implementation, input packets would modify player.velocity
        updatePhysics(player, dt);
    }

    // 2. Broadcast state snapshot
    const snapshot = {
        tick: gameState.tick,
        type: "snapshot",
        players: Array.from(gameState.players.values()).map(p => ({
            id: p.id,
            position: p.position,
            velocity: p.velocity
        })),
        splats: Array.from(gameState.voxelSplats.values()).map(s => s)
    };

    // Broadcast to all connected clients
    wss.clients.forEach(client => {
        if (client.readyState === WebSocket.OPEN) {
            client.send(JSON.stringify(snapshot));
        }
    });
}

// --- WebSocket Handling ---
wss.on('connection', (ws) => {
    console.log('Client connected');
    // Assign a unique ID (simplified)
    const playerId = Math.random().toString(36).substring(2, 9);
    
    // Initial player state
    const initialPlayerState = {
        id: playerId,
        position: { x: 0, y: 1, z: 0 },
        velocity: { x: 0, y: 0, z: 0 },
        lastInput: Date.now()
    };
    gameState.players.set(ws, initialPlayerState);

    // Send welcome/join room contract packet
    ws.send(JSON.stringify({ t: "WELCOME", id: playerId }));

    ws.on('message', (message) => {
        try {
            const packet = JSON.parse(message);

            // Handle Nickyvanurk/voidfall packets
            if (packet.type) {
                if (packet.type === "input") {
                    // Process input
                } else if (packet.type === "shoot") {
                    // Process shooting
                } else if (packet.type === "snapshot") {
                    // Client snapshot
                } else if (packet.type === "splat") {
                    // Client reported splat location
                    gameState.voxelSplats.set(packet.splatId, packet.splatData);
                }
            } 
            // Handle Contract packets
            else if (packet.t) {
                if (packet.t === "JOIN_ROOM") {
                    console.log(`Player ${playerId} joined room.`);
                } else if (packet.t === "FIRE_SHOT") {
                    // Process shot logic
                }
            }
        } catch (e) {
            console.error('Invalid packet received:', e.message);
        }
    });

    ws.on('close', () => {
        console.log(`Client ${playerId} disconnected.`);
        gameState.players.delete(ws);
    });
});

// --- Start Server and Tick Loop ---
server.listen(PORT, HOST, () => {
    console.log(`Server running at http://${HOST}:${PORT}`);
    console.log(`Starting ${TICK_RATE} Hz tick loop.`);

    // Start the authoritative tick loop
    setInterval(gameTick, TICK_INTERVAL);
});