# =============================================================================
# PARTE 1: CONCEPTO DE HERENCIA Y POLIMORFISMO
# =============================================================================
# La herencia permite que una clase hija (subclase) herede atributos y métodos
# de una clase padre (superclase), promoviendo la reutilización de código.


# 1. Definición de la Superclase 'Animal':
# - Crear la clase base 'Animal'.
# - Método Constructor (__init__): Recibir e inicializar el parámetro 'nombre: str'.
# - Método genérico 'emitir_sonido(self)': Definir la firma del método que será
#   sobrescrito por las subclases (polimorfismo).
class Animal:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def emitir_sonido(self):
        return "El animal emite un sonido generico"


# 2. Definición de Subclases:
# - Clase 'Perro(Animal)':
#     - Heredar de 'Animal' usando la sintaxis 'class Perro(Animal):'.
#     - Sobrescribir 'emitir_sonido(self)' para retornar/imprimir "¡Guau!".
# - Clase 'Gato(Animal)':
#     - Heredar de 'Animal'.
#     - Sobrescribir 'emitir_sonido(self)' para retornar/imprimir "¡Miau!".
class Perro(Animal):
    def emitir_sonido(self):
        return f"{self.nombre} dice: ¡Guau!"

class Gato(Animal):
    def emitir_sonido(self):
        return f"{self.nombre} dice: ¡Miau!"


# 3. Función Polimórfica Independiente:
# - Definir 'imprimir_sonido(animal: Animal)':
#     - Recibir cualquier objeto que sea instancia de 'Animal' (o sus subclases).
#     - Ejecutar el método 'animal.emitir_sonido()' independientemente del tipo concreto.
def imprimir_sonido(animal: Animal):
    print(animal.emitir_sonido())


# 4. Proceso de Prueba:
# - Instanciar un objeto 'Perro' y un objeto 'Gato'.
# - Pasar cada instancia a 'imprimir_sonido()' para verificar el comportamiento dinámico.
perro1 = Perro("Firulais")
gato1 = Gato("Garfield")

imprimir_sonido(perro1)
imprimir_sonido(gato1)


# =============================================================================
# DIFICULTAD EXTRA: JERARQUÍA DE EMPRESA DE DESARROLLO DE SOFTWARE
# =============================================================================

# --- 1. SUPERCLASE BASE: Empleado ---
# - Definir clase 'Empleado':
#     - __init__(self, id_empleado: int, nombre: str):
#         - Inicializar atributos base: 'id_empleado' y 'nombre'.
#         - Inicializar una lista para los empleados a su cargo (self.empleados_a_cargo = []).
#     - Método 'agregar_subordinado(self, empleado)':
#         - Añadir una instancia de 'Empleado' a la lista 'empleados_a_cargo'.
#     - Método 'mostrar_informacion(self)':
#         - Imprimir ID, Nombre y el rol o función del empleado.
#     - Método 'mostrar_subordinados(self)':
#         - Recorrer e imprimir la lista de empleados a su cargo.
class Empleado:
    def __init__(self, id_empleado: int, nombre: str):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.empleados_a_cargo = []

    def agregar_subordinado(self, empleado):
        self.empleados_a_cargo.append(empleado)

    def mostrar_informacion(self):
        rol = type(self).__name__
        print(f"ID: {self.id_empleado} | Nombre: {self.nombre} | Rol: {rol}", end = "")

    def mostrar_subordinados(self):
        print(f"\nEmpleado(s) a cargo de {self.nombre}:")
        if self.empleados_a_cargo:
            for empleado in self.empleados_a_cargo:
                print(f"- [ID: {empleado.id_empleado}] : {empleado.nombre}")
        else:
            print(" - No tiene empleados a cargo")

# --- 2. SUBCLASES ESPECIALIZADAS ---

