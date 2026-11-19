# Layer 3 Benchmark Rules: Gauntlet Suite Contracts

## 1. Gauntlet A (Voxel FPS)
- **Engine**: Three.js / WebGL.
- **Contract Requirements**: Deterministic procedural voxel generation, 60 FPS rendering under headless CDP, zero DOM errors.

## 2. Gauntlet B (Splatbox 3D Gaussian Splatting)
- **Engine**: 3D Gaussian Splatting + Computer Vision tracking.
- **Contract Requirements**: Minimum video telemetry score $\ge 1,400$ points across $>400$ frames, prefill throughput $\ge 2,000$ tokens/sec.

## 3. Gauntlet C (WebGL2 Interactive 3D Aquarium)
- **Engine**: WebGL2 GPGPU finite difference + differential area caustics.
- **Contract Requirements**:
  1. All 5 simulation modules in `output/aquarium-sim/js/` strictly $< 60$ lines.
  2. Caustics shader contains `dFdx`, `dFdy`, and `refract`.
  3. Headless Playwright CDP telemetry records `fps >= 55.0`, `fishCount >= 20`, `causticsActive == true`, `consoleErrors == 0`.
  4. Discrete RTX 3050 VRAM $\le 5,800.0$ MiB.
