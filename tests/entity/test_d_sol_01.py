"""D-SOL-01 — FR-SOL-01: solve partial grid → int[6] golden master."""

from _approval import assert_matches_golden, format_int6
from entity.solver import solve


def test_d_sol_01_step_a_success(grid_g1):
    # Given: G1 격자 — 4×4, blank 2개 (conftest grid_g1)
    # When: solve(grid_g1)
    result = solve(grid_g1)
    # Then: int[6] [r1,c1,n1,r2,c2,n2] 1-index row-major (FR-SOL-01)
    assert result == [2, 3, 11, 4, 4, 1]
    assert_matches_golden(format_int6(result), "d_sol_01_g1_step_a.approved.txt")
