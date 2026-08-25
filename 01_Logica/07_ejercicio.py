# =============================================================================
# RETO 06: RECURSIVIDAD
#
# CONCEPTOS CLAVE:
# 1. Caso Base: La condición de parada que evita que la función se llame
#    a sí misma infinitamente (evita el RecursionError / Stack Overflow).
# 2. Caso Recursivo: La llamada a la misma función, pero acercándose 
#    progresivamente al caso base.
# =============================================================================

# -----------------------------------------------------------------------------
# 1. EJERCICIO PRINCIPAL: IMPRIMIR DEL 100 AL 0
# -----------------------------------------------------------------------------

def cuenta_atras(numero: int):
    # 1. Caso Base: ¿Cuándo debemos detener la recursividad?
    if numero < 0:
        return
    # 2. Caso Recursivo: Imprimir el número actual y llamar a la función con numero - 1
    print(numero)
    
    cuenta_atras(numero - 1)

# Prueba la función inicializando en 100
# cuenta_atras(100)
cuenta_atras(100)

# =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# =============================================================================

print("\n=== DIFICULTAD EXTRA ===")

# --- 1. Factorial de un Número ---
# Enunciado: n! = n * (n - 1) * (n - 2) * ... * 1
# Ejemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120
# Caso Base: Si n == 0 o n == 1, el factorial es 1.

def factorial(n: int) -> int:
    # Escribe la condición del caso base y el retorno recursivo
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)

# Pruebas de Factorial:
numero_factorial = 5
print(f"El factorial de {numero_factorial} es: {factorial(numero_factorial)}")


# --- 2. Elemento en la Sucesión de Fibonacci ---
# Enunciado: Posiciones: 0, 1, 2, 3, 4, 5, 6, 7...
#            Valores:    0, 1, 1, 2, 3, 5, 8, 13...
# Fórmula: Fib(n) = Fib(n - 1) + Fib(n - 2)
# Casos Base: Fib(0) = 0, Fib(1) = 1.

def fibonacci(posicion: int) -> int:
    # Escribe los casos base para posición 0 y 1, y la suma recursiva para el resto
    if posicion <=1:
        return posicion

    return fibonacci(posicion-1) + fibonacci(posicion-2)

# Pruebas de Fibonacci:
pos = 7  # Debería retornar 13
print(f"El elemento en la posición {pos} de Fibonacci es: {fibonacci(pos)}")