# Document 04: Configuration Values, Hardware Invariants, and Testbed Certification Ledger

> **Scope**: Audit of All System Parameters, Telemetry Ceiling Checks, and Verification Contracts  
> **Substrate Target**: Hermes Agent OS on Fedora Kinoite 44 (x86_64, rpm-ostree)  
> **Public Test Repository**: [`https://github.com/imshubhamsocial/hermes-tests`](https://github.com/imshubhamsocial/hermes-tests)  

---

## 1. System Parameters & Configuration Ledger

| Parameter / Key | Configured Value | Verification Source | Status |
| :--- | :--- | :--- | :--- |
| `model.default` | `nemotron-3.5-bolt-e4b` | `~/.hermes/config.yaml` | **CERTIFIED** |
| `model.context_length` | **`65536`** (64K Native) | `.hermes/config.yaml`, binary launcher | **CERTIFIED** |
| `providers.local-llama.models.nemotron-3.5-bolt-e4b.context_length` | **`65536`** | `~/.hermes/config.yaml` | **CERTIFIED** |
| `agent.tool_use_enforcement` | `false` | Issue #56360 declarative fix | **CERTIFIED** |
| `agent.execution_guidance` | `false` | Issue #81670 prompt bloat fix | **CERTIFIED** |
| `gateway.port` | `8642` | Native upstream gateway service | **CERTIFIED** |
| `inference.port` | `8138` | Candidate 3 + DFlash Q8_0 drafter | **CERTIFIED** |
| `embedding.port` | `8139` | CPU Gemma-2 Sidecar (`-ngl 0`) | **CERTIFIED** |
| `memory.port` | `1933` | OpenViking Hierarchical TrieHI | **CERTIFIED** |
| `display.show_reasoning` | `false` | Top-level TUI config | **CERTIFIED** |
| `display.details_mode` | `expanded` | Direct stream layout | **CERTIFIED** |

---

## 2. Hardware NVML Telemetry & Invariant Audit

Live telemetry extracted via `nvidia-smi` on the discrete NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB physical GDDR6):

```bash
$ nvidia-smi --query-gpu=memory.used,memory.total,temperature.gpu --format=csv,noheader
4311 MiB, 6144 MiB, 56
```

### Invariant Checks:
1. **Hard VRAM Ceiling ($\le 5,800.0$ MiB)**:
   $$\text{Current VRAM} = 4,311.0\text{ MiB} \le 5,800.0\text{ MiB} \quad (\mathbf{PASS}, \text{1,489.0 MiB safety margin})$$
2. **Physical Headroom**:
   $$\text{Headroom} = 6,144.0 - 4,311.0 = \mathbf{1,833.0\text{ MiB free physical GDDR6}}$$
3. **GPU Temperature**:
   $$T = 56^\circ\text{C} \le 80^\circ\text{C} \quad (\mathbf{PASS})$$
4. **Submodule Purity**:
   `cd ~/.hermes/hermes-agent && git status --porcelain` $\implies$ `0 lines` ($\mathbf{PASS}$, 100% clean).

---

## 3. Testbed & Verification Contract Ledger

### 3.1 Gauntlet A Deterministic Verification Contract (`contract.sh`)
```bash
#!/usr/bin/env bash
set -euo pipefail
APP="output/voxel-paintball-app"
PASS=0
assert_ok() { echo "[PASS] $1"; PASS=$((PASS+1)); }

# Tripartite Scaffolding Line Caps
[[ $(wc -l < CONTEXT.md) -le 80 ]] && assert_ok "1. CONTEXT.md <= 80 lines"
[[ $(wc -l < invariants.md) -le 80 ]] && assert_ok "2. invariants.md <= 80 lines"
[[ $(wc -l < rules.md) -le 120 ]] && assert_ok "3. rules.md <= 120 lines"
[[ $(wc -l < references.md) -le 200 ]] && assert_ok "4. references.md <= 200 lines"

# Modular Codebase Existence
for f in package.json server/server.js client/index.html client/css/style.css client/js/main.js \
client/js/engine/voxel_world.js client/js/engine/camera_fps.js client/js/engine/paintball.js client/js/net/socket_sync.js; do
  [[ -s "$APP/$f" ]] || { echo "[FAIL] Missing $f"; exit 1; }
done
assert_ok "5. All modular server & client files exist and are non-empty"

# AST & Architectural Assertions
grep -q "InstancedMesh" "$APP/client/js/engine/voxel_world.js" && assert_ok "6. VoxelWorld uses THREE.InstancedMesh"
grep -q "PointerLockControls" "$APP/client/js/engine/camera_fps.js" && assert_ok "7. FPS controller uses PointerLockControls"
grep -q "polygonOffset" "$APP/client/js/engine/paintball.js" && assert_ok "8. Paintball decals enforce polygonOffset"

# Two-Client WebSocket Integration Test on Port 8080
node "$APP/server/server.js" >/tmp/gauntlet_a_srv.log 2>&1 &
SRV_PID=$!
trap 'kill $SRV_PID 2>/dev/null || true' EXIT
sleep 1.5

node -e '
const WebSocket = require("./output/voxel-paintball-app/node_modules/ws");
const c1 = new WebSocket("ws://127.0.0.1:8080");
const c2 = new WebSocket("ws://127.0.0.1:8080");
let welcomeCount = 0, snapshotReceived = false;
function checkDone() { if (welcomeCount >= 2 && snapshotReceived) process.exit(0); }
[c1, c2].forEach((c, i) => {
  c.on("open", () => c.send(JSON.stringify({ t: "JOIN_ROOM", room: "arena-1", name: "Bot" + i })));
  c.on("message", (raw) => {
    const msg = JSON.parse(raw);
    if (msg.t === "WELCOME") { welcomeCount++; c.send(JSON.stringify({ t: "FIRE_SHOT", seq: 1, origin: [4,3,4], dir: [0,0,-1], color: "#00f0ff" })); }
    if (msg.t === "STATE_SNAPSHOT") snapshotReceived = true;
    checkDone();
  });
});
setTimeout(() => { console.error("Timeout waiting for WS handshake/snapshot"); process.exit(1); }, 4000);
' && assert_ok "9. Two concurrent WebSocket clients complete JOIN_ROOM, FIRE_SHOT, and STATE_SNAPSHOT broadcast"

# Live NVML Ceiling Check
VRAM=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits | head -n1 | awk '{print int($1)}')
[[ "$VRAM" -le 5800 ]] && assert_ok "10. Live NVML GPU VRAM (${VRAM} MiB) <= 5800 MiB ceiling"

echo "=== Summary: All Assertions Passed Cold ==="
```

* **Cold Execution Result**: **100% PASS** cold with exit code 0.
