#!/usr/bin/env python3
"""Brownfield AST 5-Bucket Repository Classifier & Migrator (<60 lines)."""
import ast
import json
import pathlib
import sys

IGNORE_DIRS = {".git", "__pycache__", "node_modules", ".venv", ".hermes", ".cache", ".local", ".gemini"}

def classify_python_ast(path: pathlib.Path, source: str) -> dict:
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return {"bucket": "dead", "reason": "syntax_error", "imports": [], "defs": 0}
    imports = [n.names[0].name for n in ast.walk(tree) if isinstance(n, ast.Import)]
    imports += [n.module or "" for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)]
    defs = [n.name for n in tree.body if isinstance(n, (ast.FunctionDef, ast.ClassDef))]
    if not defs and not imports and len(source.strip()) == 0:
        return {"bucket": "dead", "reason": "empty_module", "imports": [], "defs": 0}
    if path.name.startswith("test_") or "contract" in path.name:
        return {"bucket": "contract", "reason": "verification_gate", "imports": imports, "defs": len(defs)}
    return {"bucket": "factory", "reason": "executable_module", "imports": imports, "defs": len(defs)}

def classify_file(path: pathlib.Path) -> dict:
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    name_low = path.name.lower()
    if name_low in {"readme.md", "index.md", "identity.md"}:
        info = {"bucket": "catalog", "reason": "index_router"}
    elif name_low in {"context.md", "claude.md", "agents.md"}:
        info = {"bucket": "contract", "reason": "stage_contract"}
    elif path.suffix == ".py":
        info = classify_python_ast(path, "\n".join(lines))
    elif "output" in path.parts or "dist" in path.parts:
        info = {"bucket": "product", "reason": "run_artifact"}
    elif path.suffix in {".bak", ".tmp", ".old"}:
        info = {"bucket": "dead", "reason": "obsolete_backup"}
    else:
        info = {"bucket": "factory", "reason": "reference_or_source"}
    info.update({"path": str(path), "lines": len(lines), "needs_split": len(lines) >= 60})
    return info

if __name__ == "__main__":
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    files = [p for p in root.rglob("*") if p.is_file() and not (set(p.parts) & IGNORE_DIRS)]
    report = {"root": str(root), "classified": [classify_file(f) for f in sorted(files)]}
    out = root / "migration_map.json"
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"MIGRATION_MAP_READY: {len(report['classified'])} files classified -> {out}")
