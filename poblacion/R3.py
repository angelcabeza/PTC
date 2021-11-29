#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Fichero que realiza las tareas que se piden en el apartado R3.
    
    R3: Generar un gráfico de columnas que indique la población de hombres y
    mujeres en el año 2017
"""


import funciones
import R2
import matplotlib.pyplot as plt
import numpy as np

def calcularNComunidadesMasPobladas(fichero, N = 10):
    """
        Función que calcula las N comunidades más pobladas
        dado un fichero
    """
    
    # Calculo la población dividida en mujeres y hombres
    # usando la función del ejercicio anterior
    poblacionComunidades = R2.pobMujerHombre()
    
    # Diccionario con la media de poblacion de las comunidades
    dictNPobladas = {}
    
    # Para cada comunidad (clave) calculamos la media
    # de las 8 primeras columnas que corresponden al total 
    for key in poblacionComunidades:
        media = 0
        
        for i in range(8):
            media += poblacionComunidades[key][i]
            
        media /= 8
        
        dictNPobladas[key] = media
    
    # Ordenamos el diccionario de mayor a menor media
    comunidadesOrdenadas = sorted(dictNPobladas.items(), key=lambda x: x[1], reverse=True)
    
    
    # lista donde guardo 
    mediaMasPobladas = []
    
    # AÑado a la lista las N mas pobladas (solo sus keys)
    for i in range(N):
        mediaMasPobladas.append(comunidadesOrdenadas[i][0])

    # Devuelvo el diccionario del ejercicio R2 y la lista con las
    # comunidades más pobladas
    return poblacionComunidades, mediaMasPobladas


def graficoComunidadesMasPobladas(fichero, fichero_salida):
    """
        Función para crear un gráfico de barras con la población de hombres
        y mujeres de un fichero.
    """
    # Sacamos las comunidades mas pobladas
    dictPob, masPobladas = calcularNComunidadesMasPobladas(fichero)

    # Creo valores del [0 a len(masPobladas)) que en este caso
    # será del 0 al 9.
    indices = np.arange( len(masPobladas) )


    pob_hombres = []
    pob_mujeres = []

    # guardamos la información que se nos pide
    for comunidad in masPobladas:
        # Sabemos que la población de hombres en 2017 está
        # en la columna 9 (indice 8) y la de las mujeres en 2017
        # está en la 17 (indic 16)
        pob_hombres.append(dictPob[comunidad][8])
        pob_mujeres.append(dictPob[comunidad][16])


    # hacemos el grafico
    ancho_barra = 0.3

    # Añadimos el titulo y la layenda de los ejes
    plt.clf()
    plt.title("R3: Población por hombres y mujeres en 2017\n de las 10 comunidades más pobladas", fontsize = 10)
    plt.xlabel("Comunidades")
    plt.ylabel("Población en 2017")


    # dibujamos la poblacion de hombres y mujeres
    plt.bar(indices, pob_hombres, ancho_barra, color="red", label="Hombres")
    # Le sumo el ancho de la barra para que se vea la barra y no quede en la misma
    # posicion que la de los hombres
    plt.bar(indices + ancho_barra, pob_mujeres, ancho_barra, color="blue", label="Mujeres")

    
    # hacemos que en la leyenda salga el nombre de la comunidad y su código y que
    # cada comunidad se divida en dos barras una para hombres y otra para mujeres
    plt.xticks(indices + ancho_barra/2, masPobladas, rotation = 30, ha="right",fontsize = 4)
    plt.legend()

    # guardamos la figura en la ruta dada
    plt.savefig(fichero_salida, dpi = 600)
    
def main():
    
    # Creamos el gráfico de barras
    graficoComunidadesMasPobladas("entradas/comunidadesAutonomas.htm", "imagenes/R3.png")

    # Creamos el fichero del ejercicio R2
    # porque el gráfico se inserta aqui
    R2.main()

    # Insertamos la imagen en el fichero de R2
    funciones.insertarImagenHTML("resultados/poblacionComAutonomas.html", "../imagenes/R3.png")



if __name__ == "__main__":
    main()
    