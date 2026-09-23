# =============================================================================
# DIFICULTAD EXTRA: ANALIZADOR DE PALÍNDROMOS, ANAGRAMAS E ISOGRAMAS
# =============================================================================

# --- 1. FUNCIONES AUXILIARES DE SANITIZACIÓN ---
# Crear una función para normalizar el texto antes de analizar:
# - Convertir todo a minúsculas.
# - Remover espacios en blanco y caracteres no alfabéticos.
def normalizar_texto(texto: str):
    return "".join(letra.lower() for letra in texto if letra.isalpha())

# --- 2. FUNCIONES DE COMPROBACIÓN ---

# A) Palíndromo (Palabra o frase que se lee igual de izquierda a derecha y viceversa):
# - Definir función 'es_palindromo(palabra: str) -> bool'.
# - Sanitizar la cadena.
# - Comparar la cadena original con su versión invertida ([::-1]).
# - Retornar True si son idénticas, False en caso contrario.
def es_palindromo(palabra: str) -> bool:
    palabra_limpia = normalizar_texto(palabra)
    return palabra_limpia == palabra_limpia[::-1]

# B) Anagrama (Palabra formada al reordenar TODAS las letras de otra palabra exactamente igual):
# - Definir función 'es_anagrama(palabra1: str, palabra2: str) -> bool'.
# - Sanitizar ambas palabras.
# - Verificar que no sean la misma palabra exacta (un anagrama requiere dos palabras distintas).
# - Comprobar si ambas palabras tienen la misma cantidad de caracteres.
# - Ordenar alfabéticamente las letras de ambas palabras (función sorted()) y comparar si son idénticas.
# - Retornar el resultado booleano.
def es_anagrama(palabra1: str, palabra2: str) -> bool:
    p1 = normalizar_texto(palabra1)
    p2 = normalizar_texto(palabra2)
    return len(p1) == len(p2) and p1 != p2 and sorted(p1) == sorted(p2)

# C) Isograma (Palabra en la que NINGUNA letra se repite, o cada letra se repite el mismo número de veces):
# - Definir función 'es_isograma(palabra: str) -> bool'.
# - Sanitizar la palabra.
# - Opción Heterograma / Isograma de orden 1 (ninguna letra se repite):
#     - Comparar la longitud de la palabra con la longitud de su conjunto (set(palabra)).
#     - Si len(palabra) == len(set(palabra)), significa que no hay caracteres duplicados.
# - Retornar el resultado booleano.
def es_isograma(palabra: str) -> bool:
    palabra_limpia = normalizar_texto(palabra)
    return len(palabra_limpia) == len(set(palabra_limpia))

# --- 3. BUCLE PRINCIPAL / INTERFACCIÓN DE CONSOLA ---
# - Definir la función principal para interactuar con el usuario.
# - Solicitar el ingreso de la primera palabra.
# - Solicitar el ingreso de la segunda palabra.
# - Ejecutar e imprimir las verificaciones individualmente para cada palabra y en conjunto:
#     - ¿La palabra 1 es Palíndromo?
#     - ¿La palabra 2 es Palíndromo?
#     - ¿La palabra 1 es Isograma?
#     - ¿La palabra 2 es Isograma?
#     - ¿La palabra 1 y la palabra 2 forman un Anagrama?
def funcion_principal():
    while True: 
        print("\n--- PALINDROMO, ISOGRAMA O ANAGRAMA ? ---")
    
        primera_palabra = input("Ingresar la primera palabra: ").strip()
        segunda_palabra = input("Ingresar la segunda palabra: ").strip()

        if not primera_palabra:
            print("Debe ingresar palabras validas")
            continue
        elif not segunda_palabra:
            print("Debe ingresar palabras validas")
            continue

        p1_palindromo = "SI" if es_palindromo(primera_palabra) else "NO"
        p2_palindromo = "SI" if es_palindromo(segunda_palabra) else "NO"

        p1_isograma = "SI" if es_isograma(primera_palabra) else "NO"
        p2_isograma = "SI" if es_isograma(segunda_palabra) else "NO"

        p1_p2_anagrama = "SI" if es_anagrama(primera_palabra, segunda_palabra) else "NO"

        print(f"La palabra '{primera_palabra}' es palindromo ? -> {p1_palindromo} ")
        print(f"La palabra '{segunda_palabra}' es palindromo ? -> {p2_palindromo} ")

        print(f"La palabra '{primera_palabra}' es isograma ? -> {p1_isograma} ")
        print(f"La palabra '{segunda_palabra}' es isograma ? -> {p2_isograma} ")

        print(f"La palabra '{primera_palabra}' y '{segunda_palabra}' son anagramas ? -> {p1_p2_anagrama} ")

        opcion = input("Desea probar con otras palabras ? ").strip().lower()
        if opcion in ("si", "sí", "s"):
            print("¡Comencemos denuevo!")
        else:
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    funcion_principal()