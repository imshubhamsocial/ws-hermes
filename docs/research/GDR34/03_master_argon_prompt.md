# Master Prompt for Gemini Argon (GDR34 Meta-Prompting, ICM Evolution Datasets & Visual Substrate Blueprint)

> **Instructions for User**: Copy the entire markdown block below and paste it directly into your Gemini Argon consultation session.

---

````markdown
# Architectural Consultation: Meta-Prompting, ICM Evolution Datasets, Visual Substrate Grounding, and Frontier Benchmark Certification (GDR34)

## 0. The Golden Rule for GDRs: Epistemic Self-Containment & AST Integrity Protocol

> **Epistemic Invariant**: To guarantee 100% certification verifiability even if external cloud crawlers face network firewalls, rate limits, or dynamic client-side JavaScript rendering barriers on third-party sites:
> 1. **Tier 1 — Verbatim Inlined Payloads (Zero-Network Required)**: All critical configuration files, verification receipts, test logs, hardware telemetry, and mathematical derivations are embedded verbatim within this prompt.
> 2. **Tier 2 — AI-Digest Plaintext Mirrors (Single-URL Crawl via Gitingest)**: The complete repositories are mirrored as continuous, crawler-friendly Markdown digests (`https://gitingest.com/imshubhamsocial/dotfiles-hermes` and `https://gitingest.com/imshubhamsocial/hermes-tests`).
> 3. **Tier 3 — GitHub API Recursive JSON Trees**: Complete filesystem manifests listing every file, path, and blob hash in a single structured JSON response without HTML scraping (`https://api.github.com/repos/imshubhamsocial/dotfiles-hermes/git/trees/a062d46?recursive=1` and `https://api.github.com/repos/imshubhamsocial/hermes-tests/git/trees/main?recursive=1`).
> 4. **Tier 4 — Public Raw Plaintext Endpoints**: All individual files are accessible via direct `raw.githubusercontent.com` URLs (HTTP 200 text/plain).
> 
> 5. **Markdown AST & Google Docs Document Creation Integrity (The Document Golden Rule)**:
>    - **Zero-Failure Google Docs Generation Protocol**: The user will export your response directly into Google Docs via Gemini's "Export to Docs" / Document Creation engine. To prevent Google Docs internal parser crashes (Error 3 / "Failed to create document"), the response MUST maintain 100% strict CommonMark and XML/DOM compliance.
>    - **Strict Code Fence Parity**: Every code fence opened MUST be strictly closed. Never emit unclosed code fences. The total count of code fences must always be even (`count % 2 == 0`).
>    - **Zero Nested Code Fences in Scripts/Heredocs**: Never write unescaped triple backticks inside bash setup blocks, `cat << 'EOF'` heredocs, or templates. Use 4 backticks for outer enclosing blocks, or indent code blocks by 4 spaces.
>    - **Escape All XML/HTML Angle-Bracket Tags in Prose**: Never emit raw unescaped tokens such as `<tool_call>`, `<think>`, `<turn>`, `<focus>`, `<|channel|>`, or `<image>` in markdown prose. Always enclose them in backticks (e.g. `` `<tool_call>` ``) or fenced code blocks so the Google Docs XML parser does not interpret them as malformed HTML tags.
>    - **Single-Line Headings & Clean Tables**: Headings (`#`) and table rows (`|`) must never contain unescaped line breaks. Every table row must have an exact matching count of pipe separators matching the header.
>    - **Clean LaTeX Math**: Use standard `$ ... $` for inline math and `$$ ... $$` for block math without duplicate MathML or raw HTML tags.
>    - **No Truncation or Placeholders**: Never truncate files with `// ... (rest unchanged)` or omit sections. Provide complete, drop-in verifiable files.

---

## 1. Executive Summary & The Problem Statement

