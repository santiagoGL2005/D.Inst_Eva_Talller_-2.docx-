def calcular_nota_final():
    # Pesos de las actividades
    pesos = {
        "Taller 1": 0.20,
        "Taller 2": 0.15,
        "Cuestionario 1": 0.22,
        "Cuestionario 2": 0.10,
        "Proyecto final": 0.36
    }

    # Leer una nota y revisar que está en el rango
    def leer_nota(actividad):
        while True:
            try:
                nota = float(input(f"Ingrese la nota para {actividad} : "))
                if 1.0 <= nota <= 5.0:
                    return nota
                else:
                    print("Error: La nota debe estar entre 1.0 y 5.0.")
            except ValueError:
                print("Error: Ingrese un valor numérico válido.")

    # Leer las notas
    notas = {}
    for actividad in pesos.keys():
        notas[actividad] = leer_nota(actividad)

    # Cálculo nota final
    nota_final = sum(notas[actividad] * pesos[actividad] for actividad in pesos.keys())

    # Redondear la nota final a 2 decimales
    nota_final_redondeada = round(nota_final, 2)

    # Evaluación cualitativa
    if nota_final_redondeada >= 4.5:
        evaluacion = "Excelente"
    elif nota_final_redondeada >= 4.0:
        evaluacion = "Bueno"
    elif nota_final_redondeada >= 3.0:
        evaluacion = "Regular"
    else:
        evaluacion = "Insuficiente"

    # Mostrar resultado
    print(f"\nNota final: {nota_final_redondeada} ({evaluacion})")

# calculo de nota final     
calcular_nota_final()