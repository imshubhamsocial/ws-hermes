# Hard Invariants: Gauntlet C — 3D WebGL Aquarium Simulation

> 1. **Dual-Framebuffer Ping-Pong Wave PDE**: The water surface MUST be simulated via two ping-pong THREE.WebGLRenderTarget textures (256x256, THREE.HalfFloatType) solving 2D heightfield wave PDE with damping 0.995 and mesh.frustumCulled = false.
> 2. **WebGL2 OES_texture_float_linear Check**: Before setting THREE.LinearFilter on THREE.HalfFloatType render targets, explicitly call `const hasFloatLinear = !!renderer.getContext().getExtension('OES_texture_float_linear')` and fall back to THREE.NearestFilter if false.
> 3. **Mandatory Clamped Spherical Cap Buoyancy**: In sphere_physics.js, submerged volume MUST be strictly clamped to 0.0 when ds <= 0.0, (PI * ds^2 / 3) * (3r - ds) when 0 < ds < 2r, and (4/3)*PI*r^3 when ds >= 2r. Unclamped polynomials are forbidden.
> 4. **Screen-Space Derivative Caustics**: Underwater caustics MUST compute refracted ray area ratios using GLSL dFdx and dFdy.
> 5. **Interactive Raycast Sphere Drop & Boid Fish**: Users must be able to click/drag and drop the rigid sphere into the water while >= 12 boid fish swim with flocking rules and sphere avoidance.
