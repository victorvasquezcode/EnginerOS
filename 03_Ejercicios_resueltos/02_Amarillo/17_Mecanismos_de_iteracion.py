# ------------------------------------------------------------------------------
# DIFICULTAD EXTRA: OTROS MECANISMOS DE ITERACIÓN EN PYTHON
# ------------------------------------------------------------------------------

# --- Mecanismo 4: List Comprehension (comprensión de listas con side-effect) ---
# 1. Usar una sintaxis de lista comprimida aplicando print() directamente sobre range(1, 11).
print("\n--- MECANISMO 4 ---")
[print(numero) for numero in range(1,11)]

# --- Mecanismo 5: Iterador explícito con iter() y next() ---
# 1. Crear un iterador a partir del rango range(1, 11) usando iter().
# 2. Utilizar un bucle while True para extraer cada elemento mediante next().
# 3. Manejar la excepción StopIteration mediante try/except para capturar el fin de la secuencia y salir con break.
print("\n--- MECANISMO 5 ---")
variable = iter(range(1,11))
while True:
    try:
        print(next(variable))
    except StopIteration:
        print("Fin de la secuencia")
        break

# --- Mecanismo 6: Uso del módulo 'itertools' (count + takewhile/islice) ---
# 1. Importar el generador infinito itertools.count o la función itertools.islice.
# 2. Generar una secuencia desde 1 y recortarla al llegar al elemento 10.
# 3. Iterar e imprimir cada valor resultante.
print("\n--- MECANISMO 6 ---")
import itertools
secuencia_infinita = itertools.count(1)
secuencia_infinita_2 = itertools.count(1)
iterador_recortado_1 = itertools.islice(secuencia_infinita,10)
iterador_recortado_2 = itertools.takewhile(lambda x:x <= 10, secuencia_infinita_2)

for numero in iterador_recortado_1:
    print(numero)

for numero in iterador_recortado_2:
    print(numero)

# --- Mecanismo 7: Función de orden superior map() ---
# 1. Crear una función auxiliar o usar lambda que ejecute print().
# 2. Mapear dicha función sobre range(1, 11) usando map().
# 3. Consumir el generador map (por ejemplo, convirtiéndolo a list() o usándolo en un loop) para forzar la ejecución.
print("\n--- MECANISMO 7 ---")
generador_map = list(map(lambda x: print(x), range(1,11)))
print(generador_map)

# --- Mecanismo 8: Generador personalizado (yield) ---
# 1. Definir una función generadora que alterne con yield números del 1 al 10.
# 2. Consumir el generador mediante un bucle for o convirtiéndolo en una secuencia visible.
print("\n--- MECANISMO 8 ---")
def generadora():
    for numero in range(1,11):
        yield numero

gen = generadora()
for numero in gen:
    print(numero)

# --- Mecanismo 9: Módulo 'functools' con reduce() ---
# 1. Importar reduce desde functools.
# 2. Usar reduce sobre la secuencia range(1, 11) acumulando o imprimiendo los elementos paso a paso.
print("\n--- MECANISMO 9 ---")
from functools import reduce
acumulando = reduce(lambda acc, x: acc + x , range(1,11))
print(acumulando) 

# --- Mecanismo 10: Modificación de la secuencia de entrada con pop() o shift ---
# 1. Crear una lista precargada con los números del 1 al 10.
# 2. Mientras la lista contenga elementos, extraer el primer valor (pop(0)) e imprimirlo hasta vaciarla.
print("\n--- MECANISMO 10 ---")
lista = [1,2,3,4,5,6,7,8,9,10]
while lista:
    valor = lista.pop(0)
    print (valor)

