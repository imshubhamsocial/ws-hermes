# Master Prompt for Gemini Argon (GDR32 Certification & ICM Staged Gauntlet Blueprint)

> **Instructions for User**: Copy the entire markdown block below and paste it directly into your Gemini Argon consultation session.

---

````markdown
# Architectural Consultation: Real-World Production Certification, ICM Benchmark Forensics, and 7-Gauntlet Staged Blueprint (GDR32)

## 0. The Golden Rule for GDRs: Epistemic Self-Containment & AST Integrity Protocol

> **Epistemic Invariant**: To guarantee 100% certification verifiability even if external cloud crawlers face network firewalls, rate limits, or dynamic client-side JavaScript rendering barriers on third-party sites:
> 1. **Tier 1 — Verbatim Inlined Payloads (Zero-Network Required)**: All critical configuration files, verification receipts, test logs, hardware telemetry, and mathematical derivations are embedded verbatim within this prompt.
> 2. **Tier 2 — AI-Digest Plaintext Mirrors (Single-URL Crawl via Gitingest)**: The complete repositories are mirrored as continuous, crawler-friendly Markdown digests (`https://gitingest.com/imshubhamsocial/dotfiles-hermes` and `https://gitingest.com/imshubhamsocial/hermes-tests`).
> 3. **Tier 3 — GitHub API Recursive JSON Trees**: Complete filesystem manifests listing every file, path, and blob hash in a single structured JSON response without HTML scraping.
> 4. **Tier 4 — Public Raw Plaintext Endpoints**: All individual files are accessible via direct `raw.githubusercontent.com` URLs (HTTP 200 text/plain).
> 
> 5. **Markdown AST & Google Docs Document Creation Integrity (The Document Golden Rule)**:
>    - **Zero-Failure Google Docs Generation Protocol**: The user will export this response directly into Google Docs via Gemini's "Export to Docs" / Document Creation engine. To prevent Google Docs internal parser crashes (Error 3 / "Failed to create document"), the response MUST maintain 100% strict CommonMark and XML/DOM compliance.
>    - **Strict Code Fence Parity**: Every code fence opened MUST be strictly closed. Never emit unclosed code fences. The total count of code fences must always be even (`count % 2 == 0`). (In the prior run, unclosed code fences in bash heredocs crashed Google Docs export with Error 3).
>    - **Zero Nested Code Fences in Scripts/Heredocs**: Never write unescaped triple backticks inside `cat << 'EOF'` heredocs, bash setup blocks, or templates. Use 4 backticks ```` for outer enclosing blocks, or indent code blocks by 4 spaces.
>    - **Escape All XML/HTML Angle-Bracket Tags in Prose**: Never emit raw unescaped tokens such as `<tool_call>`, `<think>`, `<turn>`, `<focus>`, `<|channel|>`, or `<image>` in markdown prose. Always enclose them in backticks (e.g. `` `<tool_call>` ``) or fenced code blocks so the Google Docs XML parser does not interpret them as malformed HTML tags.
>    - **Single-Line Headings & Clean Tables**: Headings (`#`) and table rows (`|`) must never contain unescaped line breaks. Every table row must have an exact matching count of pipe separators matching the header.
>    - **Clean LaTeX Math**: Use standard `$ ... $` for inline math and `$$ ... $$` for block math without duplicate MathML or raw HTML tags.
>    - **No Truncation or Placeholders**: Never truncate files with `// ... (rest unchanged)` or omit sections. Provide complete, drop-in verifiable files.

---

## 1. Audit of Past GDR31 Revisions and Hard Invariants to Avoid

In the prior GDR31 consultation, two iterative revisions were required due to specific execution flaws:
* **Flaw 1 (Omission of Skills & Gauntlets)**: In Revision 1, four candidate skills (`leanrea`, `ffmpeg-skill`, `diagram-design`, `markitdown`) were omitted or superficial. In GDR32, **all seven gauntlets (A through G)** must be fully scaffolded and staged without omissions.
* **Flaw 2 (AST & Markdown Code Fence Collapse)**: Unclosed triple backticks inside bash scripts crashed external Markdown parsers and Google Docs export. In GDR32, code fence parity must be 100% mathematically balanced (`count % 2 == 0`).
* **Flaw 3 (Invalid Upstream CLI Flags & Category Confusion)**: Suggesting `-s software-development` caused `error: agent init failed: Unknown skill(s): software-development` because `software-development` is an internal category, not an individual skill. Wrapper flags (`--in <dir>`, `--accept-hooks`) must be strictly aligned with canonical upstream `hermes chat` grammar.
* **Flaw 4 (The Monolithic Prompt Trap)**: Formulating Gauntlet A as a single 40-turn monolithic prompt caused conversational context to balloon to **55,124 tokens**, triggering 40-second prompt prefill latencies and stream watchdog alerts. In GDR32, **every gauntlet must be restructured into Jake Van Clief's ICM Staged Contracts (`01-spec` $\to$ `02-plan` $\to$ `03-execute` $\to$ `04-verify`)**, keeping active context strictly within the **2,000–8,000 token sweet spot**.

