# Paso 1: Solicitar el salario mínimo actual
salario_actual = float(input("Ingrese el salario mínimo actual: "))

# Paso 2: Calcular el nuevo salario con el incremento del 4.2%
incremento = 4.2 / 100
nuevo_salario = salario_actual * (1 + incremento)

# Paso 3: Mostrar el nuevo salario
print(f"El nuevo salario mínimo será: {nuevo_salario:.2f}")