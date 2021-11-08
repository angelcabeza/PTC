#!/usr/bin/env python3
# -*- coding: utf-8 -*-

############################################################################
# Lectura de datos
precio_bruto = input("Introduce el precio bruto del vehiculo: ")
precio_bruto = float(precio_bruto)

ganancia_vendedor = input("Introduce el porcentaje de ganancia del vendedor (20 para indicar 20%): ")
ganancia_vendedor = float(ganancia_vendedor)/100

iva = input("Introduce el porcentaje de IVA a aplicar (ej: 10 para 10%)")
iva = float(iva)/100

#############################################################################

# Calculamos el precio base
precio_base = precio_bruto + (precio_bruto * ganancia_vendedor)

# Calculamos el precio final
precio_final = precio_base + (precio_base * iva)

print ("El precio final de su vehiculo ha sido de {} euros.".format(precio_final))