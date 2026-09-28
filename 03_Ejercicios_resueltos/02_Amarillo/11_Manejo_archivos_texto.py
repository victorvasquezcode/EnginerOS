# =============================================================================
# DIFICULTAD EXTRA: SISTEMA DE GESTIÓN DE VENTAS CON ARCHIVO .TXT
# =============================================================================

# --- 1. CONFIGURACIÓN E INICIALIZACIÓN ---
# - Definir el nombre del archivo del sistema de ventas (ejemplo: 'ventas.txt').
# - Asegurar la creación o existencia limpia del archivo al iniciar el programa.
import os
SISTEMAS_VENTAS = 'ventas.txt'
if not os.path.exists(SISTEMAS_VENTAS):
    with open(SISTEMAS_VENTAS, "w") as archivo:
        pass

# --- 2. FUNCIONES AUXILIARES DE ARCHIVO ---
# - Función para leer todas las líneas del archivo y retornar los productos como lista estructurada.
# - Función para reescribir/actualizar todo el archivo a partir de la lista modificada.
def lista_estructurada():
    try:
        productos = []
        with open(SISTEMAS_VENTAS, "r") as archivo:
            for linea in archivo:
                if not linea.strip(): continue

                linea_limpia = linea.strip().split(",")
                nombre = linea_limpia[0]

                try:
                    cantidad_str = int(linea_limpia[1])
                    precio_str = float(linea_limpia[2])
                except ValueError:
                    print(f"No tiene el formato correcto.")
                    continue

                productos.append([nombre, cantidad_str, precio_str])
        return productos
    
    except FileNotFoundError as e:
        print(f"No esta creado o se elimino el archivo {e}")
        return []

def actualizar_lista(productos):
    with open(SISTEMAS_VENTAS, "w") as archivo:
        for producto in productos:
            nombre = producto[0]
            cantidad = int(producto[1])
            precio = float(producto[2])
            archivo.write(f"{nombre},{cantidad},{precio:.2f}\n")

def validar(mensaje: str, tipo: callable):
    while True:
        try:
            valor = tipo(input(mensaje).strip())
            if valor <= 0: raise ValueError("No se puede ingresar 0 o numeros negativos")
        except ValueError as e:
            print(f"No tiene formato correcto {e}")
            continue
        else:
            return valor

# --- 3. FUNCIONES CRUD Y OPERACIONES DEL MENÚ ---
# - Función 'añadir_producto()':
#     - Solicitar nombre del producto, cantidad vendida y precio desde la terminal.
#     - Formatear como '[nombre], [cantidad], [precio]' y adjuntarlo al archivo en modo append ('a').
def añadir_producto():
    nombre = input("Ingrese el nombre del producto: ").strip().capitalize()
    cantidad_vendida = validar("Ingrese la cantidad: ", int)
    precio = validar("Ingrese el precio: ", float)
    with open (SISTEMAS_VENTAS, "a") as archivo:
        archivo.write(f"{nombre},{cantidad_vendida},{precio:.2f}\n")

# - Función 'consultar_productos()':
#     - Leer el archivo completo e imprimir cada producto en un formato legible para el usuario.
#     - Manejar el caso donde el archivo esté vacío.
def consultar_productos():
    productos = lista_estructurada()
    if productos:
        for producto in productos:
            nombre = producto[0]
            cantidad = producto[1]
            precio = producto[2]
            print("-" * 30)
            print(f"Nombre del producto: {nombre}\nCantidad del producto: {cantidad}\nPrecio del producto: {precio}")
    else:
        print("No hay productos registrados en el sistema")

# - Función 'actualizar_producto()':
#     - Solicitar el nombre del producto a modificar.
#     - Buscar el producto en los registros, actualizar sus datos (cantidad/precio) y reescribir el archivo.
def actualizar_producto():
    producto_modificar = input("Ingrese el nombre del producto a modificar: ").strip().capitalize()
    productos = lista_estructurada()
    valor_encontrado = False

    for producto in productos:
        if producto[0] == producto_modificar:
            cantidad_vendida = validar("Ingrese la cantidad: ", int)
            precio = validar("Ingrese el precio: ",float)
            producto[1] = cantidad_vendida
            producto[2] = precio
            valor_encontrado = True
            break

    if valor_encontrado:
        actualizar_lista(productos)
        print("¡Producto actualizado con exito!")
    else:
        print(f"No se encontro '{producto_modificar}' en los productos registrados")
        
# - Función 'eliminar_producto()':
#     - Solicitar el nombre del producto a eliminar.
#     - Filtrar la lista excluyendo dicho producto y reescribir el archivo.
def eliminar_producto():
    producto_eliminar = input("Ingrese el nombre del producto a eliminar: ").strip().capitalize()
    productos = lista_estructurada()

    producto_filtrado = [producto for producto in productos if producto[0] != producto_eliminar]

    if len(producto_filtrado) != len(productos):
        actualizar_lista(producto_filtrado)
        print("¡Producto eliminado con exito!")
    else:
        print(f"No se encontro '{producto_eliminar}' en los productos registrados")

# - Función 'calcular_venta_total()':
#     - Recorrer cada registro del archivo, multiplicar (cantidad * precio) y acumular el total general.
#     - Imprimir la suma de todas las ventas registradas.
def calcular_venta_total():
    productos = lista_estructurada()
    total_general = 0
    for producto in productos:
        cantidad = producto[1]
        precio = producto[2]
        total = cantidad * precio
        total_general += total
    print(f"Suma de todas las ventas registradas: {total_general:.2f}")

# - Función 'calcular_venta_por_producto()':
#     - Solicitar o listar el producto específico.
#     - Calcular y mostrar el subtotal generado únicamente por ese producto (cantidad * precio).
def calcular_venta_por_producto():
    producto_especifico = input("Ingrese el nombre de producto para calcular sus ventas: ").strip().capitalize()
    productos = lista_estructurada()
    encontrado = False
    for producto in productos:
        if producto[0] == producto_especifico:
            cantidad = producto[1]
            precio = producto[2]
            total = cantidad * precio
            print(f"Subtotal generado solamento con el '{producto_especifico}': {total:.2f}")
            encontrado = True
            break
    if not encontrado:
        print(f"Producto '{producto_especifico}' no encontrado")

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
        print("--- MENU PRINCIPAL ---")
        print("1. Añadir producto")
        print("2. Consultar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Venta Total de productos")
        print("6. Venta por producto")
        print("7. Salir")
        opcion = input("Ingrese una opcion valida (1-7): ").strip()
        match opcion:
            case "1":
                añadir_producto()
            case "2":
                consultar_productos()
            case "3":
                actualizar_producto()
            case "4":
                eliminar_producto()
            case "5":
                calcular_venta_total()
            case "6":
                calcular_venta_por_producto()
            case "7":
                if os.path.exists(SISTEMAS_VENTAS):
                    os.remove(SISTEMAS_VENTAS)
                print("¡Hasta luego!")
                break
            case _:
                print("Ingrese opcion valida")
