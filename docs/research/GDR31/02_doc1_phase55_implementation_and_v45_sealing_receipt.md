# GDR31 Technical Report: Phase 55 Implementation & v45 Configuration Sealing

> **Status**: VERIFIED & SEALED  
> **Phase Identifier**: `phase_55_icm_tripartite_scaffolding_and_v45_sealing`  
> **Ledger Number**: Phase 55 (Total Completed: 55 Phases)  
> **Git Commit**: [`imshubhamsocial/dotfiles-hermes@a062d46`](https://github.com/imshubhamsocial/dotfiles-hermes/commit/a062d46edf2c5b79d7c7e5ac9c13c76fcaa44cb1)  
> **Verification Contract**: 15 / 15 Passing Assertions (Exit Code 0)

---

## 1. Phase 55 Problem Statement & Motivation

In GDR30, Gemini Argon conducted an exhaustive forensic autopsy of historical GDR phases, the 12 benchmark remediation fixes, Candidate 1's catastrophic tool call collapse, and Jake Van Clief's Interpretable Context Methodology (arXiv:2603.16021). Argon identified three critical engineering requirements to transition Hermes Agent OS into production:

1. **Tripartite Separation of Concerns**: Replace monolithic prompt files with Jake Van Clief's tripartite contract files across all operational directories:
   - `invariants.md`: Hard operational & mathematical bounds (The "Never" Layer, $\le 80$ lines).
   - `rules.md`: Procedural heuristics & execution order (The "Always / Ask First" Layer, $\le 120$ lines).
   - `references.md`: Machine-readable schemas & port indices (The "Knowledge" Layer, $\le 200$ lines).
   - `CONTEXT.md`: Pipeline routing & stage handoffs (The "Routing" Layer, $\le 80$ lines).
2. **Standardized Directory Topology**: Establish this tripartite structure symmetrically across:
   - Root workspace (`/rules/`, `/references/`, `AGENTS.md`, `CONTEXT.md`, `CLAUDE.md`).
   - 4-Stage Pipeline (`stages/01-spec/`, `stages/02-plan/`, `stages/03-execute/`, `stages/04-verify/`).
   - Benchmark suites (`benchmarks/tau_bench/`, `benchmarks/gaia/`, `benchmarks/ast_grep_eval/`).
   - Starter templates (`_templates/phase_template/`, `_templates/benchmark_template/`).
3. **Canonical Configuration Sealing (v45)**:
   - Crown **Candidate 3 (NVIDIA Nemotron 3.5 Bolt)** as default agent model.
   - Map stage-specific model routes in `gateway.api_server.model_routes`.
   - Purge decommissioned Candidate 1 from configuration.
   - Increase `agent.max_turns` to `40`.
   - Maintain eager core tools (`tools.tool_search: "off"`) to pin 99.8% prefix cache hits.

---

## 2. Inventory of Implemented Files (49 Files Created / Modified)

```
hermes/
├── AGENTS.md                                             # Layer 0 Map (36 lines <= 80)
├── CONTEXT.md                                            # Layer 1 Router (31 lines <= 80)
├── CLAUDE.md                                             # 1-line pointer to AGENTS.md
├── rules/
│   ├── invariants.md                                     # Hard bounds (22 lines <= 80)
│   ├── rules.md                                          # Procedural directives (23 lines <= 120)
│   ├── hardware_vram_invariants.md                       # NVML ceilings & thread pinning
│   ├── anti_rationalization_tables.md                    # Six Jev Gates
│   └── anti_sycophancy_directives.md                     # 17 grounding rules
├── references/
│   ├── references.md                                     # Schema registry (27 lines <= 200)
│   └── substrate_ports.md                                # Ports 8138, 8642, 8139, 1933, 20128
├── stages/
│   ├── 01-spec/{CONTEXT,invariants,rules,references}.md + output/.gitkeep
│   ├── 02-plan/{CONTEXT,invariants,rules,references}.md + output/.gitkeep
│   ├── 03-execute/{CONTEXT,invariants,rules,references}.md + output/.gitkeep
│   └── 04-verify/{CONTEXT,invariants,rules,references}.md + output/.gitkeep
├── benchmarks/
│   ├── tau_bench/{CONTEXT,invariants,rules,references}.md + output/.gitkeep
│   ├── gaia/{CONTEXT,invariants,rules,references}.md + output/.gitkeep (Normalized Final Answer)
│   └── ast_grep_eval/{CONTEXT,invariants,rules,references}.md + output/.gitkeep
├── _templates/
│   ├── phase_template/{CONTEXT,invariants,rules,references}.md + output/.gitkeep
│   └── benchmark_template/{CONTEXT,invariants,rules,references}.md + output/.gitkeep
├── phases/
│   ├── phase_55_icm_tripartite_scaffolding_and_v45_sealing/
│   │   ├── 01_spec/spec.md                               # Stage 1 Spec
│   │   ├── 02_impl/task.md                               # Stage 2 Plan
│   │   ├── 03_verify/contract.sh                         # Stage 3 Deterministic Contract
│   │   └── 03_verify/status.json                         # Stage 4 Receipt
│   └── status_ledger.json                                # Phase 55 marked complete
└── private_dot_hermes/config.yaml                        # Canonical v45 configuration
```

---

## 3. Canonical v45 Production Configuration

The configuration was sealed across `~/.hermes/config.yaml`, `~/.local/share/chezmoi/private_dot_hermes/config.yaml`, and workspace `./.hermes/config.yaml`:

```yaml
# ~/.hermes/config.yaml — Certified GDR30 Production Configuration
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

# Declarative Fix for Upstream Issues #56360 & #81670:
# Eliminates 7.2 KB of boilerplate prompt bloat and prevents raw-text tool leaks on Port 8642.
# Stage behavioral constraints are supplied by ICM Layer 1/2 markdown files (AGENTS.md / CONTEXT.md).
agent:
  tool_use_enforcement: false
  execution_guidance: false
  task_completion_guidance: false
  parallel_tool_call_guidance: false
  max_turns: 40

# Declarative Gateway & Zero-Code Stage Model Routing (Port 8642)
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

# Core tools are always eager; keeping tool_search "off" preserves 99.8% KV prefix cache hits
# across the 7 lightweight OpenViking/Jev plugin tools without extra tool_describe round-trips.
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

# Official OpenViking Hierarchical Memory Plugin (Port 1933, CPU Embeddings on Port 8139)
memory:
  provider: openviking
  openviking:
    host: 127.0.0.1
    port: 1933
    auto_extract: true
    session_flush: true
    prune_stale_days: 7
    ebbinghaus:
      enabled: true
      decay_rate: 0.05
      retention_threshold: 0.15
      consolidation_interval_hours: 24
      long_term_spillover_dir: ~/.hermes/memory/ebbinghaus_vault
    triehi:
      index_file: ~/.hermes/memory/triehi_index.json
      stair_l2_cache_size: 4096
      l0_exact_match_threshold: 0.95
      l1_prefix_match_threshold: 0.85
      l2_hierarchical_min_similarity: 0.70
      l3_temporal_decay_factor: 0.02
      l4_epistemic_validation_required: true

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

---

## 4. Deterministic Verification Contract Execution

The verification contract (`contract.sh`) was executed cold against the live filesystem:

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

---

## 5. Live Telemetry & Upstream Substrate State

- **Active Model**: `NVIDIA-Nemotron-3.5-Bolt-E4B-UD-Q4_K_XL.gguf` on Port 8138 (`taskset -c 0-5`, 6 CPU threads, `-ngl 99`, `-md dflash-NVIDIA-Nemotron-3.5-Bolt-E4B-Q8_0.gguf`, `-c 65536`, FlashAttention enabled, 38.83 t/s speculative decoding).
- **Physical GPU VRAM**: **4,999 MiB / 6,144 MiB** (Headroom: 1,145 MiB; Buffer to Invariant: 801 MiB).
- **GPU Temperature**: 57°C.
- **Upstream Submodule (`.hermes/hermes-agent`)**: `git status --porcelain` returns 0 lines (100% clean).
- **Status Ledger**: Appended with Phase 55 marked `complete`, `strikes: 0`, `verified: true`.
- **Git Push**: Pushed to `https://github.com/imshubhamsocial/dotfiles-hermes` at commit `a062d46`.
