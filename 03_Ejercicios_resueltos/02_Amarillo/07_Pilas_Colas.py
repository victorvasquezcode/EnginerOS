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
    if pila_atras:
        global pagina_actual
        pila_adelante.append(pagina_actual)
        pagina_actual = pila_atras.pop()
        print(f"la pagina actual es {pagina_actual}")
    else:
        print("No hay paginas atras.")

def adelante():
    if pila_adelante:
        global pagina_actual
        pila_atras.append(pagina_actual)
        pagina_actual = pila_adelante.pop()
    else:
        print("No hay paginas adelante.")

def nueva_pagina_web(palabra: str):
    global pagina_actual
    if pagina_actual:
        pila_atras.append(pagina_actual)
        pagina_actual = palabra
        pila_adelante.clear()

def ejemplo_pilas():
    while True:
        print("\n--- MENU DE NAVEGACION DE PAGINAS WEB ---")
        print(f"La pagina actual es {pagina_actual}")
        opcion = input("Ingresa el comando (atras/adelante/salir) o una pagina web: ").lower().strip()
        match opcion:
            case "atras":
                atras()
            case "adelante":
                adelante()
            case "salir":
                print("¡Hasta Luego!")
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
        print(f"Impresion de documento '{documento}'")
    else:
        print("No hay documentos pendientes.")

def nuevo_documento(documento: str):
    cola_impresion.append(documento)
    print(f"Se agrego correctamente el documento '{documento}' a la lista de espera")

def ejemplo_colas():
    while True:
        print(f"La cola de la impresion: {list(cola_impresion)}")
        opcion = input("Ingresa opcion (imprimir/salir) o un documento nuevo para imprimir: ").strip()

        if not opcion:
            print("No se puede agregar un valor vacio")
            continue
        comando = opcion.lower()

        match comando:
            case "imprimir":
                imprimir()
            case "salir":
                print("¡Hasta luego!")
                break
            case _:
                nuevo_documento(opcion)

if __name__ == "__main__":
    ejemplo_colas()
