#!/usr/bin/env python3
"""Atomic Markdown Link & Path Verifier (<60 lines)."""
import pathlib, re, sys

LINK_RE = re.compile(r"\[.*?\]\(([^)#]+)\)")

def check_links(root: pathlib.Path) -> list[str]:
    broken = []
    for p in root.rglob("*.md"):
        if any(x in p.parts for x in (".git", "node_modules", "_archive", ".gemini")):
            continue
        for target in LINK_RE.findall(p.read_text(encoding="utf-8", errors="ignore")):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            dest = (p.parent / target).resolve()
            if not dest.exists():
                broken.append(f"BROKEN_LINK: {p} -> {target}")
    return broken

if __name__ == "__main__":
    target = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errs = check_links(target)
    if errs:
        for e in errs: sys.stderr.write(e + "\n")
        sys.exit(1)
    print("ALL_LINKS_RESOLVED")
