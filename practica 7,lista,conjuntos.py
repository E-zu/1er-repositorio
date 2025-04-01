#Crear una lista de 5 valores mixtos
#Crea lista de 5 valoes del mismo tipo con numpy
#Las listas anteriores convertirlas a tuplas y conjuntos
#Crea un diccionario de 5 elementos con vslores de distinto tipo

from numpy import array
import numpy as np

#lista
lista=list([1,2,"hola",1.12,True])
tupla=tuple(lista)
conjunto=set(lista)


#lista con numpy
arreglo=np.array([1,2,3,4,5])
tupla2=tuple(arreglo)
conjunto2=set(arreglo)

#Diccionario 
dict={
    "nombre" :"Eder",
    "edad": 18,
    "ciudad": "Zacatecas",
    "meses vivo": 226.27,
    "vivo": True
}

print = (tupla2)