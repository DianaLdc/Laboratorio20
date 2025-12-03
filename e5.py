print("=== Registro de notas ===")

notas = []

while True:
    entrada = input("Ingrese una nota (o escriba 'fin' para terminar): ")

    if entrada.lower() == "fin":
        break

    try:
        nota = float(entrada)
        notas.append(nota)
    except ValueError:
        print("Entrada inválida, ingrese un número o 'fin'.")

if len(notas) > 0:
    promedio = sum(notas) / len(notas)
    print("\n--- Resultados ---")
    print("Notas registradas:", notas)
    print(f"Promedio: {promedio:.2f}")
else:
    print("No se ingresaron notas.")
