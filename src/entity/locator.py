"""Blank cell coordinate lookup — entity layer."""

from entity.constants import BLANK_CELL, INDEX_BASE


def find_blank_coords(grid: list[list[int]]) -> list[tuple[int, int]]:
    """Return 1-index (row, col) pairs for blank cells, row-major order."""
    coords: list[tuple[int, int]] = []
    for row_index, row in enumerate(grid):
        for col_index, value in enumerate(row):
            if value == BLANK_CELL:
                coords.append((row_index + INDEX_BASE, col_index + INDEX_BASE))
    return coords
