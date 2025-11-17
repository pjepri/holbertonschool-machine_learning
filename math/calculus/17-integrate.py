#!/usr/bin/env python3
"""
Function to calculate the integral of a polynomial
"""


def poly_integral(poly, C=0):
    """
    Calculates the integral of a polynomial

    Args:
        poly: A list of coefficients representing a polynomial
              where the index represents the power of x
        C: An integer representing the integration constant

    Returns:
        A new list of coefficients representing the integral,
        or None if poly or C are not valid
    """

    if not isinstance(poly, list) or len(poly) == 0:
        return None

    if not isinstance(C, (int, float)):
        return None

    if not all(isinstance(coeff, (int, float)) for coeff in poly):
        return None

    integral = [C]

    for i in range(len(poly)):
        if i + 1 == 0:
            continue
        coeff = poly[i] / (i + 1)
        if coeff == int(coeff):
            integral.append(int(coeff))
        else:
            integral.append(coeff)

    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral
