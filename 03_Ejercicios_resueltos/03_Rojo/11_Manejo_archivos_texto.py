# =============================================================================
# DIFICULTAD EXTRA: SISTEMA DE GESTIÓN DE VENTAS CON ARCHIVO .TXT
# =============================================================================

# --- 1. CONFIGURACIÓN E INICIALIZACIÓN ---
# - Definir el nombre del archivo del sistema de ventas (ejemplo: 'ventas.txt').
# - Asegurar la creación o existencia limpia del archivo al iniciar el programa.
import os

# --- 2. FUNCIONES AUXILIARES DE ARCHIVO ---
# - Función para leer todas las líneas del archivo y retornar los productos como lista estructurada.
# - Función para reescribir/actualizar todo el archivo a partir de la lista modificada.

# --- 3. FUNCIONES CRUD Y OPERACIONES DEL MENÚ ---
# - Función 'añadir_producto()':
#     - Solicitar nombre del producto, cantidad vendida y precio desde la terminal.
#     - Formatear como '[nombre], [cantidad], [precio]' y adjuntarlo al archivo en modo append ('a').

# - Función 'consultar_productos()':
#     - Leer el archivo completo e imprimir cada producto en un formato legible para el usuario.
#     - Manejar el caso donde el archivo esté vacío.

# - Función 'actualizar_producto()':
#     - Solicitar el nombre del producto a modificar.
#     - Buscar el producto en los registros, actualizar sus datos (cantidad/precio) y reescribir el archivo.

# - Función 'eliminar_producto()':
#     - Solicitar el nombre del producto a eliminar.
#     - Filtrar la lista excluyendo dicho producto y reescribir el archivo.

# - Función 'calcular_venta_total()':
#     - Recorrer cada registro del archivo, multiplicar (cantidad * precio) y acumular el total general.
#     - Imprimir la suma de todas las ventas registradas.

# - Función 'calcular_venta_por_producto()':
#     - Solicitar o listar el producto específico.
#     - Calcular y mostrar el subtotal generado únicamente por ese producto (cantidad * precio).

# --- 4. BUCLE PRINCIPAL Y MENÚ DE INTERACCIÓN POR TERMINAL ---
# - Implementar un bucle 'while True' para mantener activo el programa:
#     - Desplegar opciones: 1. Añadir, 2. Consultar, 3. Actualizar, 4. Eliminar, 5. Venta Total, 6. Venta por Producto, 7. Salir.
#     - Capturar la opción ingresada por el usuario.
#     - Invocar la función correspondiente según la opción seleccionada.
#     - Opción 7 (Salir):
#         - Eliminar el archivo de ventas usando 'os.remove()' si existe.
#         - Mostrar mensaje de despedida y romper el bucle ('break').
