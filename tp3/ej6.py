#Inciso A
def NoSingular(lista):
    
    for i in range(len(lista)):
        x = lista[i]
        for j in range (len(lista)):
            if(i != j and x == lista[j]):
                return False
    return True
        
#Inciso B
                        
def Instantaneo(lista):
    n=len(lista)
    for i in range(n):
        x = lista[i]
        for j in range(n):
            if(i != j and lista[j].startswith(x)):
                return True #Instantaneo, pues existe al menos una palabra codigo que tiene como prefijo a x
    return False #Devuelve falso por defecto

#Inciso C

def UD(lista):
    vec_act = lista.copy()   # códigos actuales que se procesan
    new_s = []               # sufijos generados en la iteracion actual

    # Repetimos mientras haya sufijos que procesar, osea mientras vec_act no este vacio
    while vec_act:
        next_s = []  # sufijos generados en esta iteracion

        # Generar sufijos a partir de los codigos actuales
        for i in range(len(vec_act)):
            x = vec_act[i]

            for j in range(len(lista)):
                y = lista[j]  # siempre comparar con la lista original
                if x != y and y.startswith(x):
                    sufijo = y[len(x):]  # obtener el sufijo restante
                    if sufijo not in next_s:  # agregar solo si no está
                        next_s.append(sufijo)

        print(next_s)  #debug 

        # si algún sufijo coincide con un código original => no UD
        if set(lista) & set(next_s):
            return False

        if not next_s:  # si no se generaron sufijos nuevos => UD
            return True

        vec_act = next_s  # iterar con los sufijos generados


lista = ['BA', 'CB', 'AC', 'C', 'BC']
if(NoSingular(lista)):
    print("La lista es No Singular")
else:
    print("La lista es Singular")


if(Instantaneo(lista)):
    print("La lista es instantanea")
else:
    print("La lista es No Instantanea")

        
if(UD(lista)):
    print("La lista es Univocamente Decodificable")
else:
    print("La lista No es univocamente decodificable")
                

                
