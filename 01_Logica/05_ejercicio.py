# =============================================================================
# RETO 04: CADENAS DE CARACTERES (STRINGS)
# Enunciado:
# 1. Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de
#    caracteres en Python:
#    - Acceso a caracteres específicos, subcadenas (slicing), longitud.
#    - Concatenación, repetición, recorrido (iteración).
#    - Conversión a mayúsculas, minúsculas, formato título.
#    - Reemplazo, división (split), unión (join).
#    - Interpolación/f-strings, verificación (start/endswith, isdigit, etc.).
# 2. DIFICULTAD EXTRA (Opcional):
#    Crea un programa que analice dos palabras y compruebe si son:
#    - Palíndromos
#    - Anagramas
#    - Isogramas
# =============================================================================

# -----------------------------------------------------------------------------
# 1. OPERACIONES BÁSICAS: Acceso, Subcadenas, Longitud y Recorrido
# Pistas: Usa índices [0], slicing [inicio:fin:paso], len() y bucles for.
# -----------------------------------------------------------------------------
print("--- 1. OPERACIONES BÁSICAS Y ACCESO ---")
texto_ejemplo = "Pythonista"

# TODO:
# - Obtén el primer y el último carácter usando índices.
primer_caracter = texto_ejemplo[0]
ultimo_caracter = texto_ejemplo[-1]
print(f"Primer caracter: {primer_caracter}\nSegundo Caracter: {ultimo_caracter}")

# - Extrae una subcadena (por ejemplo, "Python") usando slicing.
palabra_python = texto_ejemplo[0:6:1]
print(f"Subcadena: {palabra_python}")

# - Invierte la cadena usando slicing [::-1].
palabra_invertida = texto_ejemplo[::-1]
print(f"Texto invertido: {palabra_invertida}")

# - Imprime la longitud del texto con len().
longitud_texto = len(texto_ejemplo)
print(f"Longitud: {longitud_texto}")

# - Recorre la cadena imprimiendo carácter por carácter.
for letra in texto_ejemplo:
    print(f"{letra}")


# -----------------------------------------------------------------------------
# 2. CONCATENACIÓN, REPETICIÓN E INTERPOLACIÓN
# Pistas: Usa +, *, f"{variable}", format() o %.
# -----------------------------------------------------------------------------
print("\n--- 2. CONCATENACIÓN Y FORMATO ---")
saludo = "Hola"
nombre = "Víctor"

# TODO:
# - Une dos cadenas usando +.
print(saludo + " " + nombre)

# - Repite una cadena varias veces usando *.
print(saludo * 3) 

# - Muestra un mensaje interpolado usando f-strings (f"{saludo} {nombre}").
print(f"{saludo} {nombre}")
print(f"{saludo * 3}")

# -----------------------------------------------------------------------------
# 3. TRANSFORMACIÓN Y LIMPIEZA
# Pistas: Usa .upper(), .lower(), .title(), .capitalize(), .strip(), .replace()
# -----------------------------------------------------------------------------
print("\n--- 3. TRANSFORMACIÓN Y LIMPIEZA ---")
cadena_desordenada = "  hola MUNDO desde Python hola   "

# TODO:
# - Convierte todo a mayúsculas (.upper()).
print(cadena_desordenada.upper())
# - Convierte todo a minúsculas (.lower()).
print(cadena_desordenada.lower())
# - Quita los espacios al inicio y al final (.strip()).
print(cadena_desordenada.strip())
# - Reemplaza una palabra por otra (.replace()).
print(cadena_desordenada.replace("hola","como"))
# - Capitalizar.
print(cadena_desordenada.strip().capitalize())
# - Title.
print(cadena_desordenada.title())

# -----------------------------------------------------------------------------
# 4. DIVISIÓN, UNIÓN Y VERIFICACIÓN
# Pistas: Usa .split(), .join(), .startswith(), .endswith(), .isdigit(), .isalpha()
# -----------------------------------------------------------------------------
print("\n--- 4. DIVISIÓN, UNIÓN Y COMPROBACIONES ---")
lenguajes = "Python,JavaScript,SQL,HTML"

# TODO:
# - Separa la cadena en una lista de palabras usando .split(",").
lista_lenguajes = lenguajes.split(",")
print(f"{lista_lenguajes}")

# - Une una lista de palabras en una cadena usando ", ".join(lista).
cadena_unida = ", ".join(lista_lenguajes)
print(cadena_unida)

# - Comprueba si una cadena empieza o termina con cierta letra.
print(lenguajes.startswith("P"))
print(lenguajes.endswith("L"))

# - Verifica si una cadena contiene solo números (.isdigit()) o solo letras (.isalpha()).
print(lenguajes.isdigit())
print(lenguajes.isalpha())


# =============================================================================
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

print("\n=== DIFICULTAD EXTRA: ANALIZADOR DE PALABRAS ===")

def analizar_palabras(palabra1: str, palabra2: str):
        palabra1_limpia = palabra1.strip().lower().replace(" ","")
        palabra2_limpia = palabra2.strip().lower().replace(" ","")

        print(f"\n---Analisis para '{palabra1_limpia}' y '{palabra2_limpia}' ---'")
        # TODO: Implementa la lógica para verificar:
        # 1. ¿Es palabra1 o palabra2 un palíndromo?
        print(f"- '{palabra1_limpia}' : {'Es palíndromo' if palabra1_limpia == palabra1_limpia[::-1] else 'No es palíndromo'}")
        print(f"- '{palabra2_limpia}' : {'Es palíndromo' if palabra2_limpia == palabra2_limpia[::-1] else 'No es palíndromo'}")

        # 2. ¿Son palabra1 y palabra2 anagramas entre sí?
        print(f"- '{palabra1_limpia}' y '{palabra2_limpia}' : {'Son anagramas' if sorted(palabra1_limpia) == sorted(palabra2) else 'No son anagramas'}")

        # 3. ¿Es palabra1 o palabra2 un isograma?
        print(f"- '{palabra1_limpia}'  : {'Es Isograma' if len(palabra1_limpia) == len(set(palabra1_limpia)) else 'No es un Isograma'}")
        print(f"- '{palabra2_limpia}'  : {'Es Isograma' if len(palabra2_limpia) == len(set(palabra2_limpia)) else 'No es un Isograma'}")
        
        pass

# Bloque interactivo para probar el analizador
while True:
    word1 = input("Ingresa la primera palabra: ")
    word2 = input("Ingresa la segunda palabra: ")

    if not word1 or not word2:
        print("Las palabras no pueden estar vacias")
        continue

    analizar_palabras(word1, word2)

    opcion_salida = input("Desea comparar otras dos palabras? (1-Si 2-No): ").strip()

    if opcion_salida == "1":
        continue

    if opcion_salida == "2":
        print("Hasta luego")
        break
        
    else:
        print("Seleccione una opcion valida (1 o 2)")