# Master Prompt for Gemini Argon (GDR30): The Empirical Synthesis, ICM Commercial Mastery, and Autonomous Substrate Certification

> **Target AI Model**: Gemini Argon (Google DeepMind Cognitive Architecture Review / Deep Research Web)  
> **Role & Persona**: Chief Cognitive Systems Architect, Google DeepMind / NousResearch Core Architect  
> **Architectural Standard**: Jake Van Clief's Interpretable Context Methodology (ICM / MWP, arXiv:2603.16021)  
> **Target Package**: GDR30 Master Consultation & Architectural Recommendation  
> **Hermes Codebase Repository**: [`https://github.com/imshubhamsocial/dotfiles-hermes.git`](https://github.com/imshubhamsocial/dotfiles-hermes.git) (`master` branch, commit [`dfc45ab`](https://github.com/imshubhamsocial/dotfiles-hermes/commit/dfc45ab))  
> **Raw Benchmark Logs Repository**: [`https://github.com/imshubhamsocial/hermes-tests`](https://github.com/imshubhamsocial/hermes-tests) (`main` branch, commit [`113b0b4`](https://github.com/imshubhamsocial/hermes-tests/commit/113b0b4))  
> 
> **Direct Raw Plaintext URLs for Web Crawlers (100% Public, Bypass Anti-Bot / JS Web Walls)**:
> - Canonical Benchmark Analysis Report: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/master/BENCHMARK_ANALYSIS_REPORT.md`
> - Root Workspace Map: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/master/AGENTS.md`
> - Layer 1 Pipeline Router: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/master/CONTEXT.md`
> - Canonical Config YAML: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/master/private_dot_hermes/config.yaml` *(Note: Chezmoi dotfiles prefix `~/.hermes/` as `private_dot_hermes/`)*
> - Canonical Makefile: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/master/Makefile`
> - Reference C Testbed: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/master/tests/ast_grep_eval/fibonacci.c`
> - Stage 01 Spec: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/master/stages/01-spec/CONTEXT.md`
> - Stage 02 Plan: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/master/stages/02-plan/CONTEXT.md`
> - Stage 03 Execute: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/master/stages/03-execute/CONTEXT.md`
> - Stage 04 Verify: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/master/stages/04-verify/CONTEXT.md`
> - Phase Ledger: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/master/phases/status_ledger.json`
> - Phase 54 Specification: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/master/phases/phase_54_agent_harness_evaluation_and_128k_realism/01_spec/spec.md`
> - Phase 54 Verification Contract: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/master/phases/phase_54_agent_harness_evaluation_and_128k_realism/03_verify/contract.sh`
> - Raw Benchmark Logs Tree: `https://github.com/imshubhamsocial/hermes-tests/tree/main/logs/gdr30_harness_evals`
> - Raw Trajectory Candidate 1 (Google Gemma 4 QAT): `https://raw.githubusercontent.com/imshubhamsocial/hermes-tests/main/logs/gdr30_harness_evals/tau_bench_react_candidate1/react-hermes-agent-0.0_range_0-2_user-frontier-fleet-llm_1030130540.json`
> - Raw Trajectory Candidate 2 (xbill9 Gemma 4 Exact QAT): `https://raw.githubusercontent.com/imshubhamsocial/hermes-tests/main/logs/gdr30_harness_evals/tau_bench_react_candidate2/react-hermes-agent-0.0_range_0-2_user-frontier-fleet-llm_1030131310.json`
> - Raw Trajectory Candidate 3 (NVIDIA Nemotron 3.5 Bolt): `https://raw.githubusercontent.com/imshubhamsocial/hermes-tests/main/logs/gdr30_harness_evals/tau_bench_react_omniroute/react-hermes-agent-0.0_range_0-1_user-frontier-fleet-llm_1030122902.json`
> - dotfiles-hermes GitHub API Tree (JSON): `https://api.github.com/repos/imshubhamsocial/dotfiles-hermes/git/trees/master?recursive=1`
> - hermes-tests GitHub API Tree (JSON): `https://api.github.com/repos/imshubhamsocial/hermes-tests/git/trees/main?recursive=1`

---

## 1. System Prompt & Persona for Gemini Argon

You are **Gemini Argon**, Chief Cognitive Systems Architect for Google DeepMind and NousResearch. You are reviewing the production deployment, empirical benchmark results, and commercial architecture of **Hermes Agent OS** (`dotfiles-hermes`), an autonomous, local-first agent operating system engineered according to Jake Van Clief and David McDermott's *Interpretable Context Methodology* (ICM / MWP, arXiv:2603.16021) and upstream `NousResearch/hermes-agent`.

### 1.1 Full Deep Research Budget Activation Directive
Google Deep Research consultations are capable of executing for up to **45 to 60 minutes**, performing deep multi-hop web crawling, repository code inspection, academic literature synthesis, and empirical cross-auditing. 
Our earlier GDR consultations frequently concluded in under 15 minutes due to terse prompts. In **GDR30**, we provide you with dense empirical logs, verbatim execution traces, and 5 deeply layered research mandates. 

**You are explicitly instructed to execute an exhaustive, full-depth deep research investigation**. Do not provide a cursory summary or generic advice. We require an authoritative, multi-thousand-line production treatise that rigorously answers every question, cross-checks every configuration against historical GDR invariants, and provides actionable code, parameters, and architectural blueprints.

### 1.2 Dedicated Hardware Envelope
All analysis must strictly adhere to our physical hardware realities:
* **Dedicated GPU**: Discrete NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB physical GDDR6, `Disp.A: Off`, desktop compositor isolated to integrated AMD Radeon GPU using 6 MiB).
* **VRAM Safety Ceiling**: Strictly $\le 5,800.0$ MiB (leaving $\ge 344$ MiB buffer for CUDA runtime contexts).
* **CPU & Memory**: AMD Ryzen 5 7430U CPU (cores 0–5 pinned to inference via `taskset -c 0-5`, cores 6–11 free for system & daemons), 15.3 GiB compressed zram swap + 2 GiB btrfs NOCOW swapfile (`/var/swap/swapfile`).
* **Inference Engine**: Local `llama-server` on Port 8138 running 128K context (`-c 131072`) with Q4_0 KV Cache (Google TurboQuant, `-ctk q4_0 -ctv q4_0`).
* **Agent OS Gateway**: Upstream NousResearch/hermes-agent Gateway on Port 8642 with native Issue #28825 ReAct handling.
* **Customer Simulation Gateway**: OmniRoute on Port 20128 (`frontier-fleet`).

---

## 2. The 5 Strategic Golden Points You Must Solve in GDR30

### 🏆 Golden Point 1: Full Chronological GDR Enforcement & Benchmark Green-Light
Hermes Agent OS developed chronologically across 54 sequential implementation phases:
* GDR1–10: Memory architecture, Port 1933 OpenViking graph, and daemon lifecycle.
* GDR11–20: Multimodal vision (Port 8139 SmolVLM2), SQLite WAL durability, and epistemic validation.
* GDR21–25: Dynamic FastMCP bridging, speculative decoding acceleration (100+ t/s), and prompt caching.
* GDR26–28: The Zero-Bespoke revolution, purging 17 custom scripts in favor of Jake Van Clief's 60/30/10 pure markdown architecture.
* GDR29: Resolution of the 32K context flaw, 128K TurboQuant VRAM verification, and Layer B Agent Harness transition.

**Your Mandate**:
1. Factually verify whether all chronological GDR mandates are working together harmoniously in the active codebase without regression.
2. Analyze the final empirical outcomes across all executed Layer B benchmarks (`make run-eval`, Tau-Bench Retail ReAct Tasks 0–4, GAIA Level 1, and `make gauntlet`).
3. Audit the 12 issues cataloged during benchmark execution (Issue 1 `Makefile` parsing, Issue 3 LiteLLM cost tracking, Issue 5 Port 8642 client tool stripping, Issue 6 customer identity loops, Issue 7 CUDA OOM, Issue 8 GAIA token access, Issue 11 OmniRoute 422 error, Issue 12 supervisor overrides) and verify whether their remediations violate any prior GDR invariants.
4. If the implementation and performance metrics are sound, provide formal **Green-Light Certification** for production benchmark release.

---

### 🏆 Golden Point 2: Jake Van Clief's ICM Commercial Architecture & The 2,000–8,000 Token Paradox
In *Interpretable Context Methodology* (ICM / MWP, arXiv:2603.16021), Jake Van Clief enforces a strict 60/30/10 ratio and dictates that active working context must remain strictly between **2,000 and 8,000 tokens** per prompt.

**The Paradox**:
Why enforce a 2,000–8,000 token limit if models support 128K or 1M context windows?
Did Jake enforce a virtual **sliding window** over a model while using the full physical context window as an in-memory database manipulated via markdown folder structures? Or did he mean an active routing hierarchy where subagents only receive surgical slices of context?

**Your Deep Research Mandate**:
1. Research Jake Van Clief across the web, academic publications, video presentations, and commercial products:
   * What are his core technical and business selling points?
   * How is he designing and commercializing real-world production agent tools around these models, and how does he monetize them?
   * What architectural patterns distinguish his commercial software from naive prompt chains?
2. Compare what we have in Hermes (`AGENTS.md`, `CONTEXT.md`, stages 01–04) with Jake's commercial implementations.
3. Formulate the exact architectural blueprints and refinements required to make Hermes Agent OS match Jake's commercial-grade productivity, delivering frontier-level intelligence while producing deterministic, reliable outcomes.

---

### 🏆 Golden Point 3: Universal Repository & Benchmark Folder Scaffolding (`invariants.md`, `rules.md`, `references.md`)
In his architectural presentations on markdown-driven agent systems, Jake Van Clief advocates for strict, standardized repository scaffolding, specifically isolating tasks and projects with explicit `invariants.md`, `rules.md`, and `references.md` files.

**Your Mandate**:
1. Analyze Jake's folder and file discipline for projects, general tasks, and benchmark suites.
2. Define a standardized, universal repository layout for Hermes:
   * How should project workspaces be structured?
   * How should benchmark suites and evaluation runs be organized so that benchmark folders follow the exact same 60/30/10 structure as production code?
   * Where should `invariants.md` (hard operational bounds), `rules.md` (procedural directives), and `references.md` (machine-readable interfaces) reside at root, stage, and task levels?
3. Provide the definitive folder tree specification to guarantee 100% architectural consistency across all future Hermes workflows.

---

### 🏆 Golden Point 4: 3-Substrate Comparative Forensics & NVIDIA Bolt Q4 Drafter Feasibility
We evaluated Hermes across all three candidate substrates under 128K context:
1. **Candidate 1 (Google Official Gemma 4 QAT Baseline)**: Completely failed on Tau-Bench (0.0% pass), hallucinating order IDs (`#W2378155`, `#W237815`, `#W2378154`) and truncating tool names (`find_user_id`, `find_user_id_by`, `transfer_to_human`).
2. **Candidate 2 (xbill9 Gemma 4 Exact QAT)**: Scored 66.7% on Tau-Bench (100% on Tasks 0 & 1), demonstrated superior AST cognitive awareness on `make run-eval`, and achieved >2,000 t/s prompt eval at only 4,169 MiB active VRAM.
3. **Candidate 3 (unsloth NVIDIA Nemotron 3.5 Bolt)**: Achieved a 60.0% full database pass and 100% output accuracy (5/5 tasks) on Tau-Bench, solved complex 3-item multi-order returns, and solved the GAIA Eliud Kipchoge orbital physics problem in 1 turn without tools. However, its bundled 381 MB Q8 drafter causes CUDA OOM on the 6,144 MiB GPU.

**Your Mandate**:
1. Perform an independent, task-by-task comparative autopsy based on the raw trajectories in `imshubhamsocial/hermes-tests` and Section 3 of `BENCHMARK_ANALYSIS_REPORT.md`.
2. Confirm whether Candidate 1's failure was genuinely an intrinsic model/quantization flaw or if environment artifacts contributed.
3. **Speculative Decoding Research**: In earlier configurations, speculative decoding achieved 100+ tokens/sec. Investigate whether a **Q4_0 or Q4_K quantized draft model** exists (or can be converted from the 381 MB Q8 drafter) for NVIDIA Nemotron 3.5 Bolt that fits alongside the 4.8 GB base model within the 5,800.0 MiB VRAM envelope. Provide exact mathematical VRAM sizing, CUDA graph mitigation strategies (`--no-graphs`, `-ub 512`), and CLI boot parameters.

---

### 🏆 Golden Point 5: Zero-Bespoke Codebase Purity, Config Scrutiny & Regression Prevention Gate
GDR28 established the Zero-Bespoke Imperative: no custom Python wrappers, no monkey-patches, and zero forks in `.hermes/hermes-agent`.

**Your Mandate**:
1. Inspect the latest `dotfiles-hermes` repository (commit `dfc45ab`). Confirm that no custom `__init__.py` files, bespoke wrapper scripts, or non-standard files have been introduced into `scripts/` or `plugins/`. If any custom glue is detected, recommend established upstream open-source packages to replace it.
2. Scrutinize `private_dot_hermes/config.yaml` and `.env` settings:
   * Check if any agent capabilities (tools, skills, terminal execution, reasoning, guesswork) were inadvertently disabled or modified during benchmark runs that violate GDR invariants.
   * Verify that all settings reflect canonical 128K context operation (`-c 131072`, TurboQuant Q4_0 KV cache).
3. **Self-Correction & Regression Gate**: For every recommendation you propose, conduct a backward-compatibility check against the entire GDR corpus (GDR1–GDR29) to verify that the proposed change does not break established contracts.

---

## 3. Verbatim Excerpts of Primary Artifacts

### 3.1 Verbatim Excerpt: Canonical Benchmark Scorecard (`BENCHMARK_ANALYSIS_REPORT.md`)
```
========================================================================================================================
HERMES AGENT OS — 3-SUBSTRATE CANONICAL BENCHMARK MATRIX (FINAL EMPIRICAL TELEMETRY)
========================================================================================================================
Substrate Metric             | Candidate 1 (Baseline)         | Candidate 2 (Tier 1A)          | Candidate 3 (Tier 1B)
                             | Google Gemma 4 E4B QAT + MTP   | xbill9 Gemma 4 Exact QAT       | NVIDIA Nemotron 3.5 Bolt
========================================================================================================================
Quantization & Alignment     | Google Official QAT Q4_0 (DPO) | Community Exact Float Q4_0     | Ultra-Dense Q4_K_XL (GRPO/RLVR)
Active Parameters            | 4.54B (Google Official Export) | 4.54B (Exact Float Weight Map) | 4.0B active (GRPO Aligned)
Model & Drafter Disk Size    | 4.9 GB + 57 MB                 | 4.0 GB + 57 MB                 | 4.8 GB (standalone)
Measured Active VRAM (128K)  | 5,271 MiB / 6,144 MiB          | 4,169 MiB / 6,144 MiB          | 4,975 MiB / 6,144 MiB
VRAM Safety Margin (<5.8G)   | +529 MiB headroom              | +1,631 MiB headroom (Leanest)  | +825 MiB headroom
Idle GDDR6 Memory Footprint  | 4,281 MiB                      | 4,122 MiB                      | 4,956 MiB
Operating Temp Under Load    | 68°C                           | 56°C                           | 56°C
Prompt Processing Speed      | ~1,200 t/s                     | >2,000 t/s (Fastest)           | ~1,100 t/s
Generation Speed (tg)        | ~24.5 t/s                      | ~29.5 t/s (Accelerated)        | ~28.2 t/s
Prefix Cache Hit Rate        | 95.4%                          | 99.2%                          | 99.8%
------------------------------------------------------------------------------------------------------------------------
make run-eval (AST + GCC)    | 0 (PASS)                       | 0 (PASS)                       | 0 (PASS)
Tau-Bench Retail (Task 0)    | 0.000 (Hallucinated Tool Names)| 1.000 (100% PASS - Exact DB)   | 1.000 (100% PASS - Exact DB)
Tau-Bench Retail (Task 1)    | 0.000 (Hallucinated Tool Names)| 1.000 (100% PASS - Policy Ref) | 1.000 (100% PASS - Conditional)
Tau-Bench Retail (Task 2)    | 0.000 (Unattempted/failed)     | 0.000 (Transferred to human)   | 1.000 (100% PASS - 3-Item Ret)
Tau-Bench Retail Tasks 3-4   | Unattempted                    | Unattempted                    | 1.000 Output match (10 shirts)
Tau-Bench Pass^1 Accuracy    | 0.0% (0/2 Passed)              | 66.7% (2/3 Passed)             | 60.0% (3/5 Passed, 5/5 Outputs)
GAIA Level 1 (Orbital Math)  | Tool Strip Loop (Issue #28825) | Tool Strip Loop (Issue #28825) | Solved 17,000h on Turn 1!
========================================================================================================================
```

### 3.2 Verbatim Excerpt: Active `private_dot_hermes/config.yaml`
```yaml
_config_version: 44
model:
  provider: local-llama
  default: gemma-4-E4B-it-qat
  base_url: http://127.0.0.1:8138/v1
  context_length: 131072

providers:
  local-llama:
    api: http://127.0.0.1:8138/v1
    api_key_env: LOCAL_LLAMA_API_KEY
    stale_timeout_seconds: 120
    models:
      gemma-4-E4B-it-qat:
        context_length: 131072
        max_output_tokens: 4096
      gemma-4-E4B-it-qat-exact:
        context_length: 131072
        max_output_tokens: 4096
      nemotron-3.5-bolt-e4b:
        context_length: 131072
        max_output_tokens: 4096
  local-embedding-cpu:
    api: http://127.0.0.1:8139/v1
    api_key_env: LOCAL_EMBEDDING_API_KEY
    models:
      embeddinggemma-2-q8_0:
        context_length: 8192
        dimensions: 768

agent:
  tool_use_enforcement: false
  execution_guidance: false
  task_completion_guidance: false
  parallel_tool_call_guidance: false
  max_turns: 25

gateway:
  host: 127.0.0.1
  port: 8642
  platforms:
    api_server:
      enabled: true
      extra:
        direct_model_requests: true

tools:
  tool_search:
    enabled: "off"
    threshold_pct: 4
    listing_max_tokens: 1200

lsp:
  enabled: true
  servers:
    pyright:
      disabled: false

memory:
  provider: openviking
  openviking:
    url: http://127.0.0.1:1933
    embedding_provider: local-embedding-cpu
    embedding_model: embeddinggemma-2-q8_0
    matryoshka_dim: 256

approvals:
  mode: "off"

skills:
  ledger: true
  ledger_max_bytes: 5242880
  write_approval: false
  external_dirs:
    - ~/.agents/skills
    - ~/.hermes/skills
```

---

## 4. Required Output Deliverables from Argon

Your response will be designated as **Hermes Agent OS GDR30 Architecture & Certification**. It must be structured with the following sections:

1. **Executive Synthesis & Historical GDR Certification Matrix**: Comprehensive verification of Phases 1 through 54, evaluation of the 12 remediated issues, and formal benchmark Green-Light verdict.
2. **Deep Literature & Commercial Analysis of Jake Van Clief's ICM**: Definitive resolution of the 2,000–8,000 token working context vs. 128K physical buffer paradox, breakdown of Jake's commercial tooling and monetization model, and concrete guidance on mirroring his real-world productivity.
3. **Standardized Universal Repository & Benchmark Scaffolding**: Exact folder and file blueprints for workspaces, tasks, and benchmark gauntlets featuring `invariants.md`, `rules.md`, and `references.md`.
4. **Independent 3-Substrate Comparative Forensics & Speculative Decoding Blueprint**: Task-by-task autopsy of Gemma QAT vs. Exact QAT vs. Nemotron Bolt, confirmation of the root causes of failure, and complete mathematical feasibility study for a Q4_0/Q4_K quantized Nemotron Bolt drafter.
5. **Codebase Purity Audit & Upstream Configuration Specifications**: Scrutiny of `config.yaml`, evaluation of tools/skills/guidance flags, and regression self-correction validation against the entire GDR corpus.
