# Procedural Rules: Gauntlet C — 3D WebGL Aquarium Simulation

> 1. **File Modularity (output/aquarium-sim/)**:
   * index.html: Loads Three.js via ES module importmap (three r165+), mounts #canvas-container, and provides UI buttons (Drop Sphere, Toggle Gravity, Add Ripple).
   * js/water_gpgpu.js: Implements DropShader, UpdateShader (5-point discrete Laplacian), NormalShader, and SphereDisplacementShader (evanw/webgl-water & jeantimex/threejs-water).
   * js/caustics_shader.js: Renders the 512x512 caustics texture using dFdx/dFdy and projects caustics + sphere/fish shadows onto the tiled aquarium floor and glass walls.
   * js/sphere_physics.js: Integrates gravity and buoyancy with semi-implicit Euler (dt <= 1/60), pool floor/wall restitution 0.65, and couples sphere movement back into SphereDisplacementShader.
   * js/boids_fish.js: Implements 3D boid flocking (mrdoob/three.js webgl_gpgpu_birds) with sinusoidal tail-fin vertex animation and repulsive potential from the submerged sphere.
   * js/main.js: Orchestrates the render loop, Raycaster mouse picking on the sphere, and camera orbit controls.
> 2. **Numerical Stability**: Clamp dt = Math.min(clock.getDelta(), 0.033) so tab switching never explodes the wave PDE or Euler physics integrator.
