#!/usr/bin/env python3
"""
Module for plotting a scatter plot of height vs weight.
This module demonstrates scatter plot visualization with matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt


def scatter():
    """
    Plots a scatter plot of men's height vs weight.

    The function generates 2000 data points from a multivariate normal
    distribution representing height and weight measurements, then plots
    them as magenta points in a scatter plot.

    Data generation:
    - Mean height: 69 inches
    - Mean weight offset: 180 lbs (added after generation)
    - Covariance matrix creates correlation between height and weight
    - Random seed is set to 5 for reproducibility

    Returns:
        None: Displays the plot using plt.show()
    """

    mean = [69, 0]

    cov = [[15, 8], [8, 15]]

    np.random.seed(5)

    x, y = np.random.multivariate_normal(mean, cov, 2000).T

    y += 180

    plt.figure(figsize=(6.4, 4.8))

    plt.scatter(x, y, c='magenta')

    plt.xlabel('Height (in)')

    plt.ylabel('Weight (lbs)')

    plt.title("Men's Height vs Weight")

    plt.show()
