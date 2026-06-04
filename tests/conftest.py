"""Shared pytest fixtures — grid data only (no domain logic)."""

import sys
from pathlib import Path

import pytest

TESTS_ROOT = Path(__file__).resolve().parent
if str(TESTS_ROOT) not in sys.path:
    sys.path.insert(0, str(TESTS_ROOT))

__all__ = ["grid_g1"]


@pytest.fixture
def grid_g1():
    """G1 — 4×4 partial grid; two blanks (0); row-major."""
    return [
        [16, 3, 2, 13],
        [5, 10, 0, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 0],
    ]
