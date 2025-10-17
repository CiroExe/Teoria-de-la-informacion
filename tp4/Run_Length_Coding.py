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

# --- Prueba ---
mensaje = 'XXXYZZZZ'
mensajeComprimido = Run_Length_Coding(mensaje)
print(mensajeComprimido)

mensaje2 = 'AAAABBBCCDAA'
mensajeComprimido2 = Run_Length_Coding(mensaje2)
print(mensajeComprimido2)

mensaje3 = 'UUOOOOAAAIEUUUU'
mensajeComprimido3 = Run_Length_Coding(mensaje3)
print(mensajeComprimido3)