Argon, during the live physical execution of **Gauntlet B (Autonomous Browser Gaming on `https://splatbox.alexdiaz.fyi/` via Chrome DevTools Protocol Port 9222)**, Hermes became trapped in a recurring multi-turn failure loop. Rather than achieving live, verified 60-second autonomous gameplay, the agent spent 12+ conversational turns and over 50,000 tokens struggling to generate and patch a monolithic Python script (`output/splatbox_agent.py`, 6,276 bytes).

The test was cleanly canceled and halted. The system is quiescent:
- Discrete NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB GDDR6): active VRAM is **4,311 MiB** (well below the 5,800.0 MiB ceiling), Compute is **0% (Idle)**, 12W power, 55°C.
- Local Daemons: `hermes-llama-server.service` (Port 8138) and `hermes-openviking.service` (Port 1933) are active and healthy.

This failure revealed that the core issue was **not a lack of raw coding capability**, but rather:
1. **Flawed Meta-Prompting & Approach Patterns**: Our prompts spoon-fed mathematical formulas and low-level imperative instructions, triggering "coding exam syndrome" where the agent immediately generated a fragile 250-line async WebSocket client rather than using its tools incrementally to discover the environment.
2. **Missing Closed-Loop Sensory Grounding**: Handcrafting raw WebSocket JSON-RPC frames over CDP without leveraging standard browser automation libraries (`browser-use`, `agent-browser`, `playwright`) or visual scene verification (OpenCV, lightweight vision models) left Hermes blind to the actual browser DOM and Canvas state.
3. **Substrate Alignment**: In single-run isolated stages with fresh context under Jake Van Clief's Interpretable Context Methodology (ICM), we need to analyze whether transitioning to `gemma-4-E4B-it-q4_0-exact` (with 128k context and full reasoning enabled) will resolve tool-calling anomalies and multi-turn mulling loops.

To solve this fundamentally and certify Hermes Agent OS for autonomous benchmark execution, this consultation requests your authoritative architectural guidance across **Seven Golden Points**.

---

## 2. Master Machine-Readable & Plaintext URLs (HTTP 200 text/plain - 100% Public)

- **Crawler Plaintext Digest (Gitingest)**: `https://gitingest.com/imshubhamsocial/dotfiles-hermes`
- **Evaluation Tests Digest (Gitingest)**: `https://gitingest.com/imshubhamsocial/hermes-tests`
- **dotfiles-hermes GitHub API Tree**: `https://api.github.com/repos/imshubhamsocial/dotfiles-hermes/git/trees/a062d46?recursive=1`
- **hermes-tests GitHub API Tree**: `https://api.github.com/repos/imshubhamsocial/hermes-tests/git/trees/main?recursive=1`
- **Hermes Code Repository**: `https://github.com/imshubhamsocial/dotfiles-hermes` (Commit: `a062d46`)
- **Hermes Evaluation Repository**: `https://github.com/imshubhamsocial/hermes-tests` (Commit: `561a728`)
- **Upstream Hermes Agent Substrate**: `https://github.com/NousResearch/hermes-agent` (`main` branch, 100% clean)
- **Jake Van Clief ICM Specification**: `https://github.com/RinDig/Interpretable-Context-Methodology`
- **ICM Starter Template**: `https://github.com/ktncodes/icm-template`
- **Agent Composer Framework**: `https://github.com/vanclief/agent-composer`
- **Authoritative ICM Paper**: `https://arxiv.org/abs/2603.16021`

### Key Raw Plaintext Benchmark Endpoints on GitHub
- **Raw Splatbox Agent Script**: `https://raw.githubusercontent.com/imshubhamsocial/hermes-tests/main/benchmarks/gauntlet_b_splatbox/output/splatbox_agent.py`
- **Raw Gauntlet B Verification Contract**: `https://raw.githubusercontent.com/imshubhamsocial/hermes-tests/main/benchmarks/gauntlet_b_splatbox/contract.sh`
- **Raw Benchmark Analysis Report**: `https://raw.githubusercontent.com/imshubhamsocial/hermes-tests/main/BENCHMARK_ANALYSIS_REPORT.md`
- **Raw Gauntlet B CONTEXT.md**: `https://raw.githubusercontent.com/imshubhamsocial/hermes-tests/main/benchmarks/gauntlet_b_splatbox/CONTEXT.md`

