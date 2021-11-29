#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Fichero que realiza las tareas que se piden en el apartado R1.
    
    R1: Calcular la variación de la población por provincias desde el año 2011 a 2017 en términos
    absolutos y relativos generando la página web 1 (que debe llamarse variacionProvincias.html)
"""


import funciones


def calcularVariacion():
    """
        Función para calcular la variación de la población por provincias
        desde el año 2011 a 2017 en términos absolutos y relativos de un fichero
    """
    
    # Esta es la cabecera del nuevo fichero que generaremos
    cabecera = "Provincia;T2017;T2016;T2015;T2014;T2013;T2012;T2011;T2010;H2017;H2016;H2015;H2014;H2013;H2012;H2011;H2010;M2017;M2016;M2015;M2014;M2013;M2012;M2011;M2010;"

    # Convertimos el fichero CSV a diccionario
    dictPobProvincias = funciones.convertCSVtoDict('entradas/poblacionProvinciasHM2010-17.csv', ";", "Total Nacional", "Notas", cabecera)
    
    # Diccionario que contendrá la variación relativa
    dictSol = {}
    
    # Para cada clave en el diccionario que hemos leido
    for clave in dictPobProvincias:
        # NOs saltamos la clave Provincia que no contiene informacion
        if clave != "Provincia":
            # Guardamos todos los valores de la provincia
            datos = dictPobProvincias[clave]
            
            # Lista donde guardaremos las variaciones tanto absolutas como relativas
            variaciones = []
            
            # Calculamos la variación absoluta
            for i in range(7):
                var_absoluta = float(datos[i]) - float(datos[i+1])
                variaciones.append(round(var_absoluta,2))
            
            # Calculamos la variación relativa
            for i in range(7):
                var_relativa = ( float(variaciones[i]) / float(datos[i+1])) * 100.0
                variaciones.append(round(var_relativa,2))
            
            # Almacenamos las variaciones en la provincia
            dictSol[clave] = variaciones
           
    return dictSol
    
def main():
    
    # Calculamos la variación de la población del archivo correspondiente
    dictSol = calcularVariacion()
    
    # Esta será la cabecera de la tabla que generaremos    
    cabecera = ["2017", "2016", "2015", "2014", "2013", "2012", "2011","2017", "2016", "2015", "2014", "2013", "2012", "2011"]
    
    # Convertimos el diccionario que hemos obtenido en una tabla html
    funciones.convertDictToHTMLTable("resultados/variacionProvincias.html",dictSol,"R1: Variaciones poblacion", "R1: Variación anual en la población por provincias", cabecera, "estilos.css",["Var Absoluta", "Var relativa"],"7")


if __name__ == "__main__":
    main()