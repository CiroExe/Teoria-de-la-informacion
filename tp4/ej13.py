import math
def getProbabilidades(cadena):
    probs = []
    caracteres = []
    
    for c in cadena:
        if c in caracteres:
            probs[caracteres.index(c)] += 1
        else:
            caracteres.append(c)
            probs.append(1)
    
    for i in range(len(probs)):
        probs[i] /= len(cadena)
    
      
    return probs

def getAlfabeto(mensaje):
    alfabeto = []
    for i in range(len(mensaje)):
        if mensaje[i] not in alfabeto:
            alfabeto.append(mensaje[i])
    alfabeto = sorted(alfabeto)
    return alfabeto

def entropia(distribuciones, r):
    return sum(distribuciones[i] * math.log(1/distribuciones[i], r) for i in range(len(distribuciones)))

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

def longitud_media(distribucion, longitudes):
    return sum(distribucion[i] * longitudes[i] for i in range(len(longitudes)))

def rendimiento(distribucion, codigo, longitudes):
    H = entropia(distribucion, 2)
    longitudMedia = longitud_media(distribucion, longitudes)
    return H / longitudMedia

mensaje = '58784784525368669895745123656253698989656452121702300223659'
alfabeto = getAlfabeto(mensaje)
mensaje = sorted(mensaje)
distribucion = getProbabilidades(mensaje)
print(distribucion)
H = entropia(distribucion, 2)
print(H)
tablaHuffman = huffman(distribucion)
tablaShannonFano = shannon_fano(distribucion)
longitudesHuffman = [len(tablaHuffman[i]) for i in range(len(tablaHuffman))]
longitudesShannonFano = [len(tablaShannonFano[i]) for i in range(len(tablaShannonFano))]
print('L huffman ', longitudesHuffman)
print('L Shannon Fano', longitudesShannonFano)

print('Codificacion Huffman -> ', tablaHuffman)
print('Codificacion Shannon Fano -> ', tablaShannonFano)

rendimientoHuffman = rendimiento(distribucion, tablaHuffman, longitudesHuffman)
rendimientoShannonFano = rendimiento(distribucion, tablaShannonFano, longitudesShannonFano)
print('Rendimiento Huffman ', rendimientoHuffman)
print('Rendimiento Shannon Fano ',rendimientoShannonFano)
print('Redundancia Huffman ', 1-rendimientoHuffman)
print('Redundancia Shannon Fano ', 1 - rendimientoShannonFano)