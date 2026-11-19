import { connectWebSocket, sendInput, sendShoot, getLocalState } from './net/socket_sync.js';
import { VoxelWorld } from './engine/voxel_world.js';
import { CameraFPS } from './engine/camera_fps.js';
import { Paintball } from './engine/paintball.js';
import * as THREE from 'three';
import { PointerLockControls } from "three/examples/jsm/controls/PointerLockControls.js";

let scene, renderer;
let lastTime = 0;
let camera; let cameraFPS; let keys = {};
let animationFrameId;

function init() {
    scene = new THREE.Scene();
    scene.background = new THREE.Color(0x87CEEB); // Sky Blue
    scene.fog = new THREE.Fog(0x87CEEB, 20, 60);

    const canvas = document.getElementById('gameCanvas');
    renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);

    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const controls = new PointerLockControls(camera, document.body);

    // Scene Setup (Lighting)
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
    const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
    directionalLight.position.set(20, 30, 20);
    const hemiLight = new THREE.HemisphereLight(0xffffff, 0x444444, 0.6);
    scene.add(ambientLight, directionalLight, hemiLight);

    // Voxel World Setup
    VoxelWorld.init();
    VoxelWorld.voxelMesh.matrixAutoUpdate = false;
    scene.add(VoxelWorld.voxelMesh);

    // Camera and Controls setup inside the arena
    camera.position.set(16, 2.5, 20);
    controls.getObject().position.copy(camera.position);

    // Overlay click to lock controls
    const overlay = document.getElementById('overlay');
    if (overlay) {
        overlay.addEventListener('click', () => {
            controls.lock();
        });
        controls.addEventListener('lock', () => {
            overlay.style.display = 'none';
        });
        controls.addEventListener('unlock', () => {
            overlay.style.display = 'flex';
        });
    }

    // CameraFPS instance
    cameraFPS = new CameraFPS(camera, controls, VoxelWorld);

    Paintball.init();

    connectWebSocket();

    document.addEventListener('keydown', (e) => { keys[e.code] = true; });
    document.addEventListener('keyup', (e) => { keys[e.code] = false; });

    // Click to shoot
    document.addEventListener('click', () => {
        if (controls.isLocked) {
            const state = getLocalState();
            const origin = [camera.position.x, camera.position.y, camera.position.z];
            const dir = new THREE.Vector3();
            camera.getWorldDirection(dir);
            sendShoot(origin, [dir.x, dir.y, dir.z], '#F538A0', 1);
        }
    });

    document.querySelectorAll('.hotbar-slot').forEach(slot => {
        slot.addEventListener('click', () => {
            const weapon = parseInt(slot.dataset.weapon);
            const state = getLocalState();
            const origin = state.pos;
            const direction = [0, 1, 0];
            const color = '#F538A0';
            sendShoot(origin, direction, color, weapon);
        });
    });

    animate(0);
}

function animate(time) {
    const delta = (time - lastTime) / 1000;
    lastTime = time;

    cameraFPS.update(delta);
    Paintball.update(delta);

    renderer.render(scene, camera);

    if (time % 33 < 1) {
        sendInput(keys);
    }

    animationFrameId = requestAnimationFrame(animate);
}

window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});

init();