#!/usr/bin/env python3
"""Module for calculating matrix shapes."""

def matrix_shape(matrix):
    """Calculate the shape of a matrix."""
    shape = []
    current = matrix
    while isinstance(current, list) and len(current) > 0:
        shape.append(len(current))
        current = current[0]
    return shape
