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
