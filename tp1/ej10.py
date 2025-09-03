#Desarrollar una función en Python que reciba: una lista con el alfabeto de una fuente, otra 
#con su distribución de probabilidades y un entero N. Esta función debe generar dos nuevas 
#listas con la extensión de orden N y su distribución de probabilidades.


def generaNuevasListas(alfabeto, distribucion, N):
    if len(alfabeto) != len(distribucion):
        raise ValueError("El alfabeto y las probabilidades deben tener la misma longitud.")
    if abs(sum(distribucion) - 1.0) > 1e-6:
        raise ValueError("Las probabilidades deben sumar 1.")

    # Comenzamos con secuencia vacía y probabilidad 1
    extension = [""]
    nueva_distribucion = [1.0]

    for _ in range(N):
        # Listas temporales para el siguiente nivel
        nuevas_extensiones = []
        nuevas_probabilidades = []

        for i in range(len(extension)):
            secuencia_actual = extension[i]
            probabilidad_actual = nueva_distribucion[i]

            for j in range(len(alfabeto)):
                nueva_secuencia = secuencia_actual + alfabeto[j]
                nueva_probabilidad = probabilidad_actual * distribucion[j]

                nuevas_extensiones.append(nueva_secuencia)
                nuevas_probabilidades.append(nueva_probabilidad)

        # Actualizamos para el siguiente nivel
        extension = nuevas_extensiones
        nueva_distribucion = nuevas_probabilidades

    return extension, nueva_distribucion

alfabeto = ['a', 'b']
distribucion = [0.2, 0.8]
N = 2

extensiones, probabilidades = generaNuevasListas(alfabeto, distribucion, N)

for s, p in zip(extensiones, probabilidades):
    print(f"{s}: {p:.4f}")