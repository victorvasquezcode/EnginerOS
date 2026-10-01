# ==============================================================================
# EJERCICIO 17: MECANISMOS DE ITERACIÓN (1 AL 10)
# ==============================================================================

# ------------------------------------------------------------------------------
# PARTE PRINCIPAL: 3 MECANISMOS BÁSICOS
# ------------------------------------------------------------------------------

# --- Mecanismo 1: Bucle 'for' con 'range()' ---
# 1. Definir un bucle 'for' que recorra una secuencia generada por range().
# 2. Configurar range() para iniciar en 1 y finalizar en 11 (límite superior exclusivo).
# 3. Imprimir el valor del contador en cada iteración.
print("\n--- MECANISMO 1 ---")
for numero in range(1,11):
    print(numero)

# --- Mecanismo 2: Bucle 'while' con contador manual ---
# 1. Inicializar una variable contador en 1.
# 2. Establecer la condición de parada mientras el contador sea menor o igual a 10.
# 3. Imprimir el valor del contador.
# 4. Incrementar el contador en 1 al final de cada iteración para evitar bucles infinitos.
print("\n--- MECANISMO 2 ---")
contador = 1
while contador <= 10:
    print(contador)
    contador += 1

# --- Mecanismo 3: Recursividad (función que se llama a sí misma) ---
# 1. Definir una función recursiva que acepte un parámetro numérico (inicio o contador).
# 2. Caso base: si el número supera 10, detener la ejecución (return).
# 3. Imprimir el número actual.
# 4. Caso recursivo: llamar a la función pasando (número + 1).
# 5. Invocar la función por primera vez con el valor inicial 1.
print("\n--- MECANISMO 3 ---")
def recursiva(numero):
    if numero > 10:
        return
    print(numero)
    return recursiva(numero + 1)

recursiva(1)