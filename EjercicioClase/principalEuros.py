#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:22:29 2021

@author: angel
"""

import financiacion

print("Introduzca una cantidad de dinero en euros: ")
euros = financiacion.leerFloat2decimales()

print("Introduzca un interes anual en tanto por ciento: ")
interes = financiacion.leerFloat2decimales()

print("Introduzca el numero de años: ")
anios = financiacion.leerInt()

for i in range (0,anios):
    euros = financiacion.calcularCapitalAnual(euros, interes)


print("El capital acumulado durante {} años es de {}".format(anios,euros))