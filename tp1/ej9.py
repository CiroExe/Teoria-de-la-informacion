import ej8
#ω = 0.25 b. ω = 0.75 c. ω = 0.5 d. ω = 1 e. ω = 0
w1 = 0.25
w2 = 0.75
w3 = 0.5
w4 = 1
w5 = 0

Binary_H1 = ej8.CalculaEntropiaBinaria(w1)
Binary_H2 = ej8.CalculaEntropiaBinaria(w2)
Binary_H3 = ej8.CalculaEntropiaBinaria(w3)
Binary_H4 = ej8.CalculaEntropiaBinaria(w4)
Binary_H5 = ej8.CalculaEntropiaBinaria(w5)

print("Entropía para ω = 0.25:", Binary_H1)
print("Entropía para ω = 0.75:", Binary_H2)
print("Entropía para ω = 0.5:", Binary_H3)
print("Entropía para ω = 1:", Binary_H4)
print("Entropía para ω = 0:", Binary_H5)