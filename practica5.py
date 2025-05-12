#Eder Gutierrez Zuñiga
#05/02/2025
#Arreglos

#profe la vdd no se si sea la practica de numpy pero es la que se le acerca (⌒_⌒;)


from numpy import array
import numpy as np


class Arreglos:
    def __init__(self,v):
        lista =[v]
        self.arregloNp=np.array(v)
        self.arregloList = lista[0]

    def insertar(self,v):
        numeros=[1,2,3,4,5,6,7,8,9]
        valor=int(input("Escribe un valor que se agregara el final de la lista:  "))
        if valor in numeros:
            print("El elemento introducido debe de ser numerico")
        else:
            self.arregloList.append(valor)
            self.arregloNp = np.append(self.arregloNp, valor)
            print("Su nueva lista es:  ",self.arregloList)
            print("Su nuevo arreglo es:  ",self.arregloNp)

    def modificar(self,v):
        lugar=int(input("En que posicion quieres que se modifique:  "))
        index=lugar
        if 0<= index < len(self.arregloList):
            nuevoValor=int(input("¿Cual seria EL nuevo valor?  "))
            self.arregloList[index] = nuevoValor  
            self.arregloNp[index] = nuevoValor
            print("Su nueva lista es:  ",self.arregloList)
            print("Su nuevo arreglo es:  ",self.arregloNp)
        else:
            print("Esta fuera del limite")

    def eliminar(self,v):
        i=int(input("Que lugar quieres eliminar:  "))
        self.arregloList.pop(i)
        self.arregloNp = np.delete(self.arregloNp, i) 
        print("Su nueva lista es:  ",self.arregloList)
        print("Su nuevo arreglo es:  ",self.arregloNp)

v=[1,2,3]
elArreglo=Arreglos(v)

print("Su lista principal es",v)
eleccion = int(input("¿Que deseas hacer?  0.-salir 1.-Insertar 2.-Modificar 3.-Eliminar:  "))
if eleccion == 0:
    print("Finalizando programa")
elif eleccion == 1:
    elArreglo.insertar(v)
elif eleccion == 2:
    elArreglo.modificar(v)
elif eleccion == 3:
    elArreglo.eliminar(v)    