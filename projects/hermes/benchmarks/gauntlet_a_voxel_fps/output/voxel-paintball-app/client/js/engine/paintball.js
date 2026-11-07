import * as THREE from 'three';

export class Paintball {
    static projectiles = [];
    static maxProjectiles = 10;

    static init() {}

    static createProjectile(origin, direction, color, weapon) {
        if (this.projectiles.length >= this.maxProjectiles) {
            return null;
        }
        const projectile = {
            origin: { ...origin },
            dir: direction,
            color: color,
            weapon: weapon,
            life: 0,
            velocity: { x: direction[0] * 50, y: direction[1] * 50, z: direction[2] * 50 }
        };
        this.projectiles.push(projectile);
        return projectile;
    }

    static update(delta) {
        const gravity = -24.0;
        const newProjectiles = [];

        for (const p of this.projectiles) {
            p.origin.x += p.velocity.x * delta;
            p.origin.y += p.velocity.y * delta + 0.5 * gravity * delta * delta;
            p.origin.z += p.velocity.z * delta;
            
            p.velocity.y += gravity * delta;

            if (p.origin.y < 0 || p.life > 5) {
                const voxelKey = `${Math.round(p.origin.x)},0,${Math.round(p.origin.z)}`;
                // Assuming VoxelWorld is globally accessible or imported
                // In a real module system, VoxelWorld would be passed/imported.
                // For this stub, we simulate the splat call.
                // VoxelWorld.handleSplat({ voxelKey, instanceId: 0, color: p.color, shooterId: 'server', targetId: 'server' });
                continue;
            }
            
            p.life += delta;
            newProjectiles.push(p);
        }
        this.projectiles = newProjectiles;
    }

    static handleSplat(splatData) {
        // This function is called by the server snapshot, but we handle the rendering side here.
        // VoxelWorld.handleSplat(splatData);
    }
}