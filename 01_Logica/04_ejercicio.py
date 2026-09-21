# =============================================================================
# PARTE 1: OPERACIONES CON CADENAS DE CARACTERES (STRINGS) EN PYTHON
# =============================================================================

# 1. Creación e Inicialización:
# - Cadenas simples, dobles y multilínea (tres comillas).
cadena_simple = 'Hola, Python'
cadena_doble = "Hola, Python"
cadena_multilinea = """Esta es una cadena
que abarca multiples lineas
sin necesidad de usar caracteres de escape."""

# 2. Propiedades Básicas:
# - Longitud de una cadena (función len()).
print(f"Este es la longitud de una cadena simple: {len(cadena_simple)}")
print(f"Este es la longitud de una cadena doble: {len(cadena_doble)}")
print(f"Este es la longitud de una cadena multiple: {len(cadena_multilinea)}")

# 3. Acceso a Caracteres y Subcadenas (Slicing / Rebanado):
# - Acceso por índice positivo y negativo (primer caracter, último caracter).
# - Extracción de subcadenas con rangos [inicio:fin:paso].
# - Inversión de una cadena usando rebanado.
texto = "Python"
print(f"\nEste es la primera letra de mi texto: {texto[0]}")
print(f"Este es la ultima letra de mi texto: {texto[-1]}")
print(f"Extraemos las dos primeras letras: {texto[0:2:1]}")
print(f"Invertir todo el texto: {texto[::-1]}")

# 4. Concatenación y Repetición:
# - Unir cadenas con el operador '+'.
# - Repetir cadenas con el operador '*'.
lenguaje = "Python"
nivel = "Avanzado"
print("\n" + lenguaje + " " + nivel)
print(lenguaje * 3)

# 5. Formateo e Interpolación:
# - Formateo moderno usando f-strings (f"... {variable} ...").
# - Método .format().
print(f"\nMi lenguaje es {lenguaje} en un nivel {nivel}")
print("Mi lenguaje es {} en un nivel {}".format(lenguaje, nivel))
print("Nivel: {1} | Lenguaje: {0}".format(lenguaje,nivel))
print("Mi lenguaje es {lang} en un nivel {lvl}".format(lang = lenguaje , lvl = nivel))

# 6. Transformación de Caso / Mayúsculas y Minúsculas:
# - Convertir a mayúsculas (.upper()).
# - Convertir a minúsculas (.lower()).
# - Capitalizar primera letra (.capitalize()).
# - Convertir formato título (.title()).
# - Invertir mayúsculas y minúsculas (.swapcase()).
texto = "aprendiendo lenguaje python en nivel avanzado"
print(f"\nTexto original: {texto}")
print(f"Convertir a mayusculas: {texto.upper()}")
print(f"Convertir a minusculas: {texto.lower()}")
print(f"Convertir la primera letra en mayuscula: {texto.capitalize()}")
print(f"Convertir a titulo (letra inicial en mayuscula por palabra): {texto.title()}")
print(f"Invertir mayusculas en minusculas (viceversa):  {texto.swapcase()}")

# 7. Búsqueda y Reemplazo:
# - Reemplazar subcadenas o caracteres (.replace()).
# - Encontrar posición/índice de una subcadena (.find() / .index()).
# - Contar ocurrencias de una subcadena (.count()).
print(f"\nReemplazar python por Python 3: {texto.replace("python","Python 3")}")
print(f"Encontrar la posicion de la subcadena: {texto.find("python")}")
print(f"Encontrar el indice de la subcadena: {texto.index("python")}")
print(f"Contar cuantas 'a' hay en el texto: {texto.count("a")}")

# 8. Limpieza y Eliminación de Espacios:
# - Eliminar espacios en blanco iniciales y finales (.strip()).
# - Eliminar espacios a la izquierda (.lstrip()) o derecha (.rstrip()).
texto_sucio = "   hola mundo   "
print(f"\nTexto original: {texto_sucio}")
print(f"Eliminar espacios en blanco iniciales y finales: {texto_sucio.strip()}")
print(f"Eliminar espacios solo de la derecha (rigth): {texto_sucio.rstrip()}")
print(f"Eliminar espacios solo de la izquierda (left): {texto_sucio.lstrip()}")

# 9. División y Unión:
# - Dividir una cadena en lista de subcadenas por un delimitador (.split()).
# - Unir elementos de una lista en una sola cadena (.join()).
csv_datos = "java,python,javascript,c++"
print(f"\nCadena original: {csv_datos}")

lista_lenguaje = csv_datos.split(",")
print(f"Lista dividida: {lista_lenguaje}")

cadena_unida = " - ".join(lista_lenguaje)
print(f"Unidos con guion: {cadena_unida}")

cadena_con_comas_y_espacios = ", ".join(lista_lenguaje)
print(f"Unidos con coma y espacio: {cadena_con_comas_y_espacios}")

