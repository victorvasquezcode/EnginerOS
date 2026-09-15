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
variable_original_mutable = ["Pera", "Manzana", "Kiwi"]
nueva_variable_mutable = variable_original_mutable
nueva_variable_mutable.append("Tomate")

print(f"Variable original: {variable_original_mutable}")
print(f"Variable nueva: {nueva_variable_mutable}")

# 3. Funciones con Parámetros Inmutables ("Por Valor"):
# - Definir una función que reciba un argumento inmutable (ej. int).
# - Modificar el valor del parámetro dentro del cuerpo de la función.
# - Demostrar que la variable original fuera de la función NO sufre ningún cambio.
def modificar_valor(numero:int):
    numero+=10
    print(f"Dentro de la funcion: {numero}")

mi_numero = 15
print(f"\nAntes de la funcion: {mi_numero}")
modificar_valor(mi_numero)
print(f"Despues de la funcion: {mi_numero}")

# 4. Funciones con Parámetros Mutables ("Por Referencia"):
# - Definir una función que reciba un argumento mutable (ej. list).
# - Modificar la estructura directamente dentro de la función (ej. .append() o .clear()).
# - Demostrar que la variable original fuera de la función SÍ se modifica.
# - Mostrar la excepción: Reasignar la variable dentro de la función (`lista = [...]`) rompe la referencia.
def modificar_estructura(lista: list):
    lista.append("Lapiz")
    print(f"Dentro de la funcion (modificacion directa): {lista}")

def reasignar_estructura(lista: list):
    lista = ["Borrador", "Tajador"]
    print(f"Dentro de la funcion (reasignacion): {lista}")

lista_colegio = ["Cuaderno", "Regla"]
print(f"\nLista original inicial: {lista_colegio}")

modificar_estructura(lista_colegio)
print(f"Despues de modificar estructura: {lista_colegio}")

reasignar_estructura(lista_colegio)
print(f"Despues de reasignar_estructura: {lista_colegio}")



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
def intercambiar_por_valor(a: int, b:int) -> tuple:
    a , b = b , a
    return a , b

origin_a = 10
origin_b = 20
nuevo_a, nuevo_b = intercambiar_por_valor(origin_a, origin_b)

print("--- TIPOS POR VALOR (INMUTABLES) ---")
print(f"Las variables originales son '{origin_a}' y '{origin_b}'")
print(f"Las variables nuevas son '{nuevo_a}' y '{nuevo_b}'")

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

def intercambiar_por_referencia(lista_a: list, lista_b: list) ->tuple:
    copia_lista_a = lista_a.copy()
    copia_lista_b = lista_b.copy()
    copia_lista_a , copia_lista_b = copia_lista_b , copia_lista_a
    return copia_lista_a , copia_lista_b

lista_orig_a = [1, 2]
lista_orig_b = [3, 4]

lista_nueva_a , lista_nueva_b = intercambiar_por_referencia(lista_orig_a, lista_orig_b)

print("--- TIPOS POR VALOR (MUTABLES) ---")
print(f"Listas originales: '{lista_orig_a}' y '{lista_orig_b}'")
print(f"Listas nuevas: '{lista_nueva_a}' y '{lista_nueva_b}'")