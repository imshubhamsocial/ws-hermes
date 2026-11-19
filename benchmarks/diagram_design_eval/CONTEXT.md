# Stage Contract: Gauntlet F — diagram-design Editorial HTML+SVG Diagramming

## Inputs
* Workspace Root Map: ../../AGENTS.md
* Installed Upstream Skill: ~/.hermes/skills/diagram-design/SKILL.md
* Hard Structural & Geometry Bounds: ./invariants.md
* Archetype Selection & Editorial Rules: ./rules.md
* 45-Archetype Index & SVG Grid Schemas: ./references.md

## Process
> 1. Read ./invariants.md, ./rules.md, and ./references.md along with ~/.hermes/skills/diagram-design/SKILL.md.
> 2. Select Archetype 01 (Architecture, type-architecture.md) to diagram the Hermes Agent OS v45 Substrate Topology (Nested Admin Scope ws-hermes containing Gateway Port 8642, Nemotron 3.5 Bolt Port 8138, OpenViking Port 1933, and CPU Embeddings Port 8139, connected to Host Flatpak Chrome Port 9222).
> 3. Author the self-contained single-file editorial HTML + inline SVG at output/hermes_v45_architecture.html obeying the 4px grid, complexity budget (<= 9 nodes, <= 12 orthogonal connectors, <= 2 #bf4520 accent nodes), rx=4 dashed scopes, and rx=8 solid component boxes.
> 4. Run bash ./contract.sh (executing Python xml.etree.ElementTree DOM/SVG validation + geometry check) and write output/status.json.

## Outputs
* Self-Contained Editorial Diagram: output/hermes_v45_architecture.html
* Verification Receipt: output/status.json

## Verify
* Run bash ./contract.sh and confirm exit code 0.
