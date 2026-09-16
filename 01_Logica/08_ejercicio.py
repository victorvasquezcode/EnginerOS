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

# =============================================================================
# DIFICULTAD EXTRA: IMPLEMENTACIÓN DE PILA Y COLA MEDIANTE CLASES
# =============================================================================

# --- PROGRAMA 1: CLASE PILA (STACK - LIFO) ---
# - Definir la clase 'Pila':
#     - Método __init__(self):
#         - Inicializar un atributo privado o de instancia como lista vacía (self.items = []).
#     - Método push(self, elemento):
#         - Agregar un nuevo elemento al final de 'self.items' (.append()).
#     - Método pop(self):
#         - Verificar si la pila no está vacía.
#         - Extraer y retornar el último elemento (.pop()). Si está vacía, manejar el caso o retornar None.
#     - Método contar(self) -> int:
#         - Retornar la cantidad de elementos actuales (len(self.items)).
#     - Método imprimir(self):
#         - Mostrar en consola el contenido actual de la pila.
class Pila:
    def __init__(self):
        self.items = []

    def push(self, elemento: str):
        self.items.append(elemento)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            print("La pila esta vacia.")
            return None
        
    def contar(self) -> int:
        return len(self.items)
    
    def imprimir(self):
        print(f"Pila actual: {self.items}")


# --- PROGRAMA 2: CLASE COLA (QUEUE - FIFO) ---
# - Importar 'deque' desde 'collections'.
# - Definir la clase 'Cola':
#     - Método __init__(self):
#         - Inicializar un atributo de instancia como un deque vacío (self.items = deque()).
#     - Método enqueue(self, elemento):
#         - Agregar un nuevo elemento al final del deque (.append()).
#     - Método dequeue(self):
#         - Verificar si la cola no está vacía.
#         - Extraer y retornar el primer elemento ingresado (.popleft()). Si está vacía, retornar None.
#     - Método contar(self) -> int:
#         - Retornar la cantidad de elementos actuales (len(self.items)).
#     - Método imprimir(self):
#         - Mostrar en consola el contenido actual de la cola.
from collections import deque

class Cola:
    def __init__(self):
        self.items = deque()

    def enqueue(self, elemento: str):
        self.items.append(elemento)

    def dequeue(self):
        if self.items:
            return self.items.popleft()
        else:
            print("La Cola esta vacia")
            return None

    def contar(self) -> int:
        return len(self.items)

    def imprimir(self):
        print(f"Cola actual: {self.items}")


# --- PROCESO DE PRUEBA DE DIFICULTAD EXTRA ---
# 1. Instanciar un objeto de la clase 'Pila', realizar operaciones push, pop, contar e imprimir.
# 2. Instanciar un objeto de la clase 'Cola', realizar operaciones enqueue, dequeue, contar e imprimir.
print("\n--- DEMOSTRACION CLASE PILA (LIFO) ---")
pila1 = Pila()
pila1.push("Kiwi")
pila1.push("Manzana")
pila1.imprimir()
print(f"Cantidad de elementos: {pila1.contar()}")
print(f"Elemento Extraido: {pila1.pop()}")
pila1.imprimir()

print("\n--- DEMOSTRACION CLASE COLA (FIFO) ---")
cola1 = Cola()
cola1.enqueue("Turno 1")
cola1.enqueue("Turno 2")
cola1.enqueue("Turno 3")
cola1.imprimir()
print(f"Cantidad de elementos: {cola1.contar()}")
print(f"Atendido a: {cola1.dequeue()}")
cola1.imprimir()