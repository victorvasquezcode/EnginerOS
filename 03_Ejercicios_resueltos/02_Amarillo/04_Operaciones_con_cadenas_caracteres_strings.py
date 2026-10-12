# 🟡 [04] CADENAS DE CARACTERES

# DIFICULTAD EXTRA (opcional):
# Crea un programa que analice dos palabras diferentes y realice comprobaciones
# para descubrir si son:
# - Palíndromos
# - Anagramas
# - Isogramas

# Entrada: Palabra 1 y Palabra 2 de tipo String
# Salida: Valor Booleano True o False
# Reglas: Palindromo Se lee igual de derecha a izquierda que de izquierda a derecha
#         Anagrama palabra que resulta de la transposicion de todas las letras de otra palabra
#         Isograma palabra sin letras repetidas

def limpiar_palabra(palabra):
    palabra_limpia = palabra.strip().lower().replace(" ","")
    return palabra_limpia

def palindromo(palabra):
    return palabra == palabra[::-1]

def anagrama(palabra, palabra2):
    return palabra != palabra2 and sorted(palabra) == sorted(palabra2)

def isograma(palabra):
    return len(set(palabra)) == len(palabra)

while True:
    palabra_1 = input("Ingrese la primera palabra: ")
    palabra_2 = input("Ingrese la segunda palabra: ")

    p1 = limpiar_palabra(palabra_1)
    p2 = limpiar_palabra(palabra_2)

    if palindromo(p1):
        print(f"La palabra '{p1}' es palindromo")
    else:
        print(f"La palabra '{p1}' no es palindromo")

    if palindromo(p2):
        print(f"La palabra '{p2}' es palindromo")
    else:
        print(f"La palabra '{p2}' no es palindromo")

    if anagrama(p1,p2):
        print(f"La palabra '{p1}' y '{p2}' son anagramas")
    else:
        print(f"La palabra '{p1}' y '{p2}' no son anagramas")

    if isograma(p1):
        print(f"La palabra '{p1}' es isograma")
    else:
        print(f"La palabra '{p1}' no es isograma")

    if isograma(p2):
        print(f"La palabra '{p2}' es isograma")
    else:
        print(f"La palabra '{p2}' no es isograma")

    opcion = input("Desea probar con otra palabra? ").strip().lower()
    if opcion not in ("si","sí"):
        print("¡Hasta luego!")
        break