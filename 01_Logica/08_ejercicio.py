# =============================================================================
# RETO 07: PILAS (STACKS) Y COLAS (QUEUES)
#
# CONCEPTOS CLAVE:
# 1. Pila (Stack - LIFO: Last In, First Out): El último elemento en entrar 
#    es el primero en salir (ej. pila de platos, historial/deshacer).
# 2. Cola (Queue - FIFO: First In, First Out): El primer elemento en entrar 
#    es el primero en salir (ej. fila del banco, cola de impresión).
# =============================================================================

# -----------------------------------------------------------------------------
# 1. EJERCICIO PRINCIPAL: ESTRUCTURA Y MÉTODOS BÁSICOS
# -----------------------------------------------------------------------------

# --- PILA (STACK - LIFO) ---
print("=== DEMOSTRACIÓN DE PILA (STACK) ===")
pila = []

# Introducción de elementos (Push -> append)
pila.append("Página 1")
pila.append("Página 2")
pila.append("Página 3")
print(f"Pila actual: {pila}")

# Recuperación/Extracción de elementos (Pop -> pop())
# Extrae el ÚLTIMO elemento añadido
elemento_pila = pila.pop()
print(f"Elemento extraído (LIFO): {elemento_pila}")
print(f"Pila tras extracción: {pila}\n")


# --- COLA (QUEUE - FIFO) ---
print("=== DEMOSTRACIÓN DE COLA (QUEUE) ===")
cola = []

# Introducción de elementos (Enqueue -> append)
cola.append("Cliente 1")
cola.append("Cliente 2")
cola.append("Cliente 3")
print(f"Cola actual: {cola}")

# Recuperación/Extracción de elementos (Dequeue -> pop(0))
# Extrae el PRIMER elemento añadido
elemento_cola = cola.pop(0)
print(f"Elemento extraído (FIFO): {elemento_cola}")
print(f"Cola tras extracción: {cola}")


# =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# =============================================================================

print("\n=== DIFICULTAD EXTRA ===")

# --- 1. Simulador de Navegador Web (Uso de Pilas) ---
def navegador_web():
    # Pila para el historial hacia atrás y pila para el historial hacia adelante
    historial_atras = []
    historial_adelante = []
    pagina_actual = "google"

    while True:
        # Pide la instrucción o nombre de la web
        # Aplica .strip().lower() para sanear la entrada
        # Lógica para "atrás", "adelante", "salir" y nuevas webs
        print(f"\n[Pagina actual: {pagina_actual}]")
        comando = input("Ingresa una URL o un comando (atras/adelante/salir): ").strip().lower()

        if not comando:
            print("El comando no puede estar vacio.")
            continue

        if comando == "atras":

            if not historial_atras:
                print("No existe una pagina buscada anteriormente.")
            else:
                historial_adelante.append(pagina_actual)
                pagina_actual = historial_atras.pop()
                print(f"Se volvio a la pagina anterior")
            
        elif comando == "adelante":
            if not historial_adelante:
                print("No existe una pagina buscada posterior")
            else:
                historial_atras.append(pagina_actual)
                pagina_actual = historial_adelante.pop()
                
        elif comando == "salir":
            break
        else:
            historial_atras.append(pagina_actual)
            pagina_actual = comando
            historial_adelante.clear()

# Para probar:
#navegador_web()


# --- 2. Simulador de Impresora Compartida (Uso de Colas) ---
def impresora_compartida():
    cola_impresion = []

    while True:
        # Pide la instrucción o nombre del documento
        # Lógica para "imprimir", "salir" y agregar documentos a la cola
        instruccion = input("Ingrese el nombre del documento para imprimir o instruccion (imprimir / salir): ").strip().lower()
        if not instruccion:
            print("No puede estar vacia la instruccion.")
            continue
        
        if instruccion == "salir":
            break
        elif instruccion == "imprimir":
            if not cola_impresion:
                print("No hay cola para imprimir")
            else:
             impresion = cola_impresion.pop(0)
             print(f"Imprimiendo el documento '{impresion}'")
             print(f"Se imprimio correctamente el documento '{impresion}'")
        else:
            cola_impresion.append(instruccion)
            print(f"Se agrego correctamente a la cola de documentos '{instruccion}'")
        pass

# Para probar:
impresora_compartida()