from ej1 import generaListaCantInformacion, calculaEntropia


S1=['x','y','z']
lista_probabilidades1 = [0.5, 0.1, 0.4]
cantInformacionS1 = generaListaCantInformacion(lista_probabilidades1)
H1 = calculaEntropia(lista_probabilidades1)

S2=['0','1']
lista_probabilidades2 = [0.5, 0.5]
cantInformacionS2 = generaListaCantInformacion(lista_probabilidades2)
H2 = calculaEntropia(lista_probabilidades2)

S3=['A','B','C', 'D']
lista_probabilidades3 = [0.1, 0.3, 0.4, 0.2]
cantInformacionS3 = generaListaCantInformacion(lista_probabilidades3)
H3 = calculaEntropia(lista_probabilidades3)

print("Cantidad de informacion para cada simbolo del alfabeto S1: ",cantInformacionS1)
print("Cantidad de informacion para cada simbolo del alfabeto S2: ",cantInformacionS2)
print("Cantidad de informacion para cada simbolo del alfabeto S3: ",cantInformacionS3)

print("Entropia de la fuente 1: ", H1)
print("Entropia de la fuente 2: ", H2)
print("Entropia de la fuente 3: ", H3)