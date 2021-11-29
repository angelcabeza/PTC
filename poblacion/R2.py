#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Fichero que realiza las tareas que se piden en el apartado R2.
    
    R2: Usando el listado de comunidades autónomas que podemos obtener del fichero
    comunidadesAutonomas.html, así como de las provincias de cada comunidad 
    autónoma que podemos obtener de comunidadAutonoma-Provincia.html 
    y los datos de poblacionProvinciasHM2010-17.csv, hay que generar una tabla
    con los valores de población de cada comunidad autónoma en cada año de 2010
    a 2017, indicando también los valores desagregados por sexos
"""


import funciones
import numpy as np

def pobMujerHombre(fichero="entradas/comunidadesAutonomas.htm"):
    """
        Función para calcular la población total de hombres 
        y de mujeres de las comunidades
    """
    
    # Leo las comunidades y las provincias
    comunidades = funciones.leerComunidades(fichero)
    provincias = funciones.leerProvincias("entradas/comunidadAutonoma-Provincia.htm")
    
    
    # Esta es la cabecera del fichro csv limpio que voy a crear al llamar a convertCSVtoDict
    cabecera = "Provincia;T2017;T2016;T2015;T2014;T2013;T2012;T2011;T2010;H2017;H2016;H2015;H2014;H2013;H2012;H2011;H2010;M2017;M2016;M2015;M2014;M2013;M2012;M2011;M2010;"
    
    # Me creo un diccionario a partir del CSV
    dictPobProvincias = funciones.convertCSVtoDict("entradas/poblacionProvinciasHM2010-17.csv", ";","Total Nacional","Notas",cabecera)
    
    # Diccionario donde guardare la solución
    result = {}
    
    # Para comunidad creo 28 valores (8 años * 3 (total,mujeres,hombres)) de 0
    for comunidad in comunidades:
        result[comunidad] = np.zeros( (24,), np.float)
            
    
    # Para cada provincia
    for key in dictPobProvincias:
        # Me salto lo que no nos interesa
        if key != "Provincia" and key != "Total Nacional":
            # Saco la comunidad
            comunidad = provincias[key]
            
            # Si la comunidad está en las comunidades que hemos extraido antes
            # añado el valor de la población de la provincia
            if comunidad in comunidades:
                result[comunidad] += dictPobProvincias[key].astype(np.float64)
                
    return result

def main():
    # Calculo la solución
    result = pobMujerHombre()
    
    # Esta será la cabecera de la tabla
    cabecera = ["2017", "2016", "2015", "2014", "2013", "2012", "2011","2010","2017", "2016", "2015", "2014", "2013", "2012", "2011","2010","2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010"]

    # Convierto la solución en una tabla HTML
    funciones.convertDictToHTMLTable("resultados/poblacionComAutonomas.html", result, "Población por provincias y sexo", "R2: Población por provincias y sexo", cabecera,"estilos.css", ["Total","Hombres","Mujeres"],"8")
    
    
if __name__ == "__main__":
    main()