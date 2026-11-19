#!/usr/bin/env python3
"""Unit tests for icm-stage-compiler verify_stage.py (35 lines)."""
import importlib.util
import pathlib
import tempfile
import unittest

SCRIPT_PATH = pathlib.Path(__file__).resolve().parents[1] / "scripts" / "verify_stage.py"
SPEC = importlib.util.spec_from_file_location("verify_stage", SCRIPT_PATH)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)

class TestICMStageCompiler(unittest.TestCase):
    def test_valid_stage_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            stg = pathlib.Path(tmp)
            (stg / "output").mkdir()
            (stg / "CONTEXT.md").write_text("## Inputs\n## Process Steps\n## Outputs\n", encoding="utf-8")
            (stg / "output" / "helper.py").write_text("print('ok')\n" * 10, encoding="utf-8")
            ok, errs = MOD.verify_stage(stg)
            self.assertTrue(ok)
            self.assertEqual(errs, [])

    def test_oversized_script_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            stg = pathlib.Path(tmp)
            (stg / "output").mkdir()
            (stg / "CONTEXT.md").write_text("## Inputs\n## Process Steps\n## Outputs\n", encoding="utf-8")
            (stg / "output" / "bloat.py").write_text("x = 1\n" * 60, encoding="utf-8")
            ok, errs = MOD.verify_stage(stg)
            self.assertFalse(ok)
            self.assertTrue(any("ATOMIC_LIMIT_EXCEEDED" in e for e in errs))

if __name__ == "__main__":
    unittest.main()
