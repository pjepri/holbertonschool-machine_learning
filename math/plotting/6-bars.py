#!/usr/bin/env python3
"""
Module for plotting a stacked bar chart of fruit quantities per person.
This module demonstrates how to create stacked bar charts with matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt


def bars():
    """
    Plots a stacked bar chart showing the number of each fruit type per person.

    The function creates a stacked bar chart where:
    - Each bar represents one person (Farrah, Fred, or Felicia)
    - Each bar is divided into segments representing different fruit types
    - Fruit types are stacked from bottom to top:
    apples, bananas, oranges, peaches
    - Each fruit type has a specific color:
      * Apples: red
      * Bananas: yellow
      * Oranges: orange (#ff8000)
      * Peaches: peach (#ffe5b4)

    The fruit matrix is 4x3:
    - Rows represent fruit types (apples, bananas, oranges, peaches)
    - Columns represent people (Farrah, Fred, Felicia)

    Returns:
        None: Displays the plot using plt.show()
    """
    np.random.seed(5)

    fruit = np.random.randint(0, 20, (4, 3))

    plt.figure(figsize=(6.4, 4.8))

    persons = ['Farrah', 'Fred', 'Felicia']

    fruits = ['apples', 'bananas', 'oranges', 'peaches']

    colors = ['red', 'yellow', '#ff8000', '#ffe5b4']

    x = np.arange(len(persons))

    width = 0.5

    bottom = np.zeros(len(persons))

    for i in range(len(fruits)):
        plt.bar(x,
                fruit[i],
                width,
                bottom=bottom,
                label=fruits[i],
                color=colors[i])

        bottom += fruit[i]

    plt.ylabel('Quantity of Fruit')

    plt.title('Number of Fruit per Person')

    plt.xticks(x, persons)

    plt.yticks(np.arange(0, 81, 10))

    plt.ylim(0, 80)

    plt.legend(loc='upper right')

    plt.show()
