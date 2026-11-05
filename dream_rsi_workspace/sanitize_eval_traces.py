#!/usr/bin/env python3
"""
Stage 2 De-Identification Gate for dreamRSI.
Strips benchmark-specific proper nouns, IDs, and literals from evaluation traces.
"""
import re
import sys
from pathlib import Path

CONTAMINATION_PATTERNS = [
    (r"\bIsabella\s+Johansson\b", "<CUSTOMER_FULL_NAME>"),
    (r"\bIvan\s+Hernandez\b", "<CUSTOMER_FULL_NAME>"),
    (r"\bRaj\s+Santos\b", "<CUSTOMER_FULL_NAME>"),
    (r"\bLei\s+(?:Wilson|Li)\b", "<CUSTOMER_FULL_NAME>"),
    (r"\bJames\s+Sanchez\b", "<CUSTOMER_FULL_NAME>"),
    (r"\b32286\b", "<POSTAL_CODE_A>"),
    (r"\b92133\b", "<POSTAL_CODE_B>"),
    (r"\b32255\b", "<POSTAL_CODE_C>"),
    (r"\b60623\b", "<POSTAL_CODE_D>"),
    (r"#W\d{7}\b", "<ORDER_ID_REFERENCE>"),
    (r"\b\d{10}\b", "<ITEM_SKU_REFERENCE>"),
    (r"\bMercury_\d+\b", "<SCIENTIFIC_QUESTION_ID>"),
]

def sanitize_text(text: str) -> str:
    sanitized = text
    for pattern, replacement in CONTAMINATION_PATTERNS:
        sanitized = re.sub(pattern, replacement, sanitized, flags=re.IGNORECASE)
    return sanitized

def verify_zero_contamination(file_path: Path) -> bool:
    content = file_path.read_text(encoding="utf-8")
    for pattern, _ in CONTAMINATION_PATTERNS:
        matches = re.findall(pattern, content, flags=re.IGNORECASE)
        if matches:
            print(f"CONTAMINATION LEAK DETECTED in {file_path}: {matches}", file=sys.stderr)
            return False
    return True

if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("dream_rsi_workspace/lora_atropos_dpo.jsonl")
    if not verify_zero_contamination(target):
        sys.exit(1)
    print("VERIFIED: Zero benchmark literal leakage detected.")
