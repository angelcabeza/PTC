#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Archivo con todas las funciones auxiliares que he utilizado
"""


import csv
import numpy as np
from bs4 import BeautifulSoup


def formatCSV (fichero, primero, ultimo, cabecera):
    """
        Función que dado un fichero, la palabra inicial, la final y una cabecera
        crea otro fichero fichero_limpio.csv con la información que nos interesa
        (solo la información de primero a último) y la cabecera.
    """
    
    # Abrimos el fichero que nos pasan como argumento
    ficheroInicial = open(fichero,"r",encoding="utf8")
    
    # Guardamos el contenido del fichero en una variable
    cadenaPob = ficheroInicial.read()
    
    
    # Si no nos han pasado ninguna palabra como inicio del fichero
    # este será el comienzo del fichero
    if (primero == None):
        inicioFichero = 0
    else:
        # si no, el inicio será la palabra que nos pasan
        inicioFichero = cadenaPob.find(primero)
        
    # Si no nos han pasado ninguna palabra como fin del fichero
    # este será el final del fichero
    if (ultimo == None):
        finFichero = len(cadenaPob)
    else:
        # si no, el final será la palabra que nos pasan
        finFichero = cadenaPob.find(ultimo)
    
    # El archivo final contendrá los caracteres que estén entre
    # el inicio del fichero y el fin del fichero que hemos calculado antes
    cadenaFinal = cadenaPob[inicioFichero:finFichero]
    
    # Separamos la extension (.*) del nombre del fichero que nos dan
    nombreFichero = fichero.split('.')
    
    # El fichero resultante tendrá como nombre el nombre del fichero junto con
    # _limpio.csv
    nombreFichero = nombreFichero[0] + '_limpio.csv'
    
    # Abrimos el nuevo fichero con permisos de escritura
    ficheroFinal = open(nombreFichero, "w",encoding="utf8")
    
    # Si no nos pasan cabecera escribimos el contenido sin ningún añadido
    if cabecera == None:
        ficheroFinal.write(cadenaFinal)
    else:
        # Si nos pasan cabecera la añadimos, metemos una linea en blanco e 
        # insertamos el contenido del fichero
        ficheroFinal.write(cabecera+'\n'+cadenaFinal)
    
    # Cerramos el archivo y lo devolvemos
    #ficheroFinal.close()
    
    return nombreFichero

def convertCSVtoDict(fichero,delimiter,primero=None,ultimo=None,cabecera=None):
    """
        Función que dado un fichero y un separador mete la información del fichero
        en un diccionario de python. Los atributos primero ultimo y cabecera
        sirven para filtrar la información que nos interesa
    """
    
    # Si se nos ha introducido algún campo de filtro de información, llamamos
    # a la función formatCSV para crear un nuevo fichero con la información que
    # nos interese
    if (primero != None or ultimo != None or cabecera != None ):
        fichero = formatCSV(fichero,primero,ultimo,cabecera)
    
    # Diccionario que devolveremos con todos los datos dentro
    diccionarioResultante = {}
    
    
    with open(fichero) as csvarchivo:
        # Vamos leyendo el fichero csv
        diccionario = csv.reader(csvarchivo, delimiter=delimiter)
        # Por cada linea dentro del fichero csv
        for regD in diccionario:
            # Su primer elemento será la clave del diccionario
            clave = regD[0]

            # El contenido de la clave será todo lo demás
            valor = np.array(regD[1:-1])

            # Guardamos la información sacada de la linea
            diccionarioResultante[clave] = valor
        
    return diccionarioResultante


def convertDictToHTMLTable(fichero,diccionario,titulo,descripcion,cabecera,estilo,leyenda,lon_leyenda):
    """
        Función que dado un diccionario crea una tabla HTML con la información
        del diccionario con el título, la descripción y el estilo que recibe
        como argumentos y en la ruta que se le indique
    """
    
    # Abrimos el fichero donde queremos insertar la tabla html
    fileTable = open(fichero,"w", encoding="utf8")
    
    # Creamos la cabecera del html con el titulo de la tabla, su estilo
    # y su descripcion
    tabla = """<!DOCTYPE html><html>
    <head><title>"""+titulo +"""</title>
    <link rel="stylesheet" href="""+ estilo + """ >
    <meta charset="utf8"></head>
    <body><h1>"""+ descripcion + """</h1>"""

    # Creamos la tabla y su primera fila
    tabla+= """<p><table>
    <tr>"""
    
    # Creamos la fila para indicar qué columnas son de variación absoluta
    # y qué columnas de variación relativa
    for i in range(0,len(leyenda)+1):
        if (i == 0):
            tabla+="<th rowspan=2>%s</th>" % ("")
        else:
            tabla+="<th colspan="+lon_leyenda+">%s</th>" % (leyenda[i-1])
    
    tabla+="</tr>"
    tabla+="""<tr>"""
    
    # Metemos en distintas columnas los valores de la cabecera
    for nomColumna in cabecera:
        tabla+="<th>%s</th>" % (nomColumna)
        
    # Cerramos la fila de la cabecera
    tabla+="</tr>"
    
    # Para cada key del diccionario
    for key in diccionario:
        # Creamos una fila cuyo valor será el contenido de la key
        tabla+="<tr><td>"+ key +"</td>"
        
        # Para cada valor asociado a esa key lo vamos metiendo en una columna
        for value in diccionario[key]:
            tabla+="<td>%.2f</td>" % (value)
            
        # Cerramos la fila de esa key
        tabla+="</tr>"
    
    # Cerramos la tabla el párrafo el body e indicamos el final del fichero html
    tabla+="</table></p></body></html>"
    
    # Escribimos la tabla en el fichero
    fileTable.write(tabla)
    
    # Cerramos el fichero
    fileTable.close()


def buscarEtiqueta(fichero, etiqueta):
    """
        Función que busca una etiqueta en un archivo html y devuelve
        todas las coincidencias
    """
    # Abrimos el fichero
    leerFich=open(fichero, 'r', encoding="utf8")

    # Lo leemos y almacenamos como un string
    fichString=leerFich.read()

    # Usamos BeautifulSoup para encontrar todas las etiquetas que existan
    # en el fichero
    soup = BeautifulSoup(fichString, 'html.parser')
    coincidencias = soup.find_all(etiqueta)
    
    # Eliminamos las etiquetas en si y nos quedamos con los valores dentro
    # de las etiquetas
    lista = []
    for coincidencia in coincidencias:
        lista.append(coincidencia.get_text())
    
    return np.array(lista)


def leerComunidades(fichero):
    """
        Función que lee las comunidades del archivo comunidadesAutonomas
        he creado esta función porque esta tabla html y la de provincias
        tienen formatos distintos y así se me hacía más cómodo leer las tablas
    """
    
    # Sacamos todas las coincidencias de td en el fichero
    coincidencias = buscarEtiqueta(fichero,"td")
    
    i = 0
    nCols = 2
    listaComunidades = []
    
    # Recorremos todas las coincidencias
    while i < coincidencias.shape[0]:
        # Juntamos el código con el nombre de la comunidad
        valor = coincidencias[i] + coincidencias[i+1]
        
        # Si aparece Castilla la mancha cambiamos el nombre
        # de la comunidad para que sea igual al del fichero de provincias
        if valor == "08 Castilla - La Mancha":
            valor = "08 Castilla-La Mancha"
        
        # Insertamos el código con su nombre
        listaComunidades.append(valor)
        i+=nCols
        
    return np.array(listaComunidades)


def leerProvincias(fichero):
    """
        Función que lee las provincias de un archivo
    """
    
    # Sacamos todas las coincidencias de td en el fichero
    coincidencias = buscarEtiqueta(fichero,"td")
    
    # Recorremos las coincidencias
    i = 0
    listaProvincias = []
    while i < coincidencias.shape[0]:
        # Juntamos el código de la comunidad con su nombre (i e i+1)
        # y juntamos el código de la provincia y su nombre (i+2 e i+3)
        if coincidencias[i] != "Ciudades    Autónomas:":
            listaProvincias.append(coincidencias[i] + " " + coincidencias[i+1])
            listaProvincias.append(coincidencias[i+2] + " " + coincidencias[i+3])
    
            i+=4
        else:
            # Nos saltamos una parte de las coincidencias que no es información
            i+=3
     
    # Creo el diccionario 
    dictProv = {}
    
    # Recorremos la lista que hemos generado antes
    i = 0
    while i < len(listaProvincias):
        # La clave del diccionario será la provincia
        clave = listaProvincias[i+1]
        # y el valor la comunidad a la que pertenece
        val = listaProvincias[i]
        
        dictProv[clave] = val
        
        i+=2
        
    return dictProv
    

def insertarImagenHTML(fichero,imagen):
    """
        Función para insertar una imágen en un fichero HTML dado
    """
    
    # Abro el fichero solo para lectura
    ficheroLectura = open(fichero, "r", encoding = "utf-8")
    
    # Leo el fichero y lo almaceno en una variable
    ficheroLectura_str = ficheroLectura.read()
    
    # inserto la imagen al final del fichero
    webConImg= ficheroLectura_str
    webConImg += "<img src=\"{}\" />".format(imagen)
         
    # cierro el fichero
    ficheroLectura.close()
    
    # Abro el fichero para escritura
    ficheroEscritura = open(fichero,"w",encoding= "utf-8")
    
    # Escribo en el fichero lo que había antes más la imagen
    ficheroEscritura.write(webConImg)
    
    # Cierro el fichero
    ficheroEscritura.close()