import ej15
import random

def genera_mensaje(codigos, probabilidades, n):
    mensaje = ""
    for i in range(n):
        mensaje += random.choices(codigos, weights=probabilidades, k=1)[0]
    return mensaje
    
codigo = ["==", "<", "<=", ">", ">=", "<>"]
probs_codigo = [0.10, 0.50, 0.10, 0.20, 0.05, 0.05]
longitud = [len(codigo[i]) for i in range(len(codigo))]
print(genera_mensaje(codigo, probs_codigo, 30))
