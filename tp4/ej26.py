def devuelve_lista_codificada(cadena):
    caracteres_bin = []
    for c in cadena:
        newBinChar = bin(ord(c))[2:]
        caracteres_bin.append(newBinChar)
    
    matriz = []
    for i in range(len(caracteres_bin)):
        codigoAct = caracteres_bin[i]
        newRow = []
        for c in codigoAct:
            newRow.append(int(c))
        matriz.append(newRow)
    
    #agrega vrc
    mat_vrc = []
    for fila in matriz:
        cantUnos = sum(fila)
        bitParidad = 0 if cantUnos % 2 == 0 else 1
        fila_vrc = fila + [bitParidad]
        mat_vrc.append(fila_vrc)
    
    fila_lrc = []
    nFilas = len(mat_vrc)
    nCols = len(mat_vrc[0])
    for j in range(nCols):
        cantUnosCol = 0
        for i in range (nFilas):
            cantUnosCol += mat_vrc[i][j]
        bitParidad = 0 if cantUnosCol % 2 == 0 else 1
        fila_lrc.append(bitParidad)
    mat_vrc.insert(0,fila_lrc)
        
     # 6️ Convertir toda la matriz en una lista plana de bits
    bits_planos = [bit for fila in mat_vrc for bit in fila]

    # 7️ Agrupar los bits en bytes y convertirlos a enteros
    bytes_lista = []
    for i in range(0, len(bits_planos), 8):
        grupo = bits_planos[i:i+8]
        # Si el último grupo tiene menos de 8 bits, lo completamos con ceros
        while len(grupo) < 8:
            grupo.append(0)
        byte = 0
        for bit in grupo:
            byte = (byte << 1) | bit
        bytes_lista.append(byte)
    
        
    secuencia_bytes = bytearray(bytes_lista)
    
    return mat_vrc, secuencia_bytes
        
def decodifica_con_verificacion(secuencia_bytes):
    # 1️ Convertir cada byte en binario de 8 bits
    binarios = [bin(b)[2:].zfill(8) for b in secuencia_bytes]

    # 2️ Reconstruir matriz de bits
    matriz = [[int(bit) for bit in b] for b in binarios]

    # 3️ Aplanar y reagrupar en filas de 8 bits
    bits_planos = [bit for fila in matriz for bit in fila]
    filas = [bits_planos[i:i+8] for i in range(0, len(bits_planos), 8)]
    if len(filas) < 2:
        return ""  # matriz incompleta

    # 4️ Separar fila de paridad cruzada y datos
    fila_paridad = filas[0]
    datos = filas[1:]

    # 5️ Verificar paridad longitudinal (por fila)
    filas_con_error = []
    for i, fila in enumerate(datos):
        suma = sum(fila[:7])
        if suma % 2 != fila[7]:
            filas_con_error.append(i)

    # 6️ Verificar paridad vertical (por columna)
    columnas_con_error = []
    for j in range(7):
        suma = sum(datos[i][j] for i in range(len(datos)))
        if suma % 2 != fila_paridad[j]:
            columnas_con_error.append(j)

    # 7️ Si hay una sola intersección, corregir
    if len(filas_con_error) == 1 and len(columnas_con_error) == 1:
        i = filas_con_error[0]
        j = columnas_con_error[0]
        datos[i][j] ^= 1  # flip del bit

    # 8️ Si hay múltiples errores, no se puede recuperar
    if len(filas_con_error) > 1 or len(columnas_con_error) > 1:
        return ""

    # 9️ Reconstruir cadena original
    caracteres = []
    for fila in datos:
        binario = ''.join(str(b) for b in fila[:7])
        caracteres.append(chr(int(binario, 2)))

    return ''.join(caracteres)



matriz, secuencia = devuelve_lista_codificada("LUNA")
print("Matriz final:")
for fila in matriz:
    print(fila)
    
print("\nBytearray final:", list(secuencia))
print("Bytes en binario:")
for b in secuencia:
    print(bin(b)[2:].zfill(8))
print("\nBytearray final:", list(secuencia))
print(decodifica_con_verificacion(secuencia))