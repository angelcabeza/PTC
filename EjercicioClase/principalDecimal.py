#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:35:57 2021

@author: angel
"""


import financiacion
import decimal 
from decimal import Decimal, getcontext

print("Introduzca una cantidad de dinero en euros: ")
euros = financiacion.leerFloat2decimales()

print("Introduzca un interes anual en tanto por ciento: ")
interes = financiacion.leerFloat2decimales()

print("Introduzca el numero de años: ")
anios = financiacion.leerInt()


getcontext().rounding = decimal.ROUND_HALF_UP


euros = Decimal(euros)
interes = Decimal(interes)

for i in range(0,anios):
    euros = euros + euros*(interes/100)
    euros = euros.quantize(Decimal("1.00"))    


print("El capital acumulado durante {} años es de {}".format(anios,euros))