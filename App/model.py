"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
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
from ADT import list as lt
from ADT import graph as g
from ADT import map as map
from ADT import list as lt
#from Sorting import mergesort 
from DataStructures import listiterator as it
from DataStructures import orderedmapstructure as tree
from datetime import datetime
from DataStructures import dijkstra as dk
from DataStructures import dfs as dfs 
from DataStructures import bfs as bfs 
import statistics as stata

"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores 
y otra para géneros
"""

# Construccion de modelos

def consulta_integrante_seccion (data,seccion):
    """ Devuelvo primero los promedios"""
    t = []
    for row in data['elements'] :
        if ( seccion == row['Seccion '] ) :
            t.append(row)
    p = promedio_integrante(t)
    t = desviacion_estandar_integrante(t)
    return (p,t)

def promedio_integrante (t) :
    dicc = {}
    for line in t :
        tratamiento = line['Integrante']
        t_init = 0
        t_fin = 0 
        cont = 0
        for l in t :
            if (l['Integrante'] == tratamiento ) :
                cont += 1
                g_init = int( l['Glucosa (t=0)'])
                g_fin = int(l['Glucosa (t=40)'])
                t_init += g_init 
                t_fin += g_fin 
        t_i = t_init / cont
        t_f = t_fin / cont
        dicc[tratamiento] = (t_i , t_f)
    return dicc

def desviacion_estandar_integrante(t):
    dicc = {}
    for line in t :
        tratamiento = line['Integrante']
        init = []
        fin = []
        for u in t :
            if (u['Integrante'] == tratamiento ):
                glucosa_init = float(u['Glucosa (t=0)'])
                glucosa_fin = float(u['Glucosa (t=40)'])
                init.append(glucosa_init)
                fin.append(glucosa_fin)
        e = round(stata.stdev(init),4)
        y = round(stata.stdev(fin),4)
        dicc[tratamiento] = (e,y)
    return dicc

def consulta_genero(data):
    hombres = []
    mujeres = []
    dicc = {}
    for row in data['elements'] :
        if ( 'M' == row['Genero'] ) :
            hombres.append(row)
        else : 
            mujeres.append(row)
    
    ph = promedio_integrante(hombres)
    pm = promedio_integrante(mujeres)
    dh = desviacion_estandar_integrante(hombres)
    dm = desviacion_estandar_integrante(mujeres)
    dicc['info_hombres'] = (ph,dh)
    dicc['info_mujeres'] = (pm,dm)
    return dicc








            


