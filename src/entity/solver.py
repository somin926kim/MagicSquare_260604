"""Partial magic square solver — entity layer."""

from __future__ import annotations

from itertools import permutations

from entity.constants import (
    BLANK_CELL,
    GRID_SIZE,
    INDEX_BASE,
    MAGIC_CONSTANT,
    MAX_CELL_VALUE,
)
from entity.locator import find_blank_coords


def _all_lines_match_magic_constant(grid: list[list[int]]) -> bool:
    for row in grid:
        if sum(row) != MAGIC_CONSTANT:
            return False
    for col in range(GRID_SIZE):
        if sum(grid[row][col] for row in range(GRID_SIZE)) != MAGIC_CONSTANT:
            return False
    if sum(grid[i][i] for i in range(GRID_SIZE)) != MAGIC_CONSTANT:
        return False
    if sum(grid[i][GRID_SIZE - INDEX_BASE - i] for i in range(GRID_SIZE)) != MAGIC_CONSTANT:
        return False
    return True


def solve(grid: list[list[int]]) -> list[int] | None:
    """Return int[6] [r1,c1,n1,r2,c2,n2] 1-index row-major, or None if unsolved."""
    blanks = find_blank_coords(grid)
    used = {value for row in grid for value in row if value != BLANK_CELL}
    missing = [
        value
        for value in range(INDEX_BASE, MAX_CELL_VALUE + INDEX_BASE)
        if value not in used
    ]

    if len(blanks) != 2 or len(missing) != 2:
        return None

    for candidate_values in permutations(missing):
        trial = [row[:] for row in grid]
        for (row, col), value in zip(blanks, candidate_values):
            trial[row - INDEX_BASE][col - INDEX_BASE] = value
        if _all_lines_match_magic_constant(trial):
            row1, col1 = blanks[0]
            row2, col2 = blanks[1]
            return [row1, col1, candidate_values[0], row2, col2, candidate_values[1]]

    return None
