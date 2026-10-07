# 📝 Variante: [01] Operadores y Control de Flujo (Mutación)

# Crea un programa que recorra los números comprendidos entre 15 y 85 (ambos incluidos)
# e imprima por consola únicamente aquellos que cumplan todas las siguientes condiciones:

# Deben ser impares.
# No deben ser múltiplos de 5.
# La suma de sus dígitos debe ser un número par.

# Salida requerida:
# Al finalizar el recorrido, el programa debe imprimir en una última línea el conteo total
#  de números que cumplieron con todos los criterios anteriores
#  (ejemplo de formato final: Total de números encontrados: X).

# 📝 Variante: [02] Funciones y Alcance (Mutación)

# Crea una función que reciba tres parámetros: dos cadenas de texto (texto1, texto2)
#  y un número entero positivo (limite). La función debe retornar una tupla con dos
#  números enteros (conteo_reemplazos, suma_impresos).
# Comportamiento de la función:
#    Recorre los números desde el 1 hasta el valor de limite (inclusive).
#    Para cada número:
#     Si el número es múltiplo de 4, imprime únicamente texto1.
#     Si el número es múltiplo de 7, imprime únicamente texto2.
#     Si el número es múltiplo de 4 y de 7 al mismo tiempo, imprime ambas cadenas
#       concatenadas con un guión en medio (ejemplo: texto1-texto2).
#     Si el número no cumple ninguna de las condiciones anteriores, imprime el número directamente.

# Retorno de la función:
# Al finalizar el recorrido, la función debe retornar una tupla (conteo_reemplazos, suma_impresos) donde:
#     conteo_reemplazos: Es el total de veces que se imprimió un texto (o combinación) en lugar de un número.
#     suma_impresos: Es la suma acumulada de todos los números que sí se llegaron a imprimir en consola.