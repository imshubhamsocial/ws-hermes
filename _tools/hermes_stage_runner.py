#!/usr/bin/env python3
"""Autonomous ICM Stage Compiler with llama-server KV Slot Isolation shim."""
import os
import sys

TARGET = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".hermes", "skills", "icm", "icm-stage-compiler", "scripts", "hermes_stage_runner.py"))
os.execv(sys.executable, [sys.executable, TARGET] + sys.argv[1:])
