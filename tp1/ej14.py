import math

#Inciso A
def vector_estacionario(P, tol=1e-8, max_iter=1000):
    n = len(P)
    v = [1/n] * n
    for k in range(max_iter):
        nuevo_v = []
        for i in range(n):
            suma = 0
            for j in range(n):
                suma += v[j] * P[j][i]
            nuevo_v.append(suma)
        #Verifico si el nuevo vector estacionario esta lo suficientemente cerca del anterior
        
        aux = 0
        for j in range(n):
            aux += abs(nuevo_v[i] - v[i])
            
        if (aux <= tol):
            return nuevo_v
        
        v = nuevo_v
    return v

P = [
    [0.6, 0.3, 0.1],  
    [0.2, 0.5, 0.3],  
    [0.1, 0.2, 0.7]   
]

v_estacionario = vector_estacionario(P)
print("Vector estacionario:", v_estacionario)

#Inciso b

def calculaEntropia(vec_estacionario, mat):
    n = len(vec_estacionario)
    H = 0  # Entropía total

    for i in range(n):
        entropia_condicional = 0
        for j in range(n):
            p_ij = mat[i][j]
            if p_ij > 0:
                entropia_condicional += p_ij * math.log2(p_ij)
        H += vec_estacionario[i] * entropia_condicional

    return -H

H = calculaEntropia(v_estacionario, P)

print("Entropía de la fuente:", H)