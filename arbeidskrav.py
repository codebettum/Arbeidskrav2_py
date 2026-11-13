# -*- coding: utf-8 -*-
"""
Arbeidskrav 2 PY1010
Markus H.B USN
12.11.2026

"""
#Oppgave 1
alder = int(input('Hvilket år er du født?'))
alder = 2024 - alder

print('Du blir', alder, 'i 2024')

#Oppgave 2
antall_elever = int(input('Skriv inn antall elever:'))
forbruk_pizza = 1/4
nødvendig_pizza = antall_elever*forbruk_pizza

print('Det må handles', nødvendig_pizza, 'til festen')
