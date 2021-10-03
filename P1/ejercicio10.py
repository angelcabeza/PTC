#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 14:44:08 2021

@author: angel
"""


cantidad_original = 80

cantidad_obtener = input("Introduzca la cantidad que quiera obtener (en cm3): ")
cantidad_obtener = float(cantidad_obtener)

concentracion = input("Introduzca el porcentaje de concentracion (< 80%): ")
concentracion = float(concentracion)

resultado = (cantidad_obtener * concentracion) / cantidad_original

print("Necesitas {} cm3 para obtener lox {} cm3 al {} de concentracion".format(resultado,cantidad_obtener,concentracion))