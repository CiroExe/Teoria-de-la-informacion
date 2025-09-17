import math
#Inciso A
def getAlfabetoCodigo(lista_palabraCod):
    max_long = 0
    n = len(lista_palabraCod)
    alfabetoCod = []

    for i in range(n):
        if(len(lista_palabraCod[i]) < 2 and lista_palabraCod[i] not in alfabetoCod):
            alfabetoCod.append(lista_palabraCod[i])
        else:
            palabraCod = lista_palabraCod[i]
            for j in range(len(palabraCod)):
                if(palabraCod[j] not in alfabetoCod):
                    alfabetoCod.append(palabraCod[j])

    return alfabetoCod
lista_palabraCod=['A', 'AB', 'ABC', 'DBA', 'EFG']
print("Lista original de las palabras codigo: ", lista_palabraCod)
print("Alfabeto de la lista de palabras codigo: ", getAlfabetoCodigo(lista_palabraCod))

#Inciso B
lista_longitudes = [len(lista_palabraCod[i]) for i in range(len(lista_palabraCod))]
print("Lista de longitudes: ", lista_longitudes)

#Inciso C
def inecuacionKraft(lista_longitudes, r):
    n = len(lista_longitudes)
    acum = 0
    for i in range(n):
        print(i)
        acum += pow(r, -lista_longitudes[i])

    return acum

print("Inecuacion de Kraft: ", inecuacionKraft(lista_longitudes, 2))
