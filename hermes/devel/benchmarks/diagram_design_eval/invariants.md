# Hard Invariants: Gauntlet F — diagram-design Editorial HTML+SVG

> 1. **Self-Contained Single-File HTML + Inline SVG**: Output MUST be a single .html file containing an inline <svg viewBox="0 0 960 600"> with zero external <script src="...">, zero external CSS CDNs, and zero Mermaid syntax.
> 2. **Zero Box Shadows or Dark-Mode Glow ("No AI Slop")**: box-shadow, drop-shadow, filter: blur, and neon gradients are strictly forbidden (cathrynlavery/diagram-design Rule).
> 3. **Strict 4px Grid Alignment**: Every <rect>, <text>, and <path> coordinate (x, y, width, height) MUST be an exact integer multiple of 4 (except rx="6" or 1px stroke widths).
> 4. **Complexity Budget Cap**: Maximum 9 component nodes, maximum 12 orthogonal connectors, maximum 2 accent-colored (#bf4520) focal nodes, and maximum 2 annotation callouts.
> 5. **Orthogonal Connectors Only**: Every <line> must be strictly horizontal (y1 == y2) or vertical (x1 == x2). Off-axis connections MUST use <path> with right-angle r=8 (A 8 8 0 0 1 ...) rounded elbows.
> 6. **Valid XML Closure**: The <svg>...</svg> subtree must parse cleanly with zero errors under Python xml.etree.ElementTree.fromstring().
