# Layer 3 Reference Schemas: Gauntlet C (evanw/webgl-water & jeantimex/threejs-water)

## 1. Upstream GitHub Reference Repositories
* **Canonical WebGL Water**: https://github.com/evanw/webgl-water (water.js, renderer.js, main.js)
* **Three.js Port & Optics**: https://github.com/jeantimex/threejs-water (.xzy coordinate swizzle, CompoundSphereWaterDisplacement, frustumCulled = false, Schlick Fresnel)
* **Three.js Caustics & Boids**: https://github.com/martinRenou/threejs-caustics & https://github.com/mrdoob/three.js

## 2. GLSL Wave Update & Sphere Displacement Shaders (evanw/webgl-water)
* **Wave PDE Fragment Shader (UpdateShader)**:
  `vec2 dx = vec2(delta.x, 0.0); vec2 dy = vec2(0.0, delta.y);`
  `float average = (texture2D(texture, coord - dx).r + texture2D(texture, coord - dy).r + texture2D(texture, coord + dx).r + texture2D(texture, coord + dy).r) * 0.25;`
  `info.g += (average - info.r) * 2.0; info.g *= 0.995; info.r += info.g;`
* **Sphere Volume Displacement Shader (SphereDisplacementShader)**:
  `float volumeInSphere(vec3 center) { vec3 toCenter = vec3(coord.x * 2.0 - 1.0, 0.0, coord.y * 2.0 - 1.0) - center; float t = length(toCenter) / radius; float dy = exp(-pow(t * 1.5, 6.0)); float ymin = min(0.0, center.y - dy); float ymax = min(max(0.0, center.y + dy), ymin + 2.0 * dy); return (ymax - ymin) * 0.1; }`
  `info.r += volumeInSphere(oldCenter) - volumeInSphere(newCenter);`

## 3. Clamped Spherical Cap Buoyancy Function (js/sphere_physics.js)
```javascript
export function computeSubmergedVolume(ds, r) {
  if (ds <= 0.0) return 0.0;
  if (ds >= 2.0 * r) return (4.0 / 3.0) * Math.PI * r * r * r;
  return ((Math.PI * ds * ds) / 3.0) * (3.0 * r - ds);
}
```
