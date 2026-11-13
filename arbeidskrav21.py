# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 17:02:42 2026

@author: marku
"""

#Oppgave 3
import numpy as np

v_grad = float(input('Skriv inn gradtallet:'))
v_rad = v_grad*np.pi/180

print('Vinkelen', v_grad,'°','er lik', v_rad, 'radianer' )
