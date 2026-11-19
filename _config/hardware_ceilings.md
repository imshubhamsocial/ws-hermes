# Layer 3 Hardware Ceilings: GPU & Memory Allocation

## 1. Discrete GPU VRAM Ceiling
- **Hardware Target**: NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB physical VRAM).
- **Hard Allocation Limit**: Discrete memory usage must not exceed **5,800.0 MiB** at any time.
- **Buffer Reservation**: At least 344.0 MiB reserved for host desktop compositor and headless Chromium instances.

## 2. Display Compositor & Wayland Offload
- Wayland display compositor and 2D desktop operations run on the integrated Intel iGPU.
- Discrete NVIDIA GPU is reserved strictly for llama.cpp tensor compute and WebGL2 hardware acceleration.

## 3. Calibrated Model Sampling Parameters
Inference engine runs on `http://127.0.0.1:8138/v1` serving `gemma-4-exact-4b`:
| Parameter | Value | Purpose |
| :--- | :--- | :--- |
| `temperature` | **0.20** | Enforce deterministic reasoning and eliminate hallucinations |
| `top_p` | **0.95** | High-probability nucleus truncation |
| `top_k` | **64** | Upstream Google recommended token subset |
| `min_p` | **0.05** | Eliminate low-probability tail artifacts |
| `repeat_penalty` | **1.05** | Suppress degenerate token repetition |
| `ctx-size` | **131072** | Native 128K context window with 4-bit KV cache |
