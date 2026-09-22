# =============================================================================
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
def validar_telefono(telefono: str):
    telefono_limpio = telefono.strip()
    return telefono_limpio.isdigit() and 0 < len(telefono_limpio) <= 11

# --- 3. FUNCIONES DE OPERACIONES DE LA AGENDA ---

# Función: BÚSQUEDA
# - Pedir el nombre a buscar.
# - Verificar si existe en la estructura.
# - Si existe: mostrar nombre y teléfono.
# - Si no existe: mostrar mensaje de error.
def busqueda():
    nombre = input("Cual es el nombre que desea buscar en la agenda: ").strip().capitalize()

    if nombre in agenda:
        print(f"El contacto '{nombre}' esta registrado en la agenda con el numero '{agenda[nombre]}'")
    else:
        print(f"El contacto '{nombre}' no existe en la agenda")
# Función: INSERCIÓN
# - Pedir el nombre del nuevo contacto.
# - Pedir el teléfono y usar la función de validación dentro de un bucle hasta que sea válido.
# - Si el nombre ya existe, avisar al usuario o redirigir a actualización.
# - Guardar la relación nombre -> teléfono.
def insertar():
    nuevo_contacto = input("Ingresar el nombre del nuevo contacto: ").strip().capitalize()

    if nuevo_contacto in agenda:
        print(f"El contacto '{nuevo_contacto}' ya existe")
        opcion = input("Desea actualizar el contacto ? (si/no): ").strip().lower()
        if opcion in ("si","sí","s"):
            actualizar(nuevo_contacto)
        return
    
    while True:
        telefono = input("Ingresar el telefono del nuevo contacto: ").strip()
        if validar_telefono(telefono):
            print(f"El numero '{telefono}' esta correcto")
            break
        else:
            print(f"El numero '{telefono}' es invalido")

    agenda[nuevo_contacto] = telefono
    print(f"Se agrego correctamente '{nuevo_contacto}' en la agenda con el numero '{telefono}'")

# Función: ACTUALIZACIÓN
# - Pedir el nombre del contacto a actualizar.
# - Verificar si existe.
# - Si existe: pedir el nuevo teléfono (validándolo) y actualizar el valor.
# - Si no existe: informar que no se encontró el contacto.
def actualizar(nombre: str = None):
    if nombre is None:
        nombre = input("Ingresa el nombre del contacto para actualizar: ").strip().capitalize()
    if nombre in agenda:
        while True:
            nuevo_telefono = input(f"Ingresar el nuevo telefono para el contacto '{nombre}': ")
            if validar_telefono(nuevo_telefono):
                print(f"El numero '{nuevo_telefono}' esta correcto")
                break
            else:
                print(f"El numero '{nuevo_telefono}' es invalido")
        agenda[nombre] = nuevo_telefono
    else:
        print(f"No se encontro el contacto con el nombre '{nombre}'")
# Función: ELIMINACIÓN
# - Pedir el nombre a eliminar.
# - Verificar si existe.
# - Si existe: borrar el registro de la estructura y confirmar al usuario.
# - Si no existe: informar que no se encontró.
def eliminar():
    nombre_eliminar = input("Ingresa el nombre del contacto para eliminar: ").strip().capitalize()
    if nombre_eliminar in agenda:
        del agenda[nombre_eliminar]
        print(f"Se elimino correctamente {nombre_eliminar}")
    else:
        print(f"No se encontro '{nombre_eliminar}' en los contactos")

def listar_contactos():
    if not agenda:
        print("La agenda esta vacia")
        return
    
    for nombre,telefono in agenda.items():
        print("=" * 40)
        print(f"- Nombre de Contacto: {nombre:<20} | - Telefono {telefono:<20}")

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
def menu_interaccion():
    while True:
        print("1. Buscar en la agenda.")
        print("2. Insertar contacto en la agenda.")
        print("3. Actualizar contacto en la agenda.")
        print("4. Eliminar contacto en la agenda.")
        print("5. Listar contactos en la agenda.")
        print("6. Salir de la agenda.")
        opcion = input("Ingresa que desea realizar en la agenda: ").strip()
        match opcion:
            case "1":
                busqueda()
            case "2":
                insertar()
            case "3":
                actualizar()
            case "4":
                eliminar()
            case "5":
                listar_contactos()
            case "6":
                print("¡Hata Luego!")
                break
            case _:
                print("Opcion no valida")

if __name__ == "__main__":
    menu_interaccion()