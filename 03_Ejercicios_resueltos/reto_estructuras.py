# 02 =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# Enunciado: Crea un programa que imprima por consola todos los números
# comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16
# ni múltiplos de 3.
# =============================================================================

# 03 =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# Enunciado: Crea una función que reciba dos parámetros de tipo cadena de texto
# y retorne un número.
# - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#   - Si el número es múltiplo de 3, muestra la cadena del primer parámetro.
#   - Si el número es múltiplo de 5, muestra la cadena del segundo parámetro.
#   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas concatenadas.
#   - La función retorna el número de veces que se ha impreso el número en lugar
#     de los textos.
# =============================================================================

# 04 =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# Enunciado: Crea una agenda de contactos por terminal.
# - Funcionalidades: Búsqueda, inserción, actualización y eliminación de contactos.
# - Datos: Cada contacto tiene Nombre y Teléfono.
# - Validaciones: El teléfono debe ser numérico (.isdigit()) y tener máximo 11 dígitos (len() <= 11).
# ## - Incluye opción para salir/finalizar el programa. 
# =============================================================================

# 05 =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# Enunciado: Crea un programa que analice dos palabras diferentes y determine si:
# 1. Palíndromo: Se lee igual de izquierda a derecha que de derecha a izquierda.
#    (Ejemplo: "ana", "radar", "reconocer").
# 2. Anagrama: Tienen exactamente las mismas letras pero en diferente orden.
#    (Ejemplo: "roma" y "amor", "frase" y "fresa").
# 3. Isograma: Una palabra donde ninguna letra se repite.
#    (Ejemplo: "centrifugado", "murciélago").
#
# Pistas:
# - Normaliza los textos a minúsculas y elimina espacios antes de comparar.
# - Para anagramas: ¿Qué pasa si ordenas las letras con sorted()?
# - Para isogramas: ¿Qué pasa si comparas len(palabra) con len(set(palabra))?
# =============================================================================

# 06 =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# =============================================================================
# Enunciado: Utiliza el concepto de recursividad para:
# 1. Calcular el factorial de un número concreto (la función recibe ese número).
# 2. Calcular el valor de un elemento concreto (según su posición) en la 
#    sucesión de Fibonacci (la función recibe la posición).
#
# -----------------------------------------------------------------------------
# PARTE 1: FACTORIAL RECURSIVO (n! = n * (n-1) * ... * 1)
# -----------------------------------------------------------------------------
# Pasos sugeridos:
# - Define la función que reciba un entero 'n'.
# - Valida el caso de números negativos (lanzar excepción o mensaje).
# - Establece el CASO BASE: Si 'n' es 0 o 1, el factorial es 1 directamente.
# - Establece el CASO RECURSIVO: Retorna n multiplicado por la llamada recursiva 
#   pasándole (n - 1).
# - Prueba la función imprimiendo el resultado para valores como 5 (debe dar 120).

# -----------------------------------------------------------------------------
# PARTE 2: FIBONACCI RECURSIVO (0, 1, 1, 2, 3, 5, 8, 13, 21, 34...)
# -----------------------------------------------------------------------------
# Pasos sugeridos:
# - Define la función que reciba la 'posicion' deseada de la secuencia.
# - Valida posiciones negativas.
# - Establece los CASOS BASE: 
#   * Si la posición es 0, el valor es 0.
#   * Si la posición es 1, el valor es 1.
# - Establece el CASO RECURSIVO: La fórmula de Fibonacci dice que F(n) = F(n-1) + F(n-2).
#   Retorna la suma de dos llamadas recursivas: una con (posicion - 1) y otra con (posicion - 2).
# - Prueba la función para la posición 6 (debe dar 8) y la posición 9 (debe dar 34).

