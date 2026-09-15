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


# =============================================================================
# DIFICULTAD EXTRA: SIMULACIONES CON PILAS Y COLAS
# =============================================================================

# --- PROGRAMA 1: NAVEGADOR WEB (SISTEMA ADELANTE / ATRÁS CON PILAS) ---
# Se requieren dos pilas:
# - 'pila_atras': Almacena el historial de páginas visitadas previamente.
# - 'pila_adelante': Almacena las páginas a las que se puede avanzar tras usar "atrás".
# - 'pagina_actual': Variable string para controlar la página donde está posicionado el usuario.
pila_atras = []
pila_adelante = []
pagina_actual = "home.com"
# Lógica del bucle interactivo:
# 1. Leer entrada del usuario.
# 2. Comando "atras":
#    - Si 'pila_atras' NO está vacía:
#      a. Mover 'pagina_actual' a 'pila_adelante' (.append()).
#      b. Extraer la nueva 'pagina_actual' de 'pila_atras' (.pop()).
#    - Si está vacía, mostrar mensaje de alerta (no hay páginas atrás).
# 3. Comando "adelante":
#    - Si 'pila_adelante' NO está vacía:
#      a. Mover 'pagina_actual' a 'pila_atras' (.append()).
#      b. Extraer la nueva 'pagina_actual' de 'pila_adelante' (.pop()).
#    - Si está vacía, mostrar mensaje de alerta (no hay páginas adelante).
# 4. Comando de salida ("salir"):
#    - Terminar la ejecución del bucle.
# 5. Cualquier otra palabra (Nueva página web):
#    - Si ya existe una 'pagina_actual', guardarla en 'pila_atras'.
#    - Actualizar 'pagina_actual' con la nueva web ingresada.
#    - Limpiar por completo 'pila_adelante' (.clear()), ya que una nueva navegación invalida el historial "adelante".
# 6. Imprimir en todo momento la 'pagina_actual'.
def atras():
    global pagina_actual
    if pila_atras:
        pila_adelante.append(pagina_actual)
        pagina_actual = pila_atras.pop()
    else:
        print("No hay pagina atras")

def adelante():
    global pagina_actual
    if pila_adelante:
        pila_atras.append(pagina_actual)
        pagina_actual = pila_adelante.pop()
    else:
        print("No hay pagina adelante")

def navegar(nueva_pagina: str):
    global pagina_actual
    if pagina_actual:
        pila_atras.append(pagina_actual)
    pagina_actual = nueva_pagina
    pila_adelante.clear()

def ejecutar_navegador():
    print("\n--- INICIANDO SIMULADOR DE NAVEGADOR WEB ---")
    while True:
        print(f"\nPagina Actual: {pagina_actual}")
        entrada_usuario=input("Ingrese nueva pagina web o comandos (atras/adelante/salir): ").strip().lower()

        if entrada_usuario == "salir":
            print("Cerrando navegador...")
            break
        elif entrada_usuario == "atras":
            atras()
        elif entrada_usuario == "adelante":
            adelante()
        elif entrada_usuario:
            navegar(entrada_usuario)        


# --- PROGRAMA 2: IMPRESORA COMPARTIDA (SISTEMA DE COLA FIFO) ---
# Usar 'deque' para la cola de impresión ('cola_impresion').
cola_impresion = deque()
# Lógica del bucle interactivo:
# 1. Leer entrada del usuario.
# 2. Comando "imprimir":
#    - Si 'cola_impresion' NO está vacía:
#      a. Extraer el primer documento con .popleft().
#      b. Imprimir mensaje confirmando la impresión del documento.
#    - Si está vacía, informar que no hay documentos pendientes.
# 3. Comando de salida ("salir"):
#    - Terminar la ejecución del bucle.
# 4. Cualquier otra palabra (Nombre de un documento):
#    - Añadir el documento a la cola con .append().
#    - Confirmar que el documento se agregó correctamente a la lista de espera.
# 5. Mostrar el estado actual de la cola tras cada acción.
def imprimir():
    if cola_impresion:
        documento = cola_impresion.popleft()
        print(f"Imprimiendo: {documento}")
    else:
        print("No hay documentos pendientes")

def agregar_documento(documento: str):
    cola_impresion.append(documento)
    print(f"Documento '{documento}' añadido a la cola")

def ejecutar_impresora():
    print("\n--- INICIANDO SIMULADOR DE IMPRESORA ---")
    while True:
        print(f"\nCola Impresion: {list(cola_impresion)}")
        entrada_usuario = input("Ingrese documento para imprimir o comandos (Imprimir|salir): ").strip().lower()

        if entrada_usuario == "salir":
            print("Cerrando programa de impresion")
            break
        elif entrada_usuario == "imprimir":
            imprimir()
        elif entrada_usuario:
            agregar_documento(entrada_usuario)

def menu_principal():
    while True:
        print("\n" + "=" * 33)
        print("    SELECCIONE UNA SIMULACION    ")
        print("=" * 33)
        print("1. Navegador Web (Pilas - LIFO)")
        print("2. Impresora Compartida (Colas- FIFO)")
        print("3. Salir del programa")

        opcion = input("\nElija una opcion (1, 2 o 3): ").strip()

        if opcion == "1":
            ejecutar_navegador()
        elif opcion == "2":
            ejecutar_impresora()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()