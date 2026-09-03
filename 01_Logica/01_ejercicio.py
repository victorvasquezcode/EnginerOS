# =============================================================================
# RETO 01: OPERADORES Y ESTRUCTURAS DE CONTROL
#
# CONCEPTOS CLAVE:
# 1. Operadores: Símbolos que le indican al intérprete qué operación llevar a cabo
#    (Aritméticos, Comparación, Lógicos, Asignación, Identidad, Pertenencia, Bits).
# 2. Estructuras de Control: Mecanismos que dirigen el flujo de ejecución del código
#    (Condicionales, Bucle for/while, Manejo de excepciones).
# =============================================================================

# =============================================================================
# 1. EJEMPLOS DE OPERADORES EN PYTHON
# =============================================================================
# Enunciado: Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje
# e imprime por consola el resultado de todos.

# --- Aritméticos (+, -, *, /, %, **, //) ---
# Pasos sugeridos:
# - Muestra la suma, resta, multiplicación y división tradicional (float).
n1 = 20.3
n2 = 15.4
print(f"Suma: {n1 + n2}\nResta: {n1 - n2}\nMultiplicación: {n1 * n2}\nDivisión: {n1 / n2}")

# - Muestra el módulo / residuo (%), la potencia (**) y la división entera (//).
print(f"Residuo: {n1 % n2}\nPotencia: {n1 ** n2}\nDivisión entera: {n1 // n2}")

# --- Comparación (==, !=, >, <, >=, <=) ---
# Pasos sugeridos:
# - Compara dos números probando igualdad, desigualdad, mayor, menor, etc.
# - Imprime el resultado booleano (True/False) de cada operación.
print(f"Iguales: {n1 == n2}\nDesiguales: {n1 != n2}\nMayor: {n1 > n2}\nMenor: {n1 < n2}")

# --- Lógicos (and, or, not) ---
# Pasos sugeridos:
# - Combina expresiones booleanas usando 'and' (ambas verdaderas).
# - Combina expresiones booleanas usando 'or' (al menos una verdadera).
# - Invierte un valor booleano usando 'not'.
valor_booleano = True
print(f"AND: {n1 == n2 and n1 > n2}\nOR: {n1 == n2 or n1 > n2}\nNOT: {not valor_booleano}")
    
# --- Asignación (=, +=, -=, *=, /=, %=, **=, //=) ---
# Pasos sugeridos:
# - Declara una variable base y aplica operaciones compuestas para modificar su valor.
n3 = 100
n3 += 5
print(f"Asignación compuesta (+=): {n3}")

# --- Identidad (is, is not) ---
# Pasos sugeridos:
# - Compara si dos variables apuntan al mismo espacio de memoria en RAM.
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(f"x is z (Mismo espacio en RAM): {x is z}")
print(f"x is y (Diferente espacio aunque mismo contenido): {x is y}")

# --- Pertenencia (in, not in) ---
# Pasos sugeridos:
# - Verifica si un elemento existe dentro de una lista o cadena de texto.
cadena_texto = "Hola Python"
print(f"'Hola' en cadena: {'Hola' in cadena_texto}")
print(f"'Java' no en cadena: {'Java' not in cadena_texto}")

# --- Bit a Bit / Bitwise (&, |, ^, ~, <<, >>) ---
# Pasos sugeridos:
# - Aplica operaciones AND, OR, XOR, NOT y desplazamientos a nivel de bits sobre enteros.
a, b = 10, 3
print(f"Bitwise AND: {a & b} | Bitwise OR: {a | b} | Bitwise XOR: {a ^ b}")
print(f"Desplazamiento Izquierda: {a << 1} | Desplazamiento Derecha: {a >> 1}")

# =============================================================================
# 2. ESTRUCTURAS DE CONTROL EN PYTHON
# =============================================================================
# Enunciado: Crea ejemplos representando todos los tipos de estructuras de control
# existentes en el lenguaje.

# --- Condicionales (if, elif, else) ---
# Pasos sugeridos:
# - Evalúa una variable con múltiples condiciones usando 'if', 'elif' y 'else'.
edad = 18
if edad < 18:
    print("Menor de edad")
elif edad == 18:
    print("Recién cumplida la mayoría de edad")
else:
    print("Mayor de edad")

# --- Condicional Match/Case (Python 3.10+) ---
# Pasos sugeridos:
# - Implementa un control de flujo por coincidencia de patrones (similar a switch/case).
dia_semana = 3
match dia_semana:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case _:
        print("Otro día")

# --- Iterativas (Bucle for) ---
# Pasos sugeridos:
# - Recorre un rango numérico con range() o los elementos de una lista.
print("\n--- Bucle For ---")
for i in range(1, 4):
    print(f"Iteración for: {i}")

# --- Iterativas (Bucle while) ---
# Pasos sugeridos:
# - Ejecuta un bucle mientras una condición sea verdadera.
# - Muestra el uso de 'break' (para romper) y 'continue' (para saltar iteración).
print("\n--- Bucle While ---")
contador = 0
while contador < 5:
    contador += 1
    if contador == 2:
        continue  # Salta la iteración 2
    if contador == 4:
        break     # Rompe el bucle al llegar a 4
    print(f"Contador while: {contador}")

# --- Excepciones (try, except, else, finally) ---
# Pasos sugeridos:
# - Envuelve una operación susceptible a fallos (ej. división por cero) en un try/except.
print("\n--- Control de Excepciones ---")
try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("Error: División entre cero")
else:
    print(f"División exitosa: {resultado}")
finally:
    print("Finalizó la verificación de excepción.")

# =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# =============================================================================
# Enunciado: Crea un programa que imprima por consola todos los números
# comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16
# ni múltiplos de 3.
#
# Pasos sugeridos:
# - Genera un bucle que recorra los números desde 10 hasta 55 (inclusive).
# - Aplica las condiciones en un 'if':
#   1. Que sea par -> (numero % 2 == 0)
#   2. Que sea diferente de 16 -> (numero != 16)
#   3. Que NO sea múltiplo de 3 -> (numero % 3 != 0)
# - Imprime únicamente los números que cumplan TODAS las condiciones simultáneamente.
for numero in range(10 , 56 , 2):
    if numero == 16 or numero % 3 == 0:
        continue
    print(numero)
     