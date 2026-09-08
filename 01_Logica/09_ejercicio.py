# =============================================================================
# RETO 09: HERENCIA Y POLIMORFISMO
#
# CONCEPTOS CLAVE:
# 1. Herencia: Mecanismo que permite a una clase (subclase) heredar atributos 
#    y métodos de otra clase (superclase), promoviendo la reutilización de código.
# 2. Polimorfismo: Capacidad de diferentes objetos para responder al mismo 
#    nombre de método de forma personalizada según su clase.
# 3. `super().__init__()`: Llamada al constructor de la clase padre para 
#    inicializar los atributos heredados antes de añadir los propios.
# =============================================================================

# -----------------------------------------------------------------------------
# 1. EJERCICIO PRINCIPAL: ANIMAL, PERRO Y GATO
# -----------------------------------------------------------------------------

class Animal:
    """
    Superclase abstracta/base de la cual heredarán las especies concretas.
    """
    def __init__(self, nombre: str):
        self.nombre = nombre

    def emitir_sonido(self) -> str:
        # PISTA: Método base pensado para ser sobrescrito por las subclases
        return "Sonido genérico de animal"


class Perro(Animal):
    def __init__(self, nombre: str, raza: str):
        # PISTA: Llama al constructor de Animal pasando 'nombre' con super()
        super().__init__(nombre)
        self.raza = raza

    def emitir_sonido(self) -> str:
        # PISTA: Sobrescribe el método con el sonido específico del perro
        return "¡Guau!"


class Gato(Animal):
    def __init__(self, nombre: str, color: str):
        super().__init__(nombre)
        self.color = color

    def emitir_sonido(self) -> str:
        # PISTA: Sobrescribe el método con el sonido específico del gato
        return "¡Miau!"


def imprimir_sonido_animal(animal: Animal):
    """
    Función polimórfica: recibe cualquier objeto que sea de tipo Animal 
    e imprime su sonido sin importar la clase concreta.
    """
    print(f"{animal.nombre} dice: {animal.emitir_sonido()}")


# --- PRUEBAS DEL EJERCICIO PRINCIPAL ---
print("=== DEMOSTRACIÓN DE HERENCIA Y POLIMORFISMO ===")
mi_perro = Perro("Firulais", "Pastor Alemán")
mi_gato = Gato("Garfield", "Naranja")

imprimir_sonido_animal(mi_perro)
imprimir_sonido_animal(mi_gato)


# =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# =============================================================================

print("\n=== DIFICULTAD EXTRA ===")

# --- Superclase Base ---
class Empleado:
    def __init__(self, id_empleado: int, nombre: str):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.empleados_a_cargo = []  # Lista para almacenar empleados a su cargo

    def agregar_a_cargo(self, empleado):
        # PISTA: Agrega un empleado a la lista de subordinados
        self.empleados_a_cargo.append(empleado)
        return empleado

    def mostrar_detalles(self):
        # PISTA: Muestra el ID, nombre y rol básico del empleado
        print(f"[{self.__class__.__name__}] ID: {self.id_empleado} | Nombre: {self.nombre}")
        if self.empleados_a_cargo:
                    print("Empleados a cargo")
                    for emp in self.empleados_a_cargo:
                        print(f" - {emp.nombre}")


# --- Subclase Programador ---
class Programador(Empleado):
    def __init__(self, id_empleado: int, nombre: str, lenguaje_principal: str):
        # PISTA: Usa super() para id y nombre, inicializa lenguaje_principal
        super().__init__(id_empleado,nombre)
        self.lenguaje_principal = lenguaje_principal

    def programar(self):
        # PISTA: Función exclusiva de su actividad
        return f"{self.nombre} esta programando en {self.lenguaje_principal}."

    def mostrar_detalles(self):
        super().mostrar_detalles()
        print(f" Lenguaje principal: {self.lenguaje_principal}")


# --- Subclase Gerente de Proyecto ---
class GerenteProyecto(Empleado):
    def __init__(self, id_empleado: int, nombre: str, proyecto_actual: str):
        # PISTA: Usa super() e inicializa el proyecto asignado
        super().__init__(id_empleado,nombre)
        self.proyecto_actual = proyecto_actual

    def coordinar_proyecto(self):
        # PISTA: Función exclusiva de su actividad
        return f"{self.nombre} esta coordinando el proyecto {self.proyecto_actual}."

    def mostrar_detalles(self):
        super().mostrar_detalles()
        print(f" Proyecto asignado: {self.proyecto_actual}")


# --- Subclase Gerente General ---
class Gerente(Empleado):
    def __init__(self, id_empleado: int, nombre: str, departamento: str):
        # PISTA: Usa super() e inicializa departamento
        super().__init__(id_empleado,nombre)
        self.departamento = departamento

    def tomar_decision_ejecutiva(self):
        # PISTA: Función exclusiva de su actividad
        return f"{self.nombre} tomo una decision para el area de {self.departamento}"

    def mostrar_detalles(self):
        super().mostrar_detalles()
        print(f" Departamento: {self.departamento}")


# --- Pruebas de la Dificultad Extra ---
print ("=== JERARQUIA DE LA EMPRESA ===")
dev1 = Programador(1,"Victor","Python")
pm1 = GerenteProyecto(2,"Ana","Migracion ERP")
gerente1 = Gerente(3, "Carlos", "Sistemas")

gerente1.agregar_a_cargo(pm1)
pm1.agregar_a_cargo(dev1)

gerente1.mostrar_detalles()
print()
pm1.mostrar_detalles()
print()
dev1.mostrar_detalles()