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

# --- Mecanismo 2: Bucle 'while' con contador manual ---
# 1. Inicializar una variable contador en 1.
# 2. Establecer la condición de parada mientras el contador sea menor o igual a 10.
# 3. Imprimir el valor del contador.
# 4. Incrementar el contador en 1 al final de cada iteración para evitar bucles infinitos.

# --- Mecanismo 3: Recursividad (función que se llama a sí misma) ---
# 1. Definir una función recursiva que acepte un parámetro numérico (inicio o contador).
# 2. Caso base: si el número supera 10, detener la ejecución (return).
# 3. Imprimir el número actual.
# 4. Caso recursivo: llamar a la función pasando (número + 1).
# 5. Invocar la función por primera vez con el valor inicial 1.