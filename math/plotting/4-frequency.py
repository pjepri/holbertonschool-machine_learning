#!/usr/bin/env python3
"""
Module for plotting a histogram of student grades.
This module demonstrates histogram visualization with matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """
    Plots a histogram showing the distribution of student grades for Project A.

    The function generates 50 student grades from a normal distribution with:
    - Mean: 68
    - Standard deviation: 15

    The histogram uses bins of 10 units (0-10, 10-20, ..., 90-100) and
    bars are outlined in black for better visibility.

    Returns:
        None: Displays the plot using plt.show()
    """
    np.random.seed(5)

    student_grades = np.random.normal(68, 15, 50)

    plt.figure(figsize=(6.4, 4.8))

    bins = np.arange(0, 101, 10)

    plt.hist(student_grades, bins=bins, edgecolor='black')

    plt.xlabel('Grades')

    plt.ylabel('Number of Students')

    plt.title('Project A')

    plt.xlim(0, 100)

    plt.xticks(np.arange(0, 101, 10))

    plt.ylim(0, 30)

    plt.yticks(np.arange(0, 31, 5))

    plt.show()
