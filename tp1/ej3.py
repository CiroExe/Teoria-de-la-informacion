from ej1 import calculaEntropia
import math

probabilidades_dado = [1/6,1/6,1/6,1/6,1/6,1/6]
probabilidades_dado2= [1/9, 1/6, 1/9, 1/9, 1/6, 1/3]
H1 = calculaEntropia(probabilidades_dado)
H2 = calculaEntropia(probabilidades_dado2)
print("Entropia con probabilidades equiprobables: ", H1)
print("Entropia con probabilidades distintas: ", H2)
print("Log n: ", math.log2(6))

#Se puede observar que la entropia para la lista de probabilidades equiprobables es igual al limite superior 
#establecido para una fuente de memoria nula log(n)

#Mientras que por otro lado para la entropia de la segunda lista es menor al log(n) 