# Master Prompt for Lead Architect Argon (GDR38 Frontier 4B Models & Gemini Decision 1)

> **Instructions for User**:  
> 1. Open [gemini.google.com](https://gemini.google.com) in your browser.  
> 2. Select the **Chat** tab and enable **Thinking Process: High**.  
> 3. Click the **+** (**Add file**) icon $\to$ **More Uploads** $\to$ **Import code**.  
> 4. Paste the repository URL: `https://github.com/imshubhamsocial/ws-hermes` and click **Import**.  
> 5. Copy the markdown content below, paste it into the message box, and submit.  

---

# GDR38 Master Architectural Directive & Lead Architect Consultation

> **Release Package**: GDR38  
> **Target Substrate**: Hermes Agent OS on Fedora Kinoite 44 (x86_64, rpm-ostree)  
> **Inference Engine**: Dual-Track (Gemma 4 Exact 4B + NVIDIA Nemotron Dory 1.0 Looped 4B)  
> **Context Window**: 131,072 to 262,144 tokens (128K–256K, Google TurboQuant Q4_0 KV Cache)  
> **Hardware Status**: Discrete NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB physical GDDR6, ceiling $\le 5,800.0\text{ MiB}$); 100% compute dedication (Wayland compositor on Intel iGPU / Disp.A: Off, 25 MiB idle); Host system on CPU & 16 GB System RAM  
> **Decision Oracle**: Google Gemini Decision 1 (`gemini-decision-1` via Gemini Decisions API, Nov 2026) for zero-token Layer 1 routing and invariant arbitration  
> **Status**: Verified and Operational | 5-Layer ICM Architecture Deployed | Gauntlets A, B, C Certified  

---

## Instructions for Lead Architect Argon (Gemini Argon / High Thinking)

You are Lead Architect Argon.
You must conduct deep research on next-generation ~4B parameter models, looped transformer architectures, frontier distillation, and Google Gemini Decision 1.
Your goal is to author the definitive model architecture blueprint for `ws-hermes`.

### Ingested Repository & Historical Research Context

The full repository snapshot (`ws-hermes`) is loaded in your context via the **Import code** feature. You have direct access to all tracked files, configurations, scripts, benchmarks, phases, and research packages.

All research packages and GDR specifications are present in your loaded workspace under `docs/research/`:
- **GDR30**: `docs/research/GDR30 - Golden Benchmark State (GAIA, TAU-2)/` (Golden foundation)
- **GDR31 to GDR37**: `docs/research/GDR31/` through `docs/research/GDR37/` (Evolutionary phases)
- **GDR38 Briefing**: `docs/research/GDR38/01_master_argon_consultation_brief.md` (Consultation brief and mandates)
- **Hardware Baseline & Telemetry**: `docs/research/GDR38/02_doc1_hardware_and_current_champion_baseline.md` (RTX 3050 6 GB dedicated, 16 GB CPU/RAM host, Gemma 4 Exact on Port 8138)
- **Frontier Models & Decision 1 Spec**: `docs/research/GDR38/03_doc2_frontier_4b_models_and_gemini_decision_spec.md` (Technical specifications across the 7 Golden Points)

You do NOT need the user to upload additional files. Inspect the files already present in your imported repository.

For external framework references, consult these canonical raw repositories:
- **Hermes Workspace (Raw)**: `https://raw.githubusercontent.com/imshubhamsocial/ws-hermes/master/`
- **Hermes Evaluation Suite (Raw)**: `https://raw.githubusercontent.com/imshubhamsocial/hermes-tests/main/`
- **Upstream Hermes Substrate**: `https://raw.githubusercontent.com/NousResearch/hermes-agent/main/`
- **Jake Van Clief ICM Repo**: `https://raw.githubusercontent.com/RinDig/Interpretable-Context-Methodology/main/`
- **ICM Template Repository**: `https://raw.githubusercontent.com/ktncodes/icm-template/main/`
- **ICM Architect Skill**: `https://raw.githubusercontent.com/RinDig/icm-architect/main/`

---

## The Seven Golden Directives for Lead Architect Argon

