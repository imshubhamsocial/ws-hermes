# GDR31 Master Consultation Prompt for Gemini Argon

> **Instructions for User**: Copy the entire markdown block below and paste it directly into your Gemini Argon consultation session.

---

````markdown
# Architectural Consultation: Real-World Production Certification, Upstream Open-Source Skill Sourcing, and Frontier Multi-Modal Gauntlet Execution (GDR31)

## 0. The Golden Rule for GDRs: Epistemic Self-Containment Protocol

> **Epistemic Invariant**: To guarantee 100% certification verifiability even if external cloud crawlers face network firewalls, rate limits, or dynamic client-side JavaScript rendering barriers on third-party sites:
> 1. **Tier 1 — Verbatim Inlined Payloads (Zero-Network Required)**: All critical configuration files, verification receipts, test logs, target web application DOM hierarchies, and mathematical PDEs are embedded verbatim within this prompt.
> 2. **Tier 2 — AI-Digest Plaintext Mirrors (Single-URL Crawl via Gitingest)**: The complete repositories are mirrored as continuous, crawler-friendly Markdown digests (`https://gitingest.com/imshubhamsocial/dotfiles-hermes` and `https://gitingest.com/imshubhamsocial/hermes-tests`).
> 3. **Tier 3 — GitHub API Recursive JSON Trees**: Complete filesystem manifests listing every file, path, and blob hash in a single structured JSON response without HTML scraping.
> 4. **Tier 4 — Public Raw Plaintext Endpoints**: All individual files are accessible via direct `raw.githubusercontent.com` URLs (HTTP 200 text/plain).

> 5. **Markdown AST & Google Docs Export Integrity (The Document Golden Rule)**:
>    - **Strict Code Fence Parity**: Every code fence (triple-backticks) opened MUST be strictly closed. Never emit unclosed code fences. The total count of code fences must always be even (`count % 2 == 0`). (In the prior run, you omitted closing fences in 7 sections, causing Google Docs import to crash with Error 3).
>    - **Zero Nested Code Fences in Scripts/Heredocs**: Never write unescaped triple backticks inside `cat << 'EOF'` heredocs, bash setup blocks, or templates. Use 4 backticks for outer enclosing blocks, or indent code blocks by 4 spaces.
>    - **Single-Line Headings & Clean Tables**: Headings (`#`) and table rows (`|`) must never contain unescaped line breaks.
>    - **Clean LaTeX Math**: Use standard `$ ... $` for inline math and `$$ ... $$` for block math without duplicate MathML or raw HTML tags.

### Direct Machine-Readable & Plaintext URLs (HTTP 200 text/plain — 100% Public)
- **Crawler Plaintext Digest (Gitingest)**: `https://gitingest.com/imshubhamsocial/dotfiles-hermes`
- **Evaluation Tests Digest (Gitingest)**: `https://gitingest.com/imshubhamsocial/hermes-tests`
- **dotfiles-hermes GitHub API Tree**: `https://api.github.com/repos/imshubhamsocial/dotfiles-hermes/git/trees/a062d46?recursive=1`
- **hermes-tests GitHub API Tree**: `https://api.github.com/repos/imshubhamsocial/hermes-tests/git/trees/fc97c64?recursive=1`
- **Substrate Repository**: `https://github.com/imshubhamsocial/dotfiles-hermes` (Commit: `a062d46`)
- **Raw Evaluation Repository**: `https://github.com/imshubhamsocial/hermes-tests` (Commit: `fc97c64`)
- **Canonical v45 Config**: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/a062d46/private_dot_hermes/config.yaml`
- **Root Workspace Map**: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/a062d46/AGENTS.md`
- **Layer 1 Pipeline Router**: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/a062d46/CONTEXT.md`
- **Root Invariants**: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/a062d46/rules/invariants.md`
- **Root Rules**: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/a062d46/rules/rules.md`
- **Phase 55 Spec**: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/a062d46/phases/phase_55_icm_tripartite_scaffolding_and_v45_sealing/01_spec/spec.md`
- **Phase 55 Contract**: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/a062d46/phases/phase_55_icm_tripartite_scaffolding_and_v45_sealing/03_verify/contract.sh`
- **Phase 55 Signed Status**: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/a062d46/phases/phase_55_icm_tripartite_scaffolding_and_v45_sealing/03_verify/status.json`
- **Status Ledger**: `https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/a062d46/phases/status_ledger.json`

---

## 1. System Orientation & Inlined Ground-Truth Artifacts

You are evaluating **Hermes Agent OS**, an autonomous local agent operating under **Jake Van Clief's Interpretable Context Methodology (ICM / MWP, arXiv:2603.16021)**:
$$\text{60% Infrastructure (POSIX/Git/NVML)} \quad+\quad \text{30% Pure Markdown Orchestration} \quad+\quad \text{10% AI Cognition (4B Local Model)}$$

### 1.1 Inlined Signed Phase 55 Verification Receipt
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

### 1.2 Inlined Cold-Run Contract Execution Trace (15/15 Pass)
```bash
=== Executing Phase 55 Verification Contract ===
[PASS] 1. Root Tripartite files exist (rules/{invariants,rules}.md, references/{references,substrate_ports}.md, CLAUDE.md)
[PASS] 2. Stages 01-04 contain all 4 contract files (CONTEXT, invariants, rules, references)
[PASS] 3. Standardized benchmark suites exist with full tripartite contracts
[PASS] 4. Starter templates exist for phases and benchmarks
[PASS] 5. All CONTEXT.md files strictly <= 80 lines
[PASS] 6. All invariants.md files strictly <= 80 lines
[PASS] 7. All rules.md files strictly <= 120 lines
[PASS] 8. All references.md files strictly <= 200 lines
[PASS] 9. Normalized Final Output Rule enforced in benchmarks/gaia/rules.md
[PASS] 10. config.yaml specifies _config_version: 45 and default: nemotron-3.5-bolt-e4b
[PASS] 11. config.yaml sets max_turns: 40 and maps stage model_routes
[PASS] 12. Decommissioned Candidate 1 purged from config.yaml models
[PASS] 13. Zero bespoke Python or shell scripts in scripts/ or plugins/
[PASS] 14. Upstream .hermes/hermes-agent repository is 100% clean and unpatched
[PASS] 15. Live NVML GPU VRAM <= 5,800.0 MiB on RTX 3050
=== Summary: 15 Passed, 0 Failed ===
```

