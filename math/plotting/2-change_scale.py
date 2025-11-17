#!/usr/bin/env python3
"""
Module for plotting exponential decay with logarithmic y-axis scale.
This module demonstrates how to use logarithmic scaling in matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt


def change_scale():
    """
    Plots the exponential decay of Carbon-14 (C-14) with logarithmic y-axis.

    The function models radioactive decay using the exponential decay formula:
    y = e^((r/t) * x)
    where:
    - r = ln(0.5) (decay constant)
    - t = 5730 years (half-life of C-14)
    - x = time in years

    The y-axis is logarithmically scaled to better visualize exponential decay.

    Returns:
        None: Displays the plot using plt.show()
    """

    x = np.arange(0, 28651, 5730)

    r = np.log(0.5)

    t = 5730

    y = np.exp((r / t) * x)

    plt.figure(figsize=(6.4, 4.8))

    plt.plot(x, y)

    plt.xlabel('Time (years)')

    plt.ylabel('Fraction Remaining')

    plt.title('Exponential Decay of C-14')

    plt.yscale('log')

    plt.xlim(0, 28650)

    plt.show()
