#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def calcularmax (x1,x2,x3):
    maximo = x1
    epsilon = 0.0001
    
    if ( (x2 - maximo) > epsilon):
        maximo = x2
        
    if ( (x3 - maximo) > epsilon):
        maximo = x3

    return maximo


def calcularminimo (x1,x2,x3):
    minimo = x1
    epsilon = 0.0001
    
    if ( (x2 - minimo) < epsilon):
        minimo = x2
        
    if ( (x3 - minimo) < epsilon):
        minimo = x3
        
    return minimo
    

##########################################################3
# Lectura de datos
x1 = input("Introduzca el primer numero: ")
x1 = float(x1)

x2 = input("Introduzca el segundo numero: ")
x2 = float(x2)

x3 = input("Introduzca el tercer numero: ")
x3 = float(x3)
##########################################################

maximo = calcularmax(x1,x2,x3)
minimo = calcularminimo(x1,x2,x3)

print("El maximo es: {} y el minimo es: {}".format(maximo,minimo))