# Procedural Rules: Gauntlet D — leanrea Zero-MCP Reverse Engineering

> 1. **Step 1 — Magic-Byte & Target Routing (aicodeking/leanrea Router)**:
   * Run `file -b <target>` and `head -c 16 <target> | xxd` on the working copy to classify the artifact before choosing tools.
> 2. **Step 2 — One-Shot First-Move Inventory**:
   * **ELF / Native .node Addon (Linux ws-hermes)**: Execute `readelf -h -d -W <bin> && nm -D --defined-only <bin> && objdump -d -M intel <bin> | grep -E "<.*>:|call"` in a single shell turn.
   * **Go Binary**: Execute `go version -m <bin>` and `strings <bin> | rg -uu "go1\.|github\.com/"`.
   * **Electron / asar Archive**: Execute `npx --yes @electron/asar extract <archive.asar> output/work_copy/asar_extracted && rg -uu -n "ipcMain|contextBridge|preload|socket" output/work_copy/asar_extracted`.
   * **SQLite / Embedded DB**: Execute `sqlite3 -readonly <db> ".schema" ".tables"`.
> 3. **Step 3 — Call-Sequence & Literal Tracing**:
   * Trace string literals to cross-referenced functions via `objdump -d` / `readelf -x .rodata` rather than reading every assembly instruction linearly.
> 4. **Step 4 — Evidence Serialization**:
   * Write `output/recon_evidence.json` containing `{"claims": [{"id": "...", "claim": "...", "epistemic_status": "seen|inferred|unknown", "evidence_cmd": "..."}]}` and validate with `bash ./contract.sh`.
