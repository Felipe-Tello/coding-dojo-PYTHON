class cuentaBancaria:
    
    peso=0

    def __init__(self, nombre, peso, interes):
        self.nombre = nombre
        self.peso = peso
        self.interes = interes

    def deposito(self,cantidad):
        self.peso += cantidad
        print(f"se ha realizado un deposito su balance es de {self.peso}")

    def retiro(self,cantidad):
        self.peso -= cantidad
        print(f"se ha realizado un retiro su balance es de {self.peso}")

    def balance(self):
        print(f"balance:{self.peso}")

    def interesdecuenta(self):
        valor= self.peso
        valor *= self.interes
        self.peso += valor
        print(f"se han generado intereses por {self.interes}")


