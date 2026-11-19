# Document 01: Physical Implementation, Telemetry, and Verification Report

> **Standard**: ASD-STE100 (Simplified Technical English)  
> **Release Package**: GDR37  
> **Target Substrate**: Hermes Agent OS on Fedora Kinoite 44  
> **Inference Engine**: Gemma 4 Exact (`gemma-4-E4B-it-q4_0-exact.gguf` + MTP Drafter)  
> **Hardware Status**: Discrete NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB GDDR6, 4,997 MiB allocated)  
> **Status**: Verified and Sealed  

---

## 1. Executive Summary

We executed all physical actions required by GDR36.
We deployed the complete 5-layer ICM directory architecture in `ws-hermes`.
We configured the Gemma 4 Exact model with 128K context length.
We resolved the WebGL shader bugs in Gauntlet C and the network timing issues in Gauntlet A.
We migrated all workspace configurations and dotfiles into a clean native Git repository.
Phase 58 passed all deterministic audit contracts and is sealed.

---

## 2. Model Configuration and Telemetry Verification

### 2.1 Applied `llama-server` Daemon Parameters

The local daemon `/var/home/imshubhamsocial/.local/bin/llama-server` runs with these exact flags:

```bash
exec taskset -c 0-5 "/var/home/imshubhamsocial/.local/bin/llama-server.bin" \
    --model "/var/home/imshubhamsocial/.hermes/models/gemma-4-E4B-it-q4_0-exact.gguf" \
    --model-draft "/var/home/imshubhamsocial/.hermes/models/gemma-4-E4B-it-qat-assistant-q4_0-exact.gguf" \
    --n-gpu-layers-draft all \
    --spec-type draft-mtp \
    --spec-draft-n-max 2 \
    --alias "gemma-4-E4B-it-qat-exact,gemma-4-e4b-exact,google/gemma-4-E4B-it,nemotron-3.5-bolt-e4b,dory" \
    --host 127.0.0.1 --port 8138 \
    --ctx-size 131072 \
    --cache-type-k q4_0 --cache-type-v q4_0 \
    --batch-size 2048 --ubatch-size 1024 \
    --flash-attn on \
    --reasoning on \
    --jinja \
    --n-gpu-layers 99 \
    --threads 6 --threads-batch 6 --parallel 1 --cont-batching \
    --temp 1.0 --top-p 0.95 --top-k 64 --metrics
```

### 2.2 Client Configuration in `~/.hermes/config.yaml`

```yaml
_config_version: 46

model:
  provider: local-llama
  default: gemma-4-E4B-it-qat-exact
  fallback: nemotron-3.5-bolt-e4b-ud-q4_k_xl
  base_url: http://127.0.0.1:8138/v1
  context_length: 131072

providers:
  local-llama:
    api: http://127.0.0.1:8138/v1

display:
  interface: tui
  details_mode: collapsed
  sections:
    thinking: expanded
    tools: expanded
    activity: hidden
    subagents: collapsed
  mouse_tracking: all
  busy_input_mode: queue
  tui_status_indicator: unicode

skills:
  auto_install: false
  external_dirs:
    - /var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/skills
    - /var/home/imshubhamsocial/.agents/skills

browser:
  cdp_url: http://127.0.0.1:9222

tool_loop_guardrails:
  non_interactive_hard_stop_enabled: true

terminal:
  shell: /bin/bash
  interactive: true
```

### 2.3 Live System Telemetry

| Telemetry Point | Monitored Metric | Target Threshold | Measured Status |
| :--- | :--- | :--- | :--- |
| **GPU Model** | NVIDIA RTX 3050 Laptop | 6,144 MiB total | Verified |
| **Quiescent VRAM** | `nvidia-smi` live query | Maximum 5,120 MiB | 4,997 MiB (PASS) |
| **Free Headroom** | Available VRAM | Minimum 500 MiB | 861 MiB (PASS) |
| **HTTP Health** | Port 8138 `/health` | HTTP 200 `{"status":"ok"}` | PASS |
| **Active Alias** | Port 8138 `/v1/models` | `gemma-4-E4B-it-qat-exact` | PASS |
| **Context Length** | Model Metadata | 131,072 tokens | PASS |

---

## 3. Physical Workspace Scaffolding

We deployed the canonical 5-layer ICM structure inside `/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes`:

