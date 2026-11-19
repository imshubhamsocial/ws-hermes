#!/usr/bin/env python3
"""Deterministic NVIDIA RTX 3050 VRAM Ceiling & Quiescence Verifier shim."""
import os
import sys

TARGET = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".hermes", "tools", "icm", "check_vram_limit.py"))
os.execv(sys.executable, [sys.executable, TARGET] + sys.argv[1:])
