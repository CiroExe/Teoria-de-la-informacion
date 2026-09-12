import math


def vector_estacionario(P, tol=1e-8, max_iter=1000):
    n = len(P)
    v = [1 / n] * n

    for k in range(max_iter):
        nuevo_v = []
        for i in range(n):
            # M * v: Fila i de la matriz por el vector v
            suma = sum(P[i][j] * v[j] for j in range(n))
            nuevo_v.append(suma)

        aux = sum(abs(nuevo_v[j] - v[j]) for j in range(n))

        if aux <= tol:
            return nuevo_v

        v = nuevo_v
    return v


def calcular_entropia_fuente(vector_estacionario, mat):
    """Calcula la entropía de orden 1 ponderada por v* (Columna = Origen)."""
    n = len(mat)
    h = 0.0

    for j in range(n):  # j = Estado Origen (Columna j)
        h_estado = 0.0
        for i in range(n):  # i = Estado Destino (Fila i)
            p_ij = mat[i][j]
            if p_ij > 0:
                h_estado -= p_ij * math.log2(p_ij)

        h += vector_estacionario[j] * h_estado

    return h


def calcular_entropia_memoria_nula(mensaje, alfabeto):
    """Calcula H0 a partir de las frecuencias individuales del mensaje correspondiente."""
    total = len(mensaje)
    h = 0.0
    for s in alfabeto:
        p = mensaje.count(s) / total
        if p > 0:
            h -= p * math.log2(p)
    return h