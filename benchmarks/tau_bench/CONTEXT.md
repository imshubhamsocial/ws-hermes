# Benchmark Contract: Sierra Research Tau-Bench Suite (tau_bench)

> **Role**: Layer B Evaluation Contract (Retail & Airline Multi-Turn Environments).  
> **Line Discipline**: Strictly $\le 80$ lines.

---

## 1. Inputs & Routing
| Input Source | File / Location | Scope |
| :--- | :--- | :--- |
| Environment | `tau_bench.envs.retail` | Retail customer service simulation |
| Agent Endpoint | Port 8642 (`http://127.0.0.1:8642/v1`) | Hermes Agent gateway (`_run_agent`) |
| Customer Endpoint | Port 20128 (`http://127.0.0.1:20128/v1`) | OmniRoute isolated proxy simulator |

## 2. Process
> 1. Launch OmniRoute daemon on Port 20128 and Hermes Gateway on Port 8642.
> 2. Execute `tau_bench.run` with `--agent-strategy react` (`ChatReActAgent`).
> 3. Enforce sanitization of `provider_specific_fields` to prevent 422 Unprocessable Entity errors.
> 4. Record raw trajectories and action histories to `output/`.

## 3. Outputs
| Artifact | Location | Format |
| :--- | :--- | :--- |
| Evaluation Logs | `benchmarks/tau_bench/output/eval_results.json` | JSON trajectory ledger |
| Metrics Summary | `benchmarks/tau_bench/output/metrics.md` | Success rate & cost |

## 4. Verify
* [ ] Dual-port isolation enforced (Port 8642 vs Port 20128).
* [ ] LiteLLM registers models at zero cost (`$0.0`).
* [ ] Zero 422 validation rejections from LiteLLM proxy.