---

## 3. Inlined Empirical Telemetry & Gauntlet B Execution Forensics

### 3.1 Hardware Telemetry & Runtime Ledger
- **Discrete GPU**: NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB physical GDDR6).
- **Active VRAM**: 4,311 MiB ($\le 5,800.0$ MiB active invariant ceiling).
- **GPU Compute Utilization**: 0% (Quiescent idle, 12W power, 55°C).
- **Active Systemd Daemons**:
  - `hermes-llama-server.service` (Port 8138, Nemotron 3.5 Bolt + DFlash Drafter, `-b 2048 -ub 1024 -ctk q4_0 -ctv q4_0`).
  - `hermes-openviking.service` (Port 1933, external memory plugin `endpoint: http://127.0.0.1:1933`).
  - `chrome-dev-cdp.service` (Port 9222, Chrome DevTools Protocol bridge).

### 3.2 Forensic Root-Cause Dissection of Gauntlet B CDP Errors

#### Error 1: Array Parsing KeyError on `/json` Endpoint
- **Symptom**: `TypeError: list indices must be integers or slices, not str` when fetching `http://127.0.0.1:9222/json`.
- **Root Cause**: The CDP HTTP `/json` endpoint returns a JSON **array of dictionaries** (one per tab), not a single dictionary. Attempting `data['webSocketDebuggerUrl']` failed. The agent had to iterate over tabs to match `splatbox` in `tab.get('url', '')`.

#### Error 2: KeyError 0 on `Target.getTargets`
- **Symptom**: `targets['result'][0]['targetId']` threw `KeyError: 0`.
- **Root Cause**: In Chrome DevTools Protocol, `Target.getTargets` returns `{"id": 1, "result": {"targetInfos": [...]}}`. `targets['result']` is a dictionary, not a list. The list is located at `targets['result']['targetInfos']`.

#### Error 3: Chromium PointerLock Security Invariant
- **Symptom**: Synthetic JavaScript execution `document.querySelector('#play').click()` via `Runtime.evaluate` logged:
  `error: A user gesture is required to request Pointer Lock.`
- **Root Cause**: Chromium enforces that PointerLock can **only** be granted during a trusted native user gesture (`isTrusted == true`). Synthetic DOM script clicks are rejected.
- **Remediation**: The agent must call `Page.bringToFront`, compute element bounding coordinates via `getBoundingClientRect()`, and dispatch **native CDP mouse events** via `Input.dispatchMouseEvent` (`mousePressed` with `buttons: 1`, then `mouseReleased` with `buttons: 0`).

#### Error 4: CDP Nested Evaluation Return Schema
- **Symptom**: `json.loads(response)['result']['value']` threw `KeyError: 'value'`.
- **Root Cause**: In CDP `Runtime.evaluate`, successful object execution wraps the result twice: `['result']['result']['value']`.

#### Error 5: Slew Calculation vs Target Centroid Tracking
- **Symptom**: Hardcoding slew speed formulas `clip(380.0 / max(R_px^2, 25), 1.0, 28.0) px` caused the crosshair to violently overshoot or stick, failing to hit targets in the 3D canvas.
- **Root Cause**: Visual scene state must be driven by continuous visual feedback (OpenCV HoughCircles / target centroid detection) rather than static algebraic guesswork.

---

## 4. The Master Consultation Mandates (The Seven Golden Points)

Argon, please perform an exhaustive architectural analysis addressing each of the following Seven Golden Points:

