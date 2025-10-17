def Decodifica(mensaje, codigo, fuente):
    i=0
    decodificado = ""
    buffer = ""

    for letra in mensaje:
        buffer += letra
        for i in range(len(codigo)):
            if (buffer  == codigo[i]):
                decodificado += fuente[i]
                buffer = ""
    return decodificado
        
     

fuente = ['S1', 'S2', 'S3', 'S4']
distribucion = [0.3, 0.1, 0.4, 0.2]
codigo = ['BA', 'CAB', 'A', 'CBA']
mensaje1 = 'ABACBAACABABAACBABA'
print(Decodifica(mensaje1, codigo, fuente))
mensaje2 ='BACBAAABAAACBABACAB'
print(Decodifica(mensaje2,codigo, fuente))
mensaje3 = 'CBAABACBABAAACABABA'
print(Decodifica(mensaje3, codigo, fuente))