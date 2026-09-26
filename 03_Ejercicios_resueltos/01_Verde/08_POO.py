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
    def push(self, elemento):
        print(f"Se agrego a la pila '{elemento}'")
        self.items.append(elemento)
    def pop(self):
        if self.items:
            ultimo_elemento = self.items.pop()
            print(f"Se elimino el elemento '{ultimo_elemento}'")
            return ultimo_elemento
        else:
            return None
    def contar (self) -> int:
        print(f"Cantidad de elementos actuales: {len(self.items)}")
        return len(self.items)
    def imprimir(self):
        print(f"Contenido actual de la pila: {self.items}")
        
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
    def enqueue(self, elemento):
        print(f"Se agrego a la cola '{elemento}'")
        self.items.append(elemento)
    def dequeue(self):
        if self.items:
            primer_elemento = self.items.popleft()
            print(f"Se elimino el primer elemento '{primer_elemento}'")
            return primer_elemento
        else:
            return None
    def contar(self) -> int:
        print(f"Cantidad de elementos actuales: {len(self.items)}")
        return len(self.items)
    def imprimir(self):
        print(f"Contenido actual de la cola: {list(self.items)}")

# --- PROCESO DE PRUEBA DE DIFICULTAD EXTRA ---
# 1. Instanciar un objeto de la clase 'Pila', realizar operaciones push, pop, contar e imprimir.
# 2. Instanciar un objeto de la clase 'Cola', realizar operaciones enqueue, dequeue, contar e imprimir.
print("\n--- EJEMPLO PILA ---")
pila_1 = Pila()
pila_1.push("Documento")
pila_1.push("Archivo")
pila_1.push("Excel")

pila_1.imprimir()

pila_1.pop()
pila_1.contar()
pila_1.imprimir()

print("\n--- EJEMPLO COLA ---")
cola_1 = Cola()
cola_1.enqueue("Documento")
cola_1.enqueue("Archivo")
cola_1.enqueue("Excel")

cola_1.imprimir()

cola_1.dequeue()
cola_1.contar()
cola_1.imprimir()