# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:39:21 2019

@author: Eugenio
Validación de entrada a formato de euros sin usar expresiones regulares
Contamos las entradas correctas e incorrectas para informar al finalizar
el programa
"""


# vemos si el string precio corresponde a un string de euros y céntimos
def validarCentimos(precio):
    precioLista=precio.split(".")
    if len(precioLista)==1 or (len(precioLista) >1 and len(precioLista[1])<3):
        validacion=True
    else:
        validacion=False
    
    return validacion

    
    
##Main    


seguirPidiendo=0
numeroVeces=4 # pedir 4 valores correctos
entradasCorrectas=0
entradasIncorrectas=0
nombreEstudiante="Manolo García"

while seguirPidiendo< numeroVeces:    
    try:
        precio=input("Dime precio con 2 decimales: ")
        valor=float(precio)
        assert valor>0, "El precio debe ser mayor a cero y ha indicado {}".format(valor)
        assert validarCentimos(precio), "El precio debe tener formato euros, max. 2 decimales"
        print("El precio es {} y es correcto". format(valor))
        seguirPidiendo=seguirPidiendo+1
        entradasCorrectas+=1
    except ValueError:
        print ("Debe ingresar un número float con decimales.")
        entradasIncorrectas+=1
    except AssertionError as error:
        print(error)
        entradasIncorrectas+=1
 
       
   
print("Fin del programa de validación de euros")
print("Nombre estudiante: ",nombreEstudiante)
print("Entradas correctas: ",entradasCorrectas," incorrectas: ",entradasIncorrectas)



  


