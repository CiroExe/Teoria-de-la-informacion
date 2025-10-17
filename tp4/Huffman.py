 # Función para obtener el primer elemento de la sublista
def obtener_probabilidad(item):
        return item[0]


def huffman(probs):
    items = [[p, [i]] for i, p in enumerate(probs)]
    tabla = [""] * len(probs)
    while len(items) > 1:
        items = sorted(items, key=obtener_probabilidad, reverse=True)

        probMinA = items.pop()
        probMinB = items.pop()

        for indice in probMinA[1]:
            tabla[indice] = "1" + tabla[indice]
        for indice in probMinB[1]:
            tabla[indice] = "0" + tabla[indice]

        nuevoElemento = [probMinA[0] + probMinB[0], probMinA[1] + probMinB[1]]
        items.append(nuevoElemento)

    return tabla

probs = [0.385, 0.154, 0.128, 0.154, 0.179]
print(huffman(probs))
