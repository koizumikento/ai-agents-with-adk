import runpy
from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_main_prints_hello(capsys: pytest.CaptureFixture[str]) -> None:
    runpy.run_path(str(PROJECT_ROOT / "main.py"), run_name="__main__")
    captured = capsys.readouterr()
    assert "Hello from ai-agents!" in captured.out
