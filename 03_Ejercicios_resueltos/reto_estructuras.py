# =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# Enunciado: Crea un programa que imprima por consola todos los números
# comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16
# ni múltiplos de 3.
# =============================================================================
# Pista: Usa un bucle (for o while), un rango de números, y combina condiciones
# con operadores aritméticos (%) y lógicos (and, not, !=).

for numero in range (10, 56 , 2):
    if numero == 16 or numero % 3 == 0:
        continue
    else:
        print (numero)
    

# =============================================================================
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
def dificicultad_extra (nombre,apellido):
    contador = 0
    for numero in range (1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(f"{nombre}y{apellido}")
        elif numero % 3 == 0:
            print(nombre)
        elif numero % 5 == 0:
            print (apellido)
        else:
            print(numero)
            contador += 1
    return contador
print(f"El numero de veces que se a impreso el numero es: {dificicultad_extra('Victor', 'Javier')}")