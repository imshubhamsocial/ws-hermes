# Document 03: Tier 4 GitHub Repositories, Updated Source Code, and Upstream Mapping Matrix

> **Scope**: Tier 4 Dynamic Cognition, Benchmark Living Testbeds, and Upstream Substrates  
> **Public Test Provenance Repository**: [`https://github.com/imshubhamsocial/hermes-tests`](https://github.com/imshubhamsocial/hermes-tests)  
> **Dotfiles & Configurations Repository**: [`https://github.com/imshubhamsocial/dotfiles-hermes`](https://github.com/imshubhamsocial/dotfiles-hermes)  

---

## 1. Master Tier 4 GitHub Repository Registry

| Repository URL | Target Branch / Commit | Role in Hermes Agent OS Architecture |
| :--- | :--- | :--- |
| [`https://github.com/imshubhamsocial/dotfiles-hermes`](https://github.com/imshubhamsocial/dotfiles-hermes) | `main` (`a062d46`) | Canonical dotfiles, v52 config, systemd daemons, and ICM stage scaffolding. |
| [`https://github.com/imshubhamsocial/hermes-tests`](https://github.com/imshubhamsocial/hermes-tests) | `main` | Public test provenance, raw Inspect AI `.eval` archives, and gauntlet logs. |
| [`https://github.com/NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent) | `main` (`v0.22.5+3086`) | 100% pure, unpatched upstream core substrate (`.hermes/hermes-agent`). |
| [`https://github.com/RinDig/icm-architect`](https://github.com/RinDig/icm-architect) | `main` | ICM / MWP audit and tripartite restructuring skill (`~/.hermes/skills/icm-architect`). |
| [`https://github.com/zhengkid/Dream-RSI`](https://github.com/zhengkid/Dream-RSI) | `main` | Continuous self-improvement and offline memory consolidation daemon. |
| [`https://github.com/Sunwood-ai-labs/threejs-voxel-frontier`](https://github.com/Sunwood-ai-labs/threejs-voxel-frontier) | `main` | Gauntlet A Grounding: `THREE.InstancedMesh` voxel arena and PointerLockControls HUD. |
| [`https://github.com/nickyvanurk/voidfall`](https://github.com/nickyvanurk/voidfall) | `master` | Gauntlet A Grounding: Authoritative Node.js `ws` multiplayer physics & snapshot server. |
| [`https://github.com/browser-use/browser-use`](https://github.com/browser-use/browser-use) | `main` | Gauntlet B Grounding: 20 Hz CDP vision-to-action browser automation loop. |
| [`https://github.com/vercel-labs/agent-browser`](https://github.com/vercel-labs/agent-browser) | `main` | Gauntlet B Grounding: Headless Chrome DevTools Protocol control substrate. |
| [`https://github.com/evanw/webgl-water`](https://github.com/evanw/webgl-water) | `master` | Gauntlet C Grounding: Dual-FBO wave equation PDE solver and caustic textures. |
| [`https://github.com/martinRenou/threejs-water`](https://github.com/martinRenou/threejs-water) | `master` | Gauntlet C Grounding: Three.js WebGL GPGPU heightfield physics integration. |
| [`https://github.com/aicodeking/leanrea`](https://github.com/aicodeking/leanrea) | `main` | Gauntlet D Grounding: Zero-MCP POSIX reverse engineering skill (`~/.hermes/skills/leanrea`). |
| [`https://github.com/kajisho5/ffmpeg-skill`](https://github.com/kajisho5/ffmpeg-skill) | `main` | Gauntlet E Grounding: 42 deterministic FFmpeg video editing primitives. |
| [`https://github.com/cathrynlavery/diagram-design`](https://github.com/cathrynlavery/diagram-design) | `main` | Gauntlet F Grounding: Clean HTML+SVG editorial visualizer (zero Mermaid slop). |
| [`https://github.com/microsoft/markitdown`](https://github.com/microsoft/markitdown) | `main` | Gauntlet G Grounding: Multi-format document ingestion and markdown conversion. |

---

## 2. Updated Canonical Source Code & Configs (`v52`)

### 2.1 File `~/.hermes/config.yaml` (Canonical Configuration v52)
```yaml
# ~/.hermes/config.yaml — Certified GDR31 Production Configuration
_config_version: 52

model:
  provider: local-llama
  default: nemotron-3.5-bolt-e4b
  base_url: http://127.0.0.1:8138/v1
  context_length: 65536

providers:
  local-llama:
    api: http://127.0.0.1:8138/v1
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
      embeddinggemma-2-q8_0:
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
  platforms:
    api_server:
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

curator:
  enabled: true
  interval_hours: 168
  min_idle_hours: 2
  stale_after_days: 14
  archive_after_days: 30
  consolidate: true
  prune_builtins: false
  archive_ttl_days: 180

auxiliary:
  curator:
    provider: local-llama
    model: nemotron-3.5-bolt-e4b
    timeout: 600

plugins:
  enabled:
    - openviking
    - jev-curator
  entries:
    jev-curator:
      settings:
        mode: guard
        provider: custom
        allow_content_egress: false
        timeout_seconds: 25
        max_requests: 50
        max_pairs: 100
        top_k: 5

display:
  show_reasoning: false
  details_mode: expanded
```

---

## 3. Submodule & Codebase Purity Audit

To enforce Phase 55 Assertion 14 and hard invariant safety:

```bash
$ cd ~/.hermes/hermes-agent && git status --porcelain
# Returns 0 lines (100% clean upstream tree)

$ ls ~/.hermes/scripts/ ~/.hermes/plugins/ 2>/dev/null
# scripts/: No bespoke wrappers. Zero custom python hacks.
# plugins/: Contains only upstream openviking and jev-curator descriptors.
```
