# Hermes Infrastructure & Runtime Substrates

**System Identity**: Hermes Agent OS Infrastructure Layer  
**Language Standard**: ASD-STE100 (Simplified Technical English)  
**Parent Index**: [docs/README.md](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/docs/README.md)

---

## 1. Infrastructure Overview

Hermes Agent OS isolates local AI inference, semantic search, and memory into dedicated local services.  
All infrastructure services execute locally on the host or inside the container without external network dependencies.

---

## 2. Infrastructure Services Directory

| Service Name | Port | Systemd User Unit | Description |
| :--- | :--- | :--- | :--- |
| **`llama-server`** | `8138` | `llama-server.service` | Primary LLM inference server running Google Gemma 4 Exact 4B with 128K context and MTP speculative decoding. |
| **`hermes-embedding-cpu`** | `8139` | `hermes-embedding-cpu.service` | CPU-pinned semantic embedding service using EmbeddingGemma 2 at 0 MiB VRAM. |
| **`hermes-openviking`** | `1934` | `hermes-openviking.service` | Local hierarchical memory daemon and context storage engine. |
| **`llama-server-watcher`** | N/A | `llama-server-watcher.service` | Host watchdog for monitoring inference daemon health and memory ceilings. |

---

## 3. Substrate Architecture and Documentation

* [llama-server Manual](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/docs/infrastructure/llama-server.md):  
  Complete configuration, warp-aligned batching derivations, MTP speculative decoding, KV cache prefix pinning, and service management for Port 8138.
* [Hardware Ceilings Invariants](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/.hermes/_config/hardware_ceilings.md):  
  Hard limits for discrete GPU VRAM ($5,800.0$ MiB), CPU thread budgets, and context window sizes.
