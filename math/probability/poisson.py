#!/usr/bin/env python3
"""
Poisson distribution class
"""
import math


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
        res = (self.lambtha ** k * math.exp(-self.lambtha)) / math.factorial(k)
        return res
