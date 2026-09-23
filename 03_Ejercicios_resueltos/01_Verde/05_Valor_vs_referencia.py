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
def intercambiar_por_valor(a: int, b: int):
    a, b = b, a
    return a, b

origin_a = 10
origin_b = 20
nueva_a, nueva_b = intercambiar_por_valor(origin_a, origin_b)
print(f"Variables originales: {origin_a} , {origin_b}")
print(f"Variables nuevas: {nueva_a} , {nueva_b}")

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
def intercambiar_por_referencia(lista_a: list, lista_b: list):
    copia_1 = lista_a.copy()
    copia_2 = lista_b.copy()
    copia_1, copia_2 = copia_2, copia_1
    return copia_1, copia_2

lista_origin_a = [1,2]
lista_origin_b = [3,4]
lista_nueva_a, lista_nueva_b = intercambiar_por_referencia(lista_origin_a, lista_origin_b)
print(f"Lista original: {lista_origin_a}, {lista_origin_b}")
print(f"Lista nueva: {lista_nueva_a}, {lista_nueva_b}")
