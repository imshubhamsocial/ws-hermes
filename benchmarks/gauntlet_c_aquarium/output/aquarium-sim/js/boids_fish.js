// Layer 4 Atomic Module: 3D Craig Reynolds Boids Flocking System (49 lines)  
export class BoidsFlock {  
  constructor(count = 24) {  
    this.boids = Array.from({ length: count }, (_, i) => ({  
      pos: [Math.sin(i) * 0.5, -0.2 - (i % 5) * 0.1, Math.cos(i) * 0.5],  
      vel: [Math.cos(i) * 0.25, 0.02, -Math.sin(i) * 0.25],  
    }));  
    this.vMin = 0.15; this.vMax = 0.55;  
  }  
  step(dt, spherePos = [0, 0, 0], sphereRadius = 0.18) {  
    const n = this.boids.length;  
    for (let i = 0; i < n; i++) {  
      const b = this.boids[i];  
      let sx = 0, sy = 0, sz = 0, ax = 0, ay = 0, az = 0, cx = 0, cy = 0, cz = 0, cnt = 0;  
      for (let j = 0; j < n; j++) {  
        if (i === j) continue;  
        const o = this.boids[j];  
        const dx = b.pos[0] - o.pos[0], dy = b.pos[1] - o.pos[1], dz = b.pos[2] - o.pos[2];  
        const d2 = dx * dx + dy * dy + dz * dz + 0.0001;  
        if (d2 < 0.18) {  
          sx += dx / d2; sy += dy / d2; sz += dz / d2;  
          ax += o.vel[0]; ay += o.vel[1]; az += o.vel[2];  
          cx += o.pos[0]; cy += o.pos[1]; cz += o.pos[2];  
          cnt++;  
        }  
      }  
      let fx = sx * 0.04, fy = sy * 0.04, fz = sz * 0.04;  
      if (cnt > 0) {  
        fx += (ax / cnt - b.vel[0]) * 1.2 + (cx / cnt - b.pos[0]) * 0.8;  
        fy += (ay / cnt - b.vel[1]) * 1.2 + (cy / cnt - b.pos[1]) * 0.8;  
        fz += (az / cnt - b.vel[2]) * 1.2 + (cz / cnt - b.pos[2]) * 0.8;  
      }  
      for (let k = 0; k < 3; k++) {  
        const lim = k === 1 ? 0.75 : 0.85;  
        if (b.pos[k] > lim) b.vel[k] -= (b.pos[k] - lim) * 4.0 * dt;  
        if (b.pos[k] < -lim) b.vel[k] -= (b.pos[k] + lim) * 4.0 * dt;  
      }  
      const sdx = b.pos[0] - spherePos[0], sdy = b.pos[1] - spherePos[1], sdz = b.pos[2] - spherePos[2];  
      const sd = Math.hypot(sdx, sdy, sdz) + 0.001;  
      if (sd < sphereRadius + 0.15) { fx += (sdx / sd) * 1.5; fy += (sdy / sd) * 1.5; fz += (sdz / sd) * 1.5; }  
      b.vel[0] += fx * dt; b.vel[1] += fy * dt; b.vel[2] += fz * dt;  
      const spd = Math.hypot(b.vel[0], b.vel[1], b.vel[2]) + 0.0001;  
      const cSpd = Math.max(this.vMin, Math.min(this.vMax, spd));  
      b.vel[0] = (b.vel[0] / spd) * cSpd; b.vel[1] = (b.vel[1] / spd) * cSpd; b.vel[2] = (b.vel[2] / spd) * cSpd;  
      b.pos[0] += b.vel[0] * dt; b.pos[1] += b.vel[1] * dt; b.pos[2] += b.vel[2] * dt;  
    }  
  }  
}