---

## 2. Direct Machine-Readable & Plaintext URLs (HTTP 200 text/plain — 100% Public)

- **Crawler Plaintext Digest (Gitingest)**: `https://gitingest.com/imshubhamsocial/dotfiles-hermes`
- **Evaluation Tests Digest (Gitingest)**: `https://gitingest.com/imshubhamsocial/hermes-tests`
- **dotfiles-hermes GitHub API Tree**: `https://api.github.com/repos/imshubhamsocial/dotfiles-hermes/git/trees/a062d46?recursive=1`
- **hermes-tests GitHub API Tree**: `https://api.github.com/repos/imshubhamsocial/hermes-tests/git/trees/main?recursive=1`
- **Substrate Repository**: `https://github.com/imshubhamsocial/dotfiles-hermes` (Commit: `a062d46`)
- **Raw Evaluation Repository**: `https://github.com/imshubhamsocial/hermes-tests` (`main` branch)
- **Canonical v52 Config**: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/a062d46/private_dot_hermes/config.yaml`
- **Root Workspace Map**: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/a062d46/AGENTS.md`
- **Layer 1 Pipeline Router**: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/a062d46/CONTEXT.md`
- **Root Invariants**: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/a062d46/rules/invariants.md`
- **Hardware VRAM Invariants**: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/a062d46/rules/hardware_vram_invariants.md`
- **Phase 55 Signed Status**: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/a062d46/phases/phase_55_icm_tripartite_scaffolding_and_v45_sealing/03_verify/status.json`

---

## 3. Inlined Ground-Truth Artifacts & Empirical Telemetry

### 3.1 Signed Phase 55 Verification Receipt
```json
{
  "phase_id": 55,
  "phase_name": "phase_55_icm_tripartite_scaffolding_and_v45_sealing",
  "status": "VERIFIED_AND_SEALED",
  "assertions_passed": 15,
  "assertions_failed": 0,
  "config_version": 45,
  "default_model": "nemotron-3.5-bolt-e4b",
  "max_turns": 40,
  "normalized_output_rule_enforced": true,
  "vram_ceiling_mib": 5800.0,
  "verified_at": "2026-10-30T17:28:16+05:30"
}
```

### 3.2 Gauntlet A Live Empirical Telemetry & Auto-Compaction Receipt
```
=== Llama-Server Substrate Metrics (Port 8138) ===
llamacpp:prompt_tokens_total 204290
llamacpp:prompt_tokens_seconds 1095.62
llamacpp:predicted_tokens_total 22927
llamacpp:predicted_tokens_seconds 23.2537
llamacpp:n_tokens_max 59178

=== Decoding Throughput vs Context Depth ===
1. Short Context (< 8k tokens): 38.45 tokens/second (Prefill: 1,380 t/s)
2. Mid Context (25k tokens):    27.05 tokens/second (Prefill: 1,196 t/s)
3. Deep Context (55,124 tokens): 19.99 tokens/second (Prefill: 820 t/s, 42s prefill latency)
4. Compaction Event: Hermes native compaction fires at 55,124 tokens -> prunes to 7,236 tokens
5. Post-Compaction Speed (7,236 tokens): 32.56 tokens/second (Prefill: 1,003 t/s, 7.21s latency)

=== Gauntlet A Cold Verification Contract Check ===
$ cd benchmarks/gauntlet_a_voxel_fps && bash ./contract.sh
Server running on http://127.0.0.1:8080 (20Hz tick)
Client connected: id1
Client connected: id2
[PASS] Gauntlet A Contract Verified (Exit code 0)
```

