import math
import random

def devuelve_ProbsBj(probs_aPriori, matCondicionales):
    # P(bj) = Sumatoria (p(a) * Pij)
    listaProbs = []
    for j in range(len(matCondicionales[0])):
        acumCol = 0
        for i in range(len(probs_aPriori)):
            acumCol += probs_aPriori[i] * matCondicionales[i][j]
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
    
    