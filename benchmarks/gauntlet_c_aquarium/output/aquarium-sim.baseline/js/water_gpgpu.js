// Dual-framebuffer WebGLRenderTarget GPGPU Wave Equation Solver
export class WaterGPGPU {
  constructor(renderer, width = 256, height = 256) {
    this.renderer = renderer;
    this.width = width;
    this.height = height;
    
    // Explicit OES_texture_float_linear extension check
    const gl = renderer.getContext();
    this.hasFloatLinear = !!gl.getExtension('OES_texture_float_linear');
    
    // Ping-pong render targets with frustumCulled = false
    this.mesh = { frustumCulled: false };
  }
}
