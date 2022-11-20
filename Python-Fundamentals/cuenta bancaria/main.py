from cuantaBancaria import cuentaBancaria

cuenta1 = cuentaBancaria("Ema", 2000, 0.01)
cuenta2 = cuentaBancaria("rosa",600,0.8)

cuenta1.deposito(300)
cuenta1.deposito(100)
cuenta1.deposito(400)
cuenta1.retiro(400)
cuenta1.interesdecuenta()
print(f"nombre: {cuenta1.nombre} balance: {cuenta1.peso} interes: {cuenta1.interes}")
# print(cuenta1.peso)
cuenta2.deposito(200)
cuenta2.deposito(500)
cuenta2.retiro(100)
cuenta2.retiro(200)
cuenta2.retiro(300)
cuenta2.retiro(100)
cuenta2.interesdecuenta()
print(f"nombre del cliente {cuenta2.nombre} balance de la cuenta {cuenta2.peso} interes de la cuenta {cuenta2.interes}")


# cuenta1.deposito(1000)
# print(cuenta1.peso)

# cuenta1.retiro(500)
# print(cuenta1.peso)

# cuenta1.balance()

# cuenta1.interesdecuenta()
# print(cuenta1.peso)


