# Benchmark Contract: UK DSIT Inspect AI GAIA Suite (gaia)

> **Role**: Layer B General AI Assistants Benchmark (GAIA Level 1–3).  
> **Line Discipline**: Strictly $\le 80$ lines.

---

## 1. Inputs & Execution Target
| Input Source | File / Location | Scope |
| :--- | :--- | :--- |
| Dataset | `gaia/level1` via HuggingFace | Real-world multimodal reasoning tasks |
| Execution Mode | Native CLI (`hermes -z` / TUI) | Canonical ReAct execution bypassing Port 8642 stripping |
| Auth Token | `HF_TOKEN` | Required for gated GAIA dataset access |

## 2. Process
> 1. Authenticate with HuggingFace Hub using cached `HF_TOKEN`.
> 2. Execute target questions natively or via Inspect AI `--sandbox local`.
> 3. Perform web retrieval or parametric calculation per prompt specification.
> 4. Format and normalize final answer according to `rules.md`.

## 3. Outputs
| Artifact | Location | Format |
| :--- | :--- | :--- |
| Session Traces | `benchmarks/gaia/output/traces/` | Markdown and JSONL exports |
| Verification Score | `benchmarks/gaia/output/score.json` | Exact match accuracy ledger |

## 4. Verify
* [ ] Local execution sandbox provisioned (`--sandbox local`).
* [ ] Final answer strictly formatted inside `<FINAL_ANSWER>...</FINAL_ANSWER>`.
* [ ] Zero unit repetition or prose wrapper leaks.
