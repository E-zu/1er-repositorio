# Clase padre
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        return self.marca + " " + self.modelo

# Clase hija que hereda de Vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)  # Llama al constructor de la clase padre
        self.num_puertas = num_puertas

    def describir(self):
        return "Coche: " + super().describir() + ", " + str(self.num_puertas) + " puertas"

# Otra clase hija que hereda de Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)  # Llama al constructor de la clase padre
        self.tipo = tipo

    def describir(self):
        return "Bicicleta: " + super().describir() + ", tipo " + self.tipo

# Uso de las clases
mi_coche = Coche("Toyota", "Corolla", 4)
mi_bicicleta = Bicicleta("Trek", "Marlin", "Montaña")

print(mi_coche.describir())  # Salida: Coche: Toyota Corolla, 4 puertas
print(mi_bicicleta.describir())  # Salida: Bicicleta: Trek Marlin, tipo Montaña