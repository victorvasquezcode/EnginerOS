# =============================================================================
# DIFICULTAD EXTRA: ALGORITMOS RECURSIVOS (FACTORIAL Y FIBONACCI)
# =============================================================================

# --- PROGRAMA 1: Cálculo del Factorial de un Número ---
# El factorial de n (n!) es la multiplicación de todos los enteros desde 1 hasta n.
# Ejemplos: 5! = 5 * 4 * 3 * 2 * 1 = 120 | 0! = 1

# - Definir la función 'factorial(n: int) -> int':
#     - Validar que 'n' sea un entero no negativo (si n < 0, manejar error o retornar valor nulo).
#     - Caso Base: Si 'n' es 0 o 1, retornar 1 (ya que 0! = 1 y 1! = 1).
#     - Caso Recursivo: Retornar 'n * factorial(n - 1)'.
def factorial(n: int) -> int:
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# - Proceso de prueba:
#     - Probar con un número concreto (ej. factorial(5)) e imprimir el resultado (debe dar 120).
print(f"La factorial es: {factorial(5)}")

# --- PROGRAMA 2: Valor de la Sucesión de Fibonacci según su Posición ---
# La sucesión de Fibonacci inicia con 0 y 1, y cada número siguiente es la suma
# de los dos anteriores: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# Posiciones (índice 0):  0, 1, 2, 3, 4, 5, 6,  7,  8,  9, ...

# - Definir la función 'fibonacci(posicion: int) -> int':
#     - Validar que 'posicion' no sea negativa.
#     - Caso Base 1: Si 'posicion' es 0, retornar 0.
#     - Caso Base 2: Si 'posicion' es 1, retornar 1.
#     - Caso Recursivo: Retornar 'fibonacci(posicion - 1) + fibonacci(posicion - 2)'.

# - Proceso de prueba:
#     - Probar con una posición concreta (ej. fibonacci(7)) e imprimir el resultado (debe dar 13).
def fibonacci(posicion: int) -> int:
    if posicion < 0:
        return None
    if posicion == 0:
        return 0
    if posicion == 1:
        return 1
    return fibonacci(posicion - 1) + fibonacci(posicion - 2)

print(f"Fibonacci es: {fibonacci(7)}")