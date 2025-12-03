print("=== Cálculo de Impuesto Progresivo ===")
 
sueldo = float(input("Ingrese su sueldo mensual: "))

if sueldo <= 1000:
    porcentaje = 0
elif sueldo <= 2000:
    porcentaje = 5
elif sueldo <= 3000:
    porcentaje = 10
else:
    porcentaje = 15

impuesto = sueldo * (porcentaje / 100)
sueldo_final = sueldo - impuesto

print("\n--- Resultados ---")
print(f"Sueldo ingresado: {sueldo:.2f}")
print(f"Impuesto aplicado ({porcentaje}%): {impuesto:.2f}")
print(f"Sueldo final después de impuesto: {sueldo_final:.2f}")
