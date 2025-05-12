class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo privado

    def mostrar_saldo(self):
        print(f"Saldo: {self.__saldo}")

    def depositar(self, cantidad):
        self.__saldo += cantidad

mi_cuenta = CuentaBancaria(100)
# print(mi_cuenta.__saldo)
mi_cuenta.mostrar_saldo() 
