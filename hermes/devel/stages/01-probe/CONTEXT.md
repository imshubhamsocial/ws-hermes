# 01-probe - Browser and Canvas State Discovery

One job: Probe the browser canvas and write target metadata to output/probe_state.json.

## Inputs

| Source | File/Location | Section/Scope | Why |
| :--- | :--- | :--- | :--- |
| System Invariants | `../../../../_config/invariants.md` | Network Ports | Port 9222 connection |
| Vision Schemas | `../../../../shared/vision_schemas.md` | Vision Invariants | Coordinate normalization |

Do NOT load: ../02-controller/, ../03-execute/, or ../../benchmarks/.

## Process

> 1. Connect to Chrome CDP on Port 9222 using Playwright.
> 2. Locate the Splatbox HTML5 canvas element (`#gameCanvas`).
> 3. Capture a 1280x720 screenshot of the canvas.
> 4. Extract canvas CSS bounding box dimensions.
> 5. Save metadata to output/probe_state.json.

## Outputs

| Artifact | Location | Format |
| :--- | :--- | :--- |
| Probe State | output/probe_state.json | JSON schema with canvas rect |
| Stage Audit Receipt | output/check.md | YAML-frontmattered Markdown |

## Check

Run python3 -m json.tool output/probe_state.json and verify width and height keys exist.
