def getProbs(mensaje):
    mensaje = sorted(mensaje)
    n = len(mensaje)
    probs = []
    
    letraAct = mensaje[0]
    contAct = 1
    i = 1
    while i < n:
        if(mensaje[i] != letraAct):
            probs.append(round(contAct / n, 3))
            letraAct = mensaje[i]
            contAct = 1
        else:
            contAct += 1
        i+=1
    probs.append(round(contAct / n, 3))
    return probs

def getAlfabeto(mensaje):
    return sorted(set(mensaje))

def getApariciones(mensaje):
    apariciones = {}
    for c in mensaje:
        if c in apariciones:
            apariciones[c] += 1
        else:
            apariciones[c] = 1
    return sorted(apariciones.items())


def retorna_matriz_transicion_canal(entrada, salida):
    n = len(entrada)
    alfabeto_entrada = sorted(getAlfabeto(entrada))
    alfabeto_salida = sorted(getAlfabeto(salida))
    apariciones = getApariciones(entrada)  # lista de tuplas [('a',11),...]

    prob_condicional = []

    for letra in alfabeto_entrada:
        # obtener la cantidad de apariciones de esta letra en 'entrada'
        cant_letra = next(cant for l, cant in apariciones if l == letra)
        
        fila = []
        for letra_salida in alfabeto_salida:
            cont = 0
            # contar cuántas veces aparece la letra_salida cuando la entrada es 'letra'
            for i in range(n):
                if entrada[i] == letra and salida[i] == letra_salida:
                    cont += 1
            fila.append(round(cont / cant_letra, 3))
        
        prob_condicional.append(fila)
    
    return prob_condicional

def devuelve_ProbsBj(probs_aPosteriori, matCondicionales):
    # P(bj) = Sumatoria (p(a) * Pij)
    listaProbs = []
    for j in range(len(matCondicionales[0])):
        acumCol = 0
        for i in range(len(probs_aPosteriori)):
            acumCol += probs_aPosteriori[i] * matCondicionales[i][j]
        listaProbs.append(round(acumCol, 3))
    return listaProbs

def getMatAPosteriori(probs_aPriori, matCondicionales):
    mat = []
    probsBj = devuelve_ProbsBj(probs_aPriori, matCondicionales)
    
    for i in range(len(probs_aPriori)):
        fila_mat = []
        for j in range(len(matCondicionales[0])):
            fila_mat.append(round((matCondicionales[i][j]*probs_aPriori[i]) / probsBj[j], 3))
        mat.append(fila_mat)
    return mat

def getMatEventosSimultaneos(probs_aPriori, matCondicionales):
    probsAPosteriori = getMatAPosteriori(probs_aPriori, matCondicionales)
    probsBj = devuelve_ProbsBj(probs_aPriori, matCondicionales)
    n = len(probs_aPriori) #Cantidad de filas
    m = len(matCondicionales[0]) #Cantidad de columnas
    mat = []
    
    for i in range(n):
        fila_mat = []
        for j in range(m):
            fila_mat.append(round(probsAPosteriori[i][j]*probsBj[j], 3))
        mat.append(fila_mat)
    return mat

secuencia_entrada  = '1101011001101010010101010100011111'
secuencia_salida   = '1001111111100011101101010111110110'
secuencia_entrada2 = '110101100110101100110101100111110011'
secuencia_salida2  = '110021102110022010220121122100112011'
secuencia_entrada3 = 'abcacaabbcacaabcacaaabcaca'
secuencia_salida3  = '01010110011001000100010011'
#print(getProbs(secuencia_entrada))
#print(getApariciones(secuencia_salida))
mat = retorna_matriz_transicion_canal(secuencia_entrada, secuencia_salida)
mat2 = retorna_matriz_transicion_canal(secuencia_entrada2, secuencia_salida2)
mat3 = retorna_matriz_transicion_canal(secuencia_entrada3, secuencia_salida3)
#print(retorna_matriz_transicion_canal(secuencia_entrada, secuencia_salida))
#print(retorna_matriz_transicion_canal(secuencia_entrada2, secuencia_salida2))
#probsSalida = devuelve_ProbsBj(getProbs(secuencia_entrada2), mat2)
#print(probsSalida)
matAPosteriori3= getMatAPosteriori(getProbs(secuencia_entrada3), mat3)
print("P(ai/bj) ",matAPosteriori3)

matAPosteriori = getMatAPosteriori(getProbs(secuencia_entrada), mat)
print("P(ai/bj) ",matAPosteriori)

matAPosteriori2= getMatAPosteriori(getProbs(secuencia_entrada2), mat2)
print("P(ai/bj) ",matAPosteriori2)


matSimultaneos3 = getMatEventosSimultaneos(getProbs(secuencia_entrada3), mat3)
print("P(ai, bj) ", matSimultaneos3)

matSimultaneos = getMatEventosSimultaneos(getProbs(secuencia_entrada), mat)
print("P(ai, bj) ",matSimultaneos)

matSimultaneos2 = getMatEventosSimultaneos(getProbs(secuencia_entrada2), mat2)
print("P(ai, bj) ", matSimultaneos2)
