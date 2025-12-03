print("=== Cálculo de salario neto ===")
 
salario_base = float(input("Ingrese salario base: "))
horas_extras = float(input("Ingrese horas extras trabajadas: "))
pago_hora_extra = float(input("Ingrese pago por hora extra: "))
bono = float(input("Ingrese bono: "))
afp = float(input("Ingrese porcentaje AFP: "))
salud = float(input("Ingrese porcentaje de salud: "))
 
salario_bruto = salario_base + (horas_extras * pago_hora_extra) + bono
descuentos = (salario_base * afp/100) + (salario_base * salud/100)
salario_neto = salario_bruto - descuentos
 
print("\n--- Resultados ---")
print(f"Salario bruto: {salario_bruto:.2f}")
print(f"Descuentos totales: {descuentos:.2f}")
print(f"Salario neto: {salario_neto:.2f}")
