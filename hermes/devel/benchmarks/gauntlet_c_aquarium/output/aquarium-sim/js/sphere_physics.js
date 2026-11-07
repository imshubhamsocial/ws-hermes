// output/aquarium-sim/js/sphere_physics.js

/**
 * @module spherePhysics
 * @description Handles physics for submerged objects (sphere), including clamped buoyancy and integration.
 * Adheres strictly to invariants: Exact clamped spherical-cap volume, semi-implicit Euler integration.
 */

/**
 * Calculates the exact piecewise clamped spherical-cap volume.
 * 
 * @param {number} ds - Depth submerged (distance below water surface).
 * @param {number} r - Sphere radius.
 * @returns {number} Submerged volume in cubic units.
 */
export function computeSubmergedVolume(ds, r) {
    // Invariant Check 1: ds <= 0.0
    if (ds <= 0.0) {
        return 0.0;
    }
    
    // Invariant Check 2: ds >= 2.0 * r (Fully submerged)
    if (ds >= 2.0 * r) {
        return (4.0 / 3.0) * Math.PI * r * r * r;
    }
    
    // Invariant Check 3: 0 < ds < 2r (Spherical Cap Volume Formula)
    // Formula: ((PI * ds^2) / 3.0) * (3.0 * r - ds)
    return ((Math.PI * ds * ds) / 3.0) * (3.0 * r - ds);
}

/**
 * Performs semi-implicit Euler integration for a sphere in water.
 * 
 * @param {Object} sphere - { position: Vector3, velocity: Vector3, radius: number }
 * @param {number} dt - Time step.
 * @param {number} restitution - Coefficient of restitution (0.65).
 * @param {number} dragCoeff - Water drag coefficient.
 * @param {Object} waterState - { currentHeight: number, surfaceNormal: Vector3 }
 * @returns {Object} Updated sphere state.
 */
export function integrateSphere(sphere, dt, waterState) {
    // Invariant Check: dt <= 0.033 (Maximum stability)
    const safeDt = Math.min(dt, 0.033); 

    // 1. Buoyancy Calculation (coupled to SphereDisplacementShader/waterState)
    const ds = waterState.currentHeight - sphere.position.y;
    const volume = computeSubmergedVolume(ds, sphere.radius);
    
    // Archimedes: Buoyant Force F_B = density * V_submerged * g
    const buoyantForce = volume * 9.81 * 0.1; // 0.1 is effective fluid density/mass conversion

    // 2. Drag Force (Proportional to velocity squared)
    const dragMagnitude = 0.5 * 0.5 * sphere.radius * dragCoeff * sphere.velocity.lengthSq();
    const dragForce = -sphere.velocity.clone().multiplyScalar(dragMagnitude);

    // 3. Apply Forces and Euler Integration
    let acceleration = new THREE.Vector3().add(buoyantForce).add(dragForce);
    
    // Gravity force (downwards)
    acceleration.y -= 9.81;

    sphere.velocity.add(acceleration.clone().multiplyScalar(safeDt));
    sphere.position.add(sphere.velocity.clone().multiplyScalar(safeDt));

    // 4. Collision Detection and Restitution
    // Check ground collision (y=0)
    if (sphere.position.y - sphere.radius <= 0) {
        // Resolve penetration
        sphere.position.y = sphere.radius;
        
        // Apply restitution (Invariant: 0.65)
        sphere.velocity.y *= -0.65; 

        // Stop movement if velocity is too low
        if (Math.abs(sphere.velocity.y) < 0.1) {
            sphere.velocity.y = 0;
        }
    }

    return sphere;
}
// Note: Three.js Vector3 is assumed to be available in the environment.
