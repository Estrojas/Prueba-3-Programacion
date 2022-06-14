# -*- coding: utf-8 -*-
import numpy as np
from funcionprueba import grabar,buscar,certificados
menu = True
#datos = np.array(["1","2","3"],["1","2","3"])
datos = []
nif = ""
nombre = ""
edad = 0
listanif = []
#di = False
while menu:
  #aqui debe ir un try
  print("\tBienvenido\n")
  print("1.-Grabar datos")
  print("2.-Buscar persona")
  print("3.-Imprimir certificados")
  print("4.-salir")
  opcion = input("Ingrese opcion elegida: ")
  if opcion == "1":
    nif = input("Ingrese el Nif: ")
    nombre = input("Ingrese el Nombre: ")
    edad = int(input("Ingrese la edad: "))#se puede cambiar por input y revisar dentro
    grabar(nif,nombre,edad,datos)
  elif opcion == "2":
    nif = input("Ingrese el Nif a buscar: ")
    buscar(nif,datos)
  elif opcion == "3":
    nif = input("Ingrese el Nif a buscar: ")
    certificados(nif,datos)
  elif opcion == "4":
    #print(datos)
    #print(datos[0])
    menu = False
  else:
    print("Opcion no valida")