#!/usr/bin/env python3
"""Deterministic 5-Layer ICM Token Budget & Line Ceiling Auditor (42 lines)."""
import json, pathlib, sys

BUDGETS = {"IDENTITY.md": 800, "CLAUDE.md": 800, "CONTEXT.md": 500}
STAGE_MAX_TOKENS = 8000
SCRIPT_MAX_LINES = 59
IGNORE = {".hermes", ".git", "node_modules", ".gemini", ".local", ".cache", ".venv"}

def est_tokens(text: str) -> int:
    return max(1, int(len(text.split()) * 1.35))

def audit_workspace(root: pathlib.Path) -> dict:
    violations = []
    for name, limit in BUDGETS.items():
        for path in root.rglob(name):
            if any(p in IGNORE for p in path.parts):
                continue
            tok = est_tokens(path.read_text(encoding="utf-8", errors="ignore"))
            eff_limit = 300 if (name == "CONTEXT.md" and path.parent == root) else limit
            if tok > eff_limit:
                violations.append(f"TOKEN_OVERFLOW: {path} ({tok} > {eff_limit})")
    for stg in sorted((root / "stages").glob("[0-9][0-9]-*")) if (root / "stages").exists() else []:
        stg_tok = sum(est_tokens(f.read_text(encoding="utf-8", errors="ignore")) for f in stg.rglob("*.md"))
        if stg_tok > STAGE_MAX_TOKENS:
            violations.append(f"STAGE_BUDGET_OVERFLOW: {stg} ({stg_tok} > {STAGE_MAX_TOKENS})")
    for ext in ("*.py", "*.sh", "*.js"):
        for scr in root.rglob(ext):
            if any(p in IGNORE for p in scr.parts):
                continue
            cnt = len(scr.read_text(encoding="utf-8", errors="ignore").splitlines())
            if cnt > SCRIPT_MAX_LINES:
                violations.append(f"LINE_CEILING_BREACH: {scr} ({cnt} lines >= 60)")
    return {"workspace": str(root), "passed": len(violations) == 0, "violations": violations}

if __name__ == "__main__":
    target = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    res = audit_workspace(target)
    print(json.dumps(res, indent=2))
    if not res["passed"]:
        sys.exit(1)
    sys.exit(0)
