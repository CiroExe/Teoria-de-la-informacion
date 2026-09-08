import math

#Inciso A

def generaListaCantInformacion(lista_probs):
    return [math.log(1/prob, 2) for prob in lista_probs]

#lista_probs = [0.5, 0.25, 0.25]
#lista_log = generaListaCantInformacion(lista_probs)
#print(lista_log)

#[3.3219280948873626, 2.321928094887362, 1.7369655941662063, 1.3219280948873624]
#Se recibieron los resultados esperados ya que a mayor probabilidad menor cantidad de informacion sera aportada por el simbolo

#Inciso B
def calculaEntropia(lista_probs):
    return sum(prob * math.log(1/prob, 2) for prob in lista_probs if prob > 0)

#H = calculaEntropia(lista_probs)
#print(H)