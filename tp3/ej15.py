import math

#Funciones
def esCompacto(H, L):
   cumple = False
   #Podria considerar una tolerancia para verificar que sea compacto
   if (H<=L):
      cumple = True
   return cumple


def longitud_media(longitudes, distribuciones):
   return sum(longitudes[i] *distribuciones[i] for i in range(len(longitudes)))

def entropia(distribuciones, r):
   return sum([distribuciones[i] * math.log(1/distribuciones[i], 3) for i in range(len(distribuciones))])

def calculaR(codigo):
   return len(set("".join(codigo)))


#Codigos del ejercicio 8
codigo1 = ["==", "<", "<=", ">", ">=", "<>"]
longitud1 = [len(codigo1[i]) for i in range(len(codigo1))]


codigo2 = [")", "[]", "]]", "([", "[()]", "([])"]
longitud2 = [len(codigo2[i]) for i in range(len(codigo2))]


codigo3 = ["/", "*", "-", "*", "++", "+-"]
longitud3 = [len(codigo3[i]) for i in range(len(codigo3))]


codigo4 = [".,", ";", ",,", ":", "...", ".;:"]
longitud4 = [len(codigo4[i]) for i in range(len(codigo4))]


#Declaraciones
probs_codigo = [0.10, 0.50, 0.10, 0.20, 0.05, 0.05]
r = calculaR(codigo1)
print(r)
H = entropia(probs_codigo, r)
L = longitud_media(longitud1, probs_codigo)
print("Codigo 1",esCompacto(H,L))

r = calculaR(codigo2)
print(r)
H = entropia(probs_codigo, r)
L = longitud_media(longitud2, probs_codigo)
print("Codigo 2",esCompacto(H,L))

r = calculaR(codigo3)
print(r)
H = entropia(probs_codigo, r)
L = longitud_media(longitud3, probs_codigo)
print("Codigo 3",esCompacto(H,L))

r = calculaR(codigo4)
print(r)
H = entropia(probs_codigo, r)
L = longitud_media(longitud4, probs_codigo)
print("Codigo 4",esCompacto(H,L))
