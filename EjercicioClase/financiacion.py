#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Angel Cabeza Martin
"""


def leerFloat2decimales():
    seguirPidiendo = True
    
    while seguirPidiendo:
        decimal = input()
        if len(decimal)==0:
            print("Introduce un valor")
            esCorrecto=False
        else:
            esCorrecto=True
        
        for digito in decimal:
            if esCorrecto and (digito!=".") and (digito < '0' or digito > '9'):
                esCorrecto = False
                print ("Hay digitos no validos: ",digito)
                
        if esCorrecto:
            decimalLista=decimal.split(".")
            print(decimalLista)
            if (len(decimalLista) > 1):
                print("Hay decimales:",len(decimalLista[1]))
            if len(decimalLista)==1 or (len(decimalLista) > 1 and len(decimalLista[1]) < 3):
                seguirPidiendo=False
            else:
                print("Introduce solo con dos decimales")
                seguirPidiendo = True
                
    
    return (float(decimal))

def leerInt():
    seguirPidiendo = True
    
    while seguirPidiendo:
        entero = input()
        if len(entero) == 0:
            print("Introduce un valor")
            esCorrecto = False
        else:
            esCorrecto = True
            
        for digito in entero:
            if esCorrecto and (digito< '0' or digito > '9'):
                esCorrecto = False
                print ("Hay digitos no validos",digito)
                
        if esCorrecto:
            seguirPidiendo = False
            
        
    return (int(entero))

def redondear(numero, decimales):
    numero=numero*10**decimales
    numero=numero + 0.5
    numero=(int)(numero) # también se puede usar floor(numero)
    numero=numero/100
    
    return numero


def calcularCapitalAnual(capitalInicial, interes):
    
    capitalAnual = capitalInicial + capitalInicial*(interes/100)
    capitalAnual = redondear(capitalAnual,2)
    
    return capitalAnual
