from User import User
from CuentaBancaria import CuentaBancaria

Sara = User("Sara")
Kelly = User("Kelly")

# Ambos usuarios parten con un monto de 100

Sara.cuenta.hacer_deposito(1500)
Sara.cuenta.hacer_retiro(100)
Sara.cuenta.mostrar_balance_usuario()

Kelly.cuenta.hacer_deposito(100)
Kelly.cuenta.hacer_deposito(200)
Kelly.cuenta.mostrar_balance_usuario()

Sara.cuenta.transfer_dinero(Kelly.cuenta, 100)

print(Sara.cuenta.balance)
print(Kelly.cuenta.balance)
