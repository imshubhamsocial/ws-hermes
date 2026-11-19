#!/usr/bin/env bash
set -euo pipefail
HTML_FILE="output/hermes_v45_architecture.html"
test -f "$HTML_FILE"
! grep -qiE "box-shadow|drop-shadow|mermaid|cdn\.jsdelivr|unpkg\.com" "$HTML_FILE"
python3 -c '
import re, sys, xml.etree.ElementTree as ET
html = open("output/hermes_v45_architecture.html", encoding="utf-8").read()
m = re.search(r"(<svg[\s\S]*?</svg>)", html)
assert m, "No inline <svg>...</svg> block found"
svg_str = m.group(1)
root = ET.fromstring(svg_str)
nodes = [el for el in root.iter() if el.attrib.get("class") == "node"]
connectors = [el for el in root.iter() if el.attrib.get("class") == "connector"]
accents = [el for el in nodes if el.attrib.get("stroke", "").lower() == "#bf4520"]
assert 4 <= len(nodes) <= 9, f"Complexity budget requires 4..9 nodes, got {len(nodes)}"
assert 3 <= len(connectors) <= 12, f"Complexity budget requires 3..12 connectors, got {len(connectors)}"
assert 1 <= len(accents) <= 2, f"Accent budget requires 1..2 #bf4520 focal nodes, got {len(accents)}"
for el in root.iter():
    tag = el.tag.split("}")[-1]
    if tag == "line":
        x1, y1, x2, y2 = float(el.attrib["x1"]), float(el.attrib["y1"]), float(el.attrib["x2"]), float(el.attrib["y2"])
        assert x1 == x2 or y1 == y2, f"Diagonal <line> forbidden: ({x1},{y1})->({x2},{y2})"
    if tag == "rect":
        for attr in ("x", "y", "width", "height"):
            if attr in el.attrib:
                val = int(float(el.attrib[attr]))
                assert val % 4 == 0, f"<rect> {attr}={val} violates 4px grid"
print(f"[PASS] Gauntlet F diagram-design XML & 4px Grid Contract Verified ({len(nodes)} nodes, {len(connectors)} connectors)")
'
