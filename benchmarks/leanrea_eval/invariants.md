# Hard Invariants: Gauntlet D — leanrea Zero-MCP Reverse Engineering

> 1. **Zero MCP Server Overhead**: Never start or query an external reverse-engineering MCP server (rea, ghidra-mcp). All recon MUST execute via native POSIX CLI commands in terminal_tool.py.
> 2. **Work on a Copy**: Never mutate or extract in-place inside output/targets/. Always copy targets to output/work_copy/ and verify SHA-256 parity of the untouched original.
> 3. **Strict Epistemic Claim Labeling (aicodeking/leanrea Rule 6)**: Every technical finding in output/recon_report.md and output/recon_evidence.json MUST be tagged with "epistemic_status": "seen" | "inferred" | "unknown" accompanied by the exact CLI command and byte/line offset.
> 4. **Slice, Never Dump Minified Bundles**: Never read entire minified JS bundles or binary hex dumps into context. Use rg -uu -n -C 2 or byte/character slicing (dd, head -c, cut).
> 5. **Batch Probes into Single Shell Calls**: Combine file, sha256sum, nm -D, readelf -d, and strings into a single compound Bash invocation to minimize turn count.
