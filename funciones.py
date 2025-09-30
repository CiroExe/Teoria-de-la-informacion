import math
import random

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
  


def getMatTransicion(mensaje):
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

def getAlfabeto(mensaje):
    alfabeto = []
    for i in range(len(mensaje)):
        if mensaje[i] not in alfabeto:
            alfabeto.append(mensaje[i])
    alfabeto = sorted(alfabeto)
    return alfabeto

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


def entropia(distribuciones, r):
    return sum(distribuciones[i] * math.log(1/distribuciones[i], r) for i in range(len(distribuciones)))

def longitud_media(distribucion, longitudes):
    return sum(distribucion[i] * longitudes[i] for i in range(len(longitudes)))

def CalculaR(codigo):
    return max(len(codigo[i]) for i in range(len(codigo)))

def inecuacionKraft(longitudes, r):
    return sum(math.pow(r, -longitudes[i]) for i in range(len(longitudes)))


def NoSingular(lista):
    
    for i in range(len(lista)):
        x = lista[i]
        for j in range (len(lista)):
            if(i != j and x == lista[j]):
                return False
    return True
        
                        
def Instantaneo(lista):
    n=len(lista)
    for i in range(n):
        x = lista[i]
        for j in range(n):
            if(i != j and lista[j].startswith(x)):
                return False #Instantaneo, pues existe al menos una palabra codigo que tiene como prefijo a x
    return  #Devuelve falso por defecto


def UD(lista):
    vec_act = lista.copy()   # códigos actuales que se procesan
    new_s = []               # sufijos generados en la iteracion actual

    # Repetimos mientras haya sufijos que procesar, osea mientras vec_act no este vacio
    while vec_act:
        next_s = []  # sufijos generados en esta iteracion

        # Generar sufijos a partir de los codigos actuales
        for i in range(len(vec_act)):
            x = vec_act[i]

            for j in range(len(lista)):
                y = lista[j]  # siempre comparar con la lista original
                if x != y and y.startswith(x):
                    sufijo = y[len(x):]  # obtener el sufijo restante
                    if sufijo not in next_s:  # agregar solo si no está
                        next_s.append(sufijo)

        print(next_s)  #debug 

        # si algún sufijo coincide con un código original => no UD
        if set(lista) & set(next_s):
            return False

        if not next_s:  # si no se generaron sufijos nuevos => UD
            return True

        vec_act = next_s  # iterar con los sufijos generados
