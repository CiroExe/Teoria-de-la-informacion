import math
def inecuacionKraft(lista_longitudes, r):
    n = len(lista_longitudes)
    acum = 0
    for i in range(n):
        acum += pow(r, -lista_longitudes[i])

    return acum

#Ejercicio 7 
codigo1 = ["011", "000", "010", "101", "001", "100"]
longitud1 = [len(codigo1[i]) for i in range(len(codigo1))]
print("Inecuacion de Kraft para codigo 1: ", inecuacionKraft(longitud1, 2))
codigo2 = ["110", "100", "101", "001", "110", "010"]
longitud2 = [len(codigo2[i]) for i in range(len(codigo2))]
print("Inecuacion de Kraft para codigo 2: ", inecuacionKraft(longitud2, 2))
codigo3 = ["10", "1100", "0101", "1011", "0", "110"]
longitud3 = [len(codigo3[i]) for i in range(len(codigo3))]
print("Inecuacion de Kraft para codigo 3: ", inecuacionKraft(longitud3, 2))
codigo4 = ["1101", "10", "1111", "1100", "1110", "0"]
longitud4 = [len(codigo4[i]) for i in range(len(codigo4))]
print("Inecuacion de Kraft para codigo 4: ", inecuacionKraft(longitud4, 2))
codigo5 = ["011", "0111", "01", "0", "011111", "01111"]
longitud5 = [len(codigo5[i]) for i in range(len(codigo5))]
print("Inecuacion de Kraft para codigo 5: ", inecuacionKraft(longitud5, 2))
codigo6 = ["1110", "0", "110", "1101", "1011", "10"]
longitud6 = [len(codigo6[i]) for i in range(len(codigo6))]
print("Inecuacion de Kraft para codigo 6: ", inecuacionKraft(longitud6, 2))

#Ejercicio 8

codigo7 = ["==", "<", "<=", ">", ">=", "<>"]
longitud7 = [len(codigo7[i]) for i in range(len(codigo7))]
print("Inecuacion de Kraft para codigo 7: ", inecuacionKraft(longitud7, 2))

codigo8 = [")", "[]", "]]", "([", "[()]", "([])"]
longitud8 = [len(codigo8[i]) for i in range(len(codigo8))]
print("Inecuacion de Kraft para codigo 8: ", inecuacionKraft(longitud8, 2))

codigo9 = ["/", "*", "-", "*", "++", "+-"]
longitud9 = [len(codigo9[i]) for i in range(len(codigo9))]
print("Inecuacion de Kraft para codigo 9: ", inecuacionKraft(longitud9, 2))

codigo10 = [".,", ";", ",,", ":", "...", ".;:"]
longitud10 = [len(codigo10[i]) for i in range(len(codigo10))]
print("Inecuacion de Kraft para codigo 10: ", inecuacionKraft(longitud10, 2))