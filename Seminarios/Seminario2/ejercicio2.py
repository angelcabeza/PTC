#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# Lectura de datos
radio = input("Introduzca el radio de la circunferencia: ")
radio = float(radio)

# Calculo la longitud y el area de la circunferencia
longitud = 2 * math.pi * radio
area = math.pi * (radio**2)

# Muestro tanto el area como la longitud de la circunferencia por pantalla
print("La longitud de la circunferencia es {} y el area {}".format(longitud,area))