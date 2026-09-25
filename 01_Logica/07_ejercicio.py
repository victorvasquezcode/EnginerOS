# =============================================================================
# PARTE 1: ESTRUCTURAS DE DATOS - PILAS (STACK - LIFO) Y COLAS (QUEUE - FIFO)
# =============================================================================
# LIFO (Last In, First Out): El último elemento en entrar es el primero en salir.
# FIFO (First In, First Out): El primer elemento en entrar es el primero en salir.


# --- 1. IMPLEMENTACIÓN DE PILA (STACK) ---
# - Crear una lista vacía para representar la pila.
# - PUSH (Introducir): Usar el método .append() para agregar elementos al final.
# - POP (Recuperar/Eliminar): Usar el método .pop() sin argumentos para extraer el último elemento agregado.
# - PEEK (Inspeccionar): Consultar el último elemento usando indexación negativa [-1] sin eliminarlo.
# - Comprobar comportamiento vaciando la pila y verificando el orden LIFO.
pila =[]

pila.append("Pagina 1")
pila.append("Pagina 2")
pila.append("Pagina 3")
print(f"Pila tras PUSH: {pila}")

cima = pila[-1]
print(f"Elemento en la cima (PEEK): {cima}")

elemento_extraido = pila.pop()
print(f"Elemento extraido (POP): {elemento_extraido}")
print(f"Pila resultante: {pila}")

# --- 2. IMPLEMENTACIÓN DE COLA (QUEUE) ---
# - Opción A (Lista tradicional): Usar .append() para agregar y .pop(0) para extraer el primer elemento (Nota: pop(0) tiene costo O(n)).
# - Opción B (Recomendada en Python): Importar 'collections.deque' (Double Ended Queue) para operaciones O(1).
# - ENQUEUE (Introducir): Usar .append() para agregar elementos al final.
# - DEQUEUE (Recuperar/Eliminar): Usar .popleft() para extraer el primer elemento ingresado.
# - Comprobar comportamiento vaciando la cola y verificando el orden FIFO.
from collections import deque

cola = deque()

cola.append("A")
cola.append("B")
cola.append("C")
cola.append("D")
print(f"Cola inicial: {cola}")

elemento_extraido = cola.popleft()

print(f"Elemento extraido (FIFO): {elemento_extraido}")
print(f"Cola resultante: {cola}")