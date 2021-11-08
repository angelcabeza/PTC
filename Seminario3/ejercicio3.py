#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 09:55:11 2021

@author: angel

Crear una función que intercambie las mayusuclas por minusculas y viceversa
"""


def mayusculas_minusculas(palabra):
    """
    Funcion para intercambiar las mayusculas por minusculas y viceversa de una
    cadena
    """

    solucion = ""

    # para cada letra de la palabra
    for letra in palabra:
        # cambiamos de mayuscula a minuscula
        # la diferencia entre mayusculas y minusculas en binario se encuentra
        # en el sexto bit, aplicando la operacion XOR de la letra con 32 (0100000),
        # intercambiamos entre 0 y 1 ese bit.
        # primero tenemos que pasarlo el caracter a su representacion en entero
        # con ord, aplicamos la operacion, y pasamos el entero a su representacion como
        # caracter con chr
        if letra != ' ' or letra != '\n' or letra != '\t':
            solucion += chr(ord(letra) ^ 32)

    return solucion


palabra = input("Introduce una palabra: ")

solucion = mayusculas_minusculas(palabra)

print("La cadena original era: {}, tras aplicar la operacion es: {}".format(palabra, solucion))


print("\nUtilizando el metodo de str:")
print("La cadena original era: {}, tras aplicar la operacion es: {}".format(palabra, solucion))
