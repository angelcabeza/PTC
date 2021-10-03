#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################################################
# Lectura de datos

horas = input ("Introduzca una cantidad de horas: ")
horas = int(horas)
minutos = input ("Introduzca una cantdidad de minutos: ")
minutos = int(minutos)
segundos = input ("Introduzca una cantidad de segundos: ")
segundos = int(segundos)
#################################################################


# Pasamos los segundos a minutos y se lo sumamos a los minutos
minutos += segundos // 60

# Nos quedamos con los segundos que sobren
segundos = segundos % 60

# Pasamos los minutos a horas y se lo sumamos a las horas
horas += minutos // 60

# Nos quedamos con los minutos que sobren
minutos = minutos % 60


print("Resultado: %d horas, %d minutos y %d segundos" %(horas,minutos,segundos))