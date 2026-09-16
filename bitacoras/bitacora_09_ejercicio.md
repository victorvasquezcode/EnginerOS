# Bitácora de Aprendizaje: Reto 09 - Herencia y Polimorfismo

### 1. 🎯 Lo que dominé hoy (El clic mental)

- **Mecanismos de Herencia (`super()`):**
  - Comprendí cómo establecer relaciones jerárquicas entre superclases (`Empleado`) y subclases (`Programador`, `GerenteProyecto`, `Gerente`).
  - Dominé la delegación de constructores utilizando `super().__init__(...)` para inicializar atributos heredados sin duplicar código.

- **Polimorfismo e Interfaces Uniformes:**
  - Aprendí a diseñar **funciones polimórficas independientes** (`imprimir_sonido(animal: Animal)`) que interactúan uniformemente con distintas subclases sin importar su tipo concreto, confiando en la firma compartida del método (`emitir_sonido()`).

- **Sobrescritura de Métodos (*Method Overriding*) e Introspección:**
  - Implementé la extensión de comportamientos heredados combinando `super().mostrar_informacion()` con atributos exclusivos de cada subclase.
  - Utilicé la introspección con `type(self).__name__` para identificar y mostrar dinámicamente el rol exacto de un objeto dentro de su propia ejecución.

- **Modelado de Estructuras Compuestas (Jerarquías):**
  - Implementé listas de composición interna (`self.empleados_a_cargo`) dentro de la superclase para construir árboles jerárquicos organizacionales escalables.

---

### 2. ⚠️ Tropezones, errores y cómo los solucioné

- **Diferencia entre Método de Clase y Función Polimórfica:**
  - *Duda/Error:* Confusión inicial sobre por qué llamar a `imprimir_sonido(perro1)` en lugar de ejecutar directamente `perro1.imprimir_sonido()`.
  - *Solución:* Entendí que `.emitir_sonido()` es el método propio del objeto, mientras que `imprimir_sonido()` actúa como un "reproductor" o función externa polimórfica que recibe la instancia como argumento.

- **Type Hinting Erróneo en Parámetros de Objeto:**
  - *Error:* Definir `def agregar_subordinado(self, empleado: str)` indicando `str` como tipo de dato.
  - *Solución:* Corregir la anotación de tipo, ya que la función espera recibir una **instancia completa de objeto** (de tipo `Empleado` o sus subclases) y no una simple cadena de texto.

- **Impresión Directa de Instancias de Objetos:**
  - *Error:* Imprimir directamente `print(f" - {empleado}")` dentro del bucle de subordinados, lo cual mostraba referencias de memoria (`<__main__.Empleado object at 0x...>`).
  - *Solución:* Acceder a las propiedades explícitas del objeto (`emp.nombre`, `emp.id_empleado`) o llamar a su método `mostrar_informacion()`.