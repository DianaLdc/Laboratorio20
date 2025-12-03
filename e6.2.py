import numpy as np

def normalizar_np(lista, modo):
    datos = np.array(lista, dtype=float)

    if modo not in ["minmax", "zscore", "unit"]:
        raise ValueError("Modo inválido. Use: minmax, zscore o unit.")

    if modo == "minmax":
        minimo = datos.min()
        maximo = datos.max()
        if maximo - minimo == 0:
            raise ZeroDivisionError("No se puede normalizar con max = min.")
        return (datos - minimo) / (maximo - minimo)

    if modo == "zscore":
        media = datos.mean()
        desviacion = datos.std()
        if desviacion == 0:
            raise ZeroDivisionError("Desviación estándar cero.")
        return (datos - media) / desviacion

    if modo == "unit":
        norma = np.linalg.norm(datos)
        if norma == 0:
            raise ZeroDivisionError("Vector de norma cero.")
        return datos / norma

valores = [10, 20, 30]

print(normalizar_np(valores, "minmax"))
print(normalizar_np(valores, "zscore"))
print(normalizar_np(valores, "unit"))
print("Original:", valores)
