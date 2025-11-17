#!/usr/bin/env python3
"""
Function to calculate the sum of squares from 1 to n
"""


def summation_i_squared(n):
    """
    Calculates the sum of squares from 1 to n

    Args:
        n: The stopping condition (positive integer)

    Returns:
        The integer value of the sum, or None if n is not valid
    """
    if not isinstance(n, int) or n < 1:
        return None

    # Formula: sum of squares = n(n+1)(2n+1)/6
    return int(n * (n + 1) * (2 * n + 1) / 6)
