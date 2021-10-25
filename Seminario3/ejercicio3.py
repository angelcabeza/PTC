#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 09:55:11 2021

@author: angel
"""


def mayusculas_minusculas(lista):
    """
    Funcion para intercambiar las mayusculas por minusculas y viceversa de una
    cadena
    """

    solucion = ""

    # para cada letra de la palabra
    for letra in palabra:
        # cambiamos de mayuscula a minuscula
        # la diferencia entre mayusculas y minusculas es de 32, como es el
        # quito bit (2^5), aplicando la operacion XOR de la letra con 32,
        # intercambiamos entre 0 y 1 ese bit.
        # primero tenemos que pasarlo el caracter a su representacion en entero
        # aplicamos la operacion, y pasamos el entero a su representacion como
        # caracter
        if letra != ' ' or letra != '\n' or letra != '\t':
            solucion += chr(ord(letra) ^ 32)

    return solucion


# introducimos los datos
palabra = input("Introduce una palabra: ")

# probamos la funcion
solucion = mayusculas_minusculas(palabra)

print("La cadena original era: {}, tras aplicar la operacion es: {}".format(palabra, solucion))

solucion = palabra.swapcase()

print("\nUtilizando el metodo de str:")
print("La cadena original era: {}, tras aplicar la operacion es: {}".format(palabra, solucion))
