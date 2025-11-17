#!/usr/bin/env python3
"""
Function to calculate the derivative of a polynomial
"""


def poly_derivative(poly):
    """
    Calculates the derivative of a polynomial

    Args:
        poly: A list of coefficients representing a polynomial
              where the index represents the power of x

    Returns:
        A new list of coefficients representing the derivative,
        or None if poly is not valid, or [0] if derivative is 0
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    if not all(isinstance(coeff, (int, float)) for coeff in poly):
        return None

    if len(poly) == 1:
        return [0]

    derivative = []
    for i in range(1, len(poly)):
        derivative.append(i * poly[i])

    if all(coeff == 0 for coeff in derivative):
        return [0]

    return derivative
