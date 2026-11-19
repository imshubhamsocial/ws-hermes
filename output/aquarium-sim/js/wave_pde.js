// Layer 4 Atomic Module: WebGL2 2D Damped Wave PDE Solver (40 lines)  
export class WavePDESolver {  
  constructor(gl, size = 256) {  
    this.gl = gl; this.size = size;  
    gl.getExtension("EXT_color_buffer_float");  
    this.texA = this.createTex(); this.texB = this.createTex();  
    this.fbo = gl.createFramebuffer();  
    this.prog = this.createProgram();  
  }  
  createTex() {  
    const gl = this.gl, t = gl.createTexture();  
    gl.bindTexture(gl.TEXTURE_2D, t);  
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA32F, this.size, this.size, 0, gl.RGBA, gl.FLOAT, null);  
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.NEAREST);  
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.NEAREST);  
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);  
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);  
    return t;  
  }  
  createProgram() {  
    const gl = this.gl, vs = gl.createShader(gl.VERTEX_SHADER), fs = gl.createShader(gl.FRAGMENT_SHADER);  
    gl.shaderSource(vs, "#version 300 es\\nin vec2 p;out vec2 uv;void main(){uv=p*0.5+0.5;gl_Position=vec4(p,0,1);}");  
    gl.shaderSource(fs, "#version 300 es\\nprecision highp float;in vec2 uv;uniform sampler2D uH;uniform vec3 uDrop;\\nout vec4 o;void main(){vec2 d=vec2(1.0/256.0);vec4 c=texture(uH,uv);\\nfloat l=texture(uH,uv-vec2(d.x,0)).r+texture(uH,uv+vec2(d.x,0)).r+texture(uH,uv-vec2(0,d.y)).r+texture(uH,uv+vec2(0,d.y)).r-4.0*c.r;\\nfloat h=(2.0-0.015)*c.r-(1.0-0.015)*c.g+0.22*l+uDrop.z*exp(-dot(uv-uDrop.xy,uv-uDrop.xy)*400.0);\\nvec2 n=vec2(texture(uH,uv+vec2(d.x,0)).r-texture(uH,uv-vec2(d.x,0)).r,texture(uH,uv+vec2(0,d.y)).r-texture(uH,uv-vec2(0,d.y)).r);\\no=vec4(h,c.r,n.x,n.y);}");  
    gl.compileShader(vs); gl.compileShader(fs);  
    const p = gl.createProgram(); gl.attachShader(p, vs); gl.attachShader(p, fs); gl.linkProgram(p);  
    return p;  
  }  
  step(dropX = 0.5, dropY = 0.5, strength = 0.0) {  
    const gl = this.gl;  
    gl.bindFramebuffer(gl.FRAMEBUFFER, this.fbo);  
    gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, this.texB, 0);  
    gl.viewport(0, 0, this.size, this.size);  
    gl.useProgram(this.prog);  
    gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, this.texA);  
    gl.uniform3f(gl.getUniformLocation(this.prog, "uDrop"), dropX, dropY, strength);  
    gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);  
    gl.bindFramebuffer(gl.FRAMEBUFFER, null);  
    [this.texA, this.texB] = [this.texB, this.texA];  
  }  
}
