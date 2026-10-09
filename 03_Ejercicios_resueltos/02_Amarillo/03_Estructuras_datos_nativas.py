# 🟡 [03] ESTRUCTURAS DE DATOS

# DIFICULTAD EXTRA (opcional):
# Crea una agenda de contactos por terminal.
# - Debes implementar funcionalidades de búsqueda, inserción, actualización
#   y eliminación de contactos.
# - Cada contacto debe tener un nombre y un número de teléfono.
# - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
#   y a continuación los datos necesarios para llevarla a cabo.
# - El programa no puede dejar introducir números de teléfono no numéricos y con más
#   de 11 dígitos (o el número de dígitos que quieras).
# - También se debe proponer una operación de finalización del programa.

agenda = {}

def validacion(telefono: str) -> bool:
    return telefono.isdigit() and len(telefono) <= 11
    
def busqueda():
    nombre = input("Ingrese el nombre para buscar en los contactos: ").strip().capitalize()
    if nombre in agenda:
        print(f"El contacto '{nombre}' esta registrado con el numero '{agenda[nombre]}'")
    else:
        print(f"No se encontro el contacto '{nombre}' en la agenda")
        
def insercion():
    nombre = input("Ingrese el nombre del contacto: ").strip().capitalize()
    while True:
        telefono = input("Ingrese el numero del contacto: ").strip()
        if not validacion(telefono):
            continue
        agenda[nombre] = telefono
        print(f"Se registro correctamente el contacto '{nombre}' con el telefono '{telefono}'")
        break

def actualizacion():
    nombre = input("Ingrese el nombre para actualizar el telefono: ").strip().capitalize()
    encontrado = False

    if nombre in agenda:
        encontrado = True
        while True:
            telefono = input("Ingrese el nuevo numero del contacto: ").strip()
            if not validacion(telefono):
                continue
            agenda[nombre] = telefono
            print(f"Se actualizo correctamente el telefono '{telefono}' para el contacto '{nombre}'")
            break
    
    if not encontrado:
        print(f"No se encontro el contado '{nombre}' en la agenda")

def eliminacion():
    nombre = input("Ingrese el nombre para eliminar en la agenda: ").strip().capitalize()
    encontrado = False

    if nombre in agenda:
        encontrado = True
        del agenda[nombre]
        print(f"Se elimino correctamente el contacto '{nombre}'")

    if not encontrado:
        print(f"No se encontro el contacto '{nombre}' en la agenda")

while True:
    print("\n--- AGENDA ---")
    print("1. Insertar contacto en agenda")
    print("2. Buscar contacto en agenda")
    print("3. Actualizar contacto en agenda")
    print("4. Eliminar contacto en agenda")
    print("5. Salir de agenda")
    opcion = input("Ingrese una opcion: ")
    match opcion:
        case "1":
            insercion()
            print(agenda)
        case "2":
            busqueda()
        case "3":
            actualizacion()
        case "4":
            eliminacion()
        case "5":
            print("¡Hasta luego!")
            break
        case _:
            print("Seleccione una opcion valida")