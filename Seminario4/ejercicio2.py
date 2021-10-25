#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Angel Cabeza Martin

Crear una lista con valores de 1 a N y devolver el valor de los números 
impares de la lista
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


def valores_impares(lista):
    """
        Devuelve una lista con los valores impares de la lista dada
        como argumento
    """
    
    lista_sol = []
    num_impares = 0
    
    for elemento in lista:
        if elemento % 2 != 0:
            lista_sol.append(elemento)
            num_impares += 1
    
    return lista_sol, num_impares



# Pedimos al usuario que nos indique el tamaño de la lista
tam_lista = input("Introduzca el tamaño de la lista: ")
tam_lista = int(tam_lista)

# Creamos la lista
lista = crear_lista(tam_lista)

# Calculamos la lista con los numeros impares

lista_impares, num_impares = valores_impares(lista)

print("Hay {} numeros impares y son {}".format(num_impares,lista_impares))

