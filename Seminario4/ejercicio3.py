#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: angel

Crear una lista con los valores de 1 a N y calcular el máximo y el mínimo
de esa lista

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


def calcula_maximo_minimo (lista):
    """
        Función que devuelve el máximo y el mínimio de una lista
        y sus posiciones
    """
    
    minimo = lista[0]
    maximo = lista[0]
    pos_max = 0
    pos_min = 0
    
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
            pos_max = i
            
        if lista[i] < minimo:
            minimo = lista[i]
            pos_min = i
            
    
    return maximo,minimo,pos_max,pos_min

# Pedimos al usuario que nos indique el tamaño de la lista
tam_lista = input("Introduzca el tamaño de la lista: ")
tam_lista = int(tam_lista)

# Creamos la lista
lista = crear_lista(tam_lista)

# Calculamos el minimo el máximo y sus posiciones
maximo,minimo,pos_max,pos_min = calcula_maximo_minimo(lista)

print("El maximo de la lista es {} y su posicion es {}".format(maximo,pos_max))

print ("El minimo de la lista es {} y su posicion es {}".format(minimo,pos_min))

############################################################################
# Version 2

maximo = max(lista)
minimo = min(lista)

pos_max = lista.index(maximo)
pos_min = lista.index(minimo)

print("El maximo de la lista es {} y su posicion es {}".format(maximo,pos_max))

print ("El minimo de la lista es {} y su posicion es {}".format(minimo,pos_min))
