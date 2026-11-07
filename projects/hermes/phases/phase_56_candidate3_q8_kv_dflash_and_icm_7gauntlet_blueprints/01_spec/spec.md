# Phase 56 Specification: Candidate 3 Substrate & ICM 7-Gauntlet Blueprints

* **ICM Layer**: Layer 2 (Stage Contracts, Substrate Production Profile & 7-Gauntlet Blueprints)
* **Standard**: Jake Van Clief & David McDermott (arXiv:2603.16021)
* **Discipline**: Working context strictly bounded between 2,000 and 8,000 tokens per stage.

## 1. Objectives & Boundaries
1. Certified Production llama-server Profile (Candidate 3):
   - Model: `NVIDIA-Nemotron-3.5-Bolt-E4B-UD-Q4_K_XL.gguf`
   - Drafter: `dflash-NVIDIA-Nemotron-3.5-Bolt-E4B-Q8_0.gguf`
   - Speculative decoding: `--spec-draft-n-max 6 --spec-draft-n-min 2 --spec-draft-p-min 0.75`
   - Optimizations: `GGML_CUDA_GRAPH_OPT=1`, `--flash-attn on`, `-ngl 99`, `--ctx-size 65536`
   - Buffer roofline: `-b 2048 -ub 1024 -ctk q4_0 -ctv q4_0` operating at 4,285 MiB active VRAM (1,515 MiB margin below 5,800.0 MiB ceiling).
2. ICM 3-Stage Staged Architecture for all 7 Frontier Gauntlets:
   - Gauntlet A: `benchmarks/gauntlet_a_voxel_fps/` (Voxel Paintball FPS WebSockets)
   - Gauntlet B: `benchmarks/gauntlet_b_splatbox/` (Autonomous Splatbox Browser Gaming via CDP Port 9222)
   - Gauntlet C: `benchmarks/gauntlet_c_aquarium/` (3D WebGL Aquarium Dual-FBO Waves & Buoyancy)
   - Gauntlet D: `benchmarks/leanrea_eval/` (leanrea Zero-MCP POSIX Reverse Engineering)
   - Gauntlet E: `benchmarks/ffmpeg_skill_eval/` (ffmpeg-skill Deterministic Video Editor)
   - Gauntlet F: `benchmarks/diagram_design_eval/` (diagram-design Editorial HTML+SVG Visualizer)
   - Gauntlet G: `benchmarks/markitdown_eval/` (microsoft/markitdown Multi-Format Document Ingestion)
3. 21 Deterministic Staged Prompts:
   - Complete coverage: `PROMPT_STAGE1.txt` (01-spec), `PROMPT_STAGE2.txt` (02-execute), `PROMPT_STAGE3.txt` (03-verify) for every gauntlet.
4. Tripartite Markdown Discipline:
   - `CONTEXT.md` <= 80 lines
   - `invariants.md` <= 80 lines
   - `rules.md` <= 120 lines
   - `references.md` <= 200 lines
5. Upstream Substrate Purity:
   - `.hermes/hermes-agent` 100% clean (`git status --porcelain` empty).
