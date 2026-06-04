"""D-LOC-01 — FR-LOC-01: blank (0) cell coordinates, 1-index, row-major."""

from entity.locator import find_blank_coords


def test_d_loc_01_blank_coords_row_major(grid_g1):
    # Given: G1 격자 — 0이 2개, row-major (conftest grid_g1)
    # When: find_blank_coords(grid_g1)
    result = find_blank_coords(grid_g1)
    # Then: [(2, 3), (4, 4)] 반환 (1-index, row-major) (FR-LOC-01)
    assert result == [(2, 3), (4, 4)]
