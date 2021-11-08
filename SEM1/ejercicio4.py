#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 19:17:47 2021

@author: angel
"""


##################################################################
# Lectura de datos
precio = input ("Introduzca el precio del producto: ")
precio = float(precio)

cantidad = input ("Introduzca la cantidad dada por el cliente: ")
cantidad = float(cantidad)

####################################################################

# Calculamos la vuelta que tenemos que dar
vuelta = cantidad - precio;

# Calculamos las monedas de un euro que podemos usar como maximo
# y lo que nos queda por devolverle al cliente
moneda1euro = int(vuelta // 1)
vuelta = (vuelta - (moneda1euro * 1))

# Calculamos las monedas de 50cent que podemos usar como maximo
# y lo que nos queda por devolverle al cliente
moneda50cent = int (vuelta // 0.5)
vuelta = vuelta - (moneda50cent * 0.5)

# Calculamos las monedas de 10cent que podemos usar como maximo
# y lo que nos queda por devolverle al cliente
moneda10cent = int (vuelta // 0.1)
vuelta = vuelta - (moneda10cent * 0.1)

# Calculamos las monedas de 1cent que podemos usar como maximo
# usamos round porquee puede haber errores de calculo debido a la representacion
# en coma flotante
moneda1cent = round(vuelta / 0.01)

print("La vuelta es {} monedas de 1 euro, {} de 50cent, {} de 10cent y {} de 1cent: ".format(moneda1euro,moneda50cent,moneda10cent,moneda1cent))