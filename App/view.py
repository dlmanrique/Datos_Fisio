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
import sys
import controller 
import csv
from ADT import list as lt
from ADT import stack as stk
from ADT import orderedmap as map
from DataStructures import listiterator as it
from DataStructures import orderedmapstructure as tree
import sys


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido al Laboratorio 9")
    print("1- Cargar información")
    print("2- Promedio y desviacion por integrante,seccion")
    print("3- Consulta por genero ")
    print("4- Total de hombres y mujeres")
    print("0- Salir")

"""
Menu principal 
""" 
def main():
    while True: 
        printMenu()
        inputs =input("Seleccione una opción para continuar\n")
        if int(inputs[0])==1:
            t = controller.loadData()
        elif int(inputs[0])==2:
            y = controller.consulta_integrante_prom_desv(t)
            print(y)
            for r in y.keys() :
                print( "Para integrante : " + str(r) + " ")
                print(" Glucosa inicial, promedio : " +str(y[r]['Inicial'][0]) + " desviacion: " +str(y[r]['Inicial'][1])+ "" )
                print(" Glucosa final, promedio : " +str(y[r]['Final'][0]) + " desviacion: " +str(y[r]['Final'][1])+ "" )
                print("---------------------------------------------------------------------------------------------------------")
        elif int(inputs[0])==3:
            y = controller.consulta_por_genero(t)
            print(y)
            for r in y.keys():
                print("Para integrante: "+str(r)+ " ")
                print(" Hombres : ")
                print("Glucosa promedio inicial : " +str(y[r]['Hombres']['Inicial'][0])+" desviacion : " +str(y[r]['Hombres']['Inicial'][1])+" ")
                print("Glucosa promedio final : " +str(y[r]['Hombres']['Final'][0])+" desviacion : " +str(y[r]['Hombres']['Final'][1])+" ")
                print("Mujeres : ")
                print("Glucosa promedio inicial : " +str(y[r]['Mujeres']['Inicial'][0])+" desviacion : " +str(y[r]['Mujeres']['Inicial'][1])+" ")
                print("Glucosa promedio final : " +str(y[r]['Mujeres']['Final'][0])+" desviacion : " +str(y[r]['Mujeres']['Final'][1])+" ")
                print("-----------------------------------------------------------------------------------------------------------")
        elif int(inputs[0])==4:
            y = controller.consulta_total_generos(t)
            print("Total mujeres : " + str(y[1])+ " ")
            print("Total hombres : " + str(y[0])+ " ")
        else :
            sys.exit(0)
    sys.exit(0)

if __name__ == "__main__":
    main()