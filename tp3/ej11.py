import math
def maxLong(codigo):
    return max(len(x) for x in codigo)

def cantInfo(p, r):
    if p <= 0 or p > 1:
        return 0
    else:
        return math.log(1/p, r)
    
def entropia(distribuciones, r):
    H = 0
    for d in distribuciones:
        H += d * cantInfo(d, r)
    return H

def LongitudMedia(distribuciones, longitudes):
    n=len(longitudes)
    L = 0
    for i in range(n):
        L += distribuciones[i] * longitudes[i]
    return L

codigo = ["==", "<", "<=", ">", ">=", "<>"]
longitud = [len(codigo[i]) for i in range(len(codigo))]
r = maxLong(codigo)
print("Maxima longitud", r)
probs_codigo = [0.10, 0.50, 0.10, 0.20, 0.05, 0.05]
print("Entropia: ", entropia(probs_codigo, r))
print("Longitud media : ", LongitudMedia(probs_codigo, longitud))
