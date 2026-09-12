import math
from ej14 import vector_estacionario, calcular_entropia_fuente
#Inciso A

def getAlfabeto(mensaje):
    alfabeto = []
    for c in mensaje:
        if c not in alfabeto:
            alfabeto.append(c)
    return alfabeto


def getMatTransicion(mensaje):
    alfabeto = getAlfabeto(mensaje)
    n = len(alfabeto)
    indice = {simbolo: i for i, simbolo in enumerate(alfabeto)}

    # Matriz de conteo inicializada en ceros
    mat_conteo = [[0] * n for _ in range(n)]

    # Conteo de digramas: Origen = col, Destino = fila
    for i in range(len(mensaje) - 1):
        origen = mensaje[i]
        destino = mensaje[i + 1]
        col = indice[origen]
        fila = indice[destino]
        mat_conteo[fila][col] += 1

    # Normalización: cada columna suma 1
    mat_trans = [[0.0] * n for _ in range(n)]
    for j in range(n):  # j = Columna (Origen)
        total_salidas = sum(mat_conteo[k][j] for k in range(n))
        for i in range(n):  # i = Fila (Destino)
            if total_salidas > 0:
                mat_trans[i][j] = mat_conteo[i][j] / total_salidas
            else:
                mat_trans[i][j] = 0.0

    return mat_trans


def es_memoria_nula(mat_trans, tol=0.15):
    n = len(mat_trans)
    for j in range(1, n):
        for i in range(n):
            if abs(mat_trans[i][j] - mat_trans[i][0]) > tol:
                return False
    return True