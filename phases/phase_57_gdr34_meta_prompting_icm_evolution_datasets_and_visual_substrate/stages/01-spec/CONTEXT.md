# Phase 57 Stage 01: Specification (GDR34 Blueprint Implementation)

> **Architectural Standard**: ICM / MWP (arXiv:2603.16021)  
> **Golden Target**: Full alignment with Argon's GDR34 Master Blueprint adjusted for 128K hardware reality.

---

## 1. Scope & Golden Points Alignment

1. **GP1: Meta-Prompting & Coding Exam Syndrome**:
   - Eliminate monolithic prompts that ask the model to do everything in one shot.
   - Enforce compiler pipeline architecture: Spec $\to$ Plan $\to$ Execute $\to$ Verify.
2. **GP2: One Fact, One Home (Folder Architecture)**:
   - Scaffold distinct directories with isolated `CONTEXT.md` contracts.
   - Establish Layer 0 workspace map: `IDENTITY.md`, `AGENTS.md`, `SOUL.md`.
3. **GP3: ICM Evolution Datasets**:
   - Clone and maintain upstream ICM templates in `~/.cache/icm-datasets/`.
   - Deploy `icm-stage-compiler` into `~/.hermes/skills/icm/`.
4. **GP4: Benchmarks & Gauntlet Restructuring**:
   - Gauntlet B restructured into 3 deterministic stages: `01-probe/`, `02-controller/`, `03-execute/`.
5. **GP5: Substrate Context & Exact Model Selection**:
   - Deploy `gemma-4-E4B-it-q4_0-exact.gguf` with MTP drafter.
   - Adjust context from blueprint's 32k to 128k (`-c 131072`) with TurboQuant Q4_0 KV cache under 5,800.0 MiB VRAM ceiling.
6. **GP6: Visual Centroid Acquisition**:
   - Integrate OpenCV HoughCircles for zero-latency, zero-VRAM target detection.
7. **GP7: Enterprise ICM Consulting Practices**:
   - Restrict scripts to <60 lines; strictly avoid custom daemon wrappers.
