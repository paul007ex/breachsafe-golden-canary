# SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
"""Smoke tests that the breachsafe-golden-canary entry point runs."""

from __future__ import annotations

import pytest

from golden_canary.__main__ import main


def test_main_returns_zero() -> None:
    assert main([]) == 0


def test_version_flag_exits_zero(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as excinfo:
        main(["--version"])
    assert excinfo.value.code == 0
    assert capsys.readouterr().out.strip().endswith("0.0.1")
