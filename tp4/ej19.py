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

mensaje = 'XXXYZZZZ'
bytearrayRLC = RLC_Bytearray(mensaje)
RLC = Run_Length_Coding(mensaje)
print(list(bytearrayRLC))
