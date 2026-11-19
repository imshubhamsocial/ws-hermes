# Stage Contract: Gauntlet C — 3D WebGL Aquarium Simulation

## Inputs
* Workspace Root Map: ../../AGENTS.md
* Hard Mathematical & WebGL2 Bounds: ./invariants.md
* Shader & Physics Implementation Order: ./rules.md
* Upstream evanw/webgl-water & jeantimex/threejs-water Schemas: ./references.md

## Process
> 1. Read ./invariants.md, ./rules.md, and ./references.md completely.
> 2. Create the modular 3D WebGL / Three.js aquarium application inside output/aquarium-sim/ (index.html, js/main.js, js/water_gpgpu.js, js/caustics_shader.js, js/sphere_physics.js, js/boids_fish.js).
> 3. Implement dual-framebuffer GPGPU wave PDE ping-pong (water_gpgpu.js), dFdx/dFdy differential area caustics and soft shadows (caustics_shader.js), clamped spherical-cap buoyancy + drag (sphere_physics.js), and 3D boid flocking fish (boids_fish.js).
> 4. Run bash ./contract.sh to validate all mathematical, WebGL2 extension, and AST invariants.

## Outputs
* Simulation Application: output/aquarium-sim/
* Verification Receipt: output/status.json

## Check
* Run bash ./contract.sh and confirm exit code 0.