### 3.3 Live NVML Hardware Telemetry
```bash
$ nvidia-smi --query-gpu=memory.used,memory.total,temperature.gpu --format=csv,noheader
4311 MiB, 6144 MiB, 56
```
* **Active VRAM**: 4,311 MiB / 6,144 MiB physical GDDR6.
* **Safety Margin**: 1,489 MiB below the 5,800.0 MiB contract ceiling.
* **Upstream Submodule Purity**: `git -C ~/.hermes/hermes-agent status --porcelain` returns 0 lines (100% clean).

---

## 4. The Four Mandatory Directives for Gemini Argon

### Directive 1: Production Implementation Green-Light Audit
* Perform a forensic audit of the sealed Phase 55 implementation and canonical v52 configuration against upstream `NousResearch/hermes-agent`.
* Verify that Candidate 3 (`NVIDIA-Nemotron-3.5-Bolt-E4B-UD-Q4_K_XL.gguf` with companion drafter `dflash-NVIDIA-Nemotron-3.5-Bolt-E4B-Q8_0.gguf`) running on Port 8138 is completely compliant with our native 65,536 context length.
* Confirm that active VRAM (4,311 MiB) maintains a 1,489 MiB margin below the 5,800.0 MiB operational ceiling.
* Confirm upstream purity is 100% clean (`git status --porcelain` empty, 0 bespoke Python wrappers in `scripts/` or `plugins/`).
* If fully verified, **issue an authoritative production GREEN certification**.

### Directive 2: Forensic Analysis of Cancelled Benchmark & Context Dynamics
* Using `hermes-tests` and Document 02:
  * Analyze why Hermes reached 55k tokens under the initial monolithic prompt.
  * Mathematically derive the token speed curve ($38.5\text{ t/s} \to 27.1\text{ t/s} \to 19.4\text{ t/s} \to 32.56\text{ t/s}$) against the physical memory bandwidth ceiling (~192 GB/s) of the RTX 3050 Laptop GPU.
  * Prove why DFlash speculative decoding sustained 19.4 t/s at 55k context where pure autoregressive decoding would drop to 10–12 t/s.
  * Explain the stream silence watchdog notice (`⏳ waiting on nemotron... 60s waiting for first stream chunk`) from `agent/chat_completion_stream_monitor.py` as an informational heartbeat during 40s prompt prefill on 45k tokens, not an error.
  * Prove from `ui-tui/src/app/slash/commands/session.ts` why `/reasoning show` is a pure React UI display toggle adding 0 prompt tokens.
  * Verify that the underlying codebase passed [`contract.sh`](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/benchmarks/gauntlet_a_voxel_fps/contract.sh) cold on Port 8080.
  * Synthesize historical GDR findings in their original state.

### Directive 3: Formal Certification of Configs, Values, and Testbed Scripts
* Formally audit and certify:
  * Native `context_length: 65536` pinned across `.hermes/config.yaml`, binary launcher, and upstream profile.
  * Elimination of prompt bloat via `agent.tool_use_enforcement: false` and `agent.execution_guidance: false`.
  * Gateway stage model routes on Port 8642.
  * OpenViking TrieHI memory engine on Port 1933 with CPU embeddings on Port 8139.
  * Headless verification contracts (`contract.sh`) and AST linters across all gauntlets.
* **Issue an explicit GREEN certification for configs, values, and tests**.

### Directive 4: ICM Staged Restructuring for All Seven Frontier Gauntlets
Explain why monolithic prompt formulation violates Jake Van Clief's runtime context discipline (arXiv:2603.16021), which mandates maintaining active working context strictly between 2,000 and 8,000 tokens.

Then, for **ALL SEVEN GAUNTLETS**, formulate, restructure, and provide the complete operational blueprint and copy-pasteable prompts following **Jake Van Clief's ICM Staged Execution Protocol**:

