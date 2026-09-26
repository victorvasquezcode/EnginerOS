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
pagina_actual = "google.com"

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
        print("No hay paginas atras")

def adelante():
    global pagina_actual
    if pila_adelante:
        pila_atras.append(pagina_actual)
        pagina_actual = pila_adelante.pop()
    else:
        print("No hay paginas adelante")

def nueva_pagina_web(pagina: str):
    global pagina_actual
    pila_atras.append(pagina_actual)
    pagina_actual = pagina
    pila_adelante.clear()

def pagina_web():
    while True:
        print(f"La pagina actual es {pagina_actual}")
        opcion = input("Seleccione la opcion (atras/adelante/salir) o coloque una nueva pagina web: ").strip().lower()

        if not opcion:
            print("No puede estar vacia la opcion")
            continue

        match opcion:
            case "atras":
                atras()
            case "adelante":
                adelante()
            case "salir":
                print("¡Hasta luego!")
                break
            case _:
                nueva_pagina_web(opcion)

# --- PROGRAMA 2: IMPRESORA COMPARTIDA (SISTEMA DE COLA FIFO) ---
# Usar 'deque' para la cola de impresión ('cola_impresion').
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
from collections import deque
cola_impresion = deque()

def imprimir():
    if cola_impresion:
        documento = cola_impresion.popleft()
        print(f"Imprimiendo documento '{documento}'")
    else:
        print("No hay documentos pendientes")

def agregar_documento(documento: str):
    cola_impresion.append(documento)
    print(f"El documento '{documento}' se agrego correctamente a la lista de espera")

def impresion():
    while True:
        print(f"Estado actual de la cola: {list(cola_impresion)}")
        opcion = input("Ingrese opcion (imprimir/salir) o agregar nuevo documento a la cola: ").strip().lower()
        
        if not opcion:
            print("No puede estar vacia la opcion")
            continue

        match opcion:
            case "imprimir":
                imprimir()
            case "salir":
                print("¡Hasta luego!")
                break
            case _:
                agregar_documento(opcion)

if __name__ == "__main__":
    impresion()
