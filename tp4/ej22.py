import math
#Funcion que devuelve distancia de Hamming
#los errores que se pueden detectar, y la
#cantidad de errores que se pueden corregir

def getDistancia(lista_cadenas):
    
    n = len(lista_cadenas)
    distancias = []
    for i in range(n):
        palabra_codigo = lista_cadenas[i]
        for j in range(i+1,n):
            contDistintos = 0
            palabra_codigoNext = lista_cadenas[j]
            for k in range(len(palabra_codigo)):
                if palabra_codigo[k] != palabra_codigoNext[k]:
                    contDistintos += 1
            distancias.append(contDistintos)
    
    print(" ")
    distanciaHamming = min(distancias)
    deteccionErrores = round(distanciaHamming - 1)
    erroresCorregibles =  round(deteccionErrores / 2)
    return distanciaHamming, deteccionErrores, erroresCorregibles

#Ejercicio 21
#codigo1 = ['00', '01', '10', '11']
#distanciaHamming1, deteccionErrores1, erroresCorregibles1 = getDistancia(codigo1)
#print("Distancia Hamming ->", distanciaHamming1)
#print("Deteccion de errores ->", deteccionErrores1)
#print("Errores corregibles ->", erroresCorregibles1)       
                
#codigo2 = ['000', '100', '101', '111']
#distanciaHamming2, deteccionErrores2, erroresCorregibles2 = getDistancia(codigo2)
#print("Distancia Hamming ->", distanciaHamming2)
#print("Deteccion de errores ->", deteccionErrores2)
#print("Errores corregibles ->", erroresCorregibles2)         

#codigo3 = ['0000', '0011', '1010', '0101']
#distanciaHamming3, deteccionErrores3, erroresCorregibles3 = getDistancia(codigo3)
#print("Distancia Hamming ->", distanciaHamming3)
#print("Deteccion de errores ->", deteccionErrores3)
#print("Errores corregibles ->", erroresCorregibles3) 

#Ejercicio 23
codigo1 =  ['0100100', '0101000', '0010010', '0100000']
distanciaHamming1, deteccionErrores1, erroresCorregibles1 = getDistancia(codigo1)
print("Distancia Hamming ->", distanciaHamming1)
print("Deteccion de errores ->", deteccionErrores1)
print("Errores corregibles ->", erroresCorregibles1)

codigo2 = ['0100100', '0010010', '0101000', '0100001']
distanciaHamming2, deteccionErrores2, erroresCorregibles2 = getDistancia(codigo2)
print("Distancia Hamming ->", distanciaHamming2)
print("Deteccion de errores ->", deteccionErrores2)
print("Errores corregibles ->", erroresCorregibles2)


codigo3 = ['0110000', '0000011', '0101101', '0100110']
distanciaHamming3, deteccionErrores3, erroresCorregibles3 = getDistancia(codigo3)
print("Distancia Hamming ->", distanciaHamming3)
print("Deteccion de errores ->", deteccionErrores3)
print("Errores corregibles ->", erroresCorregibles3)