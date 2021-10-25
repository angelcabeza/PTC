#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Lectura de datos
base = input("Introduzca la base del triangulo: ")
base = float(base)

altura = input("Introduzca la altura del triangulo: ")
altura = float(altura)

# Calculo el area
area = (base * altura) / 2

# Muestro el area
print("El area del triangulo es: ",area)