# Shared Reference: Shader & Buoyancy Conventions (Gauntlet C)

## Three.js Shader Invariants
- Library Version: Three.js `three@0.165.0`.
- ShaderMaterial Uniforms Property: Strictly plural `uniforms: { ... }`. Singular `uniform:` is invalid.
- Water GPGPU: Dual framebuffer wave PDE ping-pong on floating-point textures.
- Caustics Shader: Differential area mapping using dFdx/dFdy.
- Buoyancy Physics: Clamped spherical-cap volume integration with drag damping.
