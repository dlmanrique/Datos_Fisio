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

def consulta_integrante_prom_desv (data):
    """ Filtro por integrante y saco promedio y desviacion estandar asociado"""
    dicc = {}
    response = {}
    for row in data['elements'] :
        trat = row['Integrante']
        glu_init =float(row['Glucosa (t=0)'])
        glu_fin = float(row['Glucosa (t=40)'])
        if trat  not in dicc :
            glut_init = []
            glut_fin = []
            glut_init.append(glu_init)
            glut_fin.append(glu_fin)
            dicc[trat] = (glut_init,glut_fin)
        else :
            r = dicc[trat][0]
            r.append(glu_init)
            t = dicc[trat][1]
            t.append(glu_fin)
            dicc[trat] = (r,t)
    for tratamiento in dicc.keys() :
        g = dicc[tratamiento][0]
        y = dicc[tratamiento][1]
        prom_init = round(promedio_integrante(g),4)
        desv_init = round(desviacion_estandar_integrante(g),4)
        prom_fin = round(promedio_integrante(y),4)
        desv_fin = round(desviacion_estandar_integrante(y),4)
        response[tratamiento] = {"Inicial":(prom_init,desv_init), "Final":(prom_fin,desv_fin)}
    return response

def consulta_por_genero(data):
    dicc = {}
    response = {}
    for row in data['elements'] :
        trat = row['Integrante']
        if trat not in dicc :
            f = []
            f.append(row)
            dicc[trat] = f
        else :
            r = dicc[trat]
            r.append(row)
            dicc[trat] = r
    for h in dicc.keys():
        er = dicc[h]
        male_i = []
        male_f = []
        female_i = []
        female_f = []
        for i in er :
            glut_inicial = float(i['Glucosa (t=0)'])
            glut_final = float(i["Glucosa (t=40)"])
            if i['Genero'] == 'M' :
                male_i.append(glut_inicial)
                male_f.append(glut_final)
            else :
                female_i.append(glut_inicial)
                female_f.append(glut_final)
        prom_male_i = round(promedio_integrante(male_i),4)
        prom_male_f = round(promedio_integrante(male_f),4)
        prom_female_i = round(promedio_integrante(female_i),4)
        prom_female_f = round(promedio_integrante(female_f),4)
        desv_male_i = round(desviacion_estandar_integrante(male_i),4)
        desv_male_f = round(desviacion_estandar_integrante(male_f),4)
        desv_female_i = round(desviacion_estandar_integrante(female_i),4)
        desv_female_f = round(desviacion_estandar_integrante(female_f),4)
        response[h] = {'Hombres':{"Inicial":(prom_male_i,desv_male_i),"Final":(prom_male_f,desv_male_f)}, "Mujeres" : {"Inicial":(prom_female_i,desv_female_i),"Final":(prom_female_f,desv_female_f)}}
    return response
def consulta_total_generos(data):
    male = 0
    female = 0
    for row in data['elements'] :
        
        if (row['Genero']== 'M'):
            male += 1
        else :
            female += 1
    return (male,female)

def promedio_integrante (t) :
    prom = stata.mean(t)
    return prom

def desviacion_estandar_integrante(t):
    desv = stata.stdev(t)
    return desv









            


