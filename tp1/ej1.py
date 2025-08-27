import math

distribuciones = [0.25, 0.40, 0.50, 0.75]
lista_informacion = []

def cantInfo(p, r):
    if p <= 0 or p > 1:
        return 0
    else:
        return math.log(1/p, r)
    
def entropia(distribuciones):
    e = 0
    for d in distribuciones:
        e += d * cantInfo(d, 2)
    return e

lista_informacion = [cantInfo(d, 2) for d in distribuciones]

print(lista_informacion)
print("Entropia de la fuente: ", entropia(distribuciones))


