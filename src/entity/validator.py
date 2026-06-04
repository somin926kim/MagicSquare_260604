"""10-line validation — entity layer (Mom Test: include `/`)."""

from entity.constants import GRID_SIZE, INDEX_BASE, MAGIC_CONSTANT


def anti_diagonal_sum(grid: list[list[int]]) -> int:
    """Sum of cells on anti-diagonal `/` (top-right to bottom-left)."""
    return sum(grid[row][GRID_SIZE - INDEX_BASE - row] for row in range(GRID_SIZE))


def validate_anti_diagonal(grid: list[list[int]]) -> bool:
    """True when anti-diagonal `/` sum equals magic constant."""
    return anti_diagonal_sum(grid) == MAGIC_CONSTANT
