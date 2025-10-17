import math
#Codificar una función booleana en Python que reciba como parámetros: una lista con la
#distribución de probabilidades de una fuente, otra lista con palabras código para la
#extensión de orden N y el valor de N, y verifique si el código cumple con el Primer Teorema
#de Shannon

def CalculaR(codigo):
    return max(len(codigo[i]) for i in range(len(codigo)))


def generarListaExtension(alfabeto, probs, grado):
    cantFilas = len(alfabeto) ** grado
    listaExtension = ["" for _ in range(cantFilas)]
    listaExtensionProb = [1 for _ in range(cantFilas)]
    
    for i in range(grado):  # los n símbolos
        tamanioParticion = len(alfabeto) ** (grado - (i + 1))
        for j in range(cantFilas):  # iterar sobre todas las filas
            elemIndex = (j // tamanioParticion) % len(alfabeto)
            listaExtension[j] += alfabeto[elemIndex]
            listaExtensionProb[j] *= probs[elemIndex]
    
    # redondear probabilidades a 2 decimales
    listaExtensionProb = [round(p, 2) for p in listaExtensionProb]
    
    return listaExtension, listaExtensionProb

def cumpleTeoremaShannon(distribucion, palabras_codigo, n, r):
    H = 0
    H = sum(distribucion[i] * math.log(1/distribucion[i], r) for i in range(len(distribucion)))
    print("Entropia-> ",H/n)
    L = sum(distribucion[i] * len(palabras_codigo[i]) for i in range(len(distribucion)))
    print("Longitud media -> ",L)
    return H <= L < H + 1
    
#alfabeto = ['A', 'B', 'C']
#distribucion = [0.5, 0.2, 0.3]
#C1 = ['11', '010', '00']
#cumpleTeoremaShannon(distribucion, C1, 1,2)
#C2 = ['10', '001', '110', '010', '0000', '0001', '111', '0110', '0111']
#alfabetoExtension,distribucionExtension = generarListaExtension(alfabeto, distribucion, 2)
#cumpleTeoremaShannon(distribucionExtension, C2, 2, 2)

alfabeto = ['1', '0']
distribucion = [0.7, 0.3]
#alfabetoBinarioExtension, distribucionBinariaExtension = generarListaExtension(alfabeto, distribucion, 3)
#print(cumpleTeoremaShannon(distribucionBinariaExtension, alfabetoBinarioExtension, 3, 2))


