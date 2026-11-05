# Substrate Network Port Topology (Layer 3)

| Port | Service Subsystem | Binding Host | Operational Role |
| :--- | :--- | :--- | :--- |
| **8138** | Candidate 3 `llama-server` | `127.0.0.1` | Nemotron 3.5 Bolt + DFlash Drafter (64K context) |
| **8642** | Hermes State Gateway | `127.0.0.1` | Inbound API platform router & stage execution |
| **8139** | CPU Embeddings Sidecar | `127.0.0.1` | EmbeddingGemma 2 CPU (0 MiB GPU VRAM impact) |
| **1933** | OpenViking Server | `127.0.0.1` | Hierarchical TrieHI associative memory engine |
| **9222** | Chrome Dev CDP Bridge | `127.0.0.1` | Autonomous browser evaluation bridge |
