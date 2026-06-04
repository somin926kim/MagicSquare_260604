"""Golden Master approval helpers — format SSOT and file comparison."""

from __future__ import annotations

import os
from pathlib import Path

GOLDEN_ROOT = Path(__file__).resolve().parent / "golden"


def format_int6(values: list[int]) -> str:
    """Golden format for success: comma-separated int[6] (1-index coords)."""
    if len(values) != 6:
        raise ValueError(f"int[6] required, got {len(values)}")
    return ",".join(str(v) for v in values)


def format_error_code(code: str) -> str:
    """Golden format for boundary error output."""
    return code.strip()


def assert_matches_golden(actual: str, relative: str) -> None:
    """Compare actual text to tests/golden/{relative}, or update when UPDATE_GOLDEN=1."""
    golden_path = GOLDEN_ROOT / relative
    normalized = actual if actual.endswith("\n") else f"{actual}\n"

    if os.environ.get("UPDATE_GOLDEN") == "1":
        golden_path.parent.mkdir(parents=True, exist_ok=True)
        golden_path.write_text(normalized, encoding="utf-8")
        return

    if not golden_path.is_file():
        raise FileNotFoundError(f"Golden file missing: {golden_path}")

    expected = golden_path.read_text(encoding="utf-8")
    assert normalized == expected, (
        f"Golden mismatch: {relative}\n"
        f"expected: {expected!r}\n"
        f"actual:   {normalized!r}"
    )
