// Layer 4 Atomic Module: Spherical-Cap Buoyancy & Hydrodynamic Drag (35 lines)  
// Enforces V_sub(d) = (pi * d^2 / 3) * (3R - d) with symplectic Euler step.  
export class BuoyantSphere {  
  constructor(radius = 0.18, density = 650.0, waterDensity = 1000.0) {  
    this.r = radius;  
    this.rhoS = density;  
    this.rhoW = waterDensity;  
    this.volTotal = (4.0 / 3.0) * Math.PI * Math.pow(this.r, 3);  
    this.mass = this.rhoS * this.volTotal;  
    this.pos = [0.0, 0.25, 0.0];  
    this.vel = [0.0, 0.0, 0.0];  
    this.g = 9.81;  
    this.cd = 0.47;  
  }  
  submergedVolume(waveHeight) {  
    const rawDepth = waveHeight - (this.pos[1] - this.r);  
    const d = Math.max(0.0, Math.min(2.0 * this.r, rawDepth));  
    return (Math.PI * d * d / 3.0) * (3.0 * this.r - d);  
  }  
  step(dt, waveHeight = 0.0, waveVelY = 0.0) {  
    const vSub = this.submergedVolume(waveHeight);  
    const fBuoy = this.rhoW * this.g * vSub;  
    const fGrav = -this.mass * this.g;  
    const subRatio = vSub / this.volTotal;  
    const areaSub = Math.PI * this.r * this.r * subRatio;  
    const relVy = this.vel[1] - waveVelY;  
    const fDragY = -0.5 * this.rhoW * this.cd * areaSub * Math.abs(relVy) * relVy;  
    const fNetY = fBuoy + fGrav + fDragY;  
    const accY = fNetY / this.mass;  
    this.vel[1] = (this.vel[1] + accY * dt) * 0.992;  
    this.pos[1] += this.vel[1] * dt;  
    if (this.pos[1] < -0.85 + this.r) { this.pos[1] = -0.85 + this.r; this.vel[1] *= -0.4; }  
    return { y: this.pos[1], vy: this.vel[1], vSub };  
  }  
}
