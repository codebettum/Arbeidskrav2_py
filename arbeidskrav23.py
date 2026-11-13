# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 19:23:24 2026

@author: marku
"""

import numpy as np

def figur(a, b):
    r = a / 2
    omkrets_sirkel = r * np.pi
    areal_sirkel = np.pi * r**2 / 2
    areal_figur = a * b / 2 + areal_sirkel
    omkrets_figur = b + (np.sqrt(a**2 + b**2)) + omkrets_sirkel
    return areal_figur, omkrets_figur
    
a = int(input('skriv inn a:'))
b = int(input('skriv inn b:'))
    
areal_figur, omkrets_figur = figur(a, b)

print('Arealet av figuren er', areal_figur,)
print('Omkretsen av figuren er', omkrets_figur,)

