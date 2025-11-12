def esCanalSinRuido(matCanal):
    
    for j in range(len(matCanal[0])):
        contElementosCol = 0
        for i in range(len(matCanal)): 
             
            if matCanal[i][j] != 0:
                contElementosCol += 1   
            if contElementosCol > 1:
                return False
    return True

def esCanalDeterminastico(matCanal):
    for i in range(len(matCanal)):
        contElementosFila = 0
        for j in range(len(matCanal[0])):  
            if matCanal[i][j] != 0:
                contElementosFila += 1   
            if contElementosFila > 1:
                return False    
    return True

# Matrices transcritas desde el adjunto
M1 = [
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0],
    [0.0, 1.0, 0.0],
    [1.0, 0.0, 0.0],
]

# Segunda matriz: transcripción aproximada (3 filas x 6 columnas).
# Revisa por favor; algunos valores no estaban totalmente nítidos en la imagen.
M2 = [
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 0.2, 0.0, 0.8],
    [0.0, 0.0, 0.1, 0.0],
]

# Tercera matriz (3x3) — se lee claramente
M3 = [
    [0.3, 0.5, 0.2],
    [0.2, 0.3, 0.5],
    [0.5, 0.2, 0.3],
]

# Cuarta matriz: transcripción propuesta (4x4). Verifica por favor.
M4 = [
    [0.0, 0.0, 1.0, 0.0],
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 1.0],
]

print("M1 es canal sin ruido:", esCanalSinRuido(M1))
print("M1 es canal determinístico:", esCanalDeterminastico(M1)) 

print("M2 es canal sin ruido:", esCanalSinRuido(M2))
print("M2 es canal determinístico:", esCanalDeterminastico(M2))    

print("M3 es canal sin ruido:", esCanalSinRuido(M3))
print("M3 es canal determinístico:", esCanalDeterminastico(M3))

print("M4 es canal sin ruido:", esCanalSinRuido(M4))
print("M4 es canal determinístico:", esCanalDeterminastico(M4))

  