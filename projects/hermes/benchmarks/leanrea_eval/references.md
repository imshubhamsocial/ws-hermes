# Layer 3 Reference Schemas: Gauntlet D (aicodeking/leanrea Fast-Path Router)

## 1. Upstream Repository & Installation
* **Source**: https://github.com/aicodeking/leanrea (SKILL.md, MIT License)
* **Benchmark Reference**: 388 s vs 627 s (-38% time), 55 vs 124 turns (-56% turns), 2.40M vs 5.93M tokens (-60% tokens), 74/75 accuracy.

## 2. Target-Type to Native POSIX CLI Fast-Path Table (ws-hermes Fedora/Arch Linux + macOS)
| Target Type | Magic / Indicator | Fastest One-Shot Native CLI Command |
| :--- | :--- | :--- |
| **ELF / .node Addon** | 7f 45 4c 46 (ELF) | `readelf -h -d -sW "$BIN" && nm -D "$BIN" && objdump -d -M intel "$BIN"` |
| **Mach-O Binary** | cf fa ed fe | `otool -hv -L "$BIN" && dyld_info -exports "$BIN" && nm -nm "$BIN"` |
| **Go Binary** | Go buildinf: | `go version -m "$BIN" && strings "$BIN" | rg "path	|mod	|dep	"` |
| **Rust Binary** | .cargo / rustc | `llvm-objdump -s --section=.dep-v0 "$BIN" || strings "$BIN" | rg "cargo|rustc"` |
| **Electron app.asar** | asar header JSON | `npx @electron/asar extract "$ASAR" "$OUT" && rg -uu -n "contextBridge|ipcMain" "$OUT"` |
| **Minified Web Bundle** | .min.js / .webpack/ | `rg -uu -b -o ".{0,80}(ipcRenderer|fetch|WebSocket).{0,80}" "$DIR"` |
| **Android APK / DEX** | PK + classes.dex | `apktool d "$APK" -o "$OUT" && jadx -d "$OUT/src" "$APK"` |
| **SQLite Database** | SQLite format 3 | `sqlite3 -readonly "$DB" ".schema" "SELECT name, type FROM sqlite_master;"` |
| **Network PCAP** | d4 c3 b2 a1 | `tshark -r "$PCAP" -q -z conv,tcp -z http,tree` |

## 3. Required output/recon_evidence.json Schema
```json
{
  "original_sha256_preserved": true,
  "mcp_tools_invoked": 0,
  "claims": [
    {
      "id": "lock_socket_path",
      "claim": "Daemon binds UNIX domain lock socket at /tmp/hermes_addon_v2_%d.sock",
      "epistemic_status": "seen",
      "evidence_cmd": "nm -D work_copy/addon.so && strings -t x work_copy/addon.so | rg hermes_addon"
    }
  ]
}
```
