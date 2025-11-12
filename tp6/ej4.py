def generaCanalCompuesto(matA, matB):
    
    colsA = len(matA[0])
    filasB = len(matB)
    if colsA != filasB:
        raise ValueError("Las matrices no son compatibles para multiplicación.")
    
    filasA = len(matA)
    colsB = len(matB[0])    
    canalCompuesto = []
    for i in range(len(matA)):
        for k in range(len(matB[0])):
            acum = 0
            for j in range(len(matA[0])):
                acum += matA[i][j] * matB[j][k] 
            canalCompuesto.append(round(acum, 3))
    return canalCompuesto

matA = [
    [0.7,0.0,0.3,0.0],
    [0.2,0.6,0.0,0.2]
]

matB = [
    [0.9, 0.0, 0.1],
    [0.0, 1.0, 0.0],
    [0.1, 0.1, 0.8],
    [0.0, 0.5, 0.5]
]

matC = generaCanalCompuesto(matA, matB) 
print("Matriz del canal compuesto:", matC)
        
            