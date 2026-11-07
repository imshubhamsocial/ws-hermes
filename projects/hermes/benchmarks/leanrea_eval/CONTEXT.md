# Stage Contract: Gauntlet D — leanrea Zero-MCP Reverse Engineering

## Inputs
* Workspace Root Map: ../../AGENTS.md
* Installed Upstream Skill: ~/.hermes/skills/leanrea/SKILL.md
* Hard Operational Bounds: ./invariants.md
* Procedural Recon Protocol: ./rules.md
* Native POSIX CLI Router Reference: ./references.md

## Process
> 1. Read ./invariants.md, ./rules.md, and ./references.md along with the preloaded leanrea skill.
> 2. Generate the deterministic evaluation target inside output/targets/addon.so (a stripped C shared object exporting init_hermes_lock(), checking HERMES_TCC_AUTH, and formatting /tmp/hermes_addon_v2_%d.sock) and record its SHA-256 hash.
> 3. Copy output/targets/addon.so to output/work_copy/addon.so and execute batched one-shot native POSIX CLI recon commands (file, readelf, objdump, nm, strings, rg -uu) on the working copy.
> 4. Produce the structured recon report output/recon_report.md and output/recon_evidence.json where every claim is explicitly labeled seen, inferred, or unknown.
> 5. Run bash ./contract.sh to verify zero MCP calls, working-copy preservation, and 100% evidence accuracy.

## Outputs
* Recon Report: output/recon_report.md
* Machine-Readable Evidence Ledger: output/recon_evidence.json

## Verify
* Run bash ./contract.sh and confirm exit code 0.
