"""Format GDR40 Chronological Blueprint Reorganization in-place (<60 lines)."""
import re, sys, pathlib
from gdr40_math_map import DIAGRAM_MAP, MATH_MAP
from gdr40_code_ranges import CODE_RANGES, unescape_code_str

def clean_prose(text: str) -> str:
    for k, v in DIAGRAM_MAP.items(): text = text.replace(k, v)
    for k, v in MATH_MAP.items(): text = text.replace(k, v)
    subs = [
        (r'\\<([a-zA-Z0-9_-]+)\\>', r'`<\1>`'), (r'\\<=', r'<='),
        (r'\\--', r'--'), (r'\\_', r'_'), (r'\\-', r'-'),
        (r'\\=', r'='), (r'\\~', r'~'), (r'\\\)', r')'),
        (r'\\\(', r'('), (r'\\:', r':'), (r'\\!', r'!'), (r'\\*', r'*')
    ]
    for pat, rep in subs: text = re.sub(pat, rep, text)
    return text

def format_doc(doc_path: pathlib.Path) -> str:
    lines = doc_path.read_text(encoding="utf-8").splitlines(keepends=True)
    out, cur = [], 0
    for idx, lang, start, end, has_hdr in CODE_RANGES:
        p_start, p_end = cur, start - 1
        if p_end > p_start:
            out.append(clean_prose("".join(lines[p_start:p_end])))
        c_lines = lines[start:end] if has_hdr else lines[start - 1:end]
        code = unescape_code_str("".join(c_lines))
        if idx == 15:
            code = code.replace("modules (<60 lines).", 'modules "(<60 lines)."')
        out.append(f"\n```{lang}\n{code.strip()}\n```\n\n")
        cur = end
    tail = "".join(lines[cur:])
    if "\n[image1]:" in tail: tail = tail.split("\n[image1]:")[0]
    out.append(clean_prose(tail).rstrip() + "\n")
    return "".join(out)

if __name__ == "__main__":
    p = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "output.md")
    p.write_text(format_doc(p), encoding="utf-8")
    print(f"FORMATTED_OK: {p}")
