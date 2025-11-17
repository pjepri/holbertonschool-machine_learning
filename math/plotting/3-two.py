#!/usr/bin/env python3
"""
Module for plotting multiple exponential decay curves on the same graph.
This module demonstrates how to plot multiple lines
with different styles and legends.
"""

import numpy as np
import matplotlib.pyplot as plt


def two():
    """
    Plots exponential decay curves for
    two radioactive elements: C-14 and Ra-226.

    The function compares the decay rates of:
    - Carbon-14 (C-14): half-life of 5730 years (dashed red line)
    - Radium-226 (Ra-226): half-life of 1600 years (solid green line)

    Both elements follow the exponential decay formula:
    y = e^((r/t) * x)
    where r = ln(0.5) and t is the half-life.

    The plot shows how
    Ra-226 decays faster than C-14 due to its shorter half-life.

    Returns:
        None: Displays the plot using plt.show()
    """

    x = np.arange(0, 21000, 1000)

    r = np.log(0.5)

    t1 = 5730

    t2 = 1600

    y1 = np.exp((r / t1) * x)

    y2 = np.exp((r / t2) * x)

    plt.figure(figsize=(6.4, 4.8))

    plt.plot(x, y1, 'r--', label='C-14')

    plt.plot(x, y2, 'g-', label='Ra-226')

    plt.xlabel('Time (years)')

    plt.ylabel('Fraction Remaining')

    plt.title('Exponential Decay of Radioactive Elements')

    plt.xlim(0, 20000)

    plt.ylim(0, 1)

    plt.legend(loc='upper right')

    plt.show()
