# =============================================================================
# PARTE 1: CONCEPTO DE CLASE Y POO (PROGRAMACIÓN ORIENTADA A OBJETOS)
# =============================================================================
# Una clase es una plantilla o molde para crear objetos. Agrupa datos (atributos)
# y comportamientos (métodos).


# 1. Definición de la Clase Básica:
# - Definir la clase con la sintaxis 'class NombreClase:' (usando PascalCase por convención).
# - Método Constructor (__init__):
#     - Recibir el parámetro obligatorio 'self' (referencia a la instancia actual).
#     - Recibir los parámetros iniciales (ej. nombre: str, edad: int).
#     - Asignar los valores a atributos de instancia (ej. self.nombre = nombre).
class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

# - Método de Impresión/Mostrado:
#     - Definir una función dentro de la clase (ej. 'mostrar_datos(self)').
#     - Imprimir el estado actual de todos los atributos de la instancia.
    def mostrar_datos(self):
        print(f"Mi nombre es {self.nombre} y mi edad es {self.edad}")


# 2. Proceso de Prueba (Instanciación y Mutación):
# - Crear/Instanciar un objeto de la clase pasando los argumentos iniciales.
# - Llamar al método de impresión para verificar el estado inicial.
# - Modificar directamente un atributo de la instancia (ej. objeto.atributo = nuevo_valor).
# - Volver a llamar al método de impresión para comprobar la actualización del estado.
persona1 = Persona("Víctor", 25)
persona1.mostrar_datos()
persona1.nombre = "Javier"
persona1.mostrar_datos()