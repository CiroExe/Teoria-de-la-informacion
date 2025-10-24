import math
# Dado un caracter devolver un byte que represente su codigo
# y utilizar el menos significativo para almacenar su paridad

def caracter_a_byte(caracter):
    #Obtengo el codigo ASCII del caracter y aseguro que uso solo 7 bits
    caracter_ascii = ord(caracter) & 0b1111111

    #Cuenta unos
    cantUnos = bin(caracter_ascii).count('1')
    
    # 0 si la cantidad de unos es par, 1 si la cantidad de unos es impar
    bitParidad = 0 if cantUnos % 2 == 0 else 1
    
    # Desplazo 1 but y agrego paridad 
    caracter_ascii = (caracter_ascii << 1) | bitParidad
    return caracter_ascii

def verificar_byte(byte):
    bitParidad = byte & 1
    
    caracter_ascii = byte >> 1
    
    cantUnos = bin(caracter_ascii).count('1')
    
    paridad_esperada = 0 if cantUnos % 2 == 0 else 1
    
     # Comparar con el bit de paridad recibido
    if paridad_esperada == bitParidad:
        print("Byte correcto (sin errores)")
    else:
        print("Error detectado en la transmisión")

print(bin(caracter_a_byte('A')))