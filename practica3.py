#Eder Gutierrez Zuñiga 
#Calculador de area y perimetro de cualquier figura en 2d
#04/02/2025

import math
lados = float(input("Que lados tiene tu figura \n"))
distancia= float(input("que distancia tiene los lados de tu figura \n"))

class figura:
    def area(lados,distancia):
        if lados <= 2 :
            print("area: no es posible generar esta el area figura")
            exit()
        elif lados == 3:
            mitadl=distancia/2
            h = math.sqrt((distancia**2) + (mitadl**2))
            area= (h*distancia)/2
        elif lados == 4:
            area=distancia*distancia
        elif lados>=5:
            area = (lados * distancia**2) / (4 * math.tan(math.pi / lados))
        return(area)
    
    #def de perimetro
    def perimetro(lados,distancia):
        if lados>2:
            perimetro=lados*distancia
        return (perimetro)

figura.area(lados, distancia)
figura.perimetro(lados, distancia)
area=figura.area(lados, distancia)
perimetro=figura.perimetro(lados, distancia)
print(" ")
print("El area de su figura es: ",area)
print("El perimetro de su figura es: ",perimetro)