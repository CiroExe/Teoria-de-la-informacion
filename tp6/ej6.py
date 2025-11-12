def sePuedenCombinar(matCanal, col1, col2):
    # Variable que guardará el factor de proporcionalidad entre las columnas
    k = None

    # Recorremos todas las filas de la matriz
    for i in range(len(matCanal)):
        a = matCanal[i][col1]   # valor en la columna 1
        b = matCanal[i][col2]   # valor en la columna 2
        
        # Caso 1: ambos son 0 → no aportan información, seguimos
        if a == 0 and b == 0:
            continue
        
        # Caso 2: uno es 0 y el otro no → no pueden ser proporcionales
        elif a == 0 or b == 0:
            return False
        
        # Caso 3: ambos distintos de 0
        else:
            # Si aún no tenemos un valor de k, lo calculamos
            if k is None:
                k = b / a    # primer cociente que encontramos
            
            # Si ya teníamos un k, verificamos que se mantenga la proporción
            # Usamos una pequeña tolerancia (1e-6) por los errores de redondeo
            elif abs(b - a * k) > 1e-6:
                return False  # si no se cumple, no son proporcionales
    
    # Si pasamos todas las filas sin devolver False, son proporcionales
    return True

def generaCanalDeterminante(matCanal, col1, col2):
    sonProporcionales = sePuedenCombinar(matCanal, col1, col2)  
    if not sonProporcionales:
        raise ValueError("Las columnas no son proporcionales y no se pueden combinar.")
        return null
    else:
        n = len(matCanal[0])  # cantidad de columnas originales
        nueva_cantidad = n - 1  # porque col1 y col2 se combinarán en una

        # Inicializamos Q con ceros
        canalDeterminante = [[0 for _ in range(nueva_cantidad)] for _ in range(n)]

        nueva_columna = 0
        for j in range(n):
            if j == col2:
                # la columna col2 se combina con col1 (ya la representamos)
                continue
            if j == col1:
                # columna combinada → ponemos un 1 en su nueva posición
                canalDeterminante[col1][nueva_columna] = 1
                canalDeterminante[col2][nueva_columna] = 1
            else:
                # columnas que no se combinan → mantienen su lugar
                canalDeterminante[j][nueva_columna] = 1
            nueva_columna += 1

    return canalDeterminante

matCanal = [
    [0.0, 0.5, 0.0, 0.5],
    [0.8, 0.0, 0.2, 0.0],
    [0.0, 0.5, 0.0, 0.5],
    [0.8, 0.0, 0.2, 0.0]
]

canalDeterminante = generaCanalDeterminante(matCanal, 1, 3)
print("Matriz del canal determinante:", canalDeterminante)

