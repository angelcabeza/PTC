#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Fichero que realiza las tareas que se piden en el apartado R4.
    
    R4: Generar una página web 3 (fichero variacionComAutonomas.html) con una 
    tabla con la variación de población por comunidades autónomas desde el año
    2011 a 2017, indicando variación absoluta, relativa y desagregando dicha 
    información por sexos
"""


import R2
import numpy as np
import funciones

def calcularVariacion(fichero="entradas/comunidadesAutonomas.htm"):
    """
        Función para calcular la variación de las comunidades
        desde el año 2011 a 2017 en términos absolutos y relativos 
        desgranando la información en hombres mujeres y total
    """
    
    # Sacamos la información de la población de las comunidades
    dictPoblacionCom = R2.pobMujerHombre(fichero)
    
    # Diccionario donde almacenaremos el resultado
    res = {}
    
    # Para cada comunidad
    for key in dictPoblacionCom:
        # Creamos un array con 42 ceros ya que vamos a necesitar
        # 42 valores (la tabla tendrá 42 columnas)
        res[key] = np.zeros(42)
        
        # Este contador lo usamos para no restar la población 
        # de 2010 de hombres con la de 2017 de mujeres por ejemplo
        cont = 0
        
        # Var absoluta total pob
        for i in range(7):
            res[key][cont] = dictPoblacionCom[key][i] - dictPoblacionCom[key][i+1]
            cont += 1
        
        # Var absoluta pob hombres
        for i in range(8,15):
            res[key][cont] = dictPoblacionCom[key][i] - dictPoblacionCom[key][i+1]
            cont += 1
            
        # Var absoluta pob mujeres
        for i in range (16,23):
            res[key][cont] = dictPoblacionCom[key][i] - dictPoblacionCom[key][i+1]
            cont += 1
            
        # Var relativa pob total
        for i in range(7):
            res[key][cont] = (res[key][i] / res[key][i+1]) * 100
            cont += 1
        
        # Var relativa pob hombres
        for i in range(8,15):
            res[key][cont] = (res[key][i-1] / res[key][i+1]) * 100
            cont += 1
            
        # Var relativa pob mujeres
        for i in range(16,23):
            res[key][cont] = (res[key][i-2] / res[key][i+1]) * 100
            cont += 1
            
    
    return res


def main():
    
    # Calculamos el diccionario con los valores
    # de variacion según sexo
    res = calcularVariacion()
    
    # Esta será la cabecera de las 42 columnas
    cabecera = ["2017", "2016", "2015", "2014", "2013", "2012", "2011",
                "2017", "2016", "2015", "2014", "2013", "2012", "2011",
                "2017", "2016", "2015", "2014", "2013", "2012", "2011",
                "2017", "2016", "2015", "2014", "2013", "2012", "2011",
                "2017", "2016", "2015", "2014", "2013", "2012", "2011",
                "2017", "2016", "2015", "2014", "2013", "2012", "2011"]
    
    
    # LO convertimmos a tabla html
    funciones.convertDictToHTMLTable("resultados/variacionComAutonomas.html",res,"Variaciones por comunidad", "R4: Variaciones por comunidad (Total, Hombres, Mujeres)",
                                         cabecera,"estilos.css",["Var absoluta Total","Var absoluta Hombre", "Var absoluta Mujer","Var relativa Total", "Var relativa Hombres","Var relativa Mujeres"],"7")
    
    

if __name__ == "__main__":
    main()