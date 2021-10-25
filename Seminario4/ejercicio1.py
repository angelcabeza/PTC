#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Angel Cabeza Martin

Crear una lista con valores entro de 1 a N y devolver la
suma de todos estos valores
"""

def crear_lista (tam_lista):
    """
        Función que crea una lista con tam = tam_lista y los valores
        del 1 a tam_lista
    """
    lista = []
    
    # Añadimos i + 1 porque el 0 no está incluido y N sí
    for i in range(tam_lista):
        lista.append(i+1)
        
    return lista


def suma_elementos(lista):
    """
    Funcion que devuelve la suma de todos los elementos
    de lista
    """

    suma = 0
    
    for elemento in lista:
        suma += elemento
        
    return suma

# Pedimos al usuario que nos indique el tamaño de la lista
tam_lista = input("Introduzca el tamaño de la lista: ")
tam_lista = int(tam_lista)

# Creamos la lista
lista = crear_lista(tam_lista)

# Hacemos la suma
suma = suma_elementos(lista)

print("La suma de todos los elementos es de: ",suma)

###################################################################
# Segunda versión

suma = sum(lista)

print("La suma de todos los elementos es de: ",suma)


