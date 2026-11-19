import { VoxelWorld } from '../engine/voxel_world.js';
import { CameraFPS } from '../engine/camera_fps.js';
import { Paintball } from '../engine/paintball.js';

const WS_URL = 'ws://127.0.0.1:8080';
let ws;
let playerId = null;
let localState = { pos: [0, 1, 0], rot: [0, 0], score: 0, hp: 100, lastAck: 0 };
let clientSequence = 0;

export function connectWebSocket() {
    ws = new WebSocket(WS_URL);

    ws.onopen = () => {
        console.log("Connected to server.");
    };

    ws.onmessage = (event) => {
        const data = JSON.parse(event.data);
        handleServerMessage(data);
    };

    ws.onclose = () => {
        console.log("Disconnected from server. Attempting reconnect in 5s...");
        setTimeout(connectWebSocket, 5000);
    };

    ws.onerror = (err) => {
        console.error("WebSocket Error:", err);
    };
}

function handleServerMessage(data) {
    const msgType = data.type || data.t;
    switch (msgType) {
        case 'WELCOME':
        case 'join':
            playerId = data.id || data.playerId;
            console.log(`Joined as player ID: ${playerId}`);
            break;
        case 'snapshot':
            let playerSnapshot = null;
            if (Array.isArray(data.players)) {
                playerSnapshot = data.players.find(p => p.id === playerId);
            } else if (data.players) {
                playerSnapshot = data.players[playerId];
            }
            if (playerSnapshot) {
                localState.pos = playerSnapshot.position || playerSnapshot.pos || localState.pos;
                localState.rot = playerSnapshot.rot || localState.rot;
                localState.score = playerSnapshot.score !== undefined ? playerSnapshot.score : localState.score;
                localState.hp = playerSnapshot.hp !== undefined ? playerSnapshot.hp : localState.hp;
            }
            VoxelWorld.updatePlayerState(localState);
            CameraFPS.updatePlayerState(localState);
            break;
        case 'splat':
            Paintball.handleSplat(data);
            break;
        default:
            console.warn("Unknown message type:", msgType);
    }
}

export function sendInput(keys) {
    if (ws && ws.readyState === WebSocket.OPEN) {
        clientSequence++;
        const message = JSON.stringify({
            type: "input",
            seq: clientSequence,
            pos: localState.pos,
            rot: localState.rot,
            keys: keys
        });
        ws.send(message);
    }
}

export function sendShoot(origin, direction, color, weapon) {
    if (ws && ws.readyState === WebSocket.OPEN) {
        clientSequence++;
        const message = JSON.stringify({
            type: "shoot",
            seq: clientSequence,
            origin: origin,
            dir: direction,
            color: color,
            weapon: weapon
        });
        ws.send(message);
    }
}

export function getLocalState() {
    return localState;
}