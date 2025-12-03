import math

def normalizar(lista, modo):
    datos = lista.copy()
    if modo not in ["minmax", "zscore", "unit"]:
        raise ValueError("Modo inválido. Use: minmax, zscore o unit.")

    if modo == "minmax":
        minimo = min(datos)
        maximo = max(datos)
        rango = maximo - minimo
        if rango == 0:
            raise ZeroDivisionError("No se puede normalizar con minmax si max = min.")
        return [(x - minimo) / rango for x in datos]

    if modo == "zscore":
        media = sum(datos) / len(datos)
        var = sum((x - media) ** 2 for x in datos) / len(datos)
        desviacion = math.sqrt(var)
        if desviacion == 0:
            raise ZeroDivisionError("La desviación estándar es cero.")
        return [(x - media) / desviacion for x in datos]

    if modo == "unit":
        norma = math.sqrt(sum(x**2 for x in datos))
        if norma == 0:
            raise ZeroDivisionError("No se puede normalizar un vector de norma cero.")
        return [x / norma for x in datos]
valores = [10, 20, 30]

print(normalizar(valores, "minmax"))
print(normalizar(valores, "zscore"))
print(normalizar(valores, "unit"))
print("Original:", valores)