1. **`AGENTS.md`**: Canonical Layer 0 operating protocol (< 60 lines).
2. **`CLAUDE.md` and `IDENTITY.md`**: Clean single-line compatibility pointers.
3. **`CONTEXT.md`**: Canonical Layer 1 router (< 80 lines) with keyword triggers (`setup`, `status`, `walk-test`, `quiesce`).
4. **`_config/` Invariants & Conventions**:
   - `_config/invariants.md`: System port map and hardware ceilings.
   - `_config/conventions.md`: 15 core ICM operational conventions.
   - `_config/glossary.md`: Canonical terminology.
   - `_config/hardware_limits.md`: Hardware specifications.
5. **`shared/` Domain Schemas**:
   - `shared/netcode_protocol.md`: 20 Hz synchronization protocol.
   - `shared/vision_schemas.md`: OpenCV HoughCircles detection schemas.
   - `shared/shader_conventions.md`: Three.js shader uniforms dictionary specification.
6. **`stages/` Pipeline**:
   - `stages/01-probe/CONTEXT.md`: Browser DOM inspection.
   - `stages/02-controller/CONTEXT.md`: Centroid and math calibration.
   - `stages/03-execute/CONTEXT.md`: Autonomous action execution.
7. **`_templates/`**: Standard templates for `check.md` and `checkpoint.md`.
8. **`_tools/`**: Deterministic verification tools:
   - `playwright_runtime_audit.py`: Headless browser audit.
   - `hermes_stage_runner.py`: Single-stage contract compiler.
   - `check_vram_limit.py`: Live NVML memory gate.
   - `hermes_icm_validator.py`: Static workspace linter.
9. **`Makefile`**: Standard build targets (`make all`, `make walk-test`, `make phase-58-seal`).

---

## 4. Benchmark Gauntlets Remediations

### 4.1 Gauntlet A: Voxel FPS Multiplayer
- **Problem**: Monolithic script failed to sync with the 20 Hz WebSocket tick.
- **Remediation**: Decomposed into 3 stages. Enforced strict 60-line script limit. Bounded socket latency to under 50 milliseconds.

### 4.2 Gauntlet B: Splatbox OpenCV Ball Tracking
- **Problem**: Python process risked GPU memory fragmentation.
- **Remediation**: Deployed CPU `cv2.HoughCircles`. Verified 0 MiB GPU VRAM consumption. Aiming accuracy within 5 pixels.

### 4.3 Gauntlet C: Three.js Aquarium Shader Material
- **Problem**: The browser logged:
  ```text
  three.module.js:9206 THREE.Material: 'uniform' is not a property of THREE.ShaderMaterial.
  ```
- **Remediation**: Replaced singular `uniform` property with dictionary `uniforms: {}`. Verified clean WebGL rendering with zero console errors.

---

## 5. Native Git Repository Migration & Chezmoi Retirement

We retired chezmoi and converted `/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes` into a native Git repository:

### 5.1 Native Workspace Migration
- We verified and migrated all 1,288 files previously managed by chezmoi into native Git.
- We eliminated all filename mangling (`dot_`, `executable_`, `private_dot_`).
- Files now exist on GitHub under their exact local paths (`_config/`, `stages/`, `benchmarks/`, `.config/`, `.local/`, `.hermes/`).

### 5.2 Native Git Configuration
- Remote origin: `https://github.com/imshubhamsocial/ws-hermes.git`.
- Branch: `master`.
- Comprehensive `.gitignore`: Ignores large archives (`pre_factory_hermes_backup.tar.gz`, 3.6 GB), models (`.hermes/models/`), databases, and caches.
- Clean working tree: `git status` reports 0 untracked files and 0 unstaged modifications.

---

## 6. Deterministic Verification Gate Receipts

We executed all verification gates. Every contract returned exit code 0:

| Gate | Execution Command | Result |
| :--- | :--- | :--- |
| **Static ICM Linting** | `python3 _tools/hermes_icm_validator.py` | 0 errors, 0 warnings (PASS) |
| **Gauntlet A Contract** | `bash benchmarks/gauntlet_a_voxel_fps/contract.sh` | PASS |
| **Gauntlet B Contract** | `bash benchmarks/gauntlet_b_splatbox/contract.sh` | PASS |
| **Gauntlet C Contract** | `bash benchmarks/gauntlet_c_aquarium/contract.sh` | PASS |
| **Phase 58 Verification** | `bash phases/phase_58_.../03_verify/contract.sh` | PASS |
| **Master Build** | `make all` | 0 errors (PASS) |
| **Status Ledger** | `phases/status_ledger.json` | Sealed (58/58 complete) |
