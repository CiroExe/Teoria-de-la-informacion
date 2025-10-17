import math
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

def CodificarBytearray(alfabeto, listaCadenas, mensaje):
    mensajeBinario = ""
    for letra in mensaje:
        mensajeBinario += listaCadenas[alfabeto.index(letra)]
    
    longitud_valida = len(mensajeBinario)
    
    # Rellenar hasta múltiplo de 8
    while len(mensajeBinario) % 8 != 0:
        mensajeBinario += '0'
    
    mensaje_bytes = int(mensajeBinario, 2).to_bytes(len(mensajeBinario) // 8, byteorder='big')
    return mensaje_bytes, longitud_valida

def decodificarByteArray(bytes_codificados, fuente, codigo, longitud_valida):
    # Pasar bytes → cadena binaria completa
    bits = ''.join(format(b, '08b') for b in bytes_codificados)
    
    # Solo los bits válidos
    bits = bits[:longitud_valida]
    
    mensaje = ''
    buffer = ''

    for bit in bits:
        buffer += bit
        if buffer in codigo:
            mensaje += fuente[codigo.index(buffer)]
            buffer = ''
    
    return mensaje

def tasa_compresion(mensaje, bytearray):
    tamanio_original = len(mensaje.encode('utf-8'))
    tamanio_comprimido = len(bytearray)
    if(tamanio_comprimido == 0):
        return float('inf')
    return tamanio_original / tamanio_comprimido

simbolos = [
    ' ', ',', '.', ':', ';', 'A', 'B', 'C',
    'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
    'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R',
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

probabilidades = [
    0.175990, 0.014093, 0.015034, 0.000542, 0.002109, 0.111066, 0.015368, 0.030176,
    0.038747, 0.101604, 0.004873, 0.008762, 0.007953, 0.049740, 0.003706, 0.000034,
    0.048149, 0.021041, 0.050490, 0.002018, 0.073793, 0.019583, 0.010246, 0.051446,
    0.058406, 0.031093, 0.033240, 0.008930, 0.000012, 0.000706, 0.007851, 0.003199
]


mensaje = 'Hola me llamo ciro'
mensaje = mensaje.upper()
mensajeComprimidoHuffman = huffman(probabilidades)
mensajeCodificado, longitudValida = CodificarBytearray(simbolos, mensajeComprimidoHuffman, mensaje)
print(list(mensajeCodificado))

nombre_archivo = "mensaje_comprimido.dat"
# Abrir archivo en modo escritura binaria
with open(nombre_archivo, "wb") as f:
    # Primero guardamos la longitud válida (4 bytes, big endian)
    f.write(longitudValida.to_bytes(3, byteorder='big'))
    # Luego guardamos los bytes codificados
    f.write(mensajeCodificado)

nombre_archivo = "mensaje_codificado.dat"

with open(nombre_archivo, "rb") as f:
    # Leer los primeros 3 bytes longitud válida
    longitud_valida = int.from_bytes(f.read(3), byteorder='big')
    
    # Leer el resto mensaje codificado
    mensaje_bytes = f.read()

# Decodificar usando Huffman
mensaje_decodificado = decodificarByteArray(
    mensaje_bytes,
    simbolos,               
    mensajeComprimidoHuffman, 
    longitud_valida
)

print("Mensaje decodificado:", mensaje_decodificado)