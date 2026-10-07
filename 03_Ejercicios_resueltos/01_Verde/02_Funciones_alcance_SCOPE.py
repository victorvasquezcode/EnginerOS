# 🟢 / 🟡 [02] FUNCIONES Y ALCANCE

# DIFICULTAD EXTRA (opcional):
# Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
# - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

# Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
# Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.

def fuzzbizz(palabra1: str, palabra2: str) -> int:
    contador = 0
    for numero in range(1,101):
        if numero % 15 == 0:
            print(f"{palabra1}{palabra2}")
        elif numero % 5 == 0:
            print(palabra2)
        elif numero % 3 == 0:
            print(palabra1)
        else:
            print(numero)
            contador += 1
    return contador

prueba1 = fuzzbizz("Victor","Javier")
print(f"El numero de veces que se imprimio el numero en lugar de texto es: {prueba1}")