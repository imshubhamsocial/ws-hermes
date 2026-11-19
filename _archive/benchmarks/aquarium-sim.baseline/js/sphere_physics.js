// Piecewise strictly clamped spherical-cap buoyancy
export function computeSubmergedVolume(ds, r) {
  if (ds <= 0.0) return 0.0;
  if (ds >= 2.0 * r) return (4.0 / 3.0) * Math.PI * r * r * r;
  return ((Math.PI * ds * ds) / 3.0) * (3.0 * r - ds);
}

export class SpherePhysics {
  constructor(radius = 0.25, mass = 1.0) {
    this.radius = radius;
    this.mass = mass;
    this.position = [0, 1.5, 0];
    this.velocity = [0, 0, 0];
  }
  step(dt, waterHeight = 0.0) {
    const ds = (waterHeight + this.radius) - this.position[1];
    const vSub = computeSubmergedVolume(ds, this.radius);
    const fBuoyancy = 1000.0 * 9.81 * vSub;
    const fGravity = -this.mass * 9.81;
    const fNet = fGravity + fBuoyancy;
    this.velocity[1] += (fNet / this.mass) * dt;
    this.position[1] += this.velocity[1] * dt;
  }
}
