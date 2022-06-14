def grabar(nif,nombre,edad,datos,listanif):
  if len(nif) != 12:
    print("El Nif no es correcto")
    return 
  elif len(nombre) <= 8:
    print("El nombre debe tener minimo 8 caracteres")
    return 
  elif edad <= 0:
    print("La edad es menor que 0")
    return #False
  elif nif in listanif:
    print("Este Nif ya esta registrado")
    return  
  else:
    listanif.append(nif)
    lista = [nif,nombre,edad,"Esta persona si nacio","Esta Persona si se caso","Esta Persona pertenece a la union europea"]
    datos.append(lista)
    #for fila in range(3):
      #if datos[fila][0] == "":
        #for columna in range(3):
          #if columna == 0:
            #datos[fila][columna] = nif
          #elif columna == 1:
            #datos[fila][columna] = nombre
          #else:
            #datos[fila][columna] = edad
        #fila = 3
        #break
    print("se ha guardado exitosamente los datos\n")
    return datos,listanif
def buscar(nif,datos,listanif):
  if nif not in listanif:
    print("Este Nif no existe")
    return
  for fila in range(len(datos)):
    if nif == datos[fila][0]:
      print("El Nif es ",datos[fila][0])
      print("El nombres es ",datos[fila][1])
      print("Y la edad es ",datos[fila][2])
      print("Esta Persona pertenece a la union europea")
      return
      #for columna in range(3):
        #print(datos[fila][columna])
  print("No se encuentra el Nif")
  return  
def certificados(nif,datos,listanif):
  if nif not in listanif:
    print("Este Nif no existe")
    return
  print("\t ¿Que certificado desea Imprimir?\n")
  print("1.- Certificado de Nacimiento")
  print("2.- Certificado Conyugal")
  print("3.- Certificado de Pertenencia a la union Europea")
  eleccion = input("Donde desea Ingresar: ")
  if eleccion == "1":
    for fila in range(len(datos)):
      if nif == datos[fila][0]:
        print("\t Certificado de Nacimiento\n")
        print(datos[fila][3])
        print("El Nif es ",datos[fila][0],)
        print("El nombres es ",datos[fila][1])
        print("Y la edad es ",datos[fila][2])
        return  
  elif eleccion == "2":
    for fila in range(len(datos)):
      if nif == datos[fila][0]:
        print("\t Certificado Conyugal\n")
        print(datos[fila][4])
        print("El Nif es ",datos[fila][0],)
        print("El nombres es ",datos[fila][1])
        print("Y la edad es ",datos[fila][2])
        return  
  elif eleccion == "3":
    for fila in range(len(datos)):
      if nif == datos[fila][0]:
        print("\t Certificado de Pertenencia a la union Europea\n")
        print(datos[fila][5])
        print("El Nif es ",datos[fila][0],)
        print("El nombres es ",datos[fila][1])
        print("Y la edad es ",datos[fila][2])
        return  
  else:
    print("Dato no valido")
    return
