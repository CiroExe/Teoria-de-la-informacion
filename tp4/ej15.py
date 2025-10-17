def getCodificacionBytearray(alfabeto, listaCadenas, mensaje):
    mensajeBinario = ""
    for letra in mensaje:
        mensajeBinario += listaCadenas[alfabeto.index(letra)]
    
    longitud_valida = len(mensajeBinario)
    
    # Rellenar hasta múltiplo de 8
    while len(mensajeBinario) % 8 != 0:
        mensajeBinario += '0'
    
    mensaje_bytes = int(mensajeBinario, 2).to_bytes(len(mensajeBinario) // 8, byteorder='big')
    return mensaje_bytes, longitud_valida

def decodificar(bytes_codificados, fuente, codigo, longitud_valida):
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

fuente = 'ABC'
listaCadenas = ['0', '10', '11']
mensaje = 'ABCCBA'
mensajeCodificado, longitudValida = getCodificacionBytearray(fuente,listaCadenas, mensaje)
print(list(mensajeCodificado))
mensajeDecodificado = decodificar(mensajeCodificado, fuente, listaCadenas, longitudValida)
print(mensajeDecodificado)
print('Tasa de compresion -> ', tasa_compresion(mensaje, mensajeCodificado))