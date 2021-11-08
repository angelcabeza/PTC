#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 14:36:36 2021

@author: angel
"""


radiacion_solar = input("Introduzca la radiacion solar media por dia (Kwh/m2): ")
radiacion_solar = float(radiacion_solar)

energia_producir = 1000
rendimiento = 0.17
tamanio = 1.6

energia_1_panel = (radiacion_solar * tamanio) * rendimiento

paneles = int(energia_producir // energia_1_panel)

print("Para generar al menos 1000Kwh, necesitas {} paneles".format(paneles))