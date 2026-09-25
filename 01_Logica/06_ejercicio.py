# =============================================================================
# PARTE 1: CONCEPTO BÁSICO DE RECURSIVIDAD
# =============================================================================
# La recursividad ocurre cuando una función se llama a sí misma para resolver
# un problema dividido en subproblemas más pequeños.
# Todo algoritmo recursivo DEBE tener dos partes fundamentales:
# 1. Caso Base: La condición de parada para evitar un bucle/recursión infinita (RecursionError).
# 2. Caso Recursivo: La llamada a la misma función modificando el argumento hacia el caso base.


# 1. Función Recursiva de Conteo Regresivo (del 100 al 0):
# - Definir la función 'imprimir_numeros(numero: int)':
#     - Caso Base: Si 'numero' es menor que 0, finalizar la ejecución (return).
#     - Acción: Imprimir el valor actual de 'numero'.
#     - Caso Recursivo: Llamar a 'imprimir_numeros(numero - 1)' para avanzar hacia el caso base.
def imprimir_numeros(numero:int):
    if numero < 0: return
    print(numero)
    imprimir_numeros(numero - 1)

# - Proceso de prueba:
#     - Llamar a la función 'imprimir_numeros(100)' para iniciar el conteo.
imprimir_numeros(100)