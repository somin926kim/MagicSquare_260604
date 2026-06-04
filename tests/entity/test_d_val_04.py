"""D-VAL-04 — FR-VAL-04: anti-diagonal `/` sum = MAGIC_CONSTANT (Mom Test)."""

from entity.constants import MAGIC_CONSTANT
from entity.validator import anti_diagonal_sum, validate_anti_diagonal


def test_d_val_04_anti_diagonal_sum(grid_g1_solved):
    # Given: G1 solved — blanks filled, 10선=34 (conftest grid_g1_solved)
    # When: validate_anti_diagonal(grid_g1_solved)
    total = anti_diagonal_sum(grid_g1_solved)
    # Then: 반대 대각선 `/` 합 = 34 (FR-VAL-04, Mom Test)
    assert total == MAGIC_CONSTANT
    assert validate_anti_diagonal(grid_g1_solved) is True
