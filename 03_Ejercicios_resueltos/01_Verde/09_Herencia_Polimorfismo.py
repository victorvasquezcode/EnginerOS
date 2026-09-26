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
        self.empleado_a_cargo = []
    def agregar_subordinado(self,empleado):
        self.empleado_a_cargo.append(empleado)
    def mostrar_informacion(self):
        print(f"-ID: {self.id_empleado}\n-NOMBRE: {self.nombre}\n-FUNCION: {self.__class__.__name__}")
    def mostrar_subordinados(self):
        if not self.empleado_a_cargo:
            print("No tiene empleados a cargo")
            return
        print("Empleado a cargo: ")
        for empleado in self.empleado_a_cargo:
            empleado.mostrar_informacion()

# --- 2. SUBCLASES ESPECIALIZADAS ---

# - Clase 'Programador(Empleado)':
#     - __init__(self, id_empleado: int, nombre: str, lenguaje_principal: str):
#         - Llamar al constructor padre con 'super().__init__(id_empleado, nombre)'.
#         - Inicializar atributo exclusivo: 'lenguaje_principal'.
#     - Método exclusivo 'escribir_codigo(self)':
#         - Imprimir un mensaje indicando que está programando en su lenguaje.
class Programador(Empleado):
    def __init__(self, id_empleado: int , nombre: str, lenguaje_principal: str):
        super().__init__(id_empleado, nombre)
        self.lenguaje_principal = lenguaje_principal
    def escribir_codigo(self):
        print(f"El programador '{self.nombre}' su lengujae de programacion es '{self.lenguaje_principal}'")

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
    def coordinar_proyecto(self):
        print(f"El gerente de proyecto '{self.nombre}' tiene a cargo el proyecto '{self.proyecto_asignado}'"
              )
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
    def tomar_decisiones_estrategicas(self):
        print(f"El gerente '{self.nombre}' toma decisiones en el departamento de '{self.departamento}'")

# --- 3. PROCESO DE PRUEBA DE DIFICULTAD EXTRA ---
# 1. Instanciar varios Programadores (ej. Programador 1, Programador 2).
# 2. Instanciar un Gerente de Proyecto y asignarle los Programadores como subordinados.
# 3. Instanciar un Gerente General y asignarle el Gerente de Proyecto como subordinado.
# 4. Probar la ejecución de métodos exclusivos de cada rol y verificar la jerarquía de subordinados.

if __name__ == "__main__":
    print("=== 1. CREACIÓN DE PROGRAMADORES ===")
    prog1 = Programador(101, "Víctor", "Python")
    prog2 = Programador(102, "Ana", "JavaScript")

    # Ejecución de métodos exclusivos
    prog1.escribir_codigo()
    prog2.escribir_codigo()

    print("\n=== 2. CREACIÓN DE GERENTE DE PROYECTO Y ASIGNACIÓN ===")
    gerente_proy = GerenteProyecto(201, "Carlos", "Sistema ERP")
    
    # Asignación de subordinados (Programadores)
    gerente_proy.agregar_subordinado(prog1)
    gerente_proy.agregar_subordinado(prog2)
    
    # Método exclusivo y verificación de jerarquía
    gerente_proy.coordinar_proyecto()
    gerente_proy.mostrar_subordinados()

    print("\n=== 3. CREACIÓN DE GERENTE GENERAL Y ASIGNACIÓN DE ALTO NIVEL ===")
    gerente_general = Gerente(301, "Sofia", "Tecnología e Innovación")
    
    # Asignación de subordinado (Gerente de Proyecto)
    gerente_general.agregar_subordinado(gerente_proy)
    
    # Método exclusivo e información general
    gerente_general.tomar_decisiones_estrategicas()
    gerente_general.mostrar_informacion()

    print("\n=== 4. MOSTRAR SUBORDINADOS DEL GERENTE GENERAL ===")
    gerente_general.mostrar_subordinados()
