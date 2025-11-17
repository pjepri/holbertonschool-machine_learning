#!/usr/bin/env python3
"""
Exponential distribution implementation
"""


class Exponential:
    """
    Class representing an exponential probability distribution
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Constructor for Exponential distribution

        Args:
            data: List of data values to estimate the distribution (optional)
            lambtha: Rate parameter of the exponential distribution
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean_data = sum(data) / len(data)
            self.lambtha = float(1.0 / mean_data)

    def pdf(self, x):
        """
        Computes the PDF value for a given time period

        Args:
            x: The time period

        Returns:
            The PDF probability density value, or 0 if x is out of range
        """
        if x < 0:
            return 0

        euler = 2.7182818285
        lambda_val = self.lambtha

        pdf_value = lambda_val * (euler ** (-lambda_val * x))

        return pdf_value

    def cdf(self, x):
        """
        Computes the CDF value for a given time period

        Args:
            x: The time period

        Returns:
            The CDF cumulative probability value, or 0 if x is out of range
        """
        if x < 0:
            return 0

        euler = 2.7182818285
        lambda_val = self.lambtha

        cdf_value = 1 - (euler ** (-lambda_val * x))

        return cdf_value
