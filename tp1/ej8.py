import ej1

def CalculaEntropiaBinaria(w):
    lista_probs = [w, 1-w]
    return ej1.calculaEntropia(lista_probs)