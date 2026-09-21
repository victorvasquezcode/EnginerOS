# 01===========================================================================
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
def ejercicio_01():
    for numero in range(10,56,2):
        if numero == 16 and numero % 3 == 0:
            continue
        print(f"numeros validos:{numero}")

# 02===========================================================================
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

def fizz_buzz(param1: str = "Fizz", param2: str = "Buzz") -> str:
    contador = 0
    for numero in range(1,101):
        if numero % 15 == 0:
            print(f"{param1} {param2}")
        elif numero % 3 == 0:
            print(param1)
        elif numero % 5 == 0:
            print(param2)
        else:
            print(numero)
            contador += 1
    return f"El numero de veces que se ha impreso solo el numero es: {contador}"

# 03===========================================================================
# PARTE 2: DIFICULTAD EXTRA - AGENDA DE CONTACTOS
# =============================================================================

# --- 1. ESTRUCTURA DE DATOS PRINCIPAL ---
# Razonar: ¿Qué estructura native es ideal para buscar rápido un contacto por su NOMBRE?
# Pista: Un diccionario donde la "clave" sea el nombre y el "valor" sea el teléfono.
agenda = {}

# --- 2. FUNCIONES DE VALIDACIÓN ---
# Crear una función para validar el teléfono según las reglas:
# - ¿El valor ingresado contiene solo dígitos numéricos?
# - ¿La longitud está dentro del límite permitido (ej. mayor a 0 y menor o igual a 11)?
# - Retornar un booleano (True/False) para saber si pasa la prueba.
def validar_telefono (telefono: str) -> bool:
    es_valido = False
    if telefono.isdigit() and 0 < len(telefono) <= 11:
        es_valido = True
    return es_valido
# --- 3. FUNCIONES DE OPERACIONES DE LA AGENDA ---

# Función: BÚSQUEDA
# - Pedir el nombre a buscar.
# - Verificar si existe en la estructura.
# - Si existe: mostrar nombre y teléfono.
# - Si no existe: mostrar mensaje de error.
def busqueda ():
    nombre = input("Ingrese el nombre que desea buscar: ").strip().capitalize()
    if nombre in agenda:
        print(f"Nombre contacto: '{nombre}' | Telefono: '{agenda[nombre]}'")
    else:
        print(f"No se encontro '{nombre}' en la agenda")
# Función: INSERCIÓN
# - Pedir el nombre del nuevo contacto.
# - Pedir el teléfono y usar la función de validación dentro de un bucle hasta que sea válido.
# - Si el nombre ya existe, avisar al usuario o redirigir a actualización.
# - Guardar la relación nombre -> teléfono.
def insercion():
    nombre_nuevo_contacto = input("Ingrese el nombre del nuevo contacto: ").strip().capitalize()

    if nombre_nuevo_contacto in agenda:
        print(f"Ya existe en la agenda {nombre_nuevo_contacto}")
        opcion = input(f"Desea actualizar el contactoñ{nombre_nuevo_contacto}? (si/no)").strip().lower()

        if opcion in ("si", "sí", "s"):
            actualizar()
            return
        else:
            print("Operacion cancelada")
            return
        
    while True:
        telefono_nuevo_contacto = input(f"Ingrese el numero para el contacto '{nombre_nuevo_contacto}': ").strip()
        if validar_telefono(telefono_nuevo_contacto):
            print(f"'{telefono_nuevo_contacto}' telefono valido")
            break
        print(f"'{telefono_nuevo_contacto}' es un numero invalido")

    agenda[nombre_nuevo_contacto] = telefono_nuevo_contacto
    print(f"Agredo correctamente el contacto {nombre_nuevo_contacto} con su telefono {telefono_nuevo_contacto}")

# Función: ACTUALIZACIÓN
# - Pedir el nombre del contacto a actualizar.
# - Verificar si existe.
# - Si existe: pedir el nuevo teléfono (validándolo) y actualizar el valor.
# - Si no existe: informar que no se encontró el contacto.
def actualizar():
    nuevo_nombre = input("Ingresa el nombre del contacto para actualizar: ").strip().capitalize()

    if nuevo_nombre in agenda:
        while True:
            nuevo_telefono = input(f"Ingrese el nuevo numero para el contacto '{nuevo_nombre}': ").strip()
            if validar_telefono(nuevo_telefono):
                print(f"'{nuevo_telefono}' es un numero valido'")
                break
            print(f"'{nuevo_telefono}' es un numero invalido'")

        agenda[nuevo_nombre] = nuevo_telefono
        print("Telefono actualizado correctamente.")
    else:
        print(f"No se encontro el contacto {nuevo_nombre}.")

# Función: ELIMINACIÓN
# - Pedir el nombre a eliminar.
# - Verificar si existe.
# - Si existe: borrar el registro de la estructura y confirmar al usuario.
# - Si no existe: informar que no se encontró.
def eliminar():
    nombre_eliminar = input("Ingrese el nombre a eliminar: ").strip().capitalize()

    if nombre_eliminar in agenda:
        del agenda[nombre_eliminar]
        print(f"Se elimino el contacto '{nombre_eliminar}' de la agenda")
    else:
        print(f"No se encontro el contacto '{nombre_eliminar}'")
# --- 4. BUCLE PRINCIPAL Y MENÚ DE INTERACCIÓN ---
# - Definir una variable de control para mantener el programa activo (ej. ejecutable = True).
# - Iniciar bucle while:
#     - Mostrar las opciones del menú (1. Buscar, 2. Insertar, 3. Actualizar, 4. Eliminar, 5. Salir).
#     - Leer la opción seleccionada por el usuario.
#     - Evaluar la opción (usar estructuras condicionales if / elif / else o match/case):
#         - Caso 1: Llamar función de Búsqueda.
#         - Caso 2: Llamar función de Inserción.
#         - Caso 3: Llamar función de Actualización.
#         - Caso 4: Llamar función de Eliminación.
#         - Caso 5: Cambiar variable de control para romper el bucle y despedir al usuario.
#         - Caso Default: Notificar que la opción elegida no es válida.

def menu_principal():
    while True:
        print("\n--- AGENDA ---")
        print("Opcion de Agenda")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion_seleccionada = input("Ingrese una opcion para la agenda: ").strip()

        match opcion_seleccionada:
            case "1":
                busqueda()
            case "2":
                insercion()
            case "3":
                actualizar()
            case "4":
                eliminar()
            case "5":
                print("¡Hasta luego!")
                break
            case __:
                print("No se selecciono una opcion valida.")

if __name__ == "__main__":
    resultado = fizz_buzz()
    print(resultado)
