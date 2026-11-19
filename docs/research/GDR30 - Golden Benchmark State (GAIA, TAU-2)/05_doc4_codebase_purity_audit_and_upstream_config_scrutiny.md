# Document 4: Codebase Purity Audit, Upstream Config Scrutiny, and Regression Prevention

> **Standard**: Jake Van Clief's Interpretable Context Methodology (ICM / MWP, arXiv:2603.16021)  
> **Repository Commit**: [`imshubhamsocial/dotfiles-hermes@dfc45ab`](https://github.com/imshubhamsocial/dotfiles-hermes/commit/dfc45ab)  
> **Core Focus**: Zero-Bespoke Code Verification, Declarative Config Audit, and GDR Regression Gate

---

## 1. Zero-Bespoke Codebase Purity Audit

A fundamental invariant established in GDR28 is the **Zero-Bespoke Imperative**:
* No bespoke Python wrappers, monkey-patches, or ad-hoc scripts in `scripts/` or `plugins/`.
* Upstream `NousResearch/hermes-agent` must remain 100% clean and un-forked.
* All orchestration must be declarative markdown contracts (`AGENTS.md`, `CONTEXT.md`, stages).

### 1.1 Live Filesystem Verification
* **`scripts/` Directory**: Verified empty. All 17 legacy scripts (`run_remediated_gauntlet.sh`, `mcp_ephemeral_bridge.py`, `ast_canonizer.py`, `epistemic_scorer.py`, etc.) were purged in Phase 53.
* **`plugins/` Directory**: Contains only canonical upstream FastMCP packages (`openviking` Port 1933 memory bridge and `jev-curator` guardrail engine). Zero custom plugin code.
* **Upstream Git Status**: Submodule `.hermes/hermes-agent` is synchronized to official upstream without local modifications.
* **Reference Testbed**: Test code is strictly isolated to canonical testbeds (`tests/ast_grep_eval/fibonacci.c`).

---

## 2. Forensic Scrutiny of Active `config.yaml` Settings

Gemini Argon is instructed to audit the active configuration file ([`private_dot_hermes/config.yaml`](https://raw.githubusercontent.com/imshubhamsocial/dotfiles-hermes/master/private_dot_hermes/config.yaml)) against historical GDR mandates:

```yaml
# ~/.hermes/config.yaml — Canonical Zero-Custom-Code Hermes Agent OS Configuration

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

# Declarative Fix for Upstream Issues #56360 & #81670 (Eliminates Tool Text Leaks & Verification Loops)
agent:
  tool_use_enforcement: false
  execution_guidance: false
  task_completion_guidance: false
  parallel_tool_call_guidance: false
  max_turns: 25

# Declarative Fix for Upstream Issues #28825 & #144082 (Preserves Bare Model Overrides on Port 8642)
gateway:
  host: 127.0.0.1
  port: 8642
  platforms:
    api_server:
      enabled: true
      extra:
        direct_model_requests: true

# Upstream Tiered Tool Search (Set "off" during external benchmark gauntlets)
tools:
  tool_search:
    enabled: "off"
    threshold_pct: 4
    listing_max_tokens: 1200

# Upstream Native LSP Diagnostics
lsp:
  enabled: true
  servers:
    pyright:
      disabled: false

# Official OpenViking Hierarchical Memory Plugin (Port 1933)
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

### 2.1 Key Audit Questions for Argon
1. **Tool Search Setting**: `tools.tool_search.enabled: "off"` was set during external benchmark gauntlets to prevent dynamic tool masking from hiding database tools. Should tool search remain off in production, or should it be toggled to `"auto"` under Jake's ICM stage routing?
2. **Guidance Flags**: `tool_use_enforcement`, `execution_guidance`, and `task_completion_guidance` are set to `false` to suppress upstream prompt text leaks (Issue #56360). Does disabling these flags harm general-purpose coding tasks, or does ICM markdown scaffolding completely replace the need for upstream text guidance?
3. **Model Selection**: Currently, `default: gemma-4-E4B-it-qat` is specified. Based on the empirical failure of Candidate 1 on Tau-Bench, should this default be permanently updated to `nemotron-3.5-bolt-e4b` (Tier 1B Champion) or `gemma-4-E4B-it-qat-exact` (Tier 1A Specialist)?
4. **Context Length**: All models specify `context_length: 131072`. Confirm that this is 100% compliant with TurboQuant Q4_0 KV cache allocations and hardware VRAM constraints.

---

## 3. The Self-Correction & Regression Prevention Protocol

To ensure long-term architectural stability, Argon must subject all recommendations to a rigorous **Regression Prevention Gate**:

```
[Argon Proposed Modification]
          │
          ▼
[GDR Corpus Cross-Check (GDR 1 through GDR 29)]
  ├─ Does it violate the 60/30/10 ratio? (If yes -> REJECT)
  ├─ Does it re-introduce bespoke Python glue code? (If yes -> REJECT)
  ├─ Does it breach the 5,800.0 MiB discrete VRAM ceiling? (If yes -> REJECT)
  ├─ Does it trigger the 32K context floor crash in agent_init.py? (If yes -> REJECT)
  ├─ Does it re-introduce single-endpoint customer identity loops? (If yes -> REJECT)
  └─ Does it break verified contracts in stages 01-04? (If yes -> REJECT)
          │
          ▼
[Formally Certified Recommendation]
```

Every suggestion provided by Argon in its final response must pass this gate and explicitly cite the historical GDR invariants that guarantee its safety.
