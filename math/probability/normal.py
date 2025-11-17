#!/usr/bin/env python3
"""
Normal distribution implementation
"""


class Normal:
    """
    Class representing a normal (Gaussian) probability distribution
    """

    def __init__(self, data=None, mean=0., stddev=1.):
        """
        Constructor for Normal distribution

        Args:
            data: List of data values to estimate the distribution (optional)
            mean: Mean of the distribution (default: 0.0)
            stddev: Standard deviation of the distribution (default: 1.0)
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = float(sum(data) / len(data))
            variance = sum((x - self.mean) ** 2 for x in data) / len(data)
            self.stddev = float(variance ** 0.5)

    def z_score(self, x):
        """
        Calculates the z-score of a given x-value

        Args:
            x: The x-value

        Returns:
            The z-score of x
        """
        z = (x - self.mean) / self.stddev
        return z

    def x_value(self, z):
        """
        Calculates the x-value of a given z-score

        Args:
            z: The z-score

        Returns:
            The x-value of z
        """
        x = self.mean + z * self.stddev
        return x

    def erf(self, x):
        """
        Approximates the error function using Taylor series
        """
        sqrt_pi = 1.7724538509055159
        result = 0.0
        term = x
        factorial = 1

        for n in range(100):
            result += term / (factorial * (2 * n + 1))
            if abs(term / (factorial * (2 * n + 1))) < 1e-15:
                break
            term *= -x * x
            factorial *= (n + 1)

        return 2.0 / sqrt_pi * result

    def cdf(self, x):
        """
        Calculates the value of the CDF for a given x-value

        Args:
            x: The x-value

        Returns:
            The CDF value for x
        """
        z = (x - self.mean) / self.stddev

        sqrt2 = 1.4142135623730951
        erf_value = self.erf(z / sqrt2)
        cdf_value = 0.5 * (1 + erf_value)

        return cdf_value
