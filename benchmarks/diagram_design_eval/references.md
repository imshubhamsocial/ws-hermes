# Layer 3 Reference Schemas: Gauntlet F (cathrynlavery/diagram-design v2.6)

## 1. Upstream Repository & 45 Visual Archetypes Catalog
* **Source**: https://github.com/cathrynlavery/diagram-design (skills/diagram-design/SKILL.md)
* **45 Supported Types (references/type-*.md)**: 01 Architecture, 02 Architecture Delta, 03 IT Current-State, 04 Flowchart, 05 Sequence, 06 State Machine, 07 ER/Data Model, 08 Timeline, 09 Swimlane, 10 Quadrant, 11 Radar/Spider, 12 Polar Chart, 13 Loop/Flywheel, 14 Nested, 15 Tree, 16 Org Chart, 17 Layer Stack, 18 Exploded Axonometric, 19 Axonometric Plan, 20 Venn, 21 Pyramid/Funnel, 22 Bar/Dumbbell, 23 Waterfall, 24 Treemap/Marimekko, 25 Heatmap, 26 Line, 27 Gantt, 28 Scatter, 29 High-Level, 30 Process, 31 Medallion, 32 Data Flow, 33 DP Integration, 34 DP Security Matrix, 35 Sankey, 36 Fishbone, 37 Wardley Map, 38 Kanban, 39 User Journey, 40 Service Blueprint, 41 Deployment, 42 Dependency Graph, 43 UML Class, 44 Story Map, 45 Database Schema.

## 2. Orthogonal Rounded-Elbow SVG Path Template (r=8 on 4px Grid)
```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 600" width="960" height="600">
  <defs>
    <marker id="arrow" viewBox="0 0 8 8" refX="8" refY="4" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 8 4 L 0 8 z" fill="#2d3142"/>
    </marker>
  </defs>
  <!-- Admin Band (rx=4, dashed) -->
  <rect x="40" y="60" width="600" height="480" rx="4" ry="4" fill="#ebebeb" stroke="#64748b" stroke-width="1" stroke-dasharray="4,3"/>
  <!-- Discrete Service Node (rx=8, solid, 4px grid aligned) -->
  <rect class="node" x="80" y="120" width="200" height="72" rx="8" ry="8" fill="#ffffff" stroke="#bf4520" stroke-width="2"/>
  <!-- Orthogonal Connector with r=8 Right-Angle Elbow -->
  <path class="connector" d="M 280 156 L 348 156 A 8 8 0 0 1 356 164 L 356 244 A 8 8 0 0 0 364 252 L 400 252" fill="none" stroke="#2d3142" stroke-width="1" marker-end="url(#arrow)"/>
  <!-- Opaque Label Mask + ALL CAPS Label (<=14 chars) -->
  <rect x="296" y="144" width="64" height="20" fill="#ebebeb"/>
  <text x="328" y="158" text-anchor="middle" font-family="ui-monospace, monospace" font-size="10" fill="#2d3142">PORT 8138</text>
</svg>
```
