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
def comparacion():
    for numero in range(10,56,2):
        if numero != 16 and numero % 3 != 0:
            print(numero)

def comparacion_una_linea():
    print(*(numero for numero in range(10,56,2) if numero != 16 and numero % 3 != 0), sep="\n")

def comparacion_bucle_sola_linea():
    for n in range(10, 56, 2): (n != 16 and n % 3 != 0) and print(n)

# EJECUCION
if __name__ == "__main__":
    comparacion_bucle_sola_linea()

