# =============================================================================
# PARTE 1: ASIGNACIÓN Y PASO DE PARÁMETROS EN PYTHON (VALOR VS. REFERENCIA)
# =============================================================================
# Nota conceptual previa para Python:
# En Python todo es un objeto. No existe la asignación por valor o referencia tradicional,
# sino el concepto de "Paso por Asignación de Objeto" (Pass-by-object-reference):
# - Tipos Inmutables (se comportan como "por valor"): int, float, str, bool, tuple.
# - Tipos Mutables (se comportan como "por referencia"): list, dict, set.


# 1. Asignación de Variables por Valor (Tipos Inmutables):
# - Crear una variable original con un tipo inmutable (ej. entero o string).
# - Asignar esa variable a una nueva variable (copia de valor).
# - Modificar la segunda variable y comprobar que la primera permanece inalterada.
variable_original = "Victor Javier Vasquez Trauco"
variable_nueva = variable_original
variable_nueva = "Victor Javier"

print(f"Variable original: {variable_original}")
print(f"Variable nueva: {variable_nueva}")

# 2. Asignación de Variables por Referencia (Tipos Mutables):
# - Crear una variable original con un tipo mutable (ej. una lista).
# - Asignar esa variable a una nueva variable (comparten la misma posición en memoria).
# - Modificar la segunda variable (ej. .append()) y comprobar que la primera también cambia.

# 3. Funciones con Parámetros Inmutables ("Por Valor"):
# - Definir una función que reciba un argumento inmutable (ej. int).
# - Modificar el valor del parámetro dentro del cuerpo de la función.
# - Demostrar que la variable original fuera de la función NO sufre ningún cambio.

# 4. Funciones con Parámetros Mutables ("Por Referencia"):
# - Definir una función que reciba un argumento mutable (ej. list).
# - Modificar la estructura directamente dentro de la función (ej. .append() o .clear()).
# - Demostrar que la variable original fuera de la función SÍ se modifica.
# - Mostrar la excepción: Reasignar la variable dentro de la función (`lista = [...]`) rompe la referencia.


# =============================================================================
# DIFICULTAD EXTRA: INTERCAMBIO DE VALORES (SWAP) Y RETORNO
# =============================================================================

# --- PROGRAMA 1: Intercambio con Tipos por Valor (Inmutables) ---
# - Definir una función 'intercambiar_por_valor(a, b)':
#     - Recibir dos variables inmutables (ej. dos números enteros).
#     - Intercambiar sus valores internamente (ej. utilizando un 'swap' tradicional o tupla).
#     - Retornar ambos valores intercambiados.
# - Proceso de prueba:
#     - Definir dos variables originales (ej. orig_a = 10, orig_b = 20).
#     - Llamar a la función pasando las variables originales y asignar el retorno a dos variables nuevas.
#     - Imprimir variables originales (deben conservar sus valores iniciales: 10 y 20).
#     - Imprimir variables nuevas (deben tener los valores invertidos: 20 y 10).


# --- PROGRAMA 2: Intercambio con Tipos por Referencia (Mutables) ---
# - Definir una función 'intercambiar_por_referencia(lista_a, lista_b)':
#     - Recibir dos variables mutables (ej. dos listas).
#     - Para conservar las listas originales intactas y evitar modificarlas por referencia:
#         - Crear copias explícitas en el interior (.copy() o slicing [:]).
#         - Intercambiar los contenidos entre las nuevas variables/copias.
#     - Retornar ambas copias intercambiadas.
# - Proceso de prueba:
#     - Definir dos listas originales (ej. lista_orig_a = [1, 2], lista_orig_b = [3, 4]).
#     - Llamar a la función pasando las listas originales y asignar el retorno a dos variables nuevas.
#     - Imprimir listas originales (deben conservar sus elementos iniciales: [1, 2] y [3, 4]).
#     - Imprimir listas nuevas (deben contener las estructuras invertidas: [3, 4] y [1, 2]).