"""D-VAL-04 — FR-VAL-04: anti-diagonal `/` sum = MAGIC_CONSTANT (Mom Test)."""

import pytest


def test_d_val_04_anti_diagonal_sum(grid_g1):
    # Given: G1 격자 — 4×4, 빈칸 0×2 (conftest grid_g1)
    # When: validate_anti_diagonal(grid_g1)  — RED 스켈레톤: 미호출
    # Then: 반대 대각선 `/` 합 = 34 (FR-VAL-04)
    pytest.fail("RED: D-VAL-04 — validate_anti_diagonal 미구현, 의도적 실패")
