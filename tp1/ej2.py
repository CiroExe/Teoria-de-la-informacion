import random
#INCISO A
def getListas(mensaje):
    n = len(mensaje)
    alfabeto = [c for i, c in enumerate(mensaje) if mensaje.index(c) == i]
    probabilidades = [mensaje.count(c) / n for c in alfabeto]
    return alfabeto, probabilidades
    
mensaje = 'BDAACAABACADAABDAADABDAAABDCDCDCDC'
alfabeto, alfabeto_probs = getListas(mensaje)
print(alfabeto)
print(alfabeto_probs)

#INCISO B
def generaCadena(n, alfabeto, alfabeto_probs):
    #Genera una lista de longitud n segun las probabilidades asignadas
    return "".join(random.choices(alfabeto, weights=alfabeto_probs, k=n))

n = int(input("Ingese un numero entero N: "))
cadena_simulada= generaCadena(n, alfabeto, alfabeto_probs)
print(cadena_simulada)