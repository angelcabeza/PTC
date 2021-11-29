#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 12:46:40 2021

@author: angel
"""


# vemos si el string precio corresponde a un string de euros y céntimos
def validarCentimos(precio):
    precioLista=precio.split(".")
    if len(precioLista)==1 or (len(precioLista) >1 and len(precioLista[1])<3):
        validacion=True
    else:
        validacion=False
    
    return validacion

def leerFLoatMax2Decimales(cadena):
    esCorrecto = False
    
    num_intentos = 0
    while (not esCorrecto):
        try:
            numerostring = input(cadena)
            numero = float(numerostring)
            assert numero > 0, "El numero debe ser mayor a cero y ha indicado {}".format(numero)
            assert validarCentimos(numerostring), "El precio debe tener formato euros, max. 2 decimales"
            esCorrecto = True
        except ValueError:
            print ("Debe ingresar un número float con decimales.")
            num_intentos+=1
        except AssertionError as error:
            print(error)
            num_intentos+=1
            
    return numero,num_intentos


def leerAnios():
    esCorrecto = False
    
    num_intentos = 0
    while (not esCorrecto):
        try:
            numerostring = input("Introduzca los años")
            numero = int(numerostring)
            assert numero > 0 , "El numero debe ser mayor a cero y ha indicado {}".format(numero)
            esCorrecto = True
        except ValueError:
            print ("Debe ingresar un número entero.")
            num_intentos+=1
        except AssertionError as error:
            print(error)
            num_intentos+=1
            
    return numero,num_intentos


if __name__=="__main__":
    nombreEstudiante="Ángel Cabeza Martín"
    capital,intentos1=leerFLoatMax2Decimales("Dime capital inicial con 2 decimales máximo: ")
    entradasCorrectas = 1
    interes,intentos2=leerFLoatMax2Decimales("Dime interés anual con 2 decimales máximo: ")
    entradasCorrectas+=1
    anios,intentos3=leerAnios()
    entradasCorrectas+=1
    
    entradasIncorrectas = intentos1 + intentos2 + intentos3
    print("Fin del programa de validación de euros")
    print("Nombre estudiante: ",nombreEstudiante)
    print("Entradas correctas: ",entradasCorrectas," incorrectas: ",entradasIncorrectas)
