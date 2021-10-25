#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 10:11:41 2021

@author: angel
"""


"""
Ejercicio 9:
Escribe una función elimina_vocales(palabra) que elimine todas las vocales
que aparecen en la palabra.
"""

def eliminar_letras(palabra, letra):
    """
    Funcion para, dada una palabra, eliminar las apariciones de una letra dada
    """

    solucion = ""

    # recorremos la palabra
    for caracter in palabra:
        # cada vez que encontramos un caracter que no coincide con la letra
        # lo añadimos a la solucion
        if letra != caracter:
            solucion += caracter

    return solucion

def elimina_vocales(palabra):

    vocales = "aeiouAEIOU"

    solucion = palabra

    # recorremos las vocales, eliminandolas de la solucion
    for vocal in vocales:
        solucion = eliminar_letras(solucion, vocal)

    return solucion

# introducimos los datos
palabra = input("Introduce una palabra: ")

sin_vocales = elimina_vocales(palabra)

print("La palabra introducida sin vocales es {}".format(sin_vocales))

print("\nUtilizando el metodo find de la clase str:")

vocales = "aeiouAEIOU"

sin_vocales = palabra

for letra in vocales:
    sin_vocales = sin_vocales.replace(letra, '')


print("La palabra introducida sin vocales es {}".format(sin_vocales))