### Golden Point 1: Meta-Prompting & Approach Pattern Failure Analysis
- **Core Mandate**: Analyze, learn the pattern, and dissect the root issues in **our approach for prompts** rather than focusing on the code solution itself. Only by understanding why our prompt structure failed can we devise the proper way of giving prompts while strictly adhering to Jake Van Clief's ICM strategy.
- **Key Questions for Argon**:
  1. Why did our prompts (e.g., `PROMPT.txt`, `PROMPT_STAGE1.txt`) cause Hermes to immediately attempt writing a monolithic 250-line async WebSocket Python script from scratch, instead of using its tools to inspect, research, and test incrementally?
  2. How did spoon-feeding formulas (e.g. `clip(380.0 / max(R_px^2, 25), 1.0, 28.0) px`, `Kp=0.65`, specific selectors) invert the agentic loop and induce "coding exam syndrome"?
  3. Under pure ICM, how should a stage prompt be structured as an architectural compiler contract (`CONTEXT.md` input/output boundary) rather than an imperative task list?

### Golden Point 2: Jake Van Clief's Research & The "One Fact, One Folder" Paradigm
- **Core Mandate**: Research Jake Van Clief and David McDermott's paper (*"Interpretable Context Methodology: Folder Structure as Agent Architecture"*, arXiv:2603.16021) and articles detailing the **"one fact, one folder"** (and "one fact, one home" / "one folder, one job") paradigm.
- **Key Questions for Argon**:
  1. How does Jake define "one fact, one home" to prevent context rot, slow leaks, and multi-agent coordination failures?
  2. How must we incorporate this paradigm properly across Hermes as a whole, including `AGENTS.md`, `SOUL.md`, `CONTEXT.md`, rules, benchmarks, and tests?
  3. What is the exact boundary between global spatial orientation (Layer 0/1) and leaf stage execution?

### Golden Point 3: ICM Datasets & Prior Evolution Artifact Importing
- **Core Mandate**: Research existing datasets, repositories, and templates created by Jake Van Clief or his ecosystem (`RinDig/Interpretable-Context-Methodology`, `ktncodes/icm-template`, `Vanclief/agent-composer`, `jonathanmalkin/icm-field-guide`).
- **Key Questions for Argon**:
  1. Can we directly import these evolution outcomes, folder layouts, and rule trees as modular datasets—analogous to importing datasets for LoRA training—to avoid manually authoring Tier 1 and Tier 2 structures from scratch?
  2. How can we import and mount these structures into Hermes while guaranteeing **zero breakages** with our existing configuration (Port 1933 OpenViking, Port 8138 local-llama, Port 8642 Gateway, upstream purity)?

### Golden Point 4: Architectural Audit of Benchmark Folders, Markdowns, and Navigation
- **Core Mandate**: Inspect our benchmark folders (`benchmarks/gauntlet_b_splatbox/`, `benchmarks/gauntlet_a_voxel_fps/`, etc.), how we separated markdowns into folders, and our actual `AGENTS.md` and `SOUL.md`.
- **Key Questions for Argon**:
  1. Are our benchmark directories currently structured exactly how Jake and his team design their software factory for optimal rule navigation and prompt efficiency?
  2. What changes are required to convert each benchmark into an autonomous, self-contained 3-stage ICM compiler pipeline (`01-probe/`, `02-controller/`, `03-execute/`)?

### Golden Point 5: Substrate Evaluation: Gemma 4 Exact vs Nemotron Bolt
- **Core Mandate**: Analyze whether we should switch our primary coding and execution substrate to `gemma-4-E4B-it-q4_0-exact` instead of `nemotron-3.5-bolt-e4b`.
- **Key Questions for Argon**:
  1. Because ICM enforces single-run, isolated-stage execution with fresh context, does `gemma4-exact` with full reasoning enabled provide superior tool calling, syntax integrity, and instruction following compared to Nemotron Bolt?
  2. Gemma 4 supports up to 128k context natively (while ICM strictly keeps active attention to 2k-8k tokens). Will Gemma 4's deeper reasoning prevent the syntax errors and long mulling loops seen with Nemotron?
  3. Why did Hermes **never perform web searches** or look up browser skill documentation (`browser_exec`, CDP protocols, click events) during Gauntlet B? Was this caused by our prompt wording, tool configuration, or model behavior?

