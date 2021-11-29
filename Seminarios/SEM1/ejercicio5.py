#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 15:12:47 2021

@author: angel
"""


def diferenciainstantes(h1,m1,s1,h2,m2,s2):
    #Pasamos a segundos ambos instantes
    seg_i1 = h1 * 3600 + m1 * 60 + s1
    seg_i2 = h2 * 3600 + m2 * 60 + s2
    
    dif_inst = abs(seg_i1 - seg_i2)
    
    h_dif = dif_inst // 3600
    m_dif = (dif_inst % 3600) // 60
    s_dif = (dif_inst % 3600) % 60
    
    return h_dif,m_dif,s_dif
    
    
horas1 = input("Introduzca las horas del primer instante: ")
horas1 = int(horas1)

minutos1 = input("Introduzca los minutos del primer instante: ")
minutos1 = int(minutos1)

segundos1 = input("Introduzca los segundos del primer instante: ")
segundos1 = int(segundos1)


horas2 = input("Introduzca las horas del primer instante: ")
horas2 = int(horas2)

minutos2 = input("Introduzca los minutos del primer instante: ")
minutos2 = int(minutos2)

segundos2 = input("Introduzca los segundos del primer instante: ")
segundos2 = int(segundos2)


h_dif,min_dif,seg_dif = diferenciainstantes(horas1,minutos1,segundos1,horas2,minutos2,segundos2)


print("La diferencia es {}h:{}m:{}s".format(h_dif,min_dif,seg_dif))