# =============================================================================
# RETO 11: MANEJO DE ARCHIVOS (.TXT)
#
# CONCEPTOS CLAVE:
# 1. open(filename, mode): Función nativa para abrir/crear archivos.
#    - "w" (Write): Abre para escribir (sobrescribe o crea si no existe).
#    - "r" (Read): Abre para lectura.
#    - "a" (Append): Abre para añadir contenido al final sin borrar lo existente.
# 2. Context Manager `with open(...) as archivo:`
#    - Garantiza el cierre automático del archivo, incluso si ocurren errores.
# 3. Módulo `os`: Permite interactuar con el sistema operativo para verificar
#    la existencia de archivos (`os.path.exists()`) y borrarlos (`os.remove()`).
# =============================================================================

import os

# -----------------------------------------------------------------------------
# 1. EJERCICIO PRINCIPAL: MANEJO BÁSICO DE ARCHIVO .TXT
# -----------------------------------------------------------------------------

print("=== MANEJO BÁSICO DE ARCHIVOS ===")

# TODO 1: Define el nombre del archivo con tu usuario de GitHub y extensión .txt
NOMBRE_ARCHIVO = "VictorVasquezT.txt"

# --- Paso A: Crear y escribir en el archivo ---
# TODO 2: Usa 'with open(NOMBRE_ARCHIVO, "w") as archivo:' para escribir tus datos:
# - Tu nombre
# - Edad
# - Lenguaje de programación favorito
with open (NOMBRE_ARCHIVO, "w") as archivo:
    archivo.write("Nombre: Victor Javier Vasquez Trauco\n")
    archivo.write("Edad: 26 años?\n")
    archivo.write("Lenguaje favorito: Python\n")


# --- Paso B: Leer e imprimir el contenido del archivo ---
# TODO 3: Usa 'with open(NOMBRE_ARCHIVO, "r") as archivo:' para leer su contenido e imprimirlo en consola
with open(NOMBRE_ARCHIVO, "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# --- Paso C: Eliminar el archivo del sistema ---
# TODO 4: Usa 'os.remove(NOMBRE_ARCHIVO)' para borrar el archivo y confirma su eliminación en consola
if os.path.exists(NOMBRE_ARCHIVO):
    os.remove(NOMBRE_ARCHIVO)
    print("Archivo eliminado del sistema correctamente.")

print("Proceso principal finalizado.\n")


# =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# =============================================================================

print("=== DIFICULTAD EXTRA: GESTIÓN DE VENTAS ===")

ARCHIVO_VENTAS = "ventas.txt"

# --- Funciones Auxiliares recomendadas ---

def guardar_producto(nombre: str, cantidad: int, precio: float):
    """
    Añade una línea al archivo con el formato: [nombre], [cantidad], [precio]
    """
    # TODO: Usa el modo "a" (append) para agregar el producto al final del archivo ventas.txt
    with open(ARCHIVO_VENTAS, "a") as archivo:
        archivo.write(f"{nombre}, {cantidad}, {precio}\n")
    pass


def consultar_productos():
    """
    Lee todas las líneas de ventas.txt e imprime la lista de productos almacenados.
    """
    # TODO: Lee el archivo con modo "r", procesa las líneas y muestra el contenido.
    # Tip: Valida primero si el archivo existe con 'if os.path.exists(ARCHIVO_VENTAS):'
    if os.path.exists(ARCHIVO_VENTAS):
        with open(ARCHIVO_VENTAS, "r") as archivo:
            consulta = archivo.read()
            print("\n--- PRODUCTOS REGISTRADOS ---")
            print(consulta if consulta else "El archivo esta vacio.")
    else:
        print("Aún no hay ningún producto registrado.")
    pass


def actualizar_producto(nombre_buscar: str, nueva_cantidad: int, nuevo_precio: float):
    """
    Busca un producto por nombre, actualiza sus datos y reescribe el archivo.
    """
    # TODO: Lee todo el archivo, modifica la línea que coincida con 'nombre_buscar' 
    # y reescribe el archivo completo en modo "w".

    if not os.path.exists(ARCHIVO_VENTAS):
        print("No existe el archivo de ventas.")
        return
    
    lineas_actualizadas = []
    encontrado = False

    with open(ARCHIVO_VENTAS, "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(", ")
            if datos[0].lower() == nombre_buscar.lower():
                lineas_actualizadas.append(f"{nombre_buscar}, {nueva_cantidad}, {nuevo_precio}")
                encontrado = True
            else:
                lineas_actualizadas.append(linea)

    if encontrado:
        with open(ARCHIVO_VENTAS, "w") as archivo:
            archivo.writelines(lineas_actualizadas)
        print(f"Producto '{nombre_buscar}' actualizado con éxito.")
    else:
        print(f"No se encontro el producto '{nombre_buscar}'.")


def eliminar_producto(nombre_buscar: str):
    """
    Busca un producto por nombre y lo elimina reescribiendo el archivo sin él.
    """
    # TODO: Lee todo el archivo, filtra omitiendo el producto a eliminar 
    # y reescribe el archivo con el resto de elementos.

    if not os.path.exists(ARCHIVO_VENTAS):
        print("No existe el archivo de ventas.")
        return

    hoja_blanco=[]
    encontrado = False

    with open(ARCHIVO_VENTAS, "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(", ")
            if datos[0].lower() == nombre_buscar.lower():
                print(f"Linea encontrada {datos}")
                encontrado = True
            else:
                hoja_blanco.append(linea)

    if encontrado:
        with open(ARCHIVO_VENTAS, "w") as archivo:
            archivo.writelines(hoja_blanco)
            print(f"Se elimino correctamente '{nombre_buscar}'")
    else:
        print(f"No se encontro el producto '{nombre_buscar}'")


def calcular_ventas_totales():
    """
    Calcula el total general de ventas (Suma de cantidad * precio de cada producto) 
    y muestra el desglose individual por producto.
    """
    # TODO: Recorre las líneas, extrae cantidad y precio, calcula (cantidad * precio) 
    # e imprime el desglose por producto y el gran total general.
    pass


# --- Menú interactivo por consola ---
def menu_ventas():
    while True:
        print("\n--- MENÚ DE GESTIÓN DE VENTAS ---")
        print("1. Añadir producto")
        print("2. Consultar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Calcular total de ventas")
        print("6. Salir (Borra ventas.txt)")
        
        opcion = input("Selecciona una opción (1-6): ")

        if opcion == "1":
            # TODO: Pide datos por input y llama a guardar_producto()
            pass
        elif opcion == "2":
            consultar_productos()
        elif opcion == "3":
            # TODO: Pide datos por input y llama a actualizar_producto()
            pass
        elif opcion == "4":
            # TODO: Pide nombre del producto y llama a eliminar_producto()
            pass
        elif opcion == "5":
            calcular_ventas_totales()
        elif opcion == "6":
            # TODO: Elimina ventas.txt si existe y rompe el bucle con 'break'
            if os.path.exists(ARCHIVO_VENTAS):
                os.remove(ARCHIVO_VENTAS)
                print("Archivo de ventas eliminado correctamente.")
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Para ejecutar el menú interactivo, desmarcar la llamada:
# menu_ventas()