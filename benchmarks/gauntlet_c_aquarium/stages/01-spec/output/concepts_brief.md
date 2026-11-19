# Stage 01 Concepts Brief: Gauntlet C WebGL2 Physics Simulation

## 1. Mathematical Physics Foundations

* 2D Damped Wave PDE: Explicit leapfrog GPGPU scheme on 256x256 RGBA32F texture with CFL^2 = 0.22 <= 0.5.
* Vector Snell's Law & Differential Area Caustics: Floor caustics via dFdx and dFdy screen-space derivative ratios.
* Spherical-Cap Buoyancy & Quadratic Drag: Exact integration of submerged spherical cross-sections V_sub(d) = (pi*d^2/3)*(3R - d) with symplectic Euler integration.
* 3D Craig Reynolds Boids: 24 autonomous fish steering via separation, alignment, cohesion, obstacle avoidance, and box boundaries.

## 2. Hardware Envelopes

* GPU: NVIDIA RTX 3050 (6,144 MiB GDDR6), allocation ceiling <= 5,800.0 MiB.
* Compositor: Intel iGPU drives Wayland display (0 MiB discrete VRAM).
* Scripts: All modules strictly < 60 lines.
