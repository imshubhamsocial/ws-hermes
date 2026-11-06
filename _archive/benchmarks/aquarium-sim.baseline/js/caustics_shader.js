// Screen-Space Derivative Caustics & Schlick Fresnel Optics
export const CausticsShader = {
  vertexShader: `
    varying vec3 vWorldPosition;
    void main() {
      vWorldPosition = (modelMatrix * vec4(position, 1.0)).xyz;
      gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
    }
  `,
  fragmentShader: `
    varying vec3 vWorldPosition;
    void main() {
      vec3 oldPos = vWorldPosition;
      vec3 newPos = vWorldPosition + vec3(0.01);
      float oldArea = length(dFdx(oldPos)) * length(dFdy(oldPos));
      float newArea = length(dFdx(newPos)) * length(dFdy(newPos));
      float causticIntensity = oldArea / max(newArea, 0.0001);
      gl_FragColor = vec4(vec3(causticIntensity * 0.5), 1.0);
    }
  `
};
