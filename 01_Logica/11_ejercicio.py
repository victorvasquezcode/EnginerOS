# =============================================================================
# PARTE 1: MANEJO BÁSICO DE ARCHIVOS DE TEXTO (.txt)
# =============================================================================
# El manejo de archivos en Python permite crear, leer, modificar y eliminar
# datos persistentes en el disco utilizando el gestor de contexto 'with open()'.
# Para operaciones del sistema de archivos (como eliminar), se utiliza el módulo 'os'.

# 1. Definición de variables base:
# - Definir el nombre del archivo (ejemplo: 'github_username.txt').
# - Definir variables para nombre, edad y lenguaje de programación favorito.
import os

NOMBRE_ARCHIVO = 'github_username.txt'
nombre = "Victor Javier Vasquez Trauco"
edad = 26
lenguaje_programacion = "Python"

# 2. Creación y Escritura del archivo ('w'):
# - Abrir el archivo en modo escritura ('w') usando 'with open(nombre_archivo, "w") as archivo:'.
# - Escribir las líneas correspondientes (Nombre, Edad, Lenguaje) agregando saltos de línea ('\n').
with open(NOMBRE_ARCHIVO, "w") as archivo:
    archivo.writelines([
        f"{nombre}\n",
        f"{edad}\n",
        f"{lenguaje_programacion}\n"
    ])

