# =============================================================================
# DIFICULTAD EXTRA: SISTEMA DE GESTIÓN DE VENTAS CON ARCHIVO .TXT
# =============================================================================

# --- 1. CONFIGURACIÓN E INICIALIZACIÓN ---
# - Definir el nombre del archivo del sistema de ventas (ejemplo: 'ventas.txt').
# - Asegurar la creación o existencia limpia del archivo al iniciar el programa.
import os
SISTEMA_VENTAS = 'ventas.txt'

if not os.path.exists(SISTEMA_VENTAS):
    with open (SISTEMA_VENTAS, "w") as archivo:
        pass

# --- 2. FUNCIONES AUXILIARES DE ARCHIVO ---
# - Función para leer todas las líneas del archivo y retornar los productos como lista estructurada.
# - Función para reescribir/actualizar todo el archivo a partir de la lista modificada.
def lista_estructurada():
    producto = []
    with open(SISTEMA_VENTAS, "r") as archivo:
        for lista in archivo:
            if not lista.strip(): continue
            lista_limpia = lista.strip().split(",")
            if len(lista_limpia) != 3: continue
            nombre = lista_limpia[0]
            cantidad = lista_limpia[1]
            precio = lista_limpia[2]

            try:
                producto.append((nombre,int(cantidad),float(precio)))
            except ValueError as e:
                print(f"Error en formato {e}")

        return producto

def actualizar(producto):
    with open (SISTEMA_VENTAS, "w") as archivo:
        for lista in producto:
            nombre = lista[0]
            cantidad = lista[1]
            precio = lista[2]
            archivo.write(f"{nombre},{cantidad},{precio:.2f}\n")

def validar(mensaje,tipo):
    try:
        valor = tipo(input(mensaje).strip())
    except ValueError as e:
        print(f"Error en formato {e}")
        return None
    else:
        if valor <= 0:
            print(f"No puede ser menor a 0")
            return None
        else:
            return valor
        
# --- 3. FUNCIONES CRUD Y OPERACIONES DEL MENÚ ---
# - Función 'añadir_producto()':
#     - Solicitar nombre del producto, cantidad vendida y precio desde la terminal.
#     - Formatear como '[nombre], [cantidad], [precio]' y adjuntarlo al archivo en modo append ('a').
def añadir_producto():
    nombre_producto = input("Ingresar el nombre del producto: ").strip().capitalize()
    cantidad = validar("Ingresa la cantidad del producto", int)
    precio = validar("Ingrese el precio del producto", float)
    if cantidad is None or precio is None: return
    with open(SISTEMA_VENTAS, "a") as archivo:
        archivo.write(f"{nombre_producto},{cantidad},{precio:.2f}\n")

# - Función 'consultar_productos()':
#     - Leer el archivo completo e imprimir cada producto en un formato legible para el usuario.
#     - Manejar el caso donde el archivo esté vacío.
def consultar_producto():
    producto = lista_estructurada()
    if not producto:
        print("No existen productos")
        return
    for lista in producto:
        print("-" * 60)
        print(f"Nombre del producto: {lista[0]}\nCantidad de producto: {lista[1]}\nPrecio del producto: {lista[2]}")


# - Función 'actualizar_producto()':
#     - Solicitar el nombre del producto a modificar.
#     - Buscar el producto en los registros, actualizar sus datos (cantidad/precio) y reescribir el archivo.
def actualizar_producto():
    nombre_producto_modificar = input("Ingrese el nombre del producto para modificar: ").strip().capitalize()
    producto = lista_estructurada()
    if not producto:
        print("No existen productos")
        return
    encontrado = False
    for i,lista in enumerate(producto):
        if nombre_producto_modificar == lista[0]:
            cantidad = validar("Ingresa la cantidad del producto", int)
            precio = validar("Ingrese el precio del producto", float)
            if cantidad is None or precio is None: return
            producto[i] = (nombre_producto_modificar,cantidad,precio)
            actualizar(producto)
            encontrado = True
            return
    if not encontrado:
        print(f"No se encontro el producto '{nombre_producto_modificar}'")
        
# - Función 'eliminar_producto()':
#     - Solicitar el nombre del producto a eliminar.
#     - Filtrar la lista excluyendo dicho producto y reescribir el archivo.
def eliminar_producto():
    nombre_eliminar = input("Ingrese el nombre a eliminar: ").strip().capitalize()
    producto = lista_estructurada()
    if not producto:
        print("No existen productos")
        return
    encontrado = False
    for i,lista in enumerate(producto):
        if nombre_eliminar == lista[0]:
            producto.pop(i)
            actualizar(producto)
            encontrado = True
    if not encontrado:
        print(f"No se encontro el nombre '{nombre_eliminar}' para eliminar")

# - Función 'calcular_venta_total()':
#     - Recorrer cada registro del archivo, multiplicar (cantidad * precio) y acumular el total general.
#     - Imprimir la suma de todas las ventas registradas.
def calcular_venta_total():
    productos = lista_estructurada()
    if not productos:
        print("No existen productos")
        return
    total_ventas = 0
    for lista in productos:
        cantidad = lista[1]
        precio = lista[2]
        total_general = cantidad * precio
        total_ventas += total_general
    print(f"La suma de todas las ventas registradas es: S/.{total_ventas:.2f}")

# - Función 'calcular_venta_por_producto()':
#     - Solicitar o listar el producto específico.
#     - Calcular y mostrar el subtotal generado únicamente por ese producto (cantidad * precio).
def calcular_venta_por_producto():
    producto_especifico = input("Ingrese el producto para calcular sus ventas: ").strip().capitalize()
    productos = lista_estructurada()
    encontrado = False
    if not productos:
        print("No existen productos")
        return
    for lista in productos:
        if producto_especifico == lista[0]:
            cantidad = lista[1]
            precio = lista[2]
            subtotal = cantidad * precio
            print(f"Las ventas del producto '{producto_especifico}' es S/.{subtotal:.2f}")
            encontrado = True
            return
    if not encontrado:
        print(f"No se encontro el producto '{producto_especifico}'")

# --- 4. BUCLE PRINCIPAL Y MENÚ DE INTERACCIÓN POR TERMINAL ---
# - Implementar un bucle 'while True' para mantener activo el programa:
#     - Desplegar opciones: 1. Añadir, 2. Consultar, 3. Actualizar, 4. Eliminar, 5. Venta Total, 6. Venta por Producto, 7. Salir.
#     - Capturar la opción ingresada por el usuario.
#     - Invocar la función correspondiente según la opción seleccionada.
#     - Opción 7 (Salir):
#         - Eliminar el archivo de ventas usando 'os.remove()' si existe.
#         - Mostrar mensaje de despedida y romper el bucle ('break').
if __name__ == "__main__":
    while True:
        print("\n--- MENU INTERACCION ---")
        print("1. Añadir producto")
        print("2. Consultar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Venta Total producto")
        print("6. Venta por producto")
        print("7. Salir del menu")
        opcion = input("Ingrese una opcion valida: ").strip()
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
                calcular_venta_total()
            case "6":
                calcular_venta_por_producto()
            case "7":
                if os.path.exists(SISTEMA_VENTAS):
                    os.remove(SISTEMA_VENTAS)

                print("¡Hasta Luego!")
                break
            case _:
                print("Seleccione una opcion valida (1-7)")