### 1.3 Inlined Canonical v45 Production Configuration (`config.yaml`)
```yaml
_config_version: 45

model:
  provider: local-llama
  default: nemotron-3.5-bolt-e4b
  base_url: http://127.0.0.1:8138/v1
  context_length: 65536

providers:
  local-llama:
    api_base: http://127.0.0.1:8138/v1
    api_key_env: LOCAL_LLAMA_API_KEY
    stale_timeout_seconds: 120
    models:
      nemotron-3.5-bolt-e4b:
        context_length: 65536
        max_output_tokens: 4096
      gemma-4-E4B-it-qat-exact:
        context_length: 131072
        max_output_tokens: 4096
  local-embedding-cpu:
    api: http://127.0.0.1:8139/v1
    api_key_env: LOCAL_EMBEDDING_API_KEY
    models:
      embeddinggemma-2-27b-cpu:
        context_length: 8192
        dimensions: 768

agent:
  tool_use_enforcement: false
  execution_guidance: false
  task_completion_guidance: false
  parallel_tool_call_guidance: false
  max_turns: 40

gateway:
  host: 127.0.0.1
  port: 8642
  api_server:
    auth:
      enabled: true
      extra:
        direct_model_requests: true
      model_routes:
        hermes-agent:
          provider: local-llama
          model: nemotron-3.5-bolt-e4b
        icm-tier1b-policy:
          provider: local-llama
          model: nemotron-3.5-bolt-e4b
        icm-tier1a-coding:
          provider: local-llama
          model: gemma-4-E4B-it-qat-exact

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
    host: 127.0.0.1
    port: 1933
    auto_extract: true
    session_flush: true
    prune_stale_days: 7

auxiliary:
  curator:
    provider: local-llama
    model: nemotron-3.5-bolt-e4b
    timeout: 600

plugins:
  enabled:
    - openviking
    - jev-curator
```

### 1.4 Dedicated Hardware Telemetry & Drafter Optimization Logic
- **Physical GPU**: Discrete NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB physical GDDR6). **The full 6 GB VRAM is dedicated and available for Hermes!**
- **Active Telemetry**: **4,303 MiB / 6,144 MiB** GDDR6, 56°C (`Disp.A: Off`), leaving **1,497 MiB (~1.5 GB)** of free safety headroom below the 5,800.0 MiB operational ceiling.
- **Substrate Daemons**:
  - Port 8138: `llama-server` running Candidate 3 (`NVIDIA-Nemotron-3.5-Bolt-E4B-UD-Q4_K_XL.gguf`, native 65,536 context, FlashAttention, Q4_0 KV cache) accelerated by companion drafter `dflash-NVIDIA-Nemotron-3.5-Bolt-E4B-Q8_0.gguf` (381 MB), delivering **38.83 tokens/second** speculative decoding throughput.
  - Port 8642: Hermes Gateway (`sk-hermes-local-prod-12345678`).
  - Port 1933: OpenViking Hierarchical TrieHI Memory Server.
  - Port 20128: OmniRoute Gateway.
- **Upstream Submodule (`.hermes/hermes-agent`)**: `git status --porcelain` is completely empty (100% clean).

> [!NOTE]
> **Substrate Context Length & Drafter Headroom Evaluation**:  
> In GDR29–GDR30, `131072` (128K) was set across all models following Gemma 4 specifications. However, official HuggingFace specifications confirm that `Nemotron-3.5-Bolt-E4B` natively supports a maximum context length of **65,536 tokens (64K)**. Realigning Bolt to its native 65,536 context cuts unified KV cache allocation in half. This critical headroom enables the companion **DFlash Q8_0 speculative decoding drafter** (which previously triggered CUDA OOM at 128K) to fit comfortably within physical GDDR6 at **4,303 MiB**, accelerating decoding from 25.5 t/s to **38.83 tokens/second** while remaining well below the 5,800.0 MiB safety ceiling. Gemma 4 variants retain their native 131,072 context length.  
> **Drafter & Headroom Question for Argon**: Since Hermes has ~1.5 GB of free VRAM headroom available before hitting the 5,800.0 MiB ceiling, could we or should we use a Q4 variant of the drafter (e.g. `dflash-NVIDIA-Nemotron-3.5-Bolt-E4B-Q4_K_M.gguf`), or a larger companion drafter model, or allocate larger batch/ubatch sizes (`-b 4096`, `-ub 2048`)? What is the mathematically and empirically optimal VRAM-to-throughput configuration given this 1.5 GB surplus on our dedicated 6 GB GPU?

### 1.5 Fresh GAIA-1 Parity Benchmark Verification Across All 3 Substrates
Following this context alignment and native `ddgs` integration, all three candidate substrates were evaluated against the original GAIA Level 1 Sample 0 benchmark in dedicated Konsole windows (`--hold`):