### Golden Point 6: Upstream Browser Tools & Visual Scene Understanding
- **Core Mandate**: Search and evaluate upstream GitHub projects and Python/pip/NodeJS packages for browser automation and visual scene understanding.
- **Key Questions for Argon**:
  1. Why did we have Hermes handcraft raw WebSocket JSON-RPC CDP frames instead of leveraging established upstream tools like `browser-use`, `agent-browser`, `playwright`, or headless CDP runners?
  2. How can OpenCV visual verification (e.g., target centroid tracking) be paired with lightweight vision models (e.g. `embeddinggemma3`, PaliGemma, or local VLM) to provide true scene analysis data so Hermes does not rely on blind coordinate guessing?
  3. How would a real human architect prompt and guide Hermes to research, plan, and implement these capabilities cleanly under Jake Van Clief's ICM methodology?

### Golden Point 7: Deep Research into Jake Van Clief's Commercial & Enterprise Engineering Practices
- **Core Mandate**: Conduct extensive research on prompt engineering, ICM/folder/markdown engineering, and production practices developed and taught by Jake Van Clief and his team in their commercial offerings, enterprise consulting (KPMG UK, Pacific Life, Colgate-Palmolive), and paid masterclass programs (e.g. Clief Notes community, VIP Vault, enterprise playbooks).
- **Key Questions for Argon**:
  1. What specific advanced prompt engineering and context compilation techniques are taught in Jake's enterprise programs that go beyond the basic open-source paper?
  2. How can we officially and natively incorporate all of these enterprise ICM patterns into Hermes Agent OS—across our system architecture, benchmark scaffolding, stage templates, rules, and tests?
  3. How will adopting these commercial-grade practices systematically reshape our current Hermes codebase, benchmark setups, and operational guidelines to guarantee flawless autonomous execution?

---

## 5. Specific Deliverables & Mandates for Argon's Next Submission

Argon, as lead systems architect, please synthesize your findings into the authoritative **GDR34 Master Architectural Blueprint**, delivering:
1. **The Meta-Prompting & ICM Stage Formulation Standard**: The definitive prompt engineering specification for instructing small 4B models without inducing monolithic coding exam syndrome.
2. **The "One Fact, One Folder" Workspace Migration Plan**: Concrete directory refactoring rules for `AGENTS.md`, `SOUL.md`, `CONTEXT.md`, and all benchmark gauntlets.
3. **The ICM Modular Evolution Dataset Specification**: How to curate, import, and mount pre-evolved ICM knowledge packs into Hermes Agent OS with zero configuration breakage.
4. **Substrate Transition Decision**: Clear recommendation on whether to transition to `gemma-4-E4B-it-q4_0-exact` with live benchmarks and VRAM allocation formulas.
5. **Upstream Browser & Visual Scene Tooling Integration**: Concrete architecture integrating `browser-use`, `playwright`, OpenCV, and lightweight vision models (`embeddinggemma3` / PaliGemma).
6. **Commercial ICM Enterprise Framework Blueprint**: Incorporation of Jake Van Clief's enterprise-grade patterns into Hermes Agent OS.
7. **Strict Adherence to Core Invariants**:
   - Hardware VRAM Ceiling: $\le 5,800.0$ MiB on discrete RTX 3050 Laptop GPU (6,144 MiB GDDR6).
   - Upstream Substrate Purity: `.hermes/hermes-agent` remains 100% clean (`git status --porcelain` empty).
   - Zero bespoke Python wrappers in `scripts/` or `plugins/`.
   - Working context discipline: 2,000–8,000 tokens strictly.
   - Zero-Failure Google Docs Generation Protocol: Strict code fence parity (`count % 2 == 0`), CommonMark compliance, and escaped XML tags in prose.

Please save your complete master blueprint output directly to:
`/var/home/imshubhamsocial/Desktop/GDR/GDR34/Output/GDR34 Meta-Prompting, ICM Evolution Datasets & Visual Substrate Blueprint.md`.

We await your authoritative architectural master plan.
````
