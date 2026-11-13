# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 20:24:36 2026

@author: marku
"""

#Oppgave 6
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return - x**2 - 1

xa = np.linspace(-10, 10, 200)

ya = f(xa)

plt.plot(xa, ya)
plt.show()