1. **Gauntlet A**: *Voxel Paintball FPS Multiplayer with WebSockets* ([`Sunwood-ai-labs/threejs-voxel-frontier`](https://github.com/Sunwood-ai-labs/threejs-voxel-frontier) & [`nickyvanurk/voidfall`](https://github.com/nickyvanurk/voidfall))
2. **Gauntlet B**: *Autonomous Browser Gaming on `splatbox.alexdiaz.fyi` via CDP Port 9222* ([`browser-use/browser-use`](https://github.com/browser-use/browser-use) & [`vercel-labs/agent-browser`](https://github.com/vercel-labs/agent-browser))
3. **Gauntlet C**: *3D WebGL Aquarium Simulation with Dual-FBO Waves* ([`evanw/webgl-water`](https://github.com/evanw/webgl-water) & [`martinRenou/threejs-water`](https://github.com/martinRenou/threejs-water))
4. **Gauntlet D**: *`leanrea` POSIX Reverse Engineering Benchmark* ([`aicodeking/leanrea`](https://github.com/aicodeking/leanrea))
5. **Gauntlet E**: *`ffmpeg-skill` Deterministic Video Editor* ([`kajisho5/ffmpeg-skill`](https://github.com/kajisho5/ffmpeg-skill))
6. **Gauntlet F**: *`diagram-design` Editorial HTML+SVG Visualizer* ([`cathrynlavery/diagram-design`](https://github.com/cathrynlavery/diagram-design))
7. **Gauntlet G**: *`markitdown` Multi-Format Document Ingestion* ([`microsoft/markitdown`](https://github.com/microsoft/markitdown))

#### Restructuring Architecture for Each Gauntlet:
For each gauntlet, you must provide:
* **The ICM Staged Pipeline**:
  * **Stage 1 (Spec & Scaffolding Prompt)**: Scopes inputs, dependencies, directory trees, and seals stage receipt (Context: ~2.5k–3.5k tokens).
  * **Stage 2 (Modular Execution Prompt)**: Generates authoritative server/engine/scripts with strict AST validation (Context: ~4k–6k tokens).
  * **Stage 3 (Fresh Verification Gate Prompt)**: Headless smoke integration test, contract execution, and `status.json` sealing.
* **Exact CLI Invocations**: Upstream `hermes` CLI commands running in KDE Konsole TUI on Wayland/X11 (using valid skill names, zero category flags, and native working directory scoping).
* **Throughput & Latency Model**: Proving how staged execution maintains peak **35.0–45.0 tokens/second** generation speed, keeps KV cache scan overhead near zero, and eliminates prompt prefill stalls entirely.

---

### Directive 5: Research Patches & Optimizations for llama-server (NVIDIA Nemotron 3.5 Bolt + DFlash Drafter)

Conduct deep architectural and open-source systems research into upstream `ggml-org/llama.cpp` PRs, patches, and runtime compiler flags specifically tailored for our local inference engine:
1. **DFlash Drafter Integration & Initialization Patches**:
   * Investigate runtime warnings observed during model init:
     * `llama_init_from_model: failed to initialize the context: dflash requires ctx_other to be set`
     * `[spec] failed to measure draft model memory: failed to create llama_context from model`
   * Evaluate upstream PRs for DFlash block-diffusion drafters in `llama.cpp` to eliminate context allocation mismatches and optimize draft model memory footprints.
2. **Tokenizer & Special EOG Token Alignment**:
   * Analyze the token override logs observed on Nemotron 3.5 Bolt:
     * `control-looking token: 212 '</s>' was not control-type; this is probably a bug in the model. its type will be overridden`
     * `control-looking token: 50 '<|tool_response>' was not control-type; its type will be overridden`
     * `special_eog_ids contains '<|tool_response>', removing '</s>' token from EOG list`
   * Provide the exact GGUF metadata or tokenizer patch to ensure canonical end-of-generation (EOG) recognition and eliminate potential tool-call truncation.
3. **Throughput & Accuracy Maximization within our 1,489 MiB VRAM Surplus**:
   * With 1,489 MiB of physical headroom below the 5,800.0 MiB ceiling, evaluate upgrading Key-cache precision from `q4_0` to `q8_0` (`--cache-type-k q8_0 --cache-type-v q4_0`, consuming ~256 MiB surplus). Quantify its impact on draft-target logit KL-divergence and speculative acceptance probability ($\alpha$).
   * Evaluate expanding prompt batch buffers (`-b 4096 -ub 1024` or `-ub 2048`) to accelerate prompt prefill beyond 1,500 tokens/second.
   * Evaluate speculative tree depth tuning (`--spec-draft-n-max`, `--spec-draft-n-min`, `--spec-draft-p-min`) and CUDA graph options (`GGML_CUDA_GRAPH_OPT=1`, `GGML_CUDA_FORCE_MMQ=1`) for sustained 42.50–46.20 tokens/second generation.
````
