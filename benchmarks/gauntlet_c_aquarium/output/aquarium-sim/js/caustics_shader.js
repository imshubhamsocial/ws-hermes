// Layer 4 Atomic Module: WebGL2 Differential Area Caustics Shader (37 lines)  
export const CAUSTICS_VERT_SRC = [  
  "#version 300 es",  
  "in vec2 aPos; out vec3 vOldPos; out vec3 vNewPos;",  
  "uniform sampler2D uWaveTex; uniform vec3 uLightDir;",  
  "void main() {",  
  "  vec2 uv = aPos * 0.5 + 0.5;",  
  "  vec4 w = texture(uWaveTex, uv);",  
  "  vec3 n = normalize(vec3(-w.b, 1.0, -w.a));",  
  "  vec3 r = refract(normalize(uLightDir), n, 0.7501875);",  
  "  vec3 surf = vec3(aPos.x, w.r, aPos.y);",  
  "  vOldPos = surf + uLightDir * ((-1.0 - w.r) / uLightDir.y);",  
  "  vNewPos = surf + r * ((-1.0 - w.r) / r.y);",  
  "  gl_Position = vec4(vNewPos.xz, 0.0, 1.0);",  
  "}"  
].join("\\n");

export const CAUSTICS_FRAG_SRC = [  
  "#version 300 es",  
  "#extension GL_OES_standard_derivatives : enable",  
  "precision highp float;",  
  "in vec3 vOldPos; in vec3 vNewPos; out vec4 fragColor;",  
  "void main() {",  
  "  float oldArea = length(dFdx(vOldPos)) * length(dFdy(vOldPos));",  
  "  float newArea = length(dFdx(vNewPos)) * length(dFdy(vNewPos));",  
  "  float intensity = 0.25 * (oldArea / max(newArea, 0.00001));",  
  "  fragColor = vec4(vec3(0.2, 0.75, 1.0) * intensity, 1.0);",  
  "}"  
].join("\\n");

export function buildCausticsProgram(gl) {  
  const vs = gl.createShader(gl.VERTEX_SHADER), fs = gl.createShader(gl.FRAGMENT_SHADER);  
  gl.shaderSource(vs, CAUSTICS_VERT_SRC); gl.compileShader(vs);  
  gl.shaderSource(fs, CAUSTICS_FRAG_SRC); gl.compileShader(fs);  
  const prog = gl.createProgram();  
  gl.attachShader(prog, vs); gl.attachShader(prog, fs); gl.linkProgram(prog); return prog;  
}
