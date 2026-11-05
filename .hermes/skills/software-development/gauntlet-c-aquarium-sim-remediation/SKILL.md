---
name: gauntlet-c-aquarium-sim-remediation
description: "Fixing Gauntlet C WebGL Aquarium simulation issues."
---
# Gauntlet C Remediation Protocol

This protocol guides the process of bringing the 3D Boid Aquarium simulation to a functional state by addressing common runtime environment and integration pitfalls.

## Procedure

1. **Context and Invariants Retrieval**
    - Read `CONTEXT.md`, `invariants.md`, and `rules.md` first. This establishes the required mathematical bounds and structural constraints before any mutation.
2. **Pre-Mutation Checks**
    - **Pitfall: Import Map/CDN Failure.** Before any code change, verify the Three.js import map or CDN link in `index.html`. Legacy URLs (like `unpkg.com/three@r165`) are prone to 404 CORS blocking.
3. **Structural Remediation (index.html)**
    - Update the import map to use a reliable CDN (e.g., `cdnjs.cloudflare.com/ajax/libs/three.js/0.165.0/three.module.js`).
4. **Logic Remediation (main.js)**
    - **Pitfall: Incorrect Canvas Mounting.** The renderer must be mounted to the dedicated simulation container (`#canvas-container`), not the `document.body`. Failure to do so prevents the simulation from being contained within the specified UI layout.
    - Implement the logic to correctly initialize and mount the renderer to the container.
    - Implement the event listeners for HUD buttons ('Drop Sphere', 'Toggle Gravity', 'Add Ripple') and ensure they trigger the corresponding actions in the simulation class.
5. **Integration and Stabilization**
    - Integrate and align the imports and functions between `main.js` and the modules (`water_gpgpu.js`, `caustics_shader.js`, etc.) to match the exported classes/functions.
    - Run `terminal("npm run test")` and `terminal("bash contract.sh")` to verify all invariants pass and zero page/console errors exist.
6. **Final Receipt**
    - Write the `output/stage4_remediation_receipt.json` file and confirm exit code 0.

## Pitfalls and Best Practices
- **CORS:** If `unpkg.com` returns a 404, immediately switch to a known stable CDN (e.g., `cdnjs`).
- **Mounting:** Always explicitly target the designated container ID (e.g., `#canvas-container`) for the renderer's DOM element to prevent layout issues.
- **Validation:** Never claim completion until `contract.sh` succeeds and the web server (8081) reports zero errors via Playwright/Python check.