# 10. Verificaciones y Validaciones de Contenido:
# - Comprobar si contiene solo caracteres alfabéticos (.isalpha()).
# - Comprobar si contiene solo dígitos numéricos (.isdigit() / .isnumeric()).
# - Comprobar si es alfanumérico (.isalnum()).
# - Comprobar si inicia o termina con una subcadena (.startswith(), .endswith()).
# - Comprobar presencia de una subcadena con el operador de pertenencia 'in'.
codigo ="12345"
print(f"\nTexto original: {codigo}")
print(f"Contiene alguna letra ? {codigo.isalpha()}")
print(f"Contiene digitos numeros ? {codigo.isdigit()} {codigo.isnumeric()}")
print(f"Contiene letras y numeros ? {codigo.isalnum()}")
print(f"Inicia en una subcadena '1'? {codigo.startswith("1")} Termina en una subcadena '5'? {codigo.endswith("5")}")
print(f"Tiene el '234' ? {'234' in codigo}")

# 11. Recorrido / Iteración:
# - Recorrer caracter por caracter usando un bucle 'for'.
# - Recorrer con índice usando 'enumerate()'.
palabra = "Code"

print(f"\nLa palabra es {palabra}")
for caracter in palabra:
    print(caracter)

for indice, caracter in enumerate(palabra):
    print(f"Indice {indice}: {caracter}")


# =============================================================================
# DIFICULTAD EXTRA: ANALIZADOR DE PALÍNDROMOS, ANAGRAMAS E ISOGRAMAS
# =============================================================================

# --- 1. FUNCIONES AUXILIARES DE SANITIZACIÓN ---
# Crear una función para normalizar el texto antes de analizar:
# - Convertir todo a minúsculas.
# - Remover espacios en blanco y caracteres no alfabéticos.
def sanitizar_texto (texto: str) -> str:
    caracteres_limpios = []
    for caracter in texto:
        if caracter.isalpha():
            caracteres_limpios.append(caracter.lower())
    return "".join(caracteres_limpios)


# --- 2. FUNCIONES DE COMPROBACIÓN ---

# A) Palíndromo (Palabra o frase que se lee igual de izquierda a derecha y viceversa):
# - Definir función 'es_palindromo(palabra: str) -> bool'.
# - Sanitizar la cadena.
# - Comparar la cadena original con su versión invertida ([::-1]).
# - Retornar True si son idénticas, False en caso contrario.
def es_palindromo(palabra: str) -> bool:
    texto_limpio = sanitizar_texto(palabra)
    return texto_limpio == texto_limpio[::-1]

# B) Anagrama (Palabra formada al reordenar TODAS las letras de otra palabra exactamente igual):
# - Definir función 'es_anagrama(palabra1: str, palabra2: str) -> bool'.
# - Sanitizar ambas palabras.
# - Verificar que no sean la misma palabra exacta (un anagrama requiere dos palabras distintas).
# - Comprobar si ambas palabras tienen la misma cantidad de caracteres.
# - Ordenar alfabéticamente las letras de ambas palabras (función sorted()) y comparar si son idénticas.
# - Retornar el resultado booleano.
def es_anagrama(palabra1:str, palabra2: str) -> bool:
    palabra1_limpio, palabra2_limpio = sanitizar_texto(palabra1) , sanitizar_texto(palabra2)
    return palabra1_limpio != palabra2_limpio and sorted(palabra1_limpio) == sorted(palabra2_limpio)

# C) Isograma (Palabra en la que NINGUNA letra se repite, o cada letra se repite el mismo número de veces):
# - Definir función 'es_isograma(palabra: str) -> bool'.
# - Sanitizar la palabra.
# - Opción Heterograma / Isograma de orden 1 (ninguna letra se repite):
#     - Comparar la longitud de la palabra con la longitud de su conjunto (set(palabra)).
#     - Si len(palabra) == len(set(palabra)), significa que no hay caracteres duplicados.
# - Retornar el resultado booleano.
def es_isograma(palabra:str) -> bool:
    palabra_limpia = sanitizar_texto(palabra)
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
    print("\n--- ANALIZADOR DE ANÁLISIS ---")
    primera_palabra = input("Ingresa la primera palabra: ").strip()
    segunda_palabra = input("Ingresa la segunda palabra: ").strip()

    print("\n--- RESULTADO DEL ANÁLISIS ---")
    es_p1 = "SÍ" if es_palindromo(primera_palabra) else "NO"
    es_i1 = "SÍ" if es_isograma(primera_palabra) else "NO"
    print(f"'{primera_palabra}' -> Palíndromo: {es_p1} | Isograma: {es_i1}")

    es_p2 = "SÍ" if es_palindromo(segunda_palabra) else "NO"
    es_i2 = "SÍ" if es_isograma(segunda_palabra) else "NO"
    print(f"'{segunda_palabra}' -> Palíndromo: {es_p2} | Isograma: {es_i2}")

    es_ana = "SÍ" if es_anagrama(primera_palabra, segunda_palabra) else "NO"
    print(f"¿ '{primera_palabra}' y '{segunda_palabra} son Anagramas?: {es_ana}'")

if __name__ == "__main__":
    funcion_principal()