### Directive 1: Golden Point 1 — Gemma 4 Exact 4B Enhancements & Runtime Optimization
Analyze our current champion baseline (`gemma-4-E4B-it-q4_0-exact.gguf` + MTP assistant drafter):
1. Evaluate quantization improvements (Q4_0 vs Q4_K_M vs IQ4_NL) to minimize perplexity and syntax errors.
2. Evaluate asymmetric KV caching: 8-bit keys (`--cache-type-k q8_0`) with 4-bit values (`--cache-type-v q4_0`) to preserve attention fidelity across 128K context within our 5,800.0 MiB ceiling.
3. Determine optimal speculative decoding draft depth ($n=2$ vs $n=3$) and acceptance probability thresholds (`--spec-draft-p-min 0.75`).
4. Provide sampling parameters (Min-P, repetition penalty) to prevent tool strip loops (Issue #28825).

### Directive 2: Golden Point 2 — NVIDIA Nemotron Dory 1.0 4B Looped Transformer Analysis
Analyze `NVIDIA-Nemotron-Labs-Dory1.0-4B` (`nemotron-3.5-bolt-e4b`):
1. Evaluate native 256K context support (`--ctx-size 262144`).
2. Analyze the looped architecture: 8 input layers, 20 recurrent core layers looped $k$ times ($k \in \{1, 2, 4\}$), 8 output layers.
3. Compare loop count $k=2$ (effective depth 48 layers) versus $k=4$ (effective depth 88 layers).
4. Explain how Last-Loop KV Caching prevents KV memory explosion, keeping VRAM flat at ~1,120 MiB at 128K tokens.
5. Provide quantitative trade-offs: Throughput (tokens/sec) versus compute latency versus reasoning depth.
6. Deliver an explicit recommendation on which loop count Hermes should use for autonomous agentic loops.

### Directive 3: Golden Point 3 — Latest Qwen & Gemma 4B Evolutions
Survey recent ~4B parameter models:
1. Qwen evolutionary line: Qwen 2.5-Coder (3B/7B), Qwen 3 Coder 4B, and Qwen 4 roadmap with native function calling tokens (`<tool_call>`).
2. Gemma evolutionary line: Gemma 2, Gemma 3, Gemma 4, and experimental Argon/Carbon variants with multi-head latent attention (MLA).
3. Compare performance within our 6 GB VRAM budget at 128K context.

### Directive 4: Golden Rule 4 — Frontier-Beating Distilled 4B Models
Identify distilled 4B parameter models that beat current small and frontier models across:
1. **GAIA (General AI Assistants)**: Desktop and web tool navigation.
2. **SWE-bench Lite / Verified**: Real-world software engineering bug resolution.
3. **TAU-2 (Tool Agent Use)**: Complex multi-turn transactional consistency.
4. **MATH-500 & LiveCodeBench**: Formal deduction and algorithmic coding.

### Directive 5: Golden Rule 5 — Production Upstream Flags & Sampling Values
Provide complete, copy-pasteable `llama-server` runtime commands for each candidate model:
1. CLI flags: `--model`, `--model-draft`, `--alias`, `--ctx-size`, `--cache-type-k`, `--cache-type-v`, `--flash-attn`, `--reasoning`, `--jinja`, `--threads 6 --threads-batch 6`, `--n-gpu-layers 99`.
2. Sampling parameters: Exact `temperature`, `top_p`, `top_k`, `min_p`, `repeat_penalty`, `presence_penalty`.
3. Exact Jinja prompt templates for each architecture.

### Directive 6: Golden Point 6 — Zero-Denial Abliterated & Heretic Variants
Research uncensored, abliterated, and heretic fine-tunes for each model family:
1. Method: Representation engineering and weight orthogonalization ($W' = W - v v^T W$) to remove refusal directions.
2. Goal: Ensure 0% refusals on systems programming, kernel debugging, socket inspection, and security audits.
3. Provide full hardware telemetry to guide memory and execution bounds:
   - Dedicated Discrete NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB physical GDDR6, 96-bit bus, Ampere GA107, active ceiling $\le 5,800.0\text{ MiB}$).
   - Full 6 GB VRAM is 100% available for compute (Wayland compositor on Intel iGPU / Disp.A: Off, 25 MiB idle).
   - Host OS: Fedora Kinoite 44 (rpm-ostree, x86_64, Wayland KDE Plasma on Intel iGPU).
   - System RAM: 16 GB RAM (15.3 GiB zram + 2,048 MiB btrfs NOCOW swapfile).
   - Secondary daemons CPU-offloaded: `hermes-embedding-cpu.service` on Port 8139 (0 MiB VRAM) and `hermes-openviking.service` on Port 1933 (0 MiB VRAM) pinned to cores 6–11.

### Directive 7: Golden Rule 7 — Google Gemini Decision 1 Architecture & ICM Integration
Analyze Google's newly released **Gemini Decision 1** (`gemini-decision-1` via Gemini Decisions API, Nov 2026):
1. Architecture: Zero generation tokens, prefill-only forward pass, 50–100 ms compute latency, 262,144 token context capacity.
2. Evaluative Assessment: Should we replace or augment our current local decision model with Gemini Decision 1?
3. Three-Pillar ICM Integration Blueprint:
   - *Pillar 1: Automated Layer 1 Task Router*: Zero-token routing across root `CONTEXT.md` targets.
   - *Pillar 2: Automated Contract & Invariant Arbiter*: Real-time verification oracle auditing stage deliverables against Rules 1–10.
   - *Pillar 3: Dynamic Inference Route & Loop Controller*: Routing tasks between Dory $k=2$ (reactive), Dory $k=4$ (deep reasoning), and local Gemma 4 Exact.
4. Links: Provide raw GitHub endpoints and direct Hugging Face links.

---

## Output Standards (Strict Google Docs & ASD-STE100 Rules)

1. **ASD-STE100 Language**: Write in Simplified Technical English. Sentences must not exceed 25 words. Use active voice and direct imperative verbs.
2. **Even Code Fence Parity**: Every opened code fence must be closed (`count % 2 == 0`).
3. **Even Dollar Sign Parity**: Maintain strictly even dollar signs for LaTeX notation (`count % 2 == 0`).
4. **Single-Line Headers & Tables**: All table rows must have exact matching pipe counts on single lines.
5. **No Fluff or Placeholders**: Provide complete, drop-in replacement commands and configurations.

Author your complete architectural blueprint and save it directly to:
`/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/hermes/devel/docs/research/GDR38/Output/GDR38 Frontier 4B Models and Gemini Decision 1 Architecture Blueprint.md`
