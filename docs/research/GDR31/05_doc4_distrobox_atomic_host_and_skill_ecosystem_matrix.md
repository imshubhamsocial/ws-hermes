# GDR31 Technical Report: Distrobox Host Bridging & Upstream Open-Source Skill Sourcing

> **Operational Framework**: Jake Van Clief's 60/30/10 Architecture  
> **Host Infrastructure**: Fedora Kinoite 44 (Atomic Desktop / rpm-ostree)  
> **Agent Runtime**: Distrobox Container (`ws-hermes`) with `/usr/bin/distrobox-host-exec`  
> **Skill Standard**: Open Agent Skill Specification (`SKILL.md`) mapped to Upstream GitHub Projects

---

## 1. Operating Environment Topology

Hermes Agent OS operates in a containerized environment to keep the host operating system completely pure and immutable:

```
┌────────────────────────────────────────────────────────────────────────┐
│ Fedora Kinoite 44 Host (Atomic / Immutable rpm-ostree Desktop)         │
│  - Flatpak Applications: com.google.ChromeDev (Chrome Dev Unstable)    │
│  - NVIDIA Driver 570.xx / NVML Kernel Module                           │
│  - Host D-Bus & Wayland Compositor                                     │
│                                                                        │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │ ws-hermes Distrobox Container (Arch/Fedora Toolchain)            │  │
│  │  - Isolated HOME: /var/home/imshubhamsocial                      │  │
│  │  - Local Daemons: llama-server (8138), Gateway (8642),           │  │
│  │                  OpenViking (1933), OmniRoute (20128)            │  │
│  │  - Host Bridge: /usr/bin/distrobox-host-exec                     │  │
│  │  - Shared Network Namespace: 127.0.0.1 (All Ports Accessible)    │  │
│  │  - Local Vision Stack: embeddinggemma2 (Port 8139) + OpenCV      │  │
│  └──────────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────────┘
```

The host bridge mechanism uses the official upstream **[`89luca89/distrobox`](https://github.com/89luca89/distrobox)** utility `/usr/bin/distrobox-host-exec`, sharing localhost port `9222` between the host Flatpak Chrome process and the container.

---

## 2. Upstream Open-Source Skill Mapping (Zero-Bespoke Grounding)

Under Jake Van Clief's 60/30/10 methodology, Layer 3 Reference skills provide the domain knowledge necessary for a 4B model to match frontier capabilities. In accordance with our core invariants, these skills must map directly to established open-source projects on GitHub rather than being authored as bespoke, unverified scripts:

| Domain / Capability | Upstream GitHub Project | Architectural Role in Hermes |
| :--- | :--- | :--- |
| **Host Execution Bridge** | **[`89luca89/distrobox`](https://github.com/89luca89/distrobox)** | Canonical documentation and command syntax for invoking host Flatpaks and binaries via `/usr/bin/distrobox-host-exec`. |
| **Browser Control (CDP)** | **[`browser-use/browser-use`](https://github.com/browser-use/browser-use)** & **[`browser-use/browser-harness`](https://github.com/browser-use/browser-harness)** | Open-source Python library and MCP server for Chrome DevTools Protocol automation, DOM extraction, and event dispatch. |
| **Agent Skill Standards** | **[`anthropics/skills`](https://github.com/anthropics/skills)** & **[`vercel-labs/agent-browser`](https://github.com/vercel-labs/agent-browser)** | Official public repository of open-standard `SKILL.md` instruction packages and reusable browser automation toolsets. |
| **3D WebGL Water Physics** | **[`evanw/webgl-water`](https://github.com/evanw/webgl-water)** & **[`jeantimex/threejs-water`](https://github.com/jeantimex/threejs-water)** | Canonical Evan Wallace WebGL Water simulation and Yong Su's Three.js port with heightfield GPGPU shaders, caustics, and rigid-body buoyancy. |
| **Voxel Multiplayer Netcode** | **[`Sunwood-ai-labs/threejs-voxel-frontier`](https://github.com/Sunwood-ai-labs/threejs-voxel-frontier)** & **[`nickyvanurk/voidfall`](https://github.com/nickyvanurk/voidfall)** | Open-source implementations of Three.js instanced voxel worlds and server-authoritative WebSocket netcode with client prediction and interpolation. |

---

## 3. Skill Architecture: Progressive Disclosure (Zero VRAM)

In compliance with Phase 4's Two-Tier Progressive Skill Catalog:
1. **Tier 1 (Catalog View)**: Only the `name` and `description` of each skill are loaded into Hermes's prompt index (~30 tokens per skill).
2. **Tier 2 (Surgical Activation)**: The full `SKILL.md` body is loaded into context **only when the active stage explicitly demands it** via Selective Section Routing.
3. **Purity Invariant**: All skills consist purely of standard Markdown (`SKILL.md`) referencing upstream GitHub packages. Zero custom C++/Python modifications to upstream `.hermes/hermes-agent`.
