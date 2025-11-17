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

    def pdf(self, x):
        """
        Calculates the value of the PDF for a given x-value

        Args:
            x: The x-value

        Returns:
            The PDF probability density value for x
        """
        euler = 2.7182818285
        pi = 3.141592653589793
        sqrt_2pi = 2.5066282746310002

        # PDF formula: (1 / (σ * √(2π))) * e^(-(x-μ)²/(2σ²))
        z = (x - self.mean) / self.stddev
        exponent = -0.5 * z * z
        pdf_value = (1.0 / (self.stddev * sqrt_2pi)) * (euler ** exponent)

        return pdf_value

    def erf(self, x):
        """
        Approximates the error function using Taylor series
        """
        sqrt_pi = 1.7724538509055159

        sign = 1
        if x < 0:
            sign = -1
            x = -x

        result = 0.0
        term = x
        factorial = 1

        for n in range(200):
            result += term / (factorial * (2 * n + 1))
            if abs(term / (factorial * (2 * n + 1))) < 1e-20:
                break
            term *= -x * x
            factorial *= (n + 1)

        return sign * 2.0 / sqrt_pi * result

    def cdf(self, x):
        """
        Calculates the value of the CDF for a given x-value

        Args:
            x: The x-value

        Returns:
            The CDF value for x
        """
        pi = 3.1415926536

        z = self.z_score(x) / (2 ** 0.5)

        erf = (2 / (pi ** 0.5)) * (
            z - (z ** 3) / 3 + (z ** 5) / 10 - (z ** 7) / 42 + (z ** 9) / 216
        )

        cdf_value = 0.5 * (1 + erf)

        return cdf_value
