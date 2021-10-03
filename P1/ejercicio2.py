#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

#####################################################################
# Lectura de datos

x1 = input("Introduzca el primer numero: ")
x1 = float(x1)

x2 = input("Introduzca el segundo numero: ")
x2 = float(x2)

x3 = input("Introduzca el tercer numero: ")
x3 = float(x3)

#####################################################################

# Calculamos la media aritmética
media = (x1 + x2  + x3) / 3

# Calculamos la desviacion típica
desviacion = (x1 -media)**2 + (x2-media)**2 + (x3-media)**2

desviacion = math.sqrt( (desviacion/3) )

# Mostramos el resultado
print("Desviacion tipica: ", desviacion)
