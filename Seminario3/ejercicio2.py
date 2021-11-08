#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 12:23:10 2021

@author: angel
"""


cadena = "Hola Mundoooo"
cadena2 = cadena
cadena3 = cadena

i = 0
while (i < len(cadena)):
    if cadena[i] == 'o':
        cadena = cadena[0:i] + cadena[i+1:]
    else:
        i += 1

print(cadena)


j = 0
for letra in cadena2:
    if letra == 'o':
        cadena2 = cadena2[0:j] + cadena2[j+1:]
    else:
        j += 1
        
print(cadena2)


for k in range(len(cadena3)):
    if cadena3[k] == 'o':
        cadena3 = cadena3[0:k] + cadena3[k+1:]
        
print (cadena3)