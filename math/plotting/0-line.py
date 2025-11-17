#!/usr/bin/env python3
"""
Module for plotting a line graph of y = x^3.
This module demonstrates basic line plotting with matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt


def line():
    """
    Plots y = x^3 as a solid red line graph.

    The function creates a line plot where:
    - x ranges from 0 to 10
    - y = x^3 (cubic function)
    - The line is solid and red
    - Figure size is 6.4 x 4.8 inches

    Returns:
        None: Displays the plot using plt.show()
    """
    y = np.arange(0, 11) ** 3

    plt.figure(figsize=(6.4, 4.8))

    x = np.arange(0, 11)

    plt.plot(x, y, 'r-')

    plt.xlim(0, 10)

    plt.show()
