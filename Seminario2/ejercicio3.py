#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# Lectura de datos
cateto1 = input("Introduzca el primer cateto: ")
cateto1 = float(cateto1)

cateto2 = input("Introduzca el segundo cateto: ")
cateto2 = float(cateto2)

# Calculo la hipotenusa
hipotenusa = math.sqrt( (cateto1**2) + (cateto2**2) )

# Muestro la hipotenusa por pantalla
print("La hipotenusa es: ",hipotenusa)