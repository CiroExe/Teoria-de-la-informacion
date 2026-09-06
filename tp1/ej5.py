import ej1, ej2

mensaje = 'BDAACAABACADAABDAADABDAAABDCDCDCDC'
alfabeto, alfabeto_probs = ej2.getListas(mensaje)
H = ej1.calculaEntropia(alfabeto_probs)
print("Alfabeto: ",alfabeto)
print("Probabilidad de aparicion de cada simbolo: ",alfabeto_probs)
print("Entropia de la fuente: H(S)= ", H)
