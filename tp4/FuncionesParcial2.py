import math
    
def redundancia(probs):
    return 1 - rendimiento(probs)

def entropia(distribuciones, r):
    return sum(distribuciones[i] * math.log(1/distribuciones[i], r) for i in range(len(distribuciones)))

def longitud_media(distribucion, longitudes):
    return sum(distribucion[i] * longitudes[i] for i in range(len(longitudes)))

def rendimiento(distribucion, codigo):
    H = entropia(distribucion, 2)
    longitudes = [len(codigo[i]) for i in range(len(codigo))]
    longitudMedia = longitud_media(distribucion, longitudes)
    return H / longitudMedia

fuente = ['A', 'B', 'C', 'D', 'E']
codigo = ['01', '111', '110', '101', '100']
codigo2 = ['00', '01', '10', '110', '111']
codigo3 = ['0110', '010', '0111', '1', '00']
codigo4 = ['11', '001', '000','10', '01']
probs = [0.2, 0.15, 0.1, 0.3, 0.25]
print("Rendimiento -> ", rendimiento(probs, codigo))
print("Redundancia -> ", 1 - rendimiento(probs, codigo))
print("Rendimiento -> ", rendimiento(probs, codigo2))
print("Redundancia -> ", 1 - rendimiento(probs, codigo2))
print("Rendimiento -> ", rendimiento(probs, codigo3))
print("Redundancia -> ", 1 - rendimiento(probs, codigo3))
print("Rendimiento -> ", rendimiento(probs, codigo4))
print("Redundancia -> ", 1 - rendimiento(probs, codigo4))

def devuelveProbabilidades(cadena):
    probs = []
    caracteres = []
    
    for c in cadena:
        if c in caracteres:
            probs[caracteres.index(c)] += 1
        else:
            caracteres.append(c)
            probs.append(1)
    
    for i in range(len(probs)):
        probs[i] /= len(cadena)
    
    return caracteres, probs

def getAlfabeto(mensaje):
    alfabeto = []
    for i in range(len(mensaje)):
        if mensaje[i] not in alfabeto:
            alfabeto.append(mensaje[i])
    alfabeto = sorted(alfabeto)
    return alfabeto

mensaje = 'ABCDABCBDCBAAABBBCBCBABADBCBABCBDBCCCAAABB'
caracteres, probs2 = devuelveProbabilidades(mensaje)
alfabeto = getAlfabeto(mensaje)
print(alfabeto)
print(probs2)

mensaje2 ='AOEAOEOOOOEOAOEOOEOOEOAOAOEOEUUUIEOEOEO'
caracteres, probs3 = devuelveProbabilidades(mensaje2)
alfabeto2 = getAlfabeto(mensaje2)
print(alfabeto2)
print(probs3)