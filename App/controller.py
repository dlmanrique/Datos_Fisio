"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Adaptado del desarrollo para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv
from ADT import list as lt
from ADT import map as map


from DataStructures import listiterator as it
#from Sorting import mergesort as sort
from time import process_time


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Funcionaes utilitarias

def printList (lst):
    iterator = it.newIterator(lst)
    while  it.hasNext(iterator):
        element = it.next(iterator)
        result = "".join(str(key) + ": " + str(value) + ". " for key, value in element.items())
        print (result)


# Funciones para la carga de datos 

def loadData ():
    """
    Carga  del archivo.
    Se almacena como una lista de diccionarios 
    """
    data  =  lt . newList ('ARRAY_LIST') #Usando implementación lista array 
    t1_start = process_time() #tiempo inicial
    stationsFile = cf.data_dir + 'FC_Endocrino_201920.csv'
    dialect = csv.excel()
    dialect.delimiter=','
    with open(stationsFile, encoding="utf-8-sig") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader:
            lt.addLast(data,row)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución carga archivo estaciones:",t1_stop-t1_start," segundos")  
    return data

def consulta_integrante_prom_desv (r) :
    t = model.consulta_integrante_prom_desv(r)
    return t 
def consulta_por_genero(data) :
    t = model.consulta_por_genero(data)
    return t 
def consulta_total_generos(data):
    r =  model.consulta_total_generos(data)
    return r 

