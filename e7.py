def buscar_palabra(texto, palabra):
    texto_min = texto.lower()
    palabra_min = palabra.lower()

    posiciones = []
    i = 0

    while i < len(texto_min):
        if texto_min.startswith(palabra_min, i):
            posiciones.append(i)
        i += 1

    return len(posiciones), posiciones

texto = "El sol brilla. El viento sopla. El día es hermoso."
palabra = "el"

cantidad, posiciones = buscar_palabra(texto, palabra)

print("Veces encontradas:", cantidad)
print("Posiciones:", posiciones)
