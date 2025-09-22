import math

#Funciones

def Instantaneo(lista):
    n=len(lista)
    for i in range(n):
        x = lista[i]
        for j in range(n):
            if(i != j and lista[j].startswith(x)):
                return False #Instantaneo, pues existe al menos una palabra codigo que tiene como prefijo a x
    return True #Devuelve falso por defecto

def esCompacto(longitudes, codigo, probabilidades, r):
   if Instantaneo(codigo):
      cumple = True
      i = 0
      while i < len(longitudes) and cumple:
         limite_superior = math.ceil(-math.log(probabilidades[i], r))
         if longitudes[i] > limite_superior:
            cumple = False
         i += 1
   else:
      cumple = False
   return cumple

def longitud_media(longitudes, distribuciones):
   return sum(longitudes[i] *distribuciones[i] for i in range(len(longitudes)))

def entropia(distribuciones, r):
   return sum([distribuciones[i] * math.log(1/distribuciones[i], r) for i in range(len(distribuciones))])

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
print("Codigo 1",esCompacto(longitud1, codigo1, probs_codigo, r))

r = calculaR(codigo2)
print(r)
H = entropia(probs_codigo, r)
L = longitud_media(longitud2, probs_codigo)
print("Codigo 2",esCompacto(longitud2, codigo2, probs_codigo, r))

r = calculaR(codigo3)
print(r)
H = entropia(probs_codigo, r)
L = longitud_media(longitud3, probs_codigo)
print("Codigo 3",esCompacto(longitud3, codigo3, probs_codigo, r))

r = calculaR(codigo4)
print(r)
H = entropia(probs_codigo, r)
L = longitud_media(longitud4, probs_codigo)
print("Codigo 4",esCompacto(longitud4, codigo4, probs_codigo, r))
