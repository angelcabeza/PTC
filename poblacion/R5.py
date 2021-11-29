#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Fichero que realiza las tareas que se piden en el apartado R5.
    
    R5: Generar un gráfico de líneas que refleje la evolución de la población 
    total de cada comunidad autónoma desde el año 2010 a 2017.
"""


import funciones
import matplotlib.pyplot as plt
import R3
import R4

def grafLineaPobTotal(fichero,salida):
    """
        Función que calcula un gráfico de líneas con el 
        avance de la poblacion en las 10 comunidades más pobladas
    """
    
    # Sacamos la información de las comunidades y cuales son las 10
    # más pobladas
    pob, comunidades = R3.calcularNComunidadesMasPobladas(fichero)
    
    # Etiquetas en el eje x del gráfico
    x_labels = ["2010","2011","2012","2013","2014","2015","2016","2017"]
    
    # Creamos el titulo y las etiquetas de los ejes
    plt.clf()
    plt.title("Evolución de la poblacion", fontsize=14)
    plt.xlabel("Año")
    plt.ylabel("Población")
    
    # Para cada comunidad
    for key in comunidades:
        # Sacamos la población total de la comunidad
        pob_total = pob[key][:8]
        
        # Como lo queremos pintar de 2010 a 2017 le damos
        # la vuelta
        pob_total = pob_total[::-1]
        
        # Dibujamos el gráfico de lineas
        plt.plot(x_labels,pob_total, label=key)
        
    
    # Esta instrucción coloca la leyenda a la derecha
    # del gráfico para que se vea tanto el gráfico como
    # la leyenda
    plt.legend(bbox_to_anchor=(1,1), loc="upper left")
    
    # Guardamos la figura, como hemos colocado la leyenda
    # a la derecha del gráfico hay que utilizar el parámetro
    # bbox_inches para que guarde la leyenda y la imagen
    plt.savefig(salida, bbox_inches = "tight")
    
    
def main():
    # Creamos el gráfico de lineas
    grafLineaPobTotal("entradas/comunidadesAutonomasBis.htm","imagenes/R5.png")
    
    # Creamos el fichero del ejercicio R4 por si no estaba hecho
    R4.main()
    
    # E insertamos el gráfico creado en el fichero que corresponde
    funciones.insertarImagenHTML("resultados/variacionComAutonomas.html", "../imagenes/R5.png")
    

if __name__ == "__main__":
    main()