| Substrate | Physical Context | Active VRAM | Decoding Speed | Final Output | Verification |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Candidate 1 (Gemma 4 QAT + MTP)** | 131,072 (128K) | 4,373 MiB | 28.21 t/s | **`17000`** | **100% PASS** |
| **Candidate 2 (xbill9 Exact QAT + Drafter)** | 131,072 (128K) | 4,169 MiB | 29.32 t/s | **`17000`** | **100% PASS** |
| **Candidate 3 (Nemotron 3.5 Bolt + DFlash)** | **65,536 (64K)** | **4,303 MiB** | **25.42 – 38.83 t/s** | **`17000`** | **100% PASS** |

All three models extracted the Moon perigee ($356,352.93\text{ – }356,400\text{ km}$) and Eliud Kipchoge's marathon record ($21.02\text{ km/h}$), calculated $\approx 16,950\text{ – }17,100\text{ hours}$, and emitted the exact ground-truth integer **`17000`**.

### 1.6 Upstream Hermes CLI Ground Truth (`hermes chat --help`)
The upstream `NousResearch/hermes-agent` CLI natively includes the following built-in flags:
```text
--in DIR              Change into DIR before starting or resuming (scopes '--resume latest' / -c lookups to DIR's workspace).
--accept-hooks        Auto-approve any unseen shell hooks declared in config.yaml without a TTY prompt.
--worktree, -w        Run in an isolated git worktree (for parallel agents on the same repo).
-s, --skills SKILLS   Preload one or more skills for the session (repeat flag or comma-separate).
--oneshot             Run the query and exit when finished without entering interactive mode.
--checkpoints         Enable filesystem checkpoints before destructive file operations.
--max-turns N         Maximum tool-calling iterations per conversation turn.
```
> [!IMPORTANT]
> **CRITICAL DIRECTIVE ON CLI GRAMMAR**:  
> In the prior run, you hallucinated that `--in <dir>` and `--accept-hooks` do not exist in upstream Hermes. They are **official built-in flags of NousResearch/hermes-agent**. Do not claim they are non-existent. Both `hermes chat --in <dir>` and `cd <dir> && hermes chat` are supported upstream patterns.

### 1.7 Complete Inventory of Available Built-In Tools, Skills, and Infrastructure
To enable Argon to architect all gauntlets, skills, and memory systems strictly under Jake Van Clief's ICM architecture without inventing non-existent wrappers:
- **Upstream Built-In Tools (`hermes-agent/tools/`)**:
  - `terminal_tool.py`: POSIX command execution, environment variable handling, output truncation.
  - `file_tools.py`: Deterministic file read, write, edit, patch, and line-range inspection.
  - `search_tools.py`: Codebase AST search via `ast-grep` and semantic pattern matching.
  - `web_tools.py` & `web_tools_extract.py`: Web crawling and content extraction backed by native DuckDuckGo (`ddgs`) with a strict 4-result cap.
  - `vision_tools.py` & `vision_sidecar`: Image inspection, UI understanding, and multimodal token handling via `embeddinggemma2` on Port 8139.
  - `approval.py` & `clarify_tool.py`: User approval gating and structured clarifications.
  - `mcp_serve.py`: Upstream native Model Context Protocol (MCP) server integration.
- **Browser-Use & Computer-Use Stack**:
  - `browser_tool.py`, `browser_cdp_tool.py`, `browser_use_cli.py`, `browser_supervisor.py`: Official upstream browser automation tools.
  - Host Google Chrome Dev (`com.google.ChromeDev`) executed via `/usr/bin/distrobox-host-exec` with `--remote-debugging-port=9222`.
  - Direct Chrome DevTools Protocol (CDP) WebSocket communication on Port 9222.
  - Host filesystem profile bridging via `/run/host/tmp/` or `$HOME/.cache/`.
- **Installed Skills Catalog (`~/.hermes/skills/`)**:
  - `icm-architect`: Pure markdown ICM tripartite auditor, folder validator, and scaffolding generator.
  - `software-development`: Git workflows, refactoring, code review, testbed generation.
  - `research`: Literature synthesis, deep paper summarization.
  - `devops`, `mlops`, `productivity`, `creative`, `engineering`.
- **ICM & Golden Rules Architecture**:
  - Layer 0: `AGENTS.md` (Workspace map, 3-tier permissions, hard invariants).
  - Layer 1: `CONTEXT.md` (Pipeline routing, stage handoffs).
  - Layer 2: `rules/{invariants,rules,hardware_vram_invariants,anti_rationalization_tables,anti_sycophancy_directives}.md`.
  - Layer 3: `references/{references,substrate_ports}.md`.
  - Active working context discipline: strictly maintained between 2,000 and 8,000 tokens.
  - Zero-bespoke invariant: no custom python plugins or handcrafted wrapper scripts in `scripts/` or `plugins/`.

---

## 2. Core Question 1: Production Green-Light Certification & Config Defaults Evaluation

In Phase 55, we established Jake Van Clief's standardized Tripartite Scaffolding (`invariants.md`, `rules.md`, `references.md`) across root, stages 01–04, benchmark suites, and templates, respecting all line caps (`CONTEXT.md` $\le 80$, `invariants.md` $\le 80$, `rules.md` $\le 120$, `references.md` $\le 200$), and sealed canonical configuration **v45**.

**Argon's Mandatory Auditing Directives**:
1. **Source Code & Default Values Analysis**:
   - Inspect our source code via the 4-Tier verification URLs (Gitingest mirrors, GitHub API trees, raw endpoints).
   - Evaluate the exact default values we set in `config.yaml` (`model.default: nemotron-3.5-bolt-e4b`, `model.context_length: 65536`, `tools.tool_search: "off"`, `agent.tool_use_enforcement: false`, `agent.execution_guidance: false`, `agent.task_completion_guidance: false`, `gateway.platforms.api_server.extra.direct_model_requests: true`, `memory.provider: openviking`, `curator.enabled: true`, etc.).
   - Compare these values with upstream `hermes-agent` default values as well as with our implementation Phases (Phases 1 through 55).
