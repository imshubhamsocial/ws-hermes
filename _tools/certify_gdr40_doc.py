"""Deterministic Gate Certification Suite for GDR40 Document (<60 lines)."""
import re, subprocess, yaml, sys, pathlib

def run_checks(p: pathlib.Path) -> bool:
    text = p.read_text(encoding="utf-8")
    blocks = re.findall(r"```([a-zA-Z0-9_-]*)\n(.*?)```", text, re.DOTALL)
    assert len(blocks) == 30, f"Expected 30 code blocks, found {len(blocks)}"
    
    for i, (lang, code) in enumerate(blocks):
        c = code.strip()
        if lang == "python":
            compile(c, f"b{i}.py", "exec")
        elif lang == "yaml":
            yaml.safe_load(c)
        elif lang == "bash":
            r = subprocess.run(["bash", "-n"], input=c, text=True, capture_output=True)
            assert r.returncode == 0, f"Bash b{i} failed: {r.stderr}"
        elif lang == "javascript":
            r = subprocess.run(["node", "--input-type=module", "--check"], input=c, text=True, capture_output=True)
            assert r.returncode == 0, f"Node b{i} failed: {r.stderr}"

    assert text.count("```") % 2 == 0, f"Backtick parity odd: {text.count('```')}"
    # Math dollars outside code blocks
    no_code = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    assert no_code.count("$") % 2 == 0, f"Math dollar parity odd: {no_code.count('$')}"
    assert "data:image/png;base64" not in text, "Base64 data present"

    for line in text.splitlines():
        s = line.strip()
        if s.startswith("|"):
            assert s.endswith("|"), f"Broken table row: {s}"

    raw_angles = re.findall(r"(?<!`)(<[a-zA-Z0-9_-]+>)(?!`)", no_code)
    assert len(raw_angles) == 0, f"Raw angle brackets found: {raw_angles}"
    return True

if __name__ == "__main__":
    target = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "output.md")
    ok = run_checks(target)
    print(f"CERTIFICATION_PASS: {target} passed all gates (30/30 blocks, even parities).")
