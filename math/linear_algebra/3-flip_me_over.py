#!/usr/bin/env python3
"""Module for matrix transpose operations."""


def matrix_transpose(matrix):
    """Return the transpose of a 2D matrix."""
    if not matrix or not matrix[0]:
        return []

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    transpose = []
    for col_idx in range(num_cols):
        new_row = []
        for row_idx in range(num_rows):
            new_row.append(matrix[row_idx][col_idx])
        transpose.append(new_row)

    return transpose