2. **ICM Architect & Benchmark Enforcement Verification**:
   - Audit our `icm-architect` skill ([`~/.hermes/skills/icm-architect/SKILL.md`](file:///var/home/imshubhamsocial/.hermes/skills/icm-architect/SKILL.md)).
   - Audit benchmark runs and logs (`benchmarks/gaia`, `benchmarks/tau_bench`, `benchmarks/ast_grep_eval`) to verify that all constraints, ICM layers, and hardware limits were factually enforced during execution without leaks.
3. **Formal Green-Light Determination**:
   - Issue a definitive, unambiguous determination: **Is Hermes Agent OS officially GREEN for actual, direct real-world engineering deployment in production workspaces?**

---

## 3. Core Question 2: Tripartite Blueprint for Seven Frontier Gauntlets and Skill Targets (Grounding in Real Upstream GitHub Projects)

> [!CRITICAL]
> **CRITICAL ZERO-BESPOKE DIRECTIVE**:  
> In our core architecture (GDR26–GDR28), **authoring bespoke, synthetic scripts or handcrafted `SKILL.md` snippets from scratch is strictly forbidden**.  
> You **MUST** conduct a real literature and GitHub repository investigation to identify, cite, and architect around **actual upstream open-source GitHub projects, established community repositories, and official agent skill packages** (such as `anthropics/skills`, `browser-use/browser-use`, `browser-use/browser-harness`, `89luca89/distrobox`, `evanw/webgl-water`, `jeantimex/threejs-water`, `Sunwood-ai-labs/threejs-voxel-frontier`, `nickyvanurk/voidfall`, `aicodeking/leanrea`, `kajisho5/ffmpeg-skill`, `cathrynlavery/diagram-design`, `microsoft/markitdown`, `zhengkid/Dream-RSI`).  
> Explain how Hermes integrates these real upstream projects as clean Layer 3 Reference schemas (`references.md`) and package dependencies under Jake Van Clief's 60/30/10 methodology. **Do NOT provide handwritten synthetic `cat << 'EOF'` skill blocks.**

> [!IMPORTANT]
> **OPERATOR INTERACTIVE TUI LAUNCH WORKFLOW ACROSS ALL SEVEN GAUNTLETS**:  
> For **ALL SEVEN** tests below (Gauntlets A, B, C, D, E, F, and G), the human operator execution workflow is simple, standardized, and interactive:  
> 1. The human operator will either `cd <target_workspace>` or invoke `hermes chat --in <target_workspace> --accept-hooks` (optionally passing preloaded skills via `-s <skill>`), launching the **Hermes interactive TUI directly**.  
> 2. The operator will then **copy-paste the exact prompt Argon provides directly into the Hermes TUI** to execute and test the task.  
> Therefore, Argon's prompt deliverables for each gauntlet must be complete, self-contained, copy-paste ready, and designed to run smoothly in an interactive Hermes TUI session without requiring complex custom shell harnesses or headless wrapper scripts.

> [!NOTE]
> **UNIVERSAL ICM ARCHITECTURE & GDR PHASE ENFORCEMENT MANDATE FOR ALL SKILLS**:  
> For all candidate skills (`leanrea`, `ffmpeg-skill`, `diagram-design`, and `markitdown`), they **MUST** strictly follow Jake Van Clief's ICM architecture (ICM / MWP, arXiv:2603.16021) and the rigorous phase enforcement standards of prior GDRs—just like how Hermes OS verified benchmarks with deterministic contract assertions, AST safety checks, and zero-code purity.  
> **AND/OR additionally**, these skills must adhere to Jake Van Clief's standardized folder and pre-requisites structure (`CONTEXT.md` $\le 80$ lines, `invariants.md` $\le 80$ lines, `rules.md` $\le 120$ lines, `references.md` $\le 200$ lines) under the strict 2,000–8,000 token active context discipline.

For **EACH** of the seven tests below, Argon must formulate the complete operational blueprint adhering strictly to Jake Van Clief's 60/30/10 tripartite contract model (`invariants.md`, `rules.md`, `references.md`, `CONTEXT.md`) and real upstream GitHub project mapping:

### 3.1 Gauntlet A: Voxel Paintball FPS Multiplayer with WebSockets
- **The Prompt**: A colleague benchmarked GPT Astra with the exact prompt:  
  `"I asked Claude to make a voxel paintball FPS multiplayer game with websockets"`  
  We want to supply this identical prompt to Hermes.
- **Environment**: Hermes runs inside the `ws-hermes` Distrobox container with an isolated home directory (`/var/home/imshubhamsocial`), hosted on Fedora Kinoite 44 (rpm-ostree atomic desktop).
- **Argon's Deliverables**:
  1. *Upstream GitHub Project Mapping*: Research and cite existing open-source GitHub projects implementing Three.js voxel sandboxes and real-time multiplayer WebSockets (e.g. `Sunwood-ai-labs/threejs-voxel-frontier`, `nickyvanurk/voidfall`, `mrdoob/three.js`, `websockets/ws`).
  2. *Tripartite Pre-requisite Structure*: Exact file contents and schemas for `invariants.md` (Node.js `ws` + Three.js instanced rendering, 60 FPS target, zero-stubs), `rules.md` (modular client-server separation, packet schemas), `references.md` (PointerLockControls and WebSocket event specs grounded in upstream repos), and `CONTEXT.md`.
  3. *Launch Protocol & Prompt*: Exact command (`cd <dir> && hermes chat` or `hermes chat --in <dir> --accept-hooks`) to launch Hermes TUI directly, and the prompt string for the user to copy-paste.

---

### 3.2 Gauntlet B: Autonomous Computer & Browser Gaming on `https://splatbox.alexdiaz.fyi/`
- **The Goal**: Open Google Chrome Dev (Flatpak installed on the host OS), navigate to `https://splatbox.alexdiaz.fyi/` (a 3D voxel browser paintball game with targets, paint physics, ammo, timer, and score), analyze the game, and achieve high-accuracy automated gameplay (approaching 100%).
- **Substrate & Environment**:
  - Host OS: Fedora Kinoite 44 with Flatpak `com.google.ChromeDev`.
  - Container OS: `ws-hermes` Distrobox container with `/usr/bin/distrobox-host-exec` and shared network localhost.
  - Multimodal Vision Stack: Local `embeddinggemma2` CPU daemon (Port 8139) / multimodal capabilities + `opencv-python` inside container.
- **Verbatim Inlined Splatbox DOM Hierarchy (Zero Web Fetch Required)**:
```html
<div id="hud" hidden>
  <div id="crosshair"></div>
  <div class="hud-top">
    <div class="stat"><span class="label">Score</span><span id="score">0</span></div>
    <div class="stat timer"><span class="label">Time</span><span id="timer">60</span></div>
    <div class="stat"><span class="label" id="third-label">Accuracy</span><span id="accuracy">–</span></div>
  </div>
  <div class="hud-bottom">
    <div class="ammo">
      <span class="label" id="weapon-name">Rifle</span>
      <span id="ammo">40</span><span class="label inline" id="capacity">/ 40</span>
      <div id="reload-bar"><div></div></div>
    </div>
  </div>
</div>
<div id="overlay">
  <div class="panel">
    <button id="play" disabled>Loading…</button>
    <ul class="controls">
      <li>WASD move · Shift sprint · Space jump · Click shoot · R reload · 1–5 weapons</li>
    </ul>
  </div>
</div>
```
- **Argon's Deliverables**:
  1. *Upstream GitHub Project Mapping*: Map this automation to real upstream projects: `browser-use/browser-use`, `browser-use/browser-harness`, `vercel-labs/agent-browser`, and `89luca89/distrobox`.
  2. *Host Bridging & Automation Loop*:
     - **Multimodal `embeddedgemma2` Integration**: Do NOT omit `embeddedgemma2` or substitute an exclusively synthetic OpenCV circle detector! You MUST architect the agent loop around `embeddedgemma2`'s multimodal vision tokens/capabilities for visual target verification, state assessment, and aiming decisions.
     - **3D PointerLockControls Reality**: `splatbox.alexdiaz.fyi` uses **PointerLockControls** (`document.pointerLockElement`). In PointerLock, absolute screen coordinates (`x, y`) are ignored by the browser. You MUST specify relative mouse delta movements (`movementX`, `movementY`) via CDP `Input.dispatchMouseEvent` to rotate the 3D camera, followed by Left Click to shoot.
     - **Distrobox Host `/tmp` Boundary**: Host Flatpak Chrome logs/profiles exist on the Host filesystem, accessed inside `ws-hermes` via `/run/host/tmp/` or `$HOME` (e.g. `~/.cache/chrome_dev_debug`), not container-isolated `/tmp`.
     - **Ballistic Gravity Compensation**: Ground target acquisition with ballistic gravity drop compensation ($\Delta y_{\text{drop}} = \text{clip}(380.0 / \max(R_{\text{px}}^2, 25), 1.0, 28.0)\text{ px}$).
  3. *Tripartite Files & Launch Prompt*: Complete `invariants.md`, `rules.md`, `references.md`, the exact launch command (`cd <dir> && hermes chat` or `hermes chat --in <dir> --accept-hooks`), and the copy-paste prompt string for the operator to paste into the interactive Hermes TUI.

---

### 3.3 Gauntlet C: 3D WebGL / JavaScript Aquarium Simulation (Water Ripples, Ball Drops, Shadows)
- **The Demonstration**: Frontier models (Qwen, Claude) demonstrated generating a 3D JavaScript aquarium simulation based on Evan Wallace's classic WebGL Water demo—featuring fish swimming with boid motion, dynamic water surface with 2D wave equation PDEs, caustic light projections, shadows, and an interactive sphere that drops into the pool causing realistic wave ripples and boundary collisions.
- **Inlined Mathematical PDEs & Physics**:
  - Wave Equation PDE: $\frac{\partial^2 z}{\partial t^2} = c^2 \nabla^2 z - d \frac{\partial z}{\partial t}$
  - Discretized Dual-Framebuffer Ping-Pong:
    $$z_{t+1}(x, y) = 2 z_t(x, y) - z_{t-1}(x, y) + c^2 \Delta t^2 \nabla^2 z_t - d \Delta t (z_t - z_{t-1})$$
  - Sphere Buoyancy & Drag: $\mathbf{F}_{net} = m \mathbf{g} + \rho_{water} V_{sub} \mathbf{g} - \frac{1}{2} C_d \rho A |\mathbf{v}|\mathbf{v}$
- **Argon's Deliverables**:
  1. *Upstream GitHub Project Mapping*: Conduct a deep analysis of:
     - **`evanw/webgl-water`** (Evan Wallace's canonical WebGL Water demo)
     - **`jeantimex/threejs-water`** (Yong Su's Three.js port with heightfield water simulation, raytraced caustics, soft shadows, and rigid-body sphere physics)
     - **`martinRenou/threejs-water`** & **`martinRenou/threejs-caustics`**
     - **`mrdoob/three.js`** (`webgl_gpgpu_birds` for boid flocking fish)
  2. *Mathematical & Shader Forensics*:
     - **Heightfield Wave PDEs & Dual Framebuffer Ping-Pong**: Discretized 2D wave equations and ping-pong render targets.
     - **Clamped Spherical Cap Buoyancy**:
       $$V_{\text{sub}}(d_s) = \begin{cases} 0 & \text{if } d_s \le 0 \\ \frac{\pi d_s^2}{3}(3r - d_s) & \text{if } 0 < d_s < 2r \\ \frac{4}{3}\pi r^3 & \text{if } d_s \ge 2r \end{cases}$$
       *(Note: Unclamped formulas produce negative buoyancy when $d_s > 3r$, causing deep submerged spheres to accelerate downward infinitely. Clamping is mandatory).*
     - **WebGL2 HalfFloat Filtering**: Note that `LinearFilter` on `THREE.HalfFloatType` textures in WebGL2 requires checking and enabling the `OES_texture_float_linear` extension.
     - **Caustics & Fresnel**: Raytraced / screen-space caustics and Fresnel reflection/refraction.
  3. *Tripartite Pre-requisite Structure*: Exact `invariants.md`, `rules.md`, `references.md`, and `CONTEXT.md` for this simulation workspace.
  4. *Launch Protocol & Prompt*: Exact command (`cd <dir> && hermes chat` or `hermes chat --in <dir> --accept-hooks`) to launch Hermes TUI directly, and the precise, self-contained prompt to copy-paste into Hermes to synthesize this complex simulation end-to-end.

---

### 3.4 Gauntlet D: Quick Installation, Pre-requisites & Recon Test for `leanrea`
- **The Upstream Repository**: [`https://github.com/aicodeking/leanrea`](https://github.com/aicodeking/leanrea)
- **Description**: *"One 8 KB skill that replaces REA (Reverse Engineer Anything): plain CLI tools, no MCP. Benchmarked: 38% faster, 35% cheaper."*
- **The Architectural Rationale**:
  REA previously introduced a 25 MB npm package and 207 MCP tools into context. `leanrea` proves that coding agents perform significantly better (38% faster wall time, 35% lower cost, 56% fewer turns, 60% fewer tokens at 74/75 accuracy) by dropping the MCP layer completely and executing native POSIX CLI tools directly through bash (`asar`, `otool`/`objdump`, `nm`, `go version -m`, `jadx`, `apktool`, `ghidra`, `tshark`, `binwalk`, `sqlite3`).
- **Argon's Deliverables**:
  1. *Folder & Pre-requisite Topology*: Define the installation and workspace layout for `skills/leanrea/` (or `benchmarks/leanrea_eval/`) inside the `ws-hermes` Distrobox container.
  2. *Tripartite Pre-requisites*: Provide the exact contents of `CONTEXT.md`, `invariants.md` (zero MCP tools, native bash commands only), `rules.md` (recon heuristics per binary target type), and `references.md` (cli flag cheatsheets for native binaries).
  3. *Quick Verification Test & Prompt*: Exact command (`cd <dir> && hermes chat -s leanrea` or `hermes chat --in <dir> --accept-hooks -s leanrea`) to launch Hermes TUI directly, and the prompt string for the operator to copy-paste to verify leanrea recon under strict Phase contracts.

---

### 3.5 Gauntlet E: Quick Installation, Machine-Readable Contract & Test for `ffmpeg-skill`
- **The Upstream Repository**: [`https://github.com/kajisho5/ffmpeg-skill`](https://github.com/kajisho5/ffmpeg-skill)
- **Description**: *"Local video editor for coding agents: 42 FFmpeg tools with a machine-readable contract and an MCP server, for Claude Code, Cursor and Codex. Cut, captions, reframe, loudness, platform exports. No cloud, no API keys."*
- **The Architectural Rationale**:
  Provides 42 deterministic video editing primitives operating 100% locally with standard `ffmpeg` and `ffprobe` binaries. Crucially enforces machine-readable contract validation, requiring the agent to inspect output stream metadata (`ffprobe`) to verify resolution, duration, and codec compliance before reporting task completion.
- **Argon's Deliverables**:
  1. *Folder & Pre-requisite Topology*: Define the layout for `skills/ffmpeg-skill/` inside `ws-hermes`, ensuring local `ffmpeg` and `ffprobe` binaries are available without cloud APIs.
  2. *Tripartite Pre-requisites*: Provide `CONTEXT.md`, `invariants.md` (local execution only, zero cloud egress, stream validation before completion), `rules.md` (codec selection, lossless cuts, EBU R128 loudness standards), and `references.md` (filtergraph chains and contract JSON schemas).
  3. *Quick Verification Test & Prompt*: Exact command (`cd <dir> && hermes chat -s ffmpeg-skill` or `hermes chat --in <dir> --accept-hooks -s ffmpeg-skill`) to launch Hermes TUI directly, and the prompt string for the operator to copy-paste to test ffmpeg-skill editing and contract verification.

---

### 3.6 Gauntlet F: Quick Installation, ICM Tripartite Contract & Test for `diagram-design`
- **The Upstream Repository**: [`https://github.com/cathrynlavery/diagram-design`](https://github.com/cathrynlavery/diagram-design)
- **Description**: *"Editorial diagram design for Claude Code, Codex, GitHub Copilot, Cursor, Factory Droid, Qoder, and Pi. 45 diagram types. Self-contained HTML + SVG. No shadows. No Mermaid slop."*
- **The Architectural Rationale**:
  Solves the fragile rendering and visual bloat of markdown diagramming tools by generating clean, self-contained single-file HTML + SVG editorial diagrams across 45 standard archetypes (architecture topologies, state machines, cloud infrastructure, sequence DAGs) with crisp typography and zero external CDN script dependencies.
- **Argon's Deliverables**:
  1. *Folder & Pre-requisite Topology*: Define the layout for `skills/diagram-design/` (or `benchmarks/diagram_design_eval/`) inside `ws-hermes`, enforcing Jake Van Clief's tripartite pre-requisites (`CONTEXT.md`, `invariants.md`, `rules.md`, `references.md`) and GDR phase contracts.
  2. *Tripartite Pre-requisites & Rules*:
     - `CONTEXT.md`: Pipeline routing & stage handoffs ($\le 80$ lines).
     - `invariants.md`: Hard structural bounds (self-contained HTML/SVG only, zero shadows, valid XML tags, zero external JS CDNs, $\le 80$ lines).
     - `rules.md`: Diagram type selection heuristics (from 45 supported archetypes), typography, and palette assignment ($\le 120$ lines).
     - `references.md`: Machine-readable SVG viewBox coordinate schemas and archetype templates ($\le 200$ lines).
  3. *GDR Phase Verification & Quick Test*: Provide the contract test script (asserting valid SVG/HTML DOM parsing via Python `xml.etree.ElementTree` with exit code 0) and the exact command (`cd <dir> && hermes chat -s diagram-design` or `hermes chat --in <dir> --accept-hooks -s diagram-design`) to launch Hermes TUI directly, along with the prompt string for the operator to copy-paste.

---

### 3.7 Gauntlet G: Quick Installation, Pre-requisite Structure & Document Ingestion Test for `microsoft/markitdown`
- **The Upstream Repository**: [`https://github.com/microsoft/markitdown`](https://github.com/microsoft/markitdown)
- **Description**: *"Python tool and library for converting files and office documents to Markdown."*
- **The Architectural Rationale**:
  Solves multi-modal document extraction and ingestion by converting diverse enterprise and technical document formats (PDF, DOCX, XLSX, PPTX, HTML, CSV, JSON, XML, Audio metadata, and Image OCR) directly into standard GitHub-Flavored Markdown. In Hermes Agent OS, this powers Layer 3 Knowledge conversion and document synthesis without vendor lock-in, external cloud parsing APIs, or context window bloating.
- **Argon's Deliverables**:
  1. *Folder & Pre-requisite Topology*: Define the layout for `skills/markitdown/` (or `benchmarks/markitdown_eval/`) inside `ws-hermes`, specifying clean dependency installation (`pip install markitdown` in container venv) while maintaining host purity.
  2. *Tripartite Pre-requisites & Rules*:
     - `CONTEXT.md`: Pipeline routing & stage handoffs ($\le 80$ lines).
     - `invariants.md`: Hard structural bounds (local execution only, zero cloud egress, deterministic output, strict exit code 0, $\le 80$ lines).
     - `rules.md`: Format conversion heuristics (PDF text extraction, tables in XLSX/DOCX to markdown tables, image OCR routing, $\le 120$ lines).
     - `references.md`: CLI syntax, Python API bindings, supported MIME types, error codes ($\le 200$ lines).
  3. *GDR Phase Verification & Quick Test*: Provide the contract test script (asserting successful conversion of a multi-format document fixture into clean markdown with exit code 0) and the exact command (`cd <dir> && hermes chat -s markitdown` or `hermes chat --in <dir> --accept-hooks -s markitdown`) to launch Hermes TUI directly, along with the prompt string for the operator to copy-paste.

---

### 3.8 Research & Architecture Directive: Direct Incorporation of Nested Learning
- **The Reference**: [`https://x.com/simplifyinAI/status/2114314774779408777`](https://x.com/simplifyinAI/status/2114314774779408777) (`https://t.co/VQVLhKUrWS` $\to$ [`arXiv:2512.24695`](https://arxiv.org/abs/2512.24695))
- **The Paper**: *"Nested Learning: The Illusion of Deep Learning Architectures"* by Ali Behrouz, Meisam Razaviyayn, Peilin Zhong, Vahab Mirrokni (Google Research).
- **Argon's Research & Architecture Mandate**:
  Conduct a thorough investigation of the Nested Learning paradigm and analyze how Hermes Agent OS can directly incorporate its principles:
  1. *Nested Multi-Timescale Optimization*: How do we formally structure Hermes' operational loops into nested optimization levels:
     - **Micro-Timescale (Turn Level)**: Fast prompt inference and eager tool selection on Port 8138 / 8642.
     - **Meso-Timescale (Session Level)**: Reflective session compression and memory card extraction.
     - **Macro-Timescale (System Level)**: Offline Dream-RSI and weightless rule/skill evolution.
  2. *Deep Optimizers as Associative Memory*: How do we model gradient-based associative memory compression into our OpenViking Hierarchical TrieHI Memory server on Port 1933 to index multi-turn trajectories without updating base model weights?
  3. *Continuum Memory System (CMS) & HOPE*: How does CMS bridge working context (strictly 2,000–8,000 tokens) with long-term memory retrieval to eliminate context dilution while maximizing task success?

---

### 3.9 `Dream-RSI` System Service Architecture (`https://github.com/zhengkid/Dream-RSI`)
- **The Upstream Repository**: [`https://github.com/zhengkid/Dream-RSI`](https://github.com/zhengkid/Dream-RSI) (*"Dream-RSI: Recursive Self-Improvement through Evolving Worlds"* by Tong Zheng et al., Google DeepMind / UMD / UVA).
- **Core Invariant**: *"An agent must dream to recursively self-improve. History is the world it dreams in."*
- **Hermes Historical Foundation**:
  Hermes previously implemented Dream-RSI foundations across Phase 16 (DreamRSI Replay Simulator & MASS Loop), Phase 20 (Continuous RSI Meta-Loop), Phase 23 (Open-World Replay Pool Dream-RSI 2.0), Phase 25 (Master ARSI Kernel), Phase 29 (Live SQLite WAL Sync), and `docs/reference/04_mathematical_foundations_rsi.md`.
- **Existing Daemon Configuration (`hermes-rsi-daemon.service`)**:
```ini
[Unit]
Description=Hermes Agent OS 24/7 Autonomous RSI & Synthetic Gauntlet Daemon
After=network.target hermes-llama-server.service hermes-openviking.service

[Service]
Type=simple
Environment="CUDA_VISIBLE_DEVICES="
Environment="HERMES_WORKSPACE=/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes"
WorkingDirectory=/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes
ExecStart=/usr/bin/distrobox enter ws-hermes -- /usr/bin/python3.13 -u .hermes/hermes_rsi_daemon.py
Restart=always
RestartSec=10
MemoryMax=2G

[Install]
WantedBy=default.target
```
- **Argon's Deliverables**:
  1. *Upstream System Service Restructuring*: Properly structure and optimize our `hermes-rsi-daemon.service` to adhere as closely as possible to the official `Dream-RSI` evolving worlds / counterfactual replay paradigm while adapting it cleanly for our local Hermes OS setup (CPU RAM execution, zero GPU VRAM impact, replay trees in `.hermes/cache/dream_worlds/`, OpenViking memory sync).
  2. *Execution Scheduling Determination*: Since Hermes has completed extensive benchmark runs (GAIA, Tau-Bench, AST-grep, synthetic gauntlets), advise on the optimal scheduling: **Should we execute a dreamRSI consolidation run once before running this GDR's tests/benchmarks (to optimize heuristics based on historical traces) or immediately after them?**

---

### 3.10 Research & Architecture Directive: Agentic Design Patterns PDF Analysis & ICM Mapping
- **The Reference**: [`https://irp.cdn-website.com/ca79032a/files/uploaded/Agentic-Design-Patterns.pdf`](https://irp.cdn-website.com/ca79032a/files/uploaded/Agentic-Design-Patterns.pdf)  
  *(Original URL with tracking payload: `https://irp.cdn-website.com/ca79032a/files/uploaded/Agentic-Design-Patterns.pdf?fbclid=IwaW9leAVRuDRjbGNrBVG4M2V4dG4DYWVtAjExAHBkb2YFc3J0YwZhcHBfaWQMMzUwNjg1NTMxNzI4AAEfqqb3ydctsZRqYDv1CvOvwfGDzArN1NTROFSYaOIQeCmFnKQs4gGeQ6QX_T0_aem_C4uoa1r5YxW0qz3k9o52AA`)*
- **The Document**: Foundational treatise detailing industry and research agentic design patterns across reflection, tool invocation, dynamic task decomposition, multi-agent collaboration, and memory architectures.
- **Argon's Research & Architecture Mandate**:
  Conduct a rigorous investigation of this PDF treatise and formulate a concrete architectural roadmap for incorporating its core agentic patterns and upstream tools into Hermes Agent OS:
  1. *Deconstruct Core Agentic Patterns*:
     - **Reflection & Self-Correction**: How to map iterative reflection and evaluation loops into deterministic Stage 04 verification gates and dreamRSI replay trees.
     - **Tool Use & Function Calling**: How to structure schema definitions, tool routing, and sandboxing via Distrobox `ws-hermes` without custom python wrappers.
     - **Planning & Task Decomposition**: How dynamic sub-goal generation maps into Jake Van Clief's stage contracts (`01-spec`, `02-plan`, `03-execute`, `04-verify`).
     - **Multi-Agent Orchestration**: How to coordinate specialized roles (architect, implementer, verifier) using Hermes built-in subagents and pure markdown state files.
  2. *Upstream Tools & Framework Mapping*: Identify the real upstream tools, agent frameworks, and evaluation benchmarks highlighted in the PDF, and evaluate which components can be directly integrated or mirrored in Hermes OS.
  3. *Strict ICM Architecture & Discipline Compliance*: All patterns, workflows, and tool configurations must strictly adhere to:
     - Jake Van Clief's Interpretable Context Methodology (ICM / MWP, arXiv:2603.16021).
     - The 60/30/10 Layering Rule (60% Infrastructure | 30% Pure Markdown Orchestration | 10% Local Cognition).
     - Active Working Context Discipline (strictly maintained between 2,000 and 8,000 tokens).
     - Folder and file line budgets (`CONTEXT.md` $\le 80$, `invariants.md` $\le 80$, `rules.md` $\le 120$, `references.md` $\le 200$).

---

## 4. Synthesis & Verdict Guidelines

- **Zero-Bespoke Invariant**: Every skill, tool, and reference pattern must be rooted in established upstream GitHub projects (`anthropics/skills`, `browser-use`, `89luca89/distrobox`, `jeantimex/threejs-water`, etc.). No synthetic handwritten scripts.
- **Adherence to Jake Van Clief's 60/30/10 Standard**: Every prescribed workspace must maintain the 2,000–8,000 token active context discipline and respect all line caps (`CONTEXT.md` $\le 80$, `invariants.md` $\le 80$, `rules.md` $\le 120$, `references.md` $\le 200$).
- **Substrate Purity**: Confirm zero custom code in `scripts/` or `plugins/` and preserve 100% upstream purity of `.hermes/hermes-agent`.
- **Actionable Precision**: Deliver ready-to-run file contents, terminal commands, and prompt strings grounded in upstream open-source code.
- **Strict Code Fence Parity & AST Closure**: Ensure every single code block opened with triple-backticks is closed with triple-backticks before any subsequent heading or text. Never emit unclosed code fences.
````