# 3. Lectura e Impresión del contenido ('r'):
# - Abrir el archivo en modo lectura ('r') usando 'with open(nombre_archivo, "r") as archivo:'.
# - Leer el contenido completo (usando .read() o recorriendo línea por línea) e imprimirlo en consola.
with open(NOMBRE_ARCHIVO, "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# 4. Eliminación del archivo:
# - Importar la librería 'os'.
# - Comprobar si el archivo existe con 'os.path.exists(nombre_archivo)'.
# - Eliminar el archivo con 'os.remove(nombre_archivo)' para limpiar el entorno.
if os.path.exists(NOMBRE_ARCHIVO):
    os.remove(NOMBRE_ARCHIVO)
    print(f"Archivo Eliminado correctamente {NOMBRE_ARCHIVO}")


# =============================================================================
# DIFICULTAD EXTRA: SISTEMA DE GESTIÓN DE VENTAS CON ARCHIVO .TXT
# =============================================================================

# --- 1. CONFIGURACIÓN E INICIALIZACIÓN ---
# - Definir el nombre del archivo del sistema de ventas (ejemplo: 'ventas.txt').
# - Asegurar la creación o existencia limpia del archivo al iniciar el programa.
import os
ARCHIVO_SISTEMA = 'ventas.txt'

if not os.path.exists(ARCHIVO_SISTEMA):
    with open(ARCHIVO_SISTEMA, "w") as archivo:
        pass

# --- 2. FUNCIONES AUXILIARES DE ARCHIVO ---
# - Función para leer todas las líneas del archivo y retornar los productos como lista estructurada.
# - Función para reescribir/actualizar todo el archivo a partir de la lista modificada.
def cargar_productos() -> list:
    productos = []

    if not os.path.exists(ARCHIVO_SISTEMA):
        return productos

    with open(ARCHIVO_SISTEMA, "r") as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            if linea_limpia:
                nombre, cantidad, precio = linea_limpia.split(",")
                productos.append([
                    nombre.strip(),
                    int(cantidad.strip()),
                    float(precio.strip())
                ])

    return productos

def guardar_todos_los_productos(productos: list) -> None:
    with open(ARCHIVO_SISTEMA, "w") as archivo:
        for prod in productos:
            nombre, cantidad, precio = prod
            archivo.write(f"{nombre}, {cantidad} , {precio}\n")

# --- 3. FUNCIONES CRUD Y OPERACIONES DEL MENÚ ---
# - Función 'añadir_producto()':
#     - Solicitar nombre del producto, cantidad vendida y precio desde la terminal.
#     - Formatear como '[nombre], [cantidad], [precio]' y adjuntarlo al archivo en modo append ('a').
def añadir_producto():
    nombre = input("Nombre del producto: ").strip()

    try:
        cantidad = int(input("Cantidad vendida: "))
        precio = float(input("Precio del producto: "))
    except ValueError:
        print("Error: Cantidad debe ser entero y Precio un numero decimal.")
        return
    
    with open(ARCHIVO_SISTEMA, "a") as archivo:
        archivo.write(f"{nombre}, {cantidad}, {precio}\n")

    print(f"Producto '{nombre}' añadido correctamente")

# - Función 'consultar_productos()':
#     - Leer el archivo completo e imprimir cada producto en un formato legible para el usuario.
#     - Manejar el caso donde el archivo esté vacío.
def consultar_producto():
    if not os.path.exists(ARCHIVO_SISTEMA):
        print(f"⚠️ El registro de ventas no existe aún.")
        return
    
    productos = cargar_productos()

    if not productos:
        print("ℹ️ El archivo de ventas está vacío.")
        return
    
    print("\n--- LISTA DE PRODUCTOS REGISTRADOS ---")
    for producto in productos:
        nombre , cantidad, precio = producto
        subtotal = cantidad * precio
        print(f"• Producto: {nombre:<15} | Cantidad: {cantidad:<5} | Precio: ${precio:<7.2f} | Subtotal: ${subtotal:.2f}")
    print("-" * 50)

# - Función 'actualizar_producto()':
#     - Solicitar el nombre del producto a modificar.
#     - Buscar el producto en los registros, actualizar sus datos (cantidad/precio) y reescribir el archivo.
def actualizar_producto():
    producto_modificar = input("Nombre del producto para actualizar: ").strip()

    productos = cargar_productos()

    if not productos:
        print("El archivo de ventas esta vacio.")
        return
    
    encontrado = False

    for i, producto in enumerate(productos):
        nombre, cantidad_actual, precio_actual = producto

        if nombre.lower() == producto_modificar.lower():
            encontrado = True
            print(f"Producto encontrado: {nombre} (Cantidad actual: {cantidad_actual}, Precio actual: ${precio_actual})")

            try:
                nueva_cantidad = int(input("Cantidad vendida: "))
                nuevo_precio = float(input("Precio del producto: "))
            except ValueError:
                print("Error: Cantidad debe ser entero y Precio un numero decimal.")
                return

            productos[i] = [nombre,nueva_cantidad,nuevo_precio]
            guardar_todos_los_productos(productos)
            print(f"Producto {nombre} actualizado correctamente")
            break

    if not encontrado:
        print(f"No se encontro el producto '{producto_modificar}'")

# - Función 'eliminar_producto()':
#     - Solicitar el nombre del producto a eliminar.
#     - Filtrar la lista excluyendo dicho producto y reescribir el archivo.
def eliminar_producto():
    producto_eliminar = input("Nombre del producto para eliminar: ").strip()

    productos = cargar_productos()

    if not productos:
        print("El archivo de ventas esta vacio.")
        return
    productos_filtrados = [p for p in productos if p[0].lower() != producto_eliminar.lower()]

    if len(productos_filtrados) < len(productos):
        guardar_todos_los_productos(productos_filtrados)
        print(f"Producto '{producto_eliminar}' eliminado correctamente")
    else:
        print(f"No se encontro el producto '{producto_eliminar}'")

# - Función 'calcular_venta_total()':
#     - Recorrer cada registro del archivo, multiplicar (cantidad * precio) y acumular el total general.
#     - Imprimir la suma de todas las ventas registradas.
def calcular_ventas_total():
    productos = cargar_productos()

    if not productos:
        print("El archivo de ventas esta vacio.")
        return
    
    total_general = 0

    for producto in productos:
        nombre, cantidad_actual, precio_actual = producto
        venta_total = cantidad_actual * precio_actual
        total_general += venta_total

    print(f"💰 La suma de todas las ventas registradas es: ${total_general:.2f}")

# - Función 'calcular_venta_por_producto()':
#     - Solicitar o listar el producto específico.
#     - Calcular y mostrar el subtotal generado únicamente por ese producto (cantidad * precio).
def calcular_venta_por_producto():
    producto_calcular_venta = input("De que producto deseas calcular su venta: ")

    productos = cargar_productos()

    if not productos:
        print("El archivo de ventas esta vacio")
        return

    encontrado = False

    for producto in productos:
        nombre, cantidad_actual, precio_actual = producto
        if nombre.lower() == producto_calcular_venta.lower():
            encontrado = True
            venta_total_producto = cantidad_actual * precio_actual
            print(f"EL total de venta del producto es: ${venta_total_producto:.2f}")
            break

    if not encontrado:
        print(f"No se encontro el producto '{producto_calcular_venta}'")

# --- 4. BUCLE PRINCIPAL Y MENÚ DE INTERACCIÓN POR TERMINAL ---
# - Implementar un bucle 'while True' para mantener activo el programa:
#     - Desplegar opciones: 1. Añadir, 2. Consultar, 3. Actualizar, 4. Eliminar, 5. Venta Total, 6. Venta por Producto, 7. Salir.
#     - Capturar la opción ingresada por el usuario.
#     - Invocar la función correspondiente según la opción seleccionada.
#     - Opción 7 (Salir):
#         - Eliminar el archivo de ventas usando 'os.remove()' si existe.
#         - Mostrar mensaje de despedida y romper el bucle ('break').
def menu_principal():
    while True:
        print("\n--- MENU DE INTERACCION ---")
        print("1. Añadir")
        print("2. Consultar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Venta Total")
        print("6. Venta por producto")
        print("7. Salir")

        opcion = input("Ingrese la opcion: ").strip()
        match opcion:
            case "1":
                añadir_producto()
            case "2":
                consultar_producto()
            case "3":
                actualizar_producto()
            case "4":
                eliminar_producto()
            case "5":
                calcular_ventas_total()
            case "6":
                calcular_venta_por_producto()
            case "7":
                if os.path.exists(ARCHIVO_SISTEMA):
                    os.remove(ARCHIVO_SISTEMA)
                    print(f"Archivo Eliminado correctamente {ARCHIVO_SISTEMA}")
                print("¡Hasta luego!")
                break
            case _:
                print("No se coloco una opcion valida")

if __name__ == "__main__":
    menu_principal()