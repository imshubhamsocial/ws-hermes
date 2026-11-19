# GDR33 Empirical Deviations, Hardware Realism & Runtime Tuning Notes

> **Context**: Empirical findings during the execution of GDR32 Certification & ICM Blueprint.  
> **Substrate Target**: Hermes Agent OS on discrete NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB physical GDDR6).  
> **Evaluation Reference**: Live Gauntlet A execution, Prometheus slot telemetry, and systemd journal logs.

---

## 1. Contiguous Buffer Allocation Roofline (-b 2048 vs. -b 4096)

* **GDR32 Blueprint Specification**:
  Recommended passing `--batch-size 4096 --ubatch-size 1024 --cache-type-k q8_0 --cache-type-v q4_0`.
* **Empirical Hardware Finding**:
  * In `llama-server`, compute prompt processing buffer (`compute pp buffer`) allocation is governed by:
    $$\text{Buffer Size} \propto \text{Batch Size} \times \text{Hidden Dimension}$$
  * At `-b 4096`, `ggml_backend_cuda_buffer_type_alloc_buffer` requests **1,070.08 MiB as a single contiguous allocation** in `cudaMalloc`.
  * Under physical desktop environments (KDE Plasma Wayland, PipeWire, Distrobox host execution), address space fragmentation can prevent allocating a single contiguous 1,070 MiB block, triggering:
    ```
    E ggml_backend_cuda_buffer_type_alloc_buffer: allocating 1070.08 MiB on device 0: cudaMalloc failed: out of memory
    E graph_reserve: failed to allocate compute buffers
    ```
  * At `-b 2048`, the contiguous allocation drops to **~535 MiB**. On a 6GB card, allocating 535 MiB contiguously succeeds 100% of the time, operating rock-solid at **4,285–4,309 MiB active VRAM** with a 1,500+ MiB safety margin.
* **GDR33 Production Invariant**:
  Maintain `-b 2048 -ub 1024 -ctk q4_0 -ctv q4_0` on 6GB GDDR6 laptop GPUs for deterministic resilience against desktop memory fragmentation.

---

## 2. CUDA MMQ vs. cuBLAS Tensor Core Dynamics (GGML_CUDA_FORCE_MMQ)

* **GDR32 Blueprint Specification**:
  Recommended exporting `GGML_CUDA_FORCE_MMQ=0` under the assumption that cuBLAS Tensor Cores would significantly outpace MMQ on prompt prefill.
* **Empirical Hardware Finding**:
  * **Short Prompts (< 100 tokens)**: `FORCE_MMQ=1` achieved **473.51 tokens/s** (147.8 ms) vs. **340.67 tokens/s** (205.5 ms) with `FORCE_MMQ=0`. Custom MMQ kernels eliminate cuBLAS runtime launch latency on small matrix operations.
  * **Medium & Deep Prompts (1,000 to 24,000 tokens)**: Both settings perform identically (~1,530 to 1,929 tokens/s) because `llama.cpp` dynamically routes large matrix multiplications (`-ub 1024`) to cuBLAS Tensor Cores regardless of the flag.
  * **Decoding Throughput**: Identical at 38.60 vs. 38.43 tokens/s (short) and 27.20 vs. 27.37 tokens/s (deep).
* **GDR33 Production Invariant**:
  Keep `GGML_CUDA_FORCE_MMQ=1` active for faster turn-by-turn tool execution latency.

---

## 3. `--fit off` and DFlash Initialization Probe Telemetry

* **GDR32 Blueprint Specification**:
  Recommended `--fit off` to bypass memory-fitting and eliminate the `dflash requires ctx_other to be set` warning.
* **Empirical Hardware Finding**:
  * The warning originates in `tools/server/server-context.cpp` inside `common_speculative_init_from_params()`, which probes the draft model before `ctx_tgt` is bound, independent of `--fit`.
  * The warning is completely benign and handled gracefully by llama-server.

---

## 4. OpenViking Hierarchical Memory Schema Key Realignment

* **Root Cause & Fix**:
  * In `~/.hermes/config.yaml`, the key under `memory.openviking` must be `endpoint: http://127.0.0.1:1933` (the plugin schema defines `endpoint`, not `url`).
  * In `~/.hermes/.env`, `OPENVIKING_ENDPOINT=http://127.0.0.1:1933` must be exported.
  * Status verified: `Status: available ✓`, provider active.

---

## 5. Tool Parameter Semantics: `search_files` Glob vs. Regex Traps in Bounded ICM Stages

* **Empirical Behavioral Finding**:
  * **Stage 1 Behavior**:
    When instructed to "Read CONTEXT.md, invariants.md, rules.md, and references.md first", Nemotron 3.5 Bolt attempted discovery via:
    `search_files(pattern="CONTEXT.md|invariants.md|rules.md|references.md", target="files")`
    In `tools/file_tools.py`, `target="files"` parses patterns using `fnmatch` / ripgrep glob (`rg --files -g`), where `|` is treated as a literal character rather than an alternation operator, matching 0 files. Hermes noted their absence and fell back cleanly to the prompt specification, authoring `server.js` and writing `stage1_spec_receipt.json` within 8 turns.
  * **Stage 2 Turn Exhaustion Traversal**:
    In Stage 2, the prompt requested:
    `Read CONTEXT.md, invariants.md, rules.md, references.md, and the Stage 1 handoff receipt output/stage1_spec_receipt.json.`
    Nemotron again emitted:
    `search_files(pattern="CONTEXT.md|invariants.md|rules.md|references.md|stage1_spec_receipt.json", target="files")`
    When this returned 0 matches in `.`, the model inferred that the context files were not in the workspace and spent successive tool turns querying `output/voxel-paintball-app` and the parent repository root (`/var/home/.../hermes`). It located the root `CONTEXT.md` and `rules/invariants.md`, but could not find `references.md` or `stage1_spec_receipt.json` in the parent directory.
    Consequently, all 12 turns of the `--max-turns 12` stage budget were consumed by directory traversal, halting execution before client code authoring began and producing:
    `"I cannot proceed with the implementation without the Stage 1 receipt and the necessary source code/dependencies."`
* **GDR33 Protocol Recommendation & Invariant**:
  * **Zero Regex Alternation in Glob Targets**: When prompting local small language models (Nemotron 3.5 Bolt 4B), never supply multiple filenames joined by commas or pipe operators in a single "Read X, Y, Z" clause without specifying direct file paths.
  * **Direct Path Explicit Handoff**: Specify exact relative paths (`./output/stage1_spec_receipt.json`, `./references.md`) and direct `read_file` semantics to prevent models from burning bounded turn budgets on glob searches.
