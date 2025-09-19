import math
codigo= ["011", "000", "010", "101", "001", "100"]
probs = [0.166666666]*6 #Supongo una distribucion uniforme de las probabilidades
print(probs)
longitud = [len(codigo[i]) for i in range(len(codigo))]


def longitud_media(longitudes, distribuciones):
   return sum(longitudes[i] *distribuciones[i] for i in range(len(longitudes)))

def entropia(distribuciones, r):
   return sum([distribuciones[i] * math.log(1/distribuciones[i], 3) for i in range(len(distribuciones))])


r = len(set("".join(codigo)))
H = entropia(probs, r)
L = longitud_media(longitud, probs)
print(H)
print(L)

def esCompacto(H, L):
   cumple = False
   #Podria considerar una tolerancia para verificar que sea compacto
   if (H<=L):
      cumple = True
   return cumple

print(esCompacto(H,L))
