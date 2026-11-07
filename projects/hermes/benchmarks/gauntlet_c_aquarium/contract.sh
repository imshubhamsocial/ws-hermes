#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
SIM_DIR="output/aquarium-sim"
test -f "$SIM_DIR/index.html"
test -f "$SIM_DIR/js/water_gpgpu.js"
test -f "$SIM_DIR/js/caustics_shader.js"
test -f "$SIM_DIR/js/sphere_physics.js"
test -f "$SIM_DIR/js/boids_fish.js"
test -f "$SIM_DIR/js/main.js"
grep -q "OES_texture_float_linear" "$SIM_DIR/js/water_gpgpu.js"
grep -q "frustumCulled = false" "$SIM_DIR/js/water_gpgpu.js"
grep -q "dFdx" "$SIM_DIR/js/caustics_shader.js"
grep -q "dFdy" "$SIM_DIR/js/caustics_shader.js"
node --input-type=module -e '
import { computeSubmergedVolume } from "./output/aquarium-sim/js/sphere_physics.js";
const r = 0.25;
const full = (4/3) * Math.PI * r**3;
if (computeSubmergedVolume(-0.5, r) !== 0) process.exit(1);
if (Math.abs(computeSubmergedVolume(r, r) - full * 0.5) > 1e-6) process.exit(1);
if (Math.abs(computeSubmergedVolume(5.0 * r, r) - full) > 1e-6) process.exit(1);
console.log("[PASS] Gauntlet C Clamped Buoyancy & Shader AST Verified");
'
