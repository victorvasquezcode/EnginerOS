# =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# Enunciado: Crea un programa que imprima por consola todos los números
# comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16
# ni múltiplos de 3.
# =============================================================================
# Pista: Usa un bucle (for o while), un rango de números, y combina condiciones
# con operadores aritméticos (%) y lógicos (and, not, !=).

for numero in range (10 , 56 , 2):
     if numero == 16 or numero % 3 == 0:
          continue
     print(f"Numero valido : {numero}")
     