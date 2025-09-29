import math
#Inciso A

def vector_estacionario(P, tol=0.01, max_iter=1000):
    n = len(P)
    v = [1/n] * n  # distribución inicial uniforme

    for k in range(max_iter):
        nuevo_v = []
        for i in range(n):
            suma = 0
            for j in range(n):
                suma += v[j] * P[i][j]  
            nuevo_v.append(suma)

        # Normalizar para evitar errores numéricos
        total = sum(nuevo_v)
        nuevo_v = [x / total for x in nuevo_v]

        # Verificar tolerancia
        aux = 0
        for j in range(n):
            aux += abs(nuevo_v[j] - v[j])
        if aux <= tol:
            return nuevo_v

        v = nuevo_v

    return v

def calculaEntropiaVecEstacionario(vec_estacionario, mat):
    n = len(vec_estacionario)
    H = 0
    for i in range(n):
        entropia_condicional = 0
        for j in range(n):
            p_ji = mat[j][i]
            if p_ji > 0:
                entropia_condicional += p_ji * math.log2(1/p_ji)
        H += vec_estacionario[i] * entropia_condicional
    return H
def getAlfabeto(mensaje):
    alfabeto = []
    for i in range(len(mensaje)):
        if mensaje[i] not in alfabeto:
            alfabeto.append(mensaje[i])
    alfabeto = sorted(alfabeto)
    return alfabeto

def getMatConteo(alfabeto):
   mat_conteo = []
   for i in range(len(alfabeto)):
        fila_conteo = []
        for j in range(len(alfabeto)):
            fila_conteo.append(0)
        mat_conteo.append(fila_conteo)
   return mat_conteo
  


def incisoA(mensaje):
    alfabeto = getAlfabeto(mensaje)

    mat_conteo = getMatConteo(alfabeto)

    # mapear simbolos a indices
    indice = {}
    for i in range(len(alfabeto)):
        simbolo = alfabeto[i]
        indice[simbolo] = i

    for i in range(len(mensaje)-1):
        letra_origen = mensaje[i]
        letra_destino = mensaje[i+1]
        fila = indice[letra_origen]
        col = indice[letra_destino]
        mat_conteo[fila][col] += 1

    #genero la matriz de transicion de probabilidades
    mat_trans = []
    for i in range(len(alfabeto)):
        fila_trans = []
        acum_fila = 0
        for j in range(len(alfabeto)):
            acum_fila += mat_conteo[i][j]

        for j in range (len(alfabeto)):
            if acum_fila == 0:
                mat_trans.append(0)
            else:
                fila_trans.append(round((mat_conteo[i][j] / acum_fila), 4))
        mat_trans.append(fila_trans)
    return  mat_trans


def es_memoria_nula(mat, tol=0.1):
    n = len(mat)
    
    for i in range(n - 1):  # hasta la penúltima fila
        for j in range(len(mat[i])):
            dif = abs(mat[i][j] - mat[i+1][j])
            if dif > tol:
                return False
    return True

mensaje ='BBAAACCAAABCCCAACCCBBACCAABBAA'
mat_trans = incisoA(mensaje)
print("Memoria nula?", es_memoria_nula(mat_trans))

v_est = vector_estacionario(incisoA(mensaje))
print("Entropia->", calculaEntropiaVecEstacionario(v_est, mat_trans))
print(mat_trans)