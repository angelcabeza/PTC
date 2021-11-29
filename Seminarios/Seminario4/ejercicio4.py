#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

"""
@author: angel

Generar dos listas de tamaño N y M respectivamente con valores aleatorios
y devolver una tercera lista con los valores de las dos anteriores ordenados
de manera ascendente
"""

def rellena_lista(tam_lista):
    """
        Crea una lista con el tamaño pasado por parámetros y la rellena con
        valores aleatorios del 1 al 10
    """
    lista = []
    
    for i in range(tam_lista):
        lista.append(random.randint(1,10))
        
    return lista


def combina_lista (lista1,lista2):
    """ 
        Crea una lista con los elementos de las dos listas pasados como
        argumentos
    """
    
    lista = lista1
    
    for elemento in lista2:
        lista.append(elemento)
        
    return lista


def estaRepetido (lista,elemento):
    """ 
        Devuelve si un elemento esta repetido en una lista o no
    """
    
    encontrado = False
    
    cont = 0
    while not encontrado and cont < len(lista):
        if (elemento == lista[cont]):
            encontrado = True
                
        cont += 1
        
    return encontrado
    
def eliminaRepetidos (lista):
    """
        Devuelve una lista con los elementos SIN repetir de una lista
        pasada como parametro
    """
    lista_res = []
    
    for i in range(len(lista)):
        if not estaRepetido(lista_res, lista[i]):
            lista_res.append(lista[i])
            
    return lista_res


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

def ordena_ascendente(lista):
    """ 
        Devuelve una lista con los elementos ordenados de manera ascendente
        de la lista pasada como parametro
    """
    
    lista_ordenar= lista.copy()
    lista_res = []
    
    for i in range(len(lista_ordenar)):
        _,minimo,_,pos_min = calcula_maximo_minimo(lista_ordenar)
        lista_res.append(minimo)
        lista_ordenar.pop(pos_min)
        
    return lista_res


# Pedimos al usuario que nos indique el tamaño de la lista
tam_lista1 = input("Introduzca el tamaño de la lista: ")
tam_lista1 = int(tam_lista1)

# Pedimos al usuario que nos indique el tamaño de la lista
tam_lista2 = input("Introduzca el tamaño de la lista: ")
tam_lista2 = int(tam_lista2)

# Creamos las listas con valores aleatorios
lista1 = rellena_lista(tam_lista1)
lista2 = rellena_lista(tam_lista2)

print("La primera lista tiene los siguients valores: ",lista1)
print("La segunda lista tiene los siguientes valores",lista2)

lista3 = combina_lista(lista1, lista2)


lista3 = eliminaRepetidos(lista3)

lista3 = ordena_ascendente(lista3)

print("Los valores ordenados de menor a mayor de la lista1 y la lista2 son: ",lista3)


#######################################################################################
# Versión 2
lista1.extend(lista2)

lista1 = eliminaRepetidos(lista1)

print("Los valores ordenados de menor a mayor de la lista1 y la lista2 son (V2): ",sorted(lista1))