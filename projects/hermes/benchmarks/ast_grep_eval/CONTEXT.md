# Benchmark Contract: AST Grep & GCC Evaluation (ast_grep_eval)

> **Role**: Layer B Code Mutation & Structural Verification Benchmark.  
> **Line Discipline**: Strictly $\le 80$ lines.

---

## 1. Inputs & Testbed Target
| Input Source | File / Location | Scope |
| :--- | :--- | :--- |
| Testbed Source | `tests/ast_grep_eval/fibonacci.c` | C source requiring recursive memoization |
| Target Function | `unsigned long long fib(int n)` | Structural optimization and compilation target |
| Routing Model | `icm-tier1a-coding` | Specialist: `gemma-4-E4B-it-qat-exact` |

## 2. Process
> 1. Execute `hermes --in tests/ast_grep_eval -z "<PROMPT>"` targeting Port 8642.
> 2. Inspect code structure using `ast-grep --lang c`.
> 3. Compile modified source with `gcc -O2 -Wall -Wextra -Werror`.
> 4. Run binary and assert stdout equals exactly `55`.

## 3. Outputs
| Artifact | Location | Format |
| :--- | :--- | :--- |
| Execution Output | `benchmarks/ast_grep_eval/output/run.log` | Linter, compiler, and binary execution log |
| Verification Receipt | `benchmarks/ast_grep_eval/output/receipt.json` | JSON test result |

## 4. Verify
* [ ] GCC compilation exits with code 0.
* [ ] Binary execution outputs exact string `55`.
* [ ] Zero compiler warnings or ast-grep pattern violations.
