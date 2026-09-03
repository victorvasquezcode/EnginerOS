# =============================================================================
# RETO 00: SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
#
# CONCEPTOS CLAVE:
# 1. Comentarios: Anotaciones en el código ignoradas por el intérprete.
# 2. Variables y Constantes: Espacios en memoria para almacenar datos.
#    - Python usa convención UPPERCASE para simular constantes.
# 3. Tipos Primitivos: Tipos de datos básicos integrados en el lenguaje
#    (int, float, bool, str, NoneType).
# =============================================================================

# =============================================================================
# 1. SITIO WEB OFICIAL DEL LENGUAJE
# =============================================================================
# Enunciado: Crea un comentario en el código y coloca la URL del sitio web
# oficial del lenguaje de programación que has seleccionado.
#
# Pasos sugeridos:
# - Escribe un comentario con la URL oficial de Python (https://www.python.org/).

# https://www.python.org/


# =============================================================================
# 2. SINTAXIS DE COMENTARIOS
# =============================================================================
# Enunciado: Representa las diferentes sintaxis que existen de crear
# comentarios en el lenguaje (en una línea, varias...).
#
# Pasos sugeridos:
# - Crea un comentario de una sola línea utilizando el símbolo de numeral (#).
# - Crea un comentario o docstring multilínea utilizando triples comillas (""" o ''').

# Comentario en una linea.

'''
Comentario
en
varias
lineas
'''

"""
Otro
comentario
en
varias
lineas
"""

# =============================================================================
# 3. VARIABLES Y CONSTANTES
# =============================================================================
# Enunciado: Crea una variable (y una constante si el lenguaje lo soporta).
#
# Pasos sugeridos:
# - Declara una variable estándar usando la convención de estilo snake_case.
# - Declara una "constante" por convención usando MAYÚSCULAS_CON_GUION_BAJO.
#   (Recuerda que en Python las constantes no se fuerzan a nivel de intérprete,
#   sino por convención para los desarrolladores).

variable_1 = "Python"
VARIABLE_2 = "constante"


# =============================================================================
# 4. TIPOS DE DATOS PRIMITIVOS
# =============================================================================
# Enunciado: Crea variables representando todos los tipos de datos primitivos
# del lenguaje (cadenas de texto, enteros, booleanos...).
#
# Pasos sugeridos:
# - Declara una variable para un número entero (int).
# - Declara una variable para un número de punto flotante/decimal (float).
# - Declara una variable para un valor booleano (bool: True o False).
# - Declara una variable para una cadena de caracteres / texto (str).
# - Declara una variable representando la ausencia de valor o tipo nulo (NoneType).

numero_1 = 20
numero_2 = 20.5
booleano = True
cadena_caracteres = "Hola"
variable_vacia = None

# =============================================================================
# 5. SALIDA POR TERMINAL (IMPRESIÓN)
# =============================================================================
# Enunciado: Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
#
# Pasos sugeridos:
# - Usa la función integrada print() para mostrar en pantalla el mensaje
#   "¡Hola, Python!" (puedes usar f-strings o concatenación simple).

print(f"¡{cadena_caracteres}, {variable_1}!")