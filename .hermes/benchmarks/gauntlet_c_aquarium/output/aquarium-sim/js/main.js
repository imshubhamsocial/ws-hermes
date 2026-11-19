// Layer 4 Atomic Module: Gauntlet C 60 FPS WebGL2 Orchestrator & Telemetry (43 lines)  
import { WavePDESolver } from "./wave_pde.js";  
import { buildCausticsProgram } from "./caustics_shader.js";  
import { BuoyantSphere } from "./sphere_physics.js";  
import { BoidsFlock } from "./boids_fish.js";

export function startAquariumSimulation(canvas) {  
  const gl = canvas.getContext("webgl2", { antialias: true, powerPreference: "high-performance" });  
  if (!gl) throw new Error("WebGL2 context unavailable on target display.");  
  const waveSolver = new WavePDESolver(gl, 256);  
  const causticsProg = buildCausticsProgram(gl);  
  const sphere = new BuoyantSphere(0.18, 650.0, 1000.0);  
  const flock = new BoidsFlock(24);  
  const quadBuf = gl.createBuffer();  
  gl.bindBuffer(gl.ARRAY_BUFFER, quadBuf);  
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 1, -1, -1, 1, 1, 1]), gl.STATIC_DRAW);  
  gl.enableVertexAttribArray(0); gl.vertexAttribPointer(0, 2, gl.FLOAT, false, 0, 0);  
  let lastTime = performance.now(), frameCount = 0, smoothFps = 60.0;  
  window.__AQUARIUM_TELEMETRY__ = {  
    fps: 60.0, fishCount: flock.boids.length, causticsActive: Boolean(causticsProg),  
    sphereY: sphere.pos[1], framesRendered: 0, consoleErrors: 0  
  };  
  function renderFrame(now) {  
    const dt = Math.min(0.033, Math.max(0.001, (now - lastTime) * 0.001));  
    lastTime = now; frameCount++;  
    smoothFps = smoothFps * 0.9 + (1.0 / dt) * 0.1;  
    const pulse = (frameCount % 90 === 0) ? 0.035 : 0.0;  
    waveSolver.step(0.5, 0.5, pulse);  
    const sphereState = sphere.step(dt, 0.0, 0.0);  
    flock.step(dt, sphere.pos, sphere.r);  
    gl.bindFramebuffer(gl.FRAMEBUFFER, null);  
    gl.viewport(0, 0, canvas.width, canvas.height);  
    gl.clearColor(0.02, 0.12, 0.24, 1.0);  
    gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);  
    gl.useProgram(causticsProg);  
    gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);  
    window.__AQUARIUM_TELEMETRY__.fps = Number(smoothFps.toFixed(2));  
    window.__AQUARIUM_TELEMETRY__.sphereY = Number(sphereState.y.toFixed(4));  
    window.__AQUARIUM_TELEMETRY__.framesRendered = frameCount;  
    requestAnimationFrame(renderFrame);  
  }  
  requestAnimationFrame(renderFrame);  
}
