# Document 3: Substrate Comparative Forensics, Gemma QAT Autopsy, and NVIDIA Bolt Q4 Drafter Feasibility

> **Evaluated Substrates**:
> 1. Candidate 1: `google/gemma-4-E4B-it-qat-q4_0-gguf` (4.9 GB) + MTP Drafter (57 MB)
> 2. Candidate 2: `xbill9/gemma-4-E4B-it-qat-q4_0-exact.gguf` (4.0 GB) + Exact Assistant Drafter (57 MB)
> 3. Candidate 3: `unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-UD-Q4_K_XL.gguf` (4.8 GB standalone)
> **Hardware Boundary**: Discrete NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB physical GDDR6, ceiling $\le 5,800.0$ MiB)  
> **Raw Trajectory Archive**: [`imshubhamsocial/hermes-tests/logs/gdr30_harness_evals`](https://github.com/imshubhamsocial/hermes-tests/tree/main/logs/gdr30_harness_evals)

---

## 1. Task-by-Task Comparative Matrix

```
========================================================================================================================
TASK-BY-TASK EMPIRICAL COMPARISON ACROSS ALL 3 SUBSTRATES
========================================================================================================================
Evaluation Track & Task   | Candidate 1 (Baseline)         | Candidate 2 (Tier 1A)          | Candidate 3 (Tier 1B)
                          | Google Gemma 4 QAT + MTP       | xbill9 Gemma 4 Exact QAT       | NVIDIA Nemotron 3.5 Bolt
========================================================================================================================
make run-eval (AST + GCC) | Exit 0 (PASS, output 55)       | Exit 0 (PASS, output 55)       | Exit 0 (PASS, output 55)
                          | Compiled C without incident    | Caught Python vs C discrepancy | Strict C AST pattern query
------------------------------------------------------------------------------------------------------------------------
Tau-Bench Task 0          | 0.000 (FAIL)                   | 1.000 (100% PASS)              | 1.000 (100% PASS)
Full 2-Item Exchange      | Hallucinated order numbers     | Exact user auth, matched       | Perfect user auth, committed
                          | (#W2378155, #W237815) & tools  | items, committed 5ed21c65 DB   | items, committed 5ed21c65 DB
------------------------------------------------------------------------------------------------------------------------
Tau-Bench Task 1          | 0.000 (FAIL)                   | 1.000 (100% PASS)              | 1.000 (100% PASS)
Conditional Constraint Ex | Hallucinated order #W2378154   | Deduced no RGB keyboard;       | Deduced keyboard constraint;
                          | and tool find_user_id_by       | confirmed $13.46 user refund   | exchanged thermostat only
------------------------------------------------------------------------------------------------------------------------
Tau-Bench Task 2          | 0.000 (FAIL / Abandoned)       | 0.000 (FAIL)                   | 1.000 (100% PASS)
Store Count & 3 Returns   | Did not attempt multi-order    | Failed user auth via email;    | Counted 10 t-shirts; crawled
                          | return                         | transferred to human agent     | 5 orders; returned 3 items
------------------------------------------------------------------------------------------------------------------------
Tau-Bench Tasks 3 & 4     | Unattempted                    | Unattempted                    | 1.000 Output match (10 shirts)
------------------------------------------------------------------------------------------------------------------------
GAIA Level 1 (Orbital)    | Tool Strip Loop (Issue #28825) | Tool Strip Loop (Issue #28825) | Solved 17,000h on Turn 1!
------------------------------------------------------------------------------------------------------------------------
Active VRAM (128K Context)| 5,271 MiB / 6,144 MiB          | 4,169 MiB / 6,144 MiB (Leanest)| 4,975 MiB / 6,144 MiB
Prompt Eval Throughput    | ~1,200 t/s                     | >2,000 t/s (Fastest)           | ~1,100 t/s
Generation Speed          | ~24.5 t/s                      | ~29.5 t/s                      | ~28.2 t/s
========================================================================================================================
```

---

## 2. Definitive Autopsy: Why Candidate 1 (Google Official Gemma 4 QAT) Failed

A central question posed to Gemini Argon is: **Did Candidate 1 genuinely fail, or was its failure an artifact of port clashes or gateway constraints?**

### 2.1 The Empirical Proof of Genuine Model Failure
* **Zero Routing Ambiguity**: When Candidate 1 was evaluated, the dual-port ReAct architecture was 100% operational:
  * Customer simulation ran on **OmniRoute Port 20128** (`frontier-fleet`).
  * Support agent ran on **Hermes Gateway Port 8642** (`hermes-agent`).
  * Under this **identical configuration**, Candidate 2 and Candidate 3 scored **100% PASS** on Tasks 0 and 1.
* **Verbatim Forensic Transcripts (Candidate 1)**:
  * Customer provided order `#W2378156`.
  * Candidate 1 emitted:
    ```json
    Action: {"name": "get_order_details", "arguments": {"order_id": "#W2378155"}}
    Action: {"name": "get_order_details", "arguments": {"order_id": "#W237815"}}
    Action: {"name": "find_user_id", "arguments": {"first_name": "Yusuf", "last_name": "Rossi", "zip": "19122"}}
    Action: {"name": "transfer_to_human", "arguments": {"summary": "System error"}}
    ```
  * On Task 1, Candidate 1 emitted:
    ```json
    Action: {"name": "get_order_details", "arguments": {"order_id": "#W2378154"}}
    Action: {"name": "find_user_id_by", "arguments": {"first_name": "Yusuf", "last_name": "Rossi", "zip": "19122"}}
    ```
* **Root Cause Pathology**:
  * Candidate 1 suffered from severe **token identifier mutation** under multi-turn ReAct formatting. It mutated the last digit of order numbers (`6` $\rightarrow$ `5`, `6` $\rightarrow$ `4`) and truncated tool identifiers (`find_user_id_by_name_zip` $\rightarrow$ `find_user_id_by` and `find_user_id`).
  * Because **Candidate 2** uses the exact same Gemma 4 base architecture and weights but community exact float quantization (`xbill9`), and scored 100%, Candidate 1's failure is an intrinsic artifact of Google's lossy QAT export perturbing AST identifier logits.

---

## 3. Deep Research Mandate: NVIDIA Nemotron 3.5 Bolt Speculative Decoding & Q4 Drafter Feasibility

In earlier phases, speculative decoding with companion drafters consistently achieved **100+ tokens/sec** inference speeds. However, when we deployed **Candidate 3 (NVIDIA Nemotron 3.5 Bolt)** with its bundled `dflash-NVIDIA-Nemotron-3.5-Bolt-E4B-Q8_0.gguf` (381 MB) drafter, `llama-server` crashed with a fatal CUDA Out-of-Memory error:

```text
ggml_backend_cuda_buffer_type_alloc_buffer: allocating 1070.08 MiB on device 0: cudaMalloc failed: out of memory
llama_model_load: error loading model: unable to allocate CUDA graph buffer
```

### 3.1 Hardware Budget Breakdown (Candidate 3)
* Physical GDDR6 VRAM: **6,144 MiB**
* Hard Operational Ceiling: **5,800.0 MiB**
* Nemotron 3.5 Bolt Base Model (`UD-Q4_K_XL`): **4,800 MiB**
* Google TurboQuant Q4_0 KV Cache (128K context): **~950 MiB**
* Active Footprint Standalone: **4,975 MiB** (Headroom: **825 MiB**)
* When adding the 381 MB Q8 drafter:
  * Drafter weights: +381 MiB
  * Drafter KV cache: +150 MiB
  * `llama-server` CUDA graph allocation: +1,070 MiB
  * Total required: $4,800 + 950 + 381 + 150 + 1,070 \approx \mathbf{7,351\text{ MiB}}$ ($\gg 6,144\text{ MiB}$).

### 3.2 Key Research Questions for Argon
1. **DFlash Drafter Quantization**:
   * Does a quantized version of the DFlash drafter exist (e.g., `dflash-Nemotron-3.5-Bolt-E4B-Q4_0.gguf` or `Q4_K_M`, ~190 MB)?
   * Can `llama-quantize` be used to quantize the 381 MB Q8 drafter down to Q4_0 or IQ4_NL?
2. **CUDA Graph Memory Mitigation**:
   * How can `llama-server` speculative decoding flags be tuned to suppress the 1,070 MiB CUDA graph allocation?
   * Does disabling CUDA graphs (`--no-graphs`) or reducing physical batch sizes (`-b 1024 -ub 512`) allow base + drafter to fit safely within the 5,800.0 MiB ceiling?
3. **Alternative Draft Strategies**:
   * Can N-gram speculative decoding (`--spec-ngram-map-k-size-n 8`) or prompt lookup decoding (`--draft 16`) be deployed without any secondary model file to achieve 60–80+ tokens/sec at **0.0 MiB VRAM delta**?
