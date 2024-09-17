# Converti metros a millas
def metros_a_millas(metros):
    factor_conversion = 1 / 1609.34
    millas = metros * factor_conversion
    return millas

# Ingrese el valor en metros
metros = float(input("Ingresa el valor en metros: "))

# Convertir metros a millas
millas = metros_a_millas(metros)

# Resultado
print(f"{metros} metros es igual a {millas} millas.")
