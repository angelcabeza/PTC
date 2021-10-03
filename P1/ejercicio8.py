#!/usr/bin/env python3
# -*- coding: utf-8 -*-


porcen_alcohol = input("Introduzca el porcentaje de alcohol (ej: 10 para 10%): ")
porcen_alcohol = float(porcen_alcohol)

capacidad_tercio = 333
max_ingerir = 50

tercios = int( max_ingerir / (max_ingerir * (porcen_alcohol/100) ) )

print("Puedes tomarte {} tercios".format(tercios) )