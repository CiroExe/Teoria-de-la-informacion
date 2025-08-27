import random
cadena = 'ESTADISTICA'

print(cadena)

caracteres = []
def devuelveProbabilidades(cadena):
     #Inicializo el arreglo que contiene los caracteres de la palabra ingresada
    probs = [] #Inicializo el arreglo que contendra la cantidad de veces que aparece la letra respectivamente en la cadena 

    for c in cadena:
        if c in caracteres: #Si el caracter esta en los caracteres de la cadena incrementa en el arreglo contadores en dicha posicion una unidad
            probs [caracteres.index(c)] += 1
        else: #Si no existe lo agrego a los arreglos
            caracteres.append(c)
            probs.append(1)
    for i in range(len(probs)): 
        probs[i] /= len(cadena)

    return  probs

print(devuelveProbabilidades(cadena))

#Inciso B

alfabeto = caracteres.copy()
longitud_random = random.randint(1,20)
print(longitud_random) #Debug para probar la funcion



def inciso_b(alfabeto):
   # nueva_cadena = ''.join(random.choice(alfabeto) for i in range(longitud_random))  
   nueva_cadena = ''
   longitud_random = random.randint(1,20)
   print(longitud_random) #Debug para probar la funcion

   for i in range(longitud_random):
        letra = random.choice(alfabeto)
        nueva_cadena += letra

   return nueva_cadena

print(inciso_b(alfabeto))


    