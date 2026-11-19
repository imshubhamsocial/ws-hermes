#!/usr/bin/env python3
"""Automated 8-Point ICM Walk Test and Workspace Contract Validator shim."""
import os
import sys

TARGET = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".hermes", "skills", "icm", "icm-stage-compiler", "scripts", "hermes_icm_validator.py"))
os.execv(sys.executable, [sys.executable, TARGET] + sys.argv[1:])
