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
    return telefono.isdigit() and 0 < len(telefono) <= 11

# --- 3. FUNCIONES DE OPERACIONES DE LA AGENDA ---

# Función: BÚSQUEDA
# - Pedir el nombre a buscar.
# - Verificar si existe en la estructura.
# - Si existe: mostrar nombre y teléfono.
# - Si no existe: mostrar mensaje de error.
def busqueda():
    nombre = input("Que nombre desea buscar en la agenda: ").strip().capitalize()
    if nombre in agenda:
        print(f"El nombre del contacto es '{nombre}' y su telefono es '{agenda[nombre]}'")
    else:
        print(f"No se encontro el contacto con el nombre '{nombre}'")

# Función: INSERCIÓN
# - Pedir el nombre del nuevo contacto.
# - Pedir el teléfono y usar la función de validación dentro de un bucle hasta que sea válido.
# - Si el nombre ya existe, avisar al usuario o redirigir a actualización.
# - Guardar la relación nombre -> teléfono.
def insertar():
    nombre = input("Con que nombre se guardara el contacto: ").strip().capitalize()
    if nombre in agenda:
        print(f"El nombre '{nombre}' ya existe en la agenda")
        opcion = input(f"Desea actualizar el contacto '{nombre}' ?")
        if opcion in ("si","sí","s"):
            actualizar(nombre)
        return
    
    while True:
        telefono = input("Con que telefono se guardara el contacto: ").strip()
        if validar_telefono(telefono):
            break
        else:
            print(f"Numero de telefono '{telefono}' no cumple con los parametros")

    agenda[nombre] = telefono
    print("Se guardo correctamente el contacto.")

# Función: ACTUALIZACIÓN
# - Pedir el nombre del contacto a actualizar.
# - Verificar si existe.
# - Si existe: pedir el nuevo teléfono (validándolo) y actualizar el valor.
# - Si no existe: informar que no se encontró el contacto.
def actualizar(nombre: str = None):
    if nombre is None:
        nombre = input("Ingresar el nombre del contacto para actualizar: ").strip().capitalize()
    if nombre in agenda:
        while True:
            telefono = input("Ingresar el nuevo telefono: ")
            if validar_telefono(telefono):
                break
            else:
                print(f"Numero de telefono '{telefono}' no cumple con los parametros")
        agenda[nombre] = telefono
    else:
        print(f"No se encontro el contacto '{nombre}'")

# Función: ELIMINACIÓN
# - Pedir el nombre a eliminar.
# - Verificar si existe.
# - Si existe: borrar el registro de la estructura y confirmar al usuario.
# - Si no existe: informar que no se encontró.
def eliminar():
    nombre = input("Cual es el nombre de contacto a eliminar: ").strip().capitalize()
    if nombre in agenda:
        del agenda[nombre]
        print(f"Se elimino correctamente el contacto '{nombre}'")
    else:
        print(f"No se encontro el contacto '{nombre}' para eliminar")

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
        print("\n--- PROGRAMA DE AGENDA ---")
        print("1. Buscar contacto en Agenda")
        print("2. Insertar contacto en Agenda")
        print("3. Actualizar contacto en Agenda")
        print("4. Eliminar contacto en Agenda")
        print("5. Salir")
        opcion = input("Seleccione una opcion valida: ").strip()
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
                print("¡Hasta Luego!")
                break
            case _:
                print("No se selecciono una opcion valida.")

if __name__ == "__main__":
    menu_principal()