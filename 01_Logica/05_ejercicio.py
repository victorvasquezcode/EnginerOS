# =============================================================================
# RETO 05: ASIGNACIÓN POR VALOR Y POR REFERENCIA
#
# CONCEPTOS CLAVE EN PYTHON:
# 1. Tipos Inmutables (Por Valor): int, float, str, bool, tuple.
#    - Al reasignar o modificar la variable, Python crea un nuevo objeto en memoria.
# 2. Tipos Mutables (Por Referencia): list, dict, set.
#    - Múltiples variables apuntan al mismo espacio de memoria (dirección).
#    - Modificar la estructura afecta a todas las variables que la refieren.
# =============================================================================

# -----------------------------------------------------------------------------
# 1. ASIGNACIÓN DE VARIABLES
# -----------------------------------------------------------------------------

# --- Asignación "Por Valor" (Tipos Inmutables) ---
# Demuestra qué pasa al asignar una variable a otra y luego modificar la segunda
# (ej. enteros o cadenas de texto).

variable = 20
variable_2 = variable
variable_2 = 40
print(variable_2)


# --- Asignación "Por Referencia" (Tipos Mutables) ---
# Demuestra qué pasa al asignar una lista o diccionario a otra variable y modificarla.

lista_1 = ["platano","manzana","pera"]
lista_2 = lista_1

lista_2.append("zanahoria")

print(lista_1)
print(lista_2)


# -----------------------------------------------------------------------------
# 2. COMPORTAMIENTO EN FUNCIONES
# -----------------------------------------------------------------------------

# --- Función con parámetro "Por Valor" (Inmutable) ---
def modificar_valor(parametro):
    # Modifica el parámetro aquí dentro e imprime su estado interno
    parametro = 40
    print(f"Dentro de la funcion: {parametro}")

# Prueba llamando a la función con una variable original e imprime ambas
variable_original = 20

print(f"Antes de la funcion: {variable_original}")
modificar_valor(variable_original)
print(f"Despues de la funcion: {variable_original}")


# --- Función con parámetro "Por Referencia" (Mutable) ---
def modificar_referencia(parametro):
    # Modifica el contenido de la lista/diccionario (ej. .append() o modificación directa)
    parametro.append("Cuaderno")
    print(f"Dentro de la funcion: {parametro}")
    pass

# Prueba llamando a la función con una lista original e imprime ambas
lista_utiles = ["Lapiz","Mochila"]

print(f"Antes de la funcion: {lista_utiles}")
modificar_referencia(lista_utiles)
print(f"Despues de la funcion: {lista_utiles}")



# =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
#
# Enunciado: Crea dos funciones/programas que reciban dos parámetros cada uno
# (definidos como variables anteriormente).
# - En un caso, pasa dos parámetros por valor. En el otro, por referencia.
# - Intercambia sus valores en el interior de la función y retórnalos.
# - Asigna el retorno a dos variables nuevas.
# - Imprime las variables originales y las nuevas para verificar:
#   1. Que en las nuevas se invirtió el valor.
#   2. Que en las originales se conservó el valor original (¡ojo con las referencias!).
# =============================================================================

print("\n=== DIFICULTAD EXTRA ===")

# --- 1. Intercambio Por Valor ---
def intercambiar_por_valor(a, b):
    # Intercambia los valores y retórnalos
    a , b = b , a
    return a , b

# Declarar variables originales (inmutables)
variable_1 = 50
variable_2 = 40

# Llamar a la función, asignar retornos y comprobar resultados
nueva_var1, nueva_var2 = intercambiar_por_valor(variable_1, variable_2)
print(f"Originales : variable 1 = {variable_1} variable 2 = {variable_2}")
print(f"Nuevos : nueva variable = {nueva_var1} nueva variable 2 = {nueva_var2}")



# --- 2. Intercambio Por Referencia ---
def intercambiar_por_referencia(lista_a, lista_b):
    # Intercambia el contenido de las listas sin romper las referencias originales
    # o retorna copias/intercambios según la prueba
    lista_a , lista_b = lista_b , lista_a
    return lista_a, lista_b

# Declarar variables originales (mutables)
lista_a = ["Pera","Manzana"]
lista_b = ["Zanahoria","Zapallo"]

# Llamar a la función, asignar retornos y comprobar resultados
nueva_lista_a , nueva_lista_b = intercambiar_por_referencia(lista_a, lista_b)
print(f"Originales : lista 1 = {lista_a} lista 2 = {lista_b}")
print(f"Nuevas : lista nueva 1 = {nueva_lista_a} lista nueva 2 = {nueva_lista_b}")