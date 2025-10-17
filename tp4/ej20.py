def tasa_compresion(mensaje, bytearray):
    tamanio_original = len(mensaje.encode('utf-8'))
    tamanio_comprimido = len(bytearray)
    if(tamanio_comprimido == 0):
        return float('inf')
    return tamanio_original / tamanio_comprimido

def Run_Length_Coding(mensaje):
    contAct = 1
    carAnt = mensaje[0]
    resultado = []

    for i in range(1, len(mensaje)):
        if mensaje[i] != carAnt:
            resultado.append((carAnt, contAct))
            contAct = 1
            carAnt = mensaje[i]
        else:
            contAct += 1

    resultado.append((carAnt, contAct))
    return resultado


def RLC_Bytearray(mensaje):
    RLC = Run_Length_Coding(mensaje)
    ba = bytearray()
    for letra, cantidad in RLC:
        ba.append(ord(letra))     # letra -> byte (ASCII)
        ba.append(cantidad)       # cantidad -> byte
    return ba

mensaje1 = 'XXXYZZZZ'
mensaje2 = 'AAAABBBCCDAA'
mensaje3 = 'UUOOOOAAAIEUUUU'

Compresion1 = RLC_Bytearray(mensaje1) 
tasa_compresion1 = tasa_compresion(mensaje1, Compresion1)
print(tasa_compresion1)

Compresion2 = RLC_Bytearray(mensaje2)
tasa_compresion2 = tasa_compresion(mensaje2, Compresion2)
print(tasa_compresion2)

Compresion3 = RLC_Bytearray(mensaje3)
tasa_compresion3 = tasa_compresion(mensaje3, Compresion3)
print(tasa_compresion3)