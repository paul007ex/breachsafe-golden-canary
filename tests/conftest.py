# SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
"""Shared pytest fixtures for the breachsafe-golden-canary test suite."""

from __future__ import annotations

import pytest


@pytest.fixture
def project_name() -> str:
    """Return the human-readable project name for assertions."""
    return "Golden Canary"
