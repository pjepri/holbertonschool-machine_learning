#!/usr/bin/env python3
"""
Binomial distribution implementation
"""


class Binomial:
    """
    Class representing a binomial probability distribution
    """

    def __init__(self, data=None, n=1, p=0.5):
        """
        Constructor for Binomial distribution

        Args:
            data: List of data values to estimate the distribution (optional)
            n: Number of Bernoulli trials (default: 1)
            p: Probability of success (default: 0.5)
        """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            mean_data = sum(data) / len(data)
            variance = sum((x - mean_data) ** 2 for x in data) / len(data)

            p_estimate = 1 - (variance / mean_data) if mean_data > 0 else 0.5

            n_estimate = mean_data / p_estimate if p_estimate > 0 else 1

            self.n = int(round(n_estimate))

            self.p = float(mean_data / self.n) if self.n > 0 else 0.5

    def factorial(self, num):
        """
        Calculates factorial of a number
        """
        if num == 0 or num == 1:
            return 1
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

    def pmf(self, k):
        """
        Calculates the value of the PMF for a given number of successes

        Args:
            k: Number of successes (converted to int if not integer)

        Returns:
            The PMF probability value, or 0 if k is out of range
        """
        if type(k) is not int:
            k = int(k)

        if k < 0 or k > self.n:
            return 0

        n_fact = self.factorial(self.n)
        k_fact = self.factorial(k)
        nk_fact = self.factorial(self.n - k)

        coefficient = n_fact / (k_fact * nk_fact)

        pmf_val = coefficient * (self.p ** k) * ((1 - self.p) ** (self.n - k))

        return pmf_val

    def cdf(self, k):
        """
        Calculates the value of the CDF for a given number of successes

        Args:
            k: Number of successes (converted to int if not integer)

        Returns:
            The CDF cumulative probability value, or 0 if k is out of range
        """
        if type(k) is not int:
            k = int(k)

        if k < 0:
            return 0

        cumulative = 0
        for i in range(k + 1):
            cumulative += self.pmf(i)

        return cumulative
