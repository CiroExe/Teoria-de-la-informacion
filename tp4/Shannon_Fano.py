def shannon_fano_rec(items, tabla, prefijo=""):
    # Si solo hay un símbolo, asignar el prefijo actual
    if len(items) == 1:
        tabla[items[0][1]] = prefijo
        return

    # Calcular el punto de división K que equilibra mejor las probabilidades
    total = sum(item[0] for item in items)
    mejor_dif = total
    suma = 0
    k = 0

    for i in range(len(items)):
        suma += items[i][0]
        dif = abs((total - suma) - suma)
        if dif < mejor_dif:
            mejor_dif = dif
            k = i

    # Dividir el conjunto
    izquierda = items[:k+1]
    derecha = items[k+1:]

    # Asignar bits diferentes y continuar recursivamente
    shannon_fano_rec(izquierda, tabla, prefijo + "0")
    shannon_fano_rec(derecha, tabla, prefijo + "1")


def shannon_fano(probs):
    # Paso 1: crear lista de [probabilidad, índice]
    items = [[p, i] for i, p in enumerate(probs)]

    # Paso 2: ordenar probabilidades en forma decreciente
    for i in range(len(items)-1):
        for j in range(i+1, len(items)):
            if items[i][0] < items[j][0]:
                items[i], items[j] = items[j], items[i]

    # Inicializar tabla vacía de códigos
    tabla = [""] * len(probs)

    # Paso 3: aplicar el algoritmo recursivo
    shannon_fano_rec(items, tabla)

    return tabla

simbolos = ['A', 'B', 'C', 'D', 'E']
probs = [ 0.385, 0.154, 0.128, 0.154, 0.179]
codigos = shannon_fano(probs)

for i in range(len(simbolos)):
    print(simbolos[i], "→", codigos[i])
