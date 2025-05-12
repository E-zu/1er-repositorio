#c={1,2,3}
#c.add(4)
#c.remove(1)    #Error si no se encuentra 
#c.discard(1)   #No hay error si no se encuentra
#print(1 in c)
#print(c)


#Crear un conjunto de elementos 
# agregatr un valor que no existe 
# eliminar un valor que no existe 
# verificar si existe un calor 
# agregar un valor repetido

a={1,2,3,4,5}
b={5,6,7,8,9}
d={1,2,3}
e={1,2,3,4,5,6}

u=b.union(a)
#u= a|b es lo mismo que la de arriba 

I=a & b
#I=b.intercection es lo mismo que lo de arriba

D= a.difference(b)
DS=a.symmetric_difference(b)

E=d.issubset(e)
F=e.issuperset(d)

#Contar elementos dentro de un conjunto
G=len(a)
#Copiar un conjunto
H=a.copy()
#diccionario
dic= {'x':"equis",'y':"ye",'D':"De"}
dic2= dict(x="equis",y="ye", D="De")#Funcion para que lo que esta adentro funcione como diccionario

x=dic.pop('y')

c={1,5,9,6,3}
c.add(2)
c.add(5) 
c.remove(3)
c.discard(4)

print("union: ",u)
print("Interseccion: ",I)
print('Diferencia respecto a "a":',D)
print("diferencia simetrica : ",DS)
print(E)
print(F)
print(G)
print(H)
print(dic)
print(dic['x'])#Debe salir un error si no existe en el diccioinario 
print(dic.get('x'))
print(dic.get('z'))#Si el valor no extiste muestra nulo
dic['x']="equisD"
dic['z']="Zeta"

print(dic)
print(x)
print('x' in dic)

llaves = dic.keys()
print(llaves)
valores= dic.values()
print(valores)
p= dic.items #Esta hace el diccionario en tuplas
print(p)

print()
print( 5 in c)
print (c)