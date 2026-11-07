/**
 * boids_fish.js
 * Implements 3D Boid Flocking with Sinusoidal Tail-Fin Vertex Animation and Sphere Repulsion.
 * @module BoidsFish
 */

import * as THREE from 'three';

class BoidFish {
    constructor(id, position, scale = 0.5) {
        this.id = id;
        this.position = new THREE.Vector3(position.x, position.y, position.z);
        this.scale = scale;
        this.mesh = this.createMesh();
        this.mesh.position.copy(this.position);
        this.mesh.scale.set(this.scale, this.scale, this.scale);
    }

    createMesh() {
        // Use a simple geometry for the fish body (e.g., a scaled cone or a custom shape)
        // For simplicity here, we use a basic box/cone and apply sinusoidal deformation later.
        const geometry = new THREE.ConeGeometry(this.scale * 0.5, this.scale * 1.5, 8);
        const colors = [0xff6b35, 0x00f5d4, 0xffd166, 0xf72585];
        const fishColor = colors[this.id % colors.length];
        const material = new THREE.MeshPhongMaterial({ color: fishColor, emissive: 0x112233, flatShading: true });
        const mesh = new THREE.Mesh(geometry, material);
        mesh.rotation.y = Math.PI / 2; // Point along Z axis
        return mesh;
    }

    // Steering behaviors
    separation(neighbors) {
        let steer = new THREE.Vector3();
        let count = 0;
        const desiredSeparation = 2.5 * this.scale;

        for (const neighbor of neighbors) {
            const distance = this.position.distanceTo(neighbor.position);
            if (distance < desiredSeparation && distance > 0) {
                const diff = new THREE.Vector3().subVectors(this.position, neighbor.position);
                diff.normalize().multiplyScalar(1.0 / distance); // Weight by inverse distance
                steer.add(diff);
                count++;
            }
        }

        if (count > 0) {
            steer.divideScalar(count);
            // Apply desired separation force
            this.applySteering(steer, 0.05);
        }
    }

    alignment(neighbors) {
        let avgVelocity = new THREE.Vector3();
        const count = neighbors.length;

        for (const neighbor of neighbors) {
            avgVelocity.add(neighbor.mesh.position.clone().sub(this.position)); // Using position vector as velocity proxy
        }

        avgVelocity.divideScalar(count);
        avgVelocity.normalize();

        const desired = avgVelocity.clone().multiplyScalar(0.05);
        this.applySteering(desired, 0.05);
    }

    cohesion(neighbors) {
        let centerOfMass = new THREE.Vector3();
        let count = 0;

        for (const neighbor of neighbors) {
            centerOfMass.add(neighbor.position);
            count++;
        }

        centerOfMass.divideScalar(count);
        const desired = centerOfMass.sub(this.position);

        this.applySteering(desired, 0.05);
    }

    // Steering helper function
    applySteering(desired, strength) {
        const currentVelocity = new THREE.Vector3().subVectors(this.position, this.mesh.position.clone()); // Dummy velocity placeholder
        const force = desired.clone().sub(currentVelocity);
        force.normalize().multiplyScalar(strength);
        // In a real implementation, this would modify the object's actual velocity vector.
        // Here we just apply the force as a translation proxy for demonstration.
        this.position.add(force.multiplyScalar(0.1));
        this.mesh.position.copy(this.position);
    }

    // Sinusoidal Tail-Fin Vertex Animation (Conceptual implementation)
    updateTailAnimation(time) {
        const positions = this.mesh.geometry.attributes.position.array;
        const vertexCount = positions.length / 3;
        
        // Simple sine wave based on vertex index and time
        for (let i = 0; i < vertexCount; i++) {
            const index = i * 3;
            const offset = Math.sin(time * 5 + i * 0.5) * 0.1; // Sinusoidal movement
            // Modify the Z or X position slightly to simulate tail movement
            positions[index + 2] += offset; 
        }
        this.mesh.geometry.attributes.position.needsUpdate = true;
    }

    // Repulsion from walls and sphere
    applyRepulsion(spherePos, sphereRadius) {
        const walls = [
            { normal: new THREE.Vector3(1, 0, 0), distance: 10 },
            { normal: new THREE.Vector3(-1, 0, 0), distance: 10 },
            { normal: new THREE.Vector3(0, 1, 0), distance: 10 },
            { normal: new THREE.Vector3(0, -1, 0), distance: 10 },
            { normal: new THREE.Vector3(0, 0, 1), distance: 10 },
            { normal: new THREE.Vector3(0, 0, -1), distance: 10 }
        ];
        const selfPos = this.position;
        let repulsionForce = new THREE.Vector3();

        // Wall repulsion
        for (const wall of walls) {
            const dist = wall.normal.dot(selfPos) - wall.distance;
            if (dist < 0) {
                repulsionForce.add(wall.normal.clone().multiplyScalar(-1 / Math.abs(dist)));
            }
        }

        // Sphere repulsion
        const sphereDistance = selfPos.distanceTo(spherePos);
        const minDistance = sphereRadius * 1.5;
        if (sphereDistance < minDistance) {
            const dir = new THREE.Vector3().subVectors(selfPos, spherePos).normalize();
            const force = new THREE.Vector3().addScaledVector(dir, 1.0 / (sphereDistance - minDistance));
            repulsionForce.add(force);
        }

        // Apply force (simplified)
        this.position.add(repulsionForce.multiplyScalar(0.01));
        this.mesh.position.copy(this.position);
    }
}

export { BoidFish };
