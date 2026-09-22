# =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# =============================================================================
# Enunciado: Crea una función que reciba dos parámetros de tipo cadena de texto
# y retorne un número.
# - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#   * Si el número es múltiplo de 3, muestra la cadena del primer parámetro.
#   * Si el número es múltiplo de 5, muestra la cadena del segundo parámetro.
#   * Si es múltiplo de 3 y de 5 (múltiplo de 15), muestra ambas concatenadas.
#   * Si no cumple ninguna, imprime el número.
#   * La función retorna el número de veces que se ha impreso el NÚMERO en lugar de los textos.
#
# Pasos sugeridos:
# - Define la función con type hints -> def fizz_buzz_custom(texto1: str, texto2: str) -> int:
# - Inicializa un contador para llevar el registro de cuántas veces se imprime un número.
# - Genera un bucle del 1 al 100 inclusive.
# - Implementa la lógica condicional priorizando el caso compuesto (múltiplo de 3 Y de 5).
# - En el caso base de la condición (else), imprime el número e incrementa el contador.
# - Retorna el contador final y muestra el resultado del retorno en consola.

def fizzbuzz (param1: str = "Fizz", param2: str = "Buzz") -> int:
    contador = 0
    for numero in range(1,101):
        if numero % 15 == 0:
            print(f"{param1}{param2}")
        elif numero % 5 == 0:
            print(param2)
        elif numero % 3 == 0:
            print(param1)
        else:
            contador += 1
            print(numero)
    return contador

if __name__ == "__main__":
    fizzbuzz1 = fizzbuzz()
    print(f"El numero de veces que se ha impreso el NUMERO es: {fizzbuzz1}")