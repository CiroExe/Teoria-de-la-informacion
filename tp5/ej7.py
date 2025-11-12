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

import math

#Ejercicio 11
def entropia_a_posteriori(probs_a_priori, canal):
    n = len(canal[0])  # número de salidas
    probsBj = devuelve_ProbsBj(probs_a_priori, canal)  # P(Yj)
    
    lista_entropia_a_posteriori = []
    
    for j in range(n):
        sumatoria = 0
        prob_a_posteriori = 0
        for i in range(len(probs_a_priori)):
            if(probsBj[j] > 0):
                prob_a_posteriori = (canal[i][j] * probs_a_priori[i]) / probsBj[j]
            if prob_a_posteriori > 0:
                sumatoria += prob_a_posteriori * math.log2(1 / prob_a_posteriori)
       # print("H(A/b=",j,") ", round(sumatoria, 4))
        lista_entropia_a_posteriori.append(round(sumatoria, 4))
        
    return lista_entropia_a_posteriori

def equivocacion(probs_a_priori, canal):
    probsBj = devuelve_ProbsBj(probs_a_priori, canal)
    H_a_posteriori = entropia_a_posteriori(probs_a_priori, canal)
    
    sumatoria = 0
    for j in range(len(probsBj)):
        sumatoria += probsBj[j]*H_a_posteriori[j]
    return sumatoria

def perdida(probs_aPriori, canal):
    # H(B/A)
    suma = 0
    for i in range(len(probs_aPriori)):
        for j in range(len(canal[0])):
            p_ab = probs_aPriori[i] * canal[i][j]
            if p_ab > 0:
                suma += p_ab * math.log2(1/canal[i][j])
    return round(suma, 4)

def informacion_mutua(probs_aPriori, canal):
    # I(A;B)
    probsBj = devuelve_ProbsBj(probs_aPriori, canal)
    suma = 0
    for i in range(len(probs_aPriori)):
        for j in range(len(canal[0])):
            p_ab = probs_aPriori[i] * canal[i][j]
            if p_ab > 0:
                suma += p_ab * math.log2(p_ab / (probs_aPriori[i]*probsBj[j]))
    return round(suma, 4)


def entropia_afin(probs_aPriori, canal):
    # H(A,B)
    suma = 0
    for i in range(len(probs_aPriori)):
        for j in range(len(canal[0])):
            p = probs_aPriori[i] * canal[i][j]
            if p > 0:
                suma += p * math.log2(1/p)
    return round(suma, 4)

#probs_a_prioriC1 = [0.14, 0.52, 0.34]
#P_C1 = [
  #[0.50, 0.30, 0.20],
  #[0.00, 0.40, 0.60],
 # [0.20, 0.80, 0.00]
#]
#entropia_a_posteriori(probs_a_prioriC1, P_C1)

#print(entropia_a_posteriori(probs_a_prioriC1, P_C1))
#print(" ")
#probs_a_prioriC2 = [0.25, 0.25, 0.50]
#P_C2 = [
#  [0.25, 0.25, 0.25, 0.25],
#  [0.25, 0.25, 0.00, 0.50],
#  [0.50, 0.00, 0.50, 0.00]
#]
#entropia_a_posteriori(probs_a_prioriC2, P_C2)
##print(entropia_a_posteriori(probs_a_prioriC2, P_C2))

#print(" ")
#probs_a_prioriC3 = [0.12, 0.24, 0.14, 0.50]
#P_C3 = [
#  [0.25, 0.15, 0.30, 0.30],
#  [0.23, 0.27, 0.25, 0.25],
#  [0.10, 0.40, 0.25, 0.25],
#  [0.34, 0.26, 0.20, 0.20]
#]
#entropia_a_posteriori(probs_a_prioriC3, P_C3)
#print(entropia_a_posteriori(probs_a_prioriC3, P_C3))

#Pruebas ejercicio 11
p_C1 = [0.70, 0.30]
P_C1 = [
  [0.7, 0.3],
  [0.4, 0.6]
]

p_C2 = [0.50, 0.50]
P_C2 = [
  [0.3, 0.3, 0.4],
  [0.3, 0.3, 0.4]
]


p_C3 = [0.25, 0.50, 0.25]
P_C3 = [
  [1.0, 0.0, 0.0, 0.0],
  [0.0, 0.5, 0.5, 0.0],
  [0.0, 0.0, 0.0, 1.0]
]

p_C4 = [0.25, 0.25, 0.25, 0.25]
P_C4 = [
  [1.0, 0.0, 0.0, 0.0],
  [0.0, 1.0, 0.0, 0.0],
  [0.0, 1.0, 1.0, 0.0],
  [0.0, 0.0, 0.0, 1.0]
]
print("C1")
print("H(A/B)", equivocacion(p_C1, P_C1))
print("H(B/A)", perdida(p_C1, P_C1))
print("H(A,B)", entropia_afin(p_C1, P_C1))
print("I(A,B)", informacion_mutua(p_C1, P_C1))

print(" ")

print("C2")
print("H(A/B)", equivocacion(p_C2, P_C2))
print("H(B/A)", perdida(p_C2, P_C2))
print("H(A,B)", entropia_afin(p_C2, P_C2))
print("I(A,B)", informacion_mutua(p_C2, P_C2))

print(" ")
print("C3")
print("H(A/B)", equivocacion(p_C3, P_C3))
print("H(B/A)", perdida(p_C3, P_C3))
print("H(A,B)", entropia_afin(p_C3, P_C3))
print("I(A,B)", informacion_mutua(p_C3, P_C3))

print(" ")
print("C4")
print("H(A/B)", equivocacion(p_C4, P_C4))
print("H(B/A)", perdida(p_C4, P_C4))
print("H(A,B)", entropia_afin(p_C4, P_C4))
print("I(A,B)", informacion_mutua(p_C4, P_C4))