# - Clase 'Programador(Empleado)':
#     - __init__(self, id_empleado: int, nombre: str, lenguaje_principal: str):
#         - Llamar al constructor padre con 'super().__init__(id_empleado, nombre)'.
#         - Inicializar atributo exclusivo: 'lenguaje_principal'.
#     - Método exclusivo 'escribir_codigo(self)':
#         - Imprimir un mensaje indicando que está programando en su lenguaje.
class Programador(Empleado):
    def __init__(self, id_empleado: int, nombre: str, lenguaje_principal: str):
        super().__init__(id_empleado, nombre)
        self.lenguaje_principal = lenguaje_principal

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f" | Lenguaje: {self.lenguaje_principal}")
    
    def escribir_codigo(self):
        print(f"El empleado {self.nombre} con el id {self.id_empleado} esta programando en su lenguaje {self.lenguaje_principal}")

# - Clase 'GerenteProyecto(Empleado)':
#     - __init__(self, id_empleado: int, nombre: str, proyecto_asignado: str):
#         - Llamar a 'super().__init__(id_empleado, nombre)'.
#         - Inicializar atributo exclusivo: 'proyecto_asignado'.
#     - Método exclusivo 'coordinar_proyecto(self)':
#         - Imprimir mensaje indicando el proyecto que está gestionando.
class GerenteProyecto(Empleado):
    def __init__(self, id_empleado: int, nombre: str, proyecto_asignado: str):
        super().__init__(id_empleado, nombre)
        self.proyecto_asignado = proyecto_asignado

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f" | Proyecto: {self.proyecto_asignado}")

    def coordinar_proyecto(self):
        print(f"El empleado {self.nombre} con el id {self.id_empleado} esta en el proyecto asignado {self.proyecto_asignado}")

# - Clase 'Gerente(Empleado)':
#     - __init__(self, id_empleado: int, nombre: str, departamento: str):
#         - Llamar a 'super().__init__(id_empleado, nombre)'.
#         - Inicializar atributo exclusivo: 'departamento'.
#     - Método exclusivo 'tomar_decisiones_estrategicas(self)':
#         - Imprimir mensaje indicando las decisiones que ejecuta sobre su departamento.
class Gerente(Empleado):
    def __init__(self, id_empleado: int, nombre: str, departamento: str):
        super().__init__(id_empleado, nombre)
        self.departamento = departamento

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f" | Departamento: {self.departamento}")

    def tomar_decisiones_estrategicas(self):
        print(f"El empleado {self.nombre} con el id {self.id_empleado} esta en el departamento {self.departamento}")


# --- 3. PROCESO DE PRUEBA DE DIFICULTAD EXTRA ---
# 1. Instanciar varios Programadores (ej. Programador 1, Programador 2).
# 2. Instanciar un Gerente de Proyecto y asignarle los Programadores como subordinados.
# 3. Instanciar un Gerente General y asignarle el Gerente de Proyecto como subordinado.
# 4. Probar la ejecución de métodos exclusivos de cada rol y verificar la jerarquía de subordinados.
programador1 = Programador(101,"Javier","Python")
programador2 = Programador(102,"Carlos","Javascript")

pm = GerenteProyecto(201, "Roberto", "Sistema CRM")
pm.agregar_subordinado(programador1)
pm.agregar_subordinado(programador2)

gerente_general = Gerente(301,"Laura", "Tecnologia")
gerente_general.agregar_subordinado(pm)

print("--- METODOS EXCLUSIVOS ---")
programador1.escribir_codigo()
pm.coordinar_proyecto()
gerente_general.tomar_decisiones_estrategicas()

print("\n --- INFORMACION DE EMPLEADOS ---")
programador1.mostrar_informacion()
programador2.mostrar_informacion()
pm.mostrar_informacion()
gerente_general.mostrar_informacion()

print("\n --- JERARQUIA DE SUBORDINADOS ---")
gerente_general.mostrar_subordinados()
pm.mostrar_subordinados()
programador1.mostrar_subordinados()