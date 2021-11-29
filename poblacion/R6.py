#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Fichero que realiza las tareas que se piden en el apartado R6.
    
    R6: Implementar un programa que compare los datos de variación de población
    de 2011 a 2017 (absoluta y relativa) de ambos ficheros para comprobar que
    son los mismos valores en cada caso. Despúes usar el fichero comunidadesAutonomasBis.html
    para generar una versión Bis de las páginas web 2 (ver R2 y R3) y web 3 (ver R4 y R5)
    con sus respectivos gráficos debiendo llamarse poblacionComAutonomasBis.html
    y variacionComAutonomasBis.html respectivamente.
"""

import R1
import R2
import R3
import R4
import R5
import funciones
import numpy as np


def main():
    
    # Sacamos las claves (el código de la comunidad autónoma y el nombre de esta)
    claves = funciones.buscarEtiqueta("entradas/variacionProvincias2011-17.htm", "th")

    # Nos saltamos la información que no nos interesa
    inicio = np.where( claves == "Total Nacional")[0][0]
    claves = claves[inicio:]
    
    # Sacamos todos los valores
    valores = funciones.buscarEtiqueta("entradas/variacionProvincias2011-17.htm", "td")
    
    
    # Quitamos los . porque en la tabla que leemos los usan para
    # denotar que han pasado 3 cifras y no para los decimales y las
    # , las transformamos en .
    for i in range(valores.shape[0]):
        valores[i] = valores[i].replace(".","")
        valores[i] = valores[i].replace(",",".")
        
    
    # Diccionario dodne guardaremos las claves y sus respectivos valores
    dictValores = {}
    
    i = 0
    # Por cada clave meteremos los 14 valores que les corresponden
    # (14 valores porque cada comunidad tiene 14 columnas)
    for key in claves:
        dictValores[key] = np.array(valores[i:i+14], np.float64)
        i+=14
    
    # Calculamos con nuestra función la variación de la poblacion
    # (debe ser igual al diccionario que acabmos de generar anteriormente)
    dictR1 = R1.calcularVariacion()
    
    # Convertimos los valores en arrays de numpy
    # y almacenamos las claves en una lista
    clavesR1 = []
    for key in dictR1:
        dictR1[key] = np.array(dictR1[key], np.float64)
        clavesR1.append(key)


    # Recorremos los diccionarios y comparamos los arrays con numpy
    # Y si algun array no es igual a su par salimos del bucle y lo notificamos
    iguales = True
    i = 0
    while i < len(clavesR1) and iguales:
        comparacion = dictR1[clavesR1[i]] == dictValores[clavesR1[i]]
        if not comparacion.all():
            iguales = False
                      
        i+=1
        
    
    if iguales:
        print("Todos los valores son iguales")
    else:
        print("NO todos los valores son iguales")
        
    
    ###########################################################################
    # Generamos los archivos BIS
        
    
    # Sacamos la población total de hombres y de mujeres del fichero
    dictR2bis = R2.pobMujerHombre("entradas/comunidadesAutonomasBis.htm")
    
    # Esta es la cabecera del archivo
    cabecera = ["2017","2016","2015","2014","2011","2010",
                "2017","2016","2015","2014","2011","2010",
                "2017","2016","2015","2014","2011","2010"]
    
    # Lo convertimos a tabla HTML
    funciones.convertDictToHTMLTable("resultados/poblacionComAutonomasBis.html", dictR2bis,
                                         "Población por provincias y sexo BIS", 
                                         "R6: Población por provincias y sexo BIS", cabecera, 
                                         "estilos.css", ["Total","Hombres","Mujeres"],"8")
    
    # Calculamos el gráfico de este archivo
    R3.graficoComunidadesMasPobladas("entradas/comunidadesAutonomasBis.htm","imagenes/R3_BIS.png")
    
    # Lo insertamos
    funciones.insertarImagenHTML("resultados/poblacionComAutonomasBis.html", "../imagenes/R3_BIS.png")

    # Calculamos la variación de la población del ejercicio 4
    dictR4 = R4.calcularVariacion("entradas/comunidadesAutonomasBis.htm")

    # Esta es la cabecera del archivo
    cabecera = ["2017", "2016", "2015", "2014", "2013", "2012", "2011",
                "2017", "2016", "2015", "2014", "2013", "2012", "2011",
                "2017", "2016", "2015", "2014", "2013", "2012", "2011",
                "2017", "2016", "2015", "2014", "2013", "2012", "2011",
                "2017", "2016", "2015", "2014", "2013", "2012", "2011",
                "2017", "2016", "2015", "2014", "2013", "2012", "2011"]


    # Lo convertimos a tabla HTML
    funciones.convertDictToHTMLTable("resultados/variacionComAutonomasBis.html", dictR4,"Variaciones por comunidad", 
                                         "R6: Variaciones por comunidad (Total, Hombres, Mujeres)", cabecera, 
                                         "estilos.css", ["Var absoluta Total","Var absoluta Hombre", 
                                         "Var absoluta Mujer","Var relativa Total", 
                                         "Var relativa Hombres","Var relativa Mujeres"],"7")
    
    # Y le agregamos el gráfico de lineas correspondiente
    R5.grafLineaPobTotal("entradas/comunidadesAutonomasBis.htm","imagenes/R5_BIS.png")
    funciones.insertarImagenHTML("resultados/variacionComAutonomasBis.html", "../imagenes/R5_BIS.png")
    
    
if __name__ == "__main__":
    main()