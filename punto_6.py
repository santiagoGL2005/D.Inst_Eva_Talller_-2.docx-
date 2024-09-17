# Definir la tasa de cambio (por ejemplo, 1 USD = 4206.27 COP)
tasa_de_cambio = 4206.27

# Ingrese la cantidad en pesos colombianos
cantidad_en_pesos = float(input("Ingrese la cantidad en pesos colombianos: "))

# Realizar la conversión
cantidad_en_dolares = cantidad_en_pesos / tasa_de_cambio

# Resultado
print(f"El valor en dólares es: {cantidad_en_dolares:.2f} USD")
