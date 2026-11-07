# Procedural Rules: Gauntlet F — diagram-design Editorial HTML+SVG

> 1. **Style Guide Token Application (references/style-guide.md)**:
   * Apply editorial tokens: --paper: #f5f5f5, --paper-2: #ebebeb, --ink: #2d3142, --muted: #64748b, --accent: #bf4520 (4.5:1+ WCAG AA contrast over #f5f5f5), --hairline: #cbd5e1.
> 2. **Corner Radii & Border Hierarchy (type-architecture.md)**:
   * Administrative bands / container boundaries (ws-hermes Distrobox, Fedora Kinoite 44 Host): `<rect rx="4" ry="4" stroke-dasharray="4,3" stroke="#64748b" fill="#ebebeb" stroke-width="1"/>`.
   * Service / daemon blocks (Port 8642 Gateway, Port 8138 Nemotron Bolt, Port 1933 OpenViking, Port 8139 EmbeddingGemma2, Port 9222 Chrome CDP): `<rect rx="8" ry="8" stroke="#2d3142" fill="#ffffff" stroke-width="1"/>`.
   * Highlight at most 2 focal nodes (Port 8642 Gateway and Port 8138 Nemotron Bolt) with `stroke="#bf4520" stroke-width="2"`.
> 3. **Connector Label Masks**:
   * Place every connector label (<= 14 chars, ALL CAPS, e.g., CDP WS 9222, TRIEHI RPC) over an opaque `<rect fill="#f5f5f5"/>` mask drawn before the text and before endpoint nodes.
> 4. **Typography**:
   * Use clean sans-serif (system-ui, -apple-system, sans-serif) for titles and node names, and monospace (ui-monospace, monospace) strictly for ports, paths, and commands.
