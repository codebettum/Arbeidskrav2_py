# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 17:22:21 2026

@author: marku
"""
#a
data = {
     "Norge":["Oslo", 0.634],
     "England":["London", 8.982],
     "Frankrike": ["Paris", 2.161],
     "Italia": ["Roma", 2.873]
     }
#b
land = input('Hvilket land vil du vite mer om?').capitalize()
hovedstad = data[land][0]
innbyggere  = data [land][1]
print(hovedstad, "er hovedstaden i", land, "og det er", innbyggere, "innbyggere i", hovedstad)

#c
nytt_land = input('Skriv inn navnet på et land:')
ny_hovedstad = input('Hva er hovedstaden i'" " + nytt_land + '?')
nye_innbyggere = input('Hvor mange innbyggere er det i'" " + ny_hovedstad + '?')

data[nytt_land] = [ny_hovedstad, nye_innbyggere]

print(data)




