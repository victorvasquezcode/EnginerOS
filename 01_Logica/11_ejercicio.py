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