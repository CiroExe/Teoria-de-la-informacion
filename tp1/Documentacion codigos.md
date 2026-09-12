# Documentación Técnica: Práctico de Teoría de la Información (Ejercicios 14, 15 y 16)

Este documento detalla la fundamentación matemática, convenciones adoptadas, lógica algorítmica y código de los módulos `ej14.py`, `ej15.py` y del script de prueba `ej16.py`.

---

## 1. Convenciones Matemáticas Adoptadas

A lo largo de los tres ejercicios se sigue la convención matricial estocástica por columnas:

* **Columnas:** Representan el **Estado de Origen** (o estado previo).
* **Filas:** Representan el **Estado de Destino** (o estado siguiente).
* **Propiedad estocástica:** Cada columna suma 1 ($\sum_{i} P_{ij} = 1$).
* **Vector Estacionario ($v^*$):** Vector columna de equilibrio a largo plazo tal que $M \cdot v^* = v^*$, normalizado con $\sum v_i^* = 1$.

---

## 2. Módulo `ej14.py`

Contiene las funciones encargadas del cálculo iterativo del vector estacionario y la determinación de la entropía de fuentes ergódicas o con memoria.

### 2.1. `vector_estacionario(P, tol=1e-8, max_iter=1000)`
* **Objetivo:** Calcular la distribución estacionaria $v^*$ de una matriz de transición $P$ mediante el método iterativo de las potencias.
* **Entrada:** 
  * `P`: Matriz cuadrada de probabilidades donde cada columna suma 1[cite: 1].
  * `tol`: Tolerancia de convergencia ($10^{-8}$)[cite: 1].
  * `max_iter`: Número máximo de iteraciones[cite: 1].
* **Lógica:**
  1. Inicia con un vector uniforme $v = [1/n, \dots, 1/n]$[cite: 1].
  2. En cada iteración $k$, calcula el nuevo vector mediante $v_{\text{nuevo}}[i] = \sum_j P[i][j] \cdot v[j]$ (o de manera traspuesta por índices de columna)[cite: 1].
  3. Evalúa la suma de diferencias absolutas: $\text{aux} = \sum_j \vert{}v_{\text{nuevo}}[j] - v[j]\vert{}$[cite: 1].
  4. Si $\text{aux} \le \text{tol}$, detiene el ciclo y retorna el vector equilibrado[cite: 1].

### 2.2. `calcular_entropia_fuente(vector_estacionario, mat)`
* **Objetivo:** Calcular la entropía de primer orden ($H_1$) para fuentes con memoria de Markov[cite: 1].
* **Fórmula aplicada:**
  $$H(S) = \sum_{j} v_j^* \cdot H(S_j) = -\sum_{j} v_j^* \left( \sum_{i} P_{ij} \log_2 P_{ij} \right)$$
[cite: 1]
* **Lógica:**
  1. Para cada estado de origen $j$ (columna), calcula su entropía condicional sumando $-P[i][j] \cdot \log_2(P[i][j])$ a lo largo de las filas $i$[cite: 1].
  2. Pondera la entropía de cada columna por la componente correspondiente del vector estacionario $v^*[j]$[cite: 1].

### 2.3. `calcular_entropia_memoria_nula(mensaje, alfabeto)`
* **Objetivo:** Calcular la entropía a priori de orden 0 ($H_0$) para mensajes provenientes de fuentes sin memoria[cite: 1].
* **Fórmula aplicada:**
  $$H_0(S) = -\sum_{s \in S} P(s) \log_2 P(s)$$
[cite: 1]
* **Lógica:** Recorre los símbolos únicos del alfabeto, obtiene su frecuencia muestral relativa en el mensaje y acumula la entropía individual[cite: 1].

```python
import math

def vector_estacionario(P, tol=1e-8, max_iter=1000):
    n = len(P)
    v = [1 / n] * n

    for k in range(max_iter):
        nuevo_v = []
        for i in range(n):
            suma = 0
            for j in range(n):
                suma += v[j] * P[j][i]
            nuevo_v.append(suma)

        aux = sum(abs(nuevo_v[j] - v[j]) for j in range(n))
        if aux <= tol:
            return nuevo_v

        v = nuevo_v
    return v

def calcular_entropia_fuente(vector_estacionario, mat):
    vector_entropias = []
    h = 0.0
    for i in range(len(mat)):
        suma = 0.0
        for j in range(len(mat[i])):
            if mat[j][i] != 0:
                suma += mat[j][i] * math.log2(mat[j][i])
        vector_entropias.append(suma * -1)

    for a, b in zip(vector_estacionario, vector_entropias):
        h += a * b
    return h

def calcular_entropia_memoria_nula(mensaje, alfabeto):
    total = len(mensaje)
    h = 0.0
    for s in alfabeto:
        p = mensaje.count(s) / total
        if p > 0:
            h -= p * math.log2(p)
    return h