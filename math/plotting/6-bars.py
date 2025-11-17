#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def bars():
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4,3))
    plt.figure(figsize=(6.4, 4.8))

    persons = ['Farrah', 'Fred', 'Felicia']
    fruits = ['apples', 'bananas', 'oranges', 'peaches']
    colors = ['red', 'yellow', '#ff8000', '#ffe5b4']
    
    x = np.arange(len(persons))
    width = 0.5
    
    bottom = np.zeros(len(persons))
    
    for i in range(len(fruits)):
        plt.bar(x, fruit[i], width, bottom=bottom, label=fruits[i], color=colors[i])
        bottom += fruit[i]
    
    plt.xlabel('Person')
    plt.ylabel('Quantity of Fruit')
    plt.title('Number of Fruit per Person')
    plt.xticks(x, persons)
    plt.yticks(np.arange(0, 81, 10))
    plt.ylim(0, 80)
    plt.legend()
    plt.show()
