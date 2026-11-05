import os
import pathlib
import re
from typing import List, Dict

WORKSPACE_ROOT = pathlib.Path("/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes")
ICM_LAYERS = {
    0: "AGENTS.md",
    1: "CONTEXT.md",
    2: "stages/01-spec/CONTEXT.md",
    3: "rules/",
    4: "artifacts/"
}
LINE_CAPS = {
    "CONTEXT.md": 80,
    "rules/": 200
}

def check_file_existence(path: pathlib.Path) -> bool:
    """Checks if a file or directory exists."""
    return path.exists()

def count_lines(path: pathlib.Path) -> int:
    """Counts lines in a file."""
    try:
        with open(path, 'r') as f:
            return sum(1 for line in f)
    except FileNotFoundError:
        return -1

def check_4_column_table(path: pathlib.Path) -> bool:
    """Checks if a CONTEXT.md file contains the 4-column table standard."""
    try:
        content = path.read_text()
        # Simple regex check for a markdown table structure with 4 columns
        # Requires at least a header row and a separator row
        table_pattern = r"\|.*?\|.*?\|.*?\|.*?\|.*?\|"
        return bool(re.search(table_pattern, content))
    except Exception:
        return False

def run_8_point_walk_test() -> Dict[str, bool]:
    """Executes the 8-Point Walk Test based on ICM invariants."""
    results = {}
    print("--- ICM 8-Point Walk Test ---")

    # 1. Check Layer Existence (0-4)
    for layer, file_or_dir in ICM_LAYERS.items():
        path = WORKSPACE_ROOT / file_or_dir
        exists = check_file_existence(path)
        results[f"Layer {layer} Exists"] = exists
        print(f"Layer {layer} ({file_or_dir}): {'PASS' if exists else 'FAIL'}")

    # 2. Check AGENTS.md existence (Layer 0)
    results["L0_AGENTS_md_present"] = check_file_existence(WORKSPACE_ROOT / "AGENTS.md")
    print(f"L0 AGENTS.md: {'PASS' if results['L0_AGENTS_md_present'] else 'FAIL'}")

    # 3. Check CONTEXT.md line cap (Layer 1)
    context_path = WORKSPACE_ROOT / "CONTEXT.md"
    lines = count_lines(context_path)
    cap = LINE_CAPS.get("CONTEXT.md", 0)
    results["L1_CONTEXT_md_cap"] = lines <= cap
    print(f"L1 CONTEXT.md lines ({lines}): {'PASS' if results['L1_CONTEXT_md_cap'] else 'FAIL'} (Cap: {cap})")

    # 4. Check Stage Context line cap (Layer 2)
    stage_context_path = WORKSPACE_ROOT / "stages/01-spec/CONTEXT.md"
    lines = count_lines(stage_context_path)
    cap = LINE_CAPS.get("CONTEXT.md", 0)
    results["L2_STAGE_CONTEXT_md_cap"] = lines <= cap
    print(f"L2 Stage CONTEXT.md lines ({lines}): {'PASS' if results['L2_STAGE_CONTEXT_md_cap'] else 'FAIL'} (Cap: {cap})")

    # 5. Check Rules/Config line cap (Layer 3)
    rules_path = WORKSPACE_ROOT / "rules/"
    if rules_path.is_dir():
        for item in rules_path.iterdir():
            if item.is_file():
                lines = count_lines(item)
                cap = LINE_CAPS.get("rules/", 0)
                results[f"L3_Rule_Cap_{item.name}"] = lines <= cap
                print(f"L3 Rule {item.name} lines ({lines}): {'PASS' if results[f'L3_Rule_Cap_{item.name}'] else 'FAIL'} (Cap: {cap})")
    else:
        results["L3_Rules_Dir_Exists"] = False
        print("L3 Rules Dir: FAIL (Directory not found)")

    # 6. Check 4-Column Table Standard (Layer 1)
    results["L1_4_Column_Table"] = check_4_column_table(context_path)
    print(f"L1 4-Column Table: {'PASS' if results['L1_4_Column_Table'] else 'FAIL'}")

    # 7. Check Layer 4 Artifacts existence
    results["L4_Artifacts_Dir_Exists"] = check_file_existence(WORKSPACE_ROOT / "artifacts/")
    print(f"L4 Artifacts Dir: {'PASS' if results['L4_Artifacts_Dir_Exists'] else 'FAIL'}")

    # 8. Overall Status
    all_passed = all(results.values())
    print("\\n--- SUMMARY ---")
    print(f"ICM Validation Status: {'SUCCESS' if all_passed else 'FAILURE'}")
    return results

if __name__ == "__main__":
    validation_results = run_8_point_walk_test()
    # Exit with non-zero code on failure for CI/automation
    if not all(validation_results.values()):
        exit(1)
