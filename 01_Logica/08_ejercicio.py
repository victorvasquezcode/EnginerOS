# =============================================================================
# RETO 08: CLASES Y OBJETOS (PROGRAMACIÓN ORIENTADA A OBJETOS - POO)
#
# CONCEPTOS CLAVE:
# 1. Clase: Plantilla o molde para crear objetos (define atributos y métodos).
# 2. Atributos: Variables asociadas al objeto (guardan su estado).
# 3. Métodos: Funciones asociadas al objeto (definen su comportamiento).
# 4. Constructor (__init__): Método especial que se ejecuta automáticamente
#    al instanciar un objeto para inicializar sus atributos.
# 5. Parámetro `self`: Referencia obligatoria dentro de la clase para acceder
#    a las propiedades y métodos de la propia instancia.
# =============================================================================

# -----------------------------------------------------------------------------
# 1. EJERCICIO PRINCIPAL: CREACIÓN Y MANIPULACIÓN DE UNA CLASE
# -----------------------------------------------------------------------------

class Persona:
    """
    Clase que representa a una persona básica con atributos y métodos de impresión.
    """
    def __init__(self, nombre: str, edad: int):
        # Inicializador de atributos de instancia
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        # Método para imprimir la información del objeto
        print(f"Nombre: {self.nombre} | Edad: {self.edad}")


# --- PRUEBAS DEL EJERCICIO PRINCIPAL ---
print("=== DEMOSTRACIÓN DE CLASE Y OBJETOS ===")

# Instanciación y establecimiento de parámetros iniciales
persona1 = Persona("Víctor", 26)
print("Datos iniciales:")
persona1.mostrar_datos()

# Modificación de atributos directamente
persona1.nombre = "Víctor Javier"
persona1.edad = 27

print("\nDatos modificados:")
persona1.mostrar_datos()


# =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# =============================================================================

print("\n=== DIFICULTAD EXTRA ===")

# --- 1. Clase Pila (Stack - LIFO) ---
class Pila:
    def __init__(self):
        # PISTA: Inicializa una lista vacía para almacenar los elementos
        self.elementos = []

    def push(self, elemento):
        # PISTA: Añade un elemento al final de la lista
        self.elementos.append(elemento)

    def pop(self):
        # PISTA: Valida si no está vacía antes de extraer el último elemento (.pop())
        if not self.elementos:
            print("La pila esta vacia")
            return None
        return self.elementos.pop()

    def contar(self) -> int:
        # PISTA: Retorna el número total de elementos (len())
        return len(self.elementos)

    def mostrar(self):
        # PISTA: Imprime el contenido actual de la pila
        print(f"Pila actual: {self.elementos}")


# --- 2. Clase Cola (Queue - FIFO) ---
class Cola:
    def __init__(self):
        # PISTA: Inicializa una lista vacía para almacenar los elementos
        self.elementos = []

    def enqueue(self, elemento):
        # PISTA: Añade un elemento al final de la lista
        self.elementos.append(elemento)

    def dequeue(self):
        # PISTA: Valida si no está vacía antes de extraer el primer elemento (.pop(0))
        if not self.elementos:
            print("La cola esta vacia")
            return None
        return self.elementos.pop(0)

    def contar(self) -> int:
        # PISTA: Retorna el número total de elementos (len())
        return len(self.elementos)

    def mostrar(self):
        # PISTA: Imprime el contenido actual de la cola
        print(f"Cola actual: {self.elementos}")


# --- Pruebas de la Dificultad Extra ---
mi_pila = Pila()
mi_pila.push("Documento 1")
mi_pila.push("Documento 2")
mi_pila.push("Documento 3")
extraido_pila = mi_pila.pop()
print(f"Elemento retirado de la pila: {extraido_pila}")
print(f"Total de elementos en pila: {mi_pila.contar()}")
mi_pila.mostrar()

mi_cola = Cola()
mi_cola.enqueue("Turno 1")
mi_cola.enqueue("Turno 2")
mi_cola.enqueue("Turno 3")
extraido_cola = mi_cola.dequeue()
print(f"Elemento retirado de la cola: {extraido_cola}")
print(f"Total de elementos en cola: {mi_cola.contar()}")
mi_cola.mostrar()