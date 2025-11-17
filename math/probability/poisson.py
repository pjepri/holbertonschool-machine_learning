#!/usr/bin/env python3
"""
Poisson distribution class for probability calculations
"""


class Poisson:
    """
    Class representing a Poisson probability distribution
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Constructor for Poisson distribution

        Args:
            data: List of data values to estimate the distribution (optional)
            lambtha: Mean number of occurrences in the time interval
        """
        if data is None:
            if lambtha < 1:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        Computes the PMF value for a given number of successes

        Args:
            k: The number of successes (converted to int if not integer)

        Returns:
            The PMF probability value, or 0 for negative k values
        """
        if type(k) is not int:
            k = int(k)

        if k < 0:
            return 0

        euler = 2.7182818285
        lambda_val = self.lambtha

        fact = 1
        for j in range(1, k + 1):
            fact *= j

        probability = ((lambda_val ** k) * (euler ** -lambda_val)) / fact

        return probability

    def cdf(self, k):
        """
        Computes the CDF value for a given number of successes

        Args:
            k: The number of successes (converted to int if not integer)

        Returns:
            The CDF probability value, or 0 for negative k values
        """
        if type(k) is not int:
            k = int(k)

        if k < 0:
            return 0

        cumulative = 0
        for i in range(k + 1):
            cumulative += self.pmf(i)

        return cumulative
