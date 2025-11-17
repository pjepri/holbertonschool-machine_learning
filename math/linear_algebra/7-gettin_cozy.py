#!/usr/bin/env python3
"""Module for 2D matrix concatenation operations."""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenate two 2D matrices along a specific axis."""
    if axis == 0:
        if len(mat1) == 0 or len(mat2) == 0:
            return None
        if len(mat1[0]) != len(mat2[0]):
            return None

        result = []
        for row in mat1:
            result.append(row[:])
        for row in mat2:
            result.append(row[:])
        return result

    elif axis == 1:
        if len(mat1) != len(mat2):
            return None

        result = []
        for i in range(len(mat1)):
            new_row = mat1[i][:] + mat2[i][:]
            result.append(new_row)
        return result

    return None
