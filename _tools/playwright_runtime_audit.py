#!/usr/bin/env python3
"""Immutable 4-Gate Headless Browser Runtime & Framebuffer Verifier."""
import argparse
import json
import sys
import numpy as np
import cv2
from playwright.sync_api import sync_playwright

def run_audit(url: str, width: int, height: int, min_std: float, out_json: str) -> int:
    console_errors, page_errors, bad_http, warnings = [], [], [], []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": width, "height": height})
        page.on("console", lambda m: console_errors.append(m.text) if m.type == "error" else (
            warnings.append(m.text) if m.type == "warning" else None))
        page.on("pageerror", lambda exc: page_errors.append(str(exc)))
        page.on("response", lambda r: bad_http.append(f"{r.status}:{r.url}") if r.status >= 400 else None)
        page.goto(url, wait_until="networkidle", timeout=15000)
        page.wait_for_timeout(1500)
        canvas = page.locator("canvas").first
        box = canvas.bounding_box() if canvas.count() > 0 else None
        png_bytes = canvas.screenshot() if box else b""
        browser.close()
    img = cv2.imdecode(np.frombuffer(png_bytes, np.uint8), cv2.IMREAD_COLOR) if png_bytes else None
    pixel_std = float(np.std(img)) if img is not None else 0.0
    geom_ok = bool(box and int(round(box["width"])) == width and int(round(box["height"])) == height)
    passed = (len(console_errors) == 0 and len(page_errors) == 0 and len(bad_http) == 0
              and len(warnings) == 0 and geom_ok and pixel_std >= min_std)
    receipt = {"url": url, "passed": passed, "console_errors": len(console_errors),
               "page_errors": len(page_errors), "warnings": len(warnings),
               "http_4xx_5xx": len(bad_http), "canvas_box": box, "pixel_std": round(pixel_std, 2)}
    if out_json:
        with open(out_json, "w", encoding="utf-8") as f:
            json.dump(receipt, f, indent=2)
    print(json.dumps(receipt))
    return 0 if passed else 1

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--width", type=int, default=1280)
    ap.add_argument("--height", type=int, default=720)
    ap.add_argument("--min-std", type=float, default=5.0)
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    sys.exit(run_audit(args.url, args.width, args.height, args.min_std, args.out))
