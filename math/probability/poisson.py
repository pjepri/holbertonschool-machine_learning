#!/usr/bin/env python3
"""
Poisson distribution class
"""


class Poisson:
    """
    Represents a Poisson distribution
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Initialize Poisson distribution

        Args:
            data: list of data to estimate the distribution
            lambtha: expected number of occurrences in a given time frame
        """
        if data is None:
            # Use the given lambtha
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def factorial(self, n):
        """
        Calculate factorial of n
        """
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def exp(self, x):
        """
        Calculate e^x using Taylor series
        """
        result = 1.0
        term = 1.0
        for i in range(1, 200):
            term *= x / i
            result += term
            if abs(term) < 1e-15:
                break
        return result

    def pmf(self, k):
        """
        Calculate the value of the PMF for a given number of
        "successes"

        Args:
            k: number of "successes"

        Returns:
            PMF value for k
        """
        k = int(k)

        if k < 0:
            return 0
        res = (self.lambtha ** k * self.exp(-self.lambtha)) / self.factorial(k)
        return res
