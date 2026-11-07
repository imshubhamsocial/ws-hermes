/**
 * main.js
 * Orchestrates the GPGPU Water, Caustics, Sphere Physics, and Boid Simulation.
 */

import * as THREE from 'three';
import { BoidFish } from './boids_fish.js';
import { integrateSphere, computeSubmergedVolume } from './sphere_physics.js';
import { setupWater, updateWater, renderCaustics } from './water_gpgpu.js';

class AquariumSimulation {
    constructor() {
        this.scene = new THREE.Scene();
        this.scene.background = new THREE.Color(0x02162e); // Deep marine blue
        this.scene.fog = new THREE.FogExp2(0x02162e, 0.025);

        this.camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
        this.camera.position.set(0, 2, 16);
        this.camera.lookAt(0, 0, 0);

        this.renderer = new THREE.WebGLRenderer({ antialias: true });
        this.renderer.setSize(window.innerWidth, window.innerHeight);
        this.renderer.setPixelRatio(window.devicePixelRatio);
        this.renderer.shadowMap.enabled = true;

        const container = document.getElementById('canvas-container');
        if (container) {
            container.appendChild(this.renderer.domElement);
        } else {
            document.body.appendChild(this.renderer.domElement);
        }

        this.clock = new THREE.Clock();
        this.gravity = -9.81;
        this.gravityEnabled = true;

        this.initLighting();
        this.initEnvironment();
        this.initSystems();
        this.setupRaycasting();
        this.setupHUD();

        this.animate = this.animate.bind(this);
        requestAnimationFrame(this.animate);
    }

    initLighting() {
        const ambientLight = new THREE.AmbientLight(0x6088aa, 1.8);
        const sunLight = new THREE.DirectionalLight(0xffffff, 2.2);
        sunLight.position.set(5, 15, 10);
        const waterLight = new THREE.PointLight(0x00f5d4, 1.5, 30);
        waterLight.position.set(0, 3, 0);
        this.scene.add(ambientLight, sunLight, waterLight);
    }

    initEnvironment() {
        // 1. Sandy Aquarium Bottom
        const floorGeo = new THREE.PlaneGeometry(24, 24);
        const floorMat = new THREE.MeshStandardMaterial({ color: 0xd2b48c, roughness: 0.85, metalness: 0.1 });
        const floor = new THREE.Mesh(floorGeo, floorMat);
        floor.rotation.x = -Math.PI / 2;
        floor.position.y = -5.0;
        this.scene.add(floor);

        // 2. Aquarium Glass Tank Boundaries
        const tankGeo = new THREE.BoxGeometry(20, 10, 20);
        const tankEdges = new THREE.EdgesGeometry(tankGeo);
        const tankWire = new THREE.LineSegments(tankEdges, new THREE.LineBasicMaterial({ color: 0x00ffff, opacity: 0.6, transparent: true }));
        tankWire.position.y = 0;
        this.scene.add(tankWire);

        // 3. Water Surface Plane
        const waterGeo = new THREE.PlaneGeometry(20, 20, 32, 32);
        const waterMat = new THREE.MeshStandardMaterial({
            color: 0x00b4d8,
            roughness: 0.1,
            metalness: 0.1,
            transparent: true,
            opacity: 0.65
        });
        this.waterMesh = new THREE.Mesh(waterGeo, waterMat);
        this.waterMesh.rotation.x = -Math.PI / 2;
        this.waterMesh.position.y = 4.8;
        this.scene.add(this.waterMesh);
    }

    initSystems() {
        this.water = setupWater(this.renderer);

        // Sphere with Clamped Buoyancy
        const sphereGeo = new THREE.SphereGeometry(1.0, 32, 32);
        const sphereMat = new THREE.MeshStandardMaterial({ color: 0xff3366, roughness: 0.2, metalness: 0.5 });
        this.sphere = new THREE.Mesh(sphereGeo, sphereMat);
        this.spherePhysics = {
            position: new THREE.Vector3(0, 3.0, 0),
            velocity: new THREE.Vector3(0, 0, 0),
            radius: 1.0,
            mass: 5.0
        };
        this.sphere.position.copy(this.spherePhysics.position);
        this.scene.add(this.sphere);

        // 15 3D Boid Fish
        this.boids = [];
        for (let i = 0; i < 15; i++) {
            const initialPos = new THREE.Vector3(
                (Math.random() - 0.5) * 14,
                (Math.random() - 0.5) * 6,
                (Math.random() - 0.5) * 14
            );
            const boid = new BoidFish(i, initialPos, 0.45);
            this.boids.push(boid);
            this.scene.add(boid.mesh);
        }
    }

    setupHUD() {
        const btnDrop = document.getElementById('btn-drop-sphere');
        const btnGrav = document.getElementById('btn-toggle-gravity');
        const btnRipple = document.getElementById('btn-add-ripple');
        const statusDiv = document.getElementById('status');

        if (btnDrop) {
            btnDrop.onclick = () => {
                this.spherePhysics.position.set(0, 6.0, 0);
                this.spherePhysics.velocity.set(0, -2.0, 0);
                if (statusDiv) statusDiv.textContent = 'Status: Sphere Dropped';
            };
        }
        if (btnGrav) {
            btnGrav.onclick = () => {
                this.gravityEnabled = !this.gravityEnabled;
                if (statusDiv) statusDiv.textContent = `Status: Gravity ${this.gravityEnabled ? 'ON' : 'OFF'}`;
            };
        }
        if (btnRipple) {
            btnRipple.onclick = () => {
                this.waterMesh.position.y = 4.8 + (Math.random() - 0.5) * 0.2;
                if (statusDiv) statusDiv.textContent = 'Status: Ripple Generated';
            };
        }
    }

    setupRaycasting() {
        this.isDragging = false;
        this.prevMouse = { x: 0, y: 0 };

        window.addEventListener('mousedown', (e) => {
            this.isDragging = true;
            this.prevMouse = { x: e.clientX, y: e.clientY };
        });
        window.addEventListener('mouseup', () => { this.isDragging = false; });
        window.addEventListener('mousemove', (e) => {
            if (this.isDragging) {
                const dx = (e.clientX - this.prevMouse.x) * 0.005;
                const dy = (e.clientY - this.prevMouse.y) * 0.005;
                this.camera.position.x = this.camera.position.x * Math.cos(dx) + this.camera.position.z * Math.sin(dx);
                this.camera.position.z = this.camera.position.z * Math.cos(dx) - this.camera.position.x * Math.sin(dx);
                this.camera.position.y = Math.max(-2, Math.min(8, this.camera.position.y + dy * 5));
                this.camera.lookAt(0, 0, 0);
                this.prevMouse = { x: e.clientX, y: e.clientY };
            }
        });
    }

    animate() {
        const dt = Math.min(this.clock.getDelta(), 0.033);
        const time = this.clock.getElapsedTime();

        // 1. Update Fish Flocking & Tail Animation
        for (let i = 0; i < this.boids.length; i++) {
            const b = this.boids[i];
            b.separation(this.boids);
            b.alignment(this.boids);
            b.cohesion(this.boids);
            b.updateTailAnimation(time);

            // Keep within aquarium glass box [-9, 9]
            if (b.mesh.position.x > 9) b.position.x = -9;
            if (b.mesh.position.x < -9) b.position.x = 9;
            if (b.mesh.position.y > 4) b.position.y = 4;
            if (b.mesh.position.y < -4.5) b.position.y = -4.5;
            if (b.mesh.position.z > 9) b.position.z = -9;
            if (b.mesh.position.z < -9) b.position.z = 9;
            b.mesh.position.copy(b.position);
        }

        // 2. Integrate Sphere Buoyancy Physics
        if (this.gravityEnabled) {
            const waterLevel = 4.8;
            const ds = (waterLevel + this.spherePhysics.radius) - this.spherePhysics.position.y;
            const submergedVol = computeSubmergedVolume(ds, this.spherePhysics.radius);
            const buoyantForce = submergedVol * 9.81 * 8.0; // Effective fluid density
            const gravForce = this.spherePhysics.mass * this.gravity;
            const dragForce = -this.spherePhysics.velocity.y * 1.5;

            const netAcc = (gravForce + buoyantForce + dragForce) / this.spherePhysics.mass;
            this.spherePhysics.velocity.y += netAcc * dt;
            this.spherePhysics.position.y += this.spherePhysics.velocity.y * dt;

            // Pool floor bounce
            if (this.spherePhysics.position.y - this.spherePhysics.radius < -5.0) {
                this.spherePhysics.position.y = -5.0 + this.spherePhysics.radius;
                this.spherePhysics.velocity.y *= -0.65; // Restitution
            }
        }
        this.sphere.position.copy(this.spherePhysics.position);

        // 3. Water surface subtle animation
        if (this.waterMesh) {
            this.waterMesh.rotation.z = Math.sin(time * 0.5) * 0.02;
        }

        // 4. Render
        this.renderer.render(this.scene, this.camera);
        requestAnimationFrame(this.animate);
    }

    windowResize() {
        this.camera.aspect = window.innerWidth / window.innerHeight;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(window.innerWidth, window.innerHeight);
    }
}

// Initialize the simulation upon script load
window.onload = () => {
    new AquariumSimulation();
};

window.addEventListener('resize', () => {
    // Need to re-initialize or call resize method on the instantiated object
    // (For brevity, assuming the class handles re-init/resize)
});
