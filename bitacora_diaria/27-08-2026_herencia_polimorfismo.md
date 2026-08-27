# Bitácora de Aprendizaje: Reto 09 - Herencia y Polimorfismo

### 1. 🎯 Lo que dominé hoy (El clic mental)

* **Reutilización y extensión mediante Herencia:**
  * Comprendí cómo una subclase (`Programador`, `Gerente`) extiende las capacidades de una superclase (`Empleado`), reutilizando atributos compartidos (`id_empleado`, `nombre`, `empleados_a_cargo`) e integrando propiedades o métodos exclusivos de su rol.
* **Invocación correcta de `super().__init__()`:**
  * Entendí que la llamada al constructor padre debe realizarse en una sola línea pasando todos los parámetros requeridos juntos (`super().__init__(id_empleado, nombre)`), asegurando que la superclase inicialice correctamente su estado base antes de agregar los atributos propios de la subclase.
* **Polimorfismo y extensión de métodos:**
  * Comprendí cómo sobrescribir métodos de la superclase para adaptar el comportamiento a cada subclase, y cómo combinar el comportamiento base usando `super().mostrar_detalles()` seguido de la impresión de atributos específicos.
* **Obtención dinámica del nombre de la clase con `self.__class__.__name__`:**
  * Aprendí a usar la introspección de Python mediante `self.__class__.__name__` para obtener dinámicamente el nombre exacto de la clase de una instancia en tiempo de ejecución. Esto evita hardcodear cadenas de texto al imprimir detalles de objetos heredados.

---

### 2. ⚠️ Tropezones, errores y cómo los solucioné

* **Llamadas dobles y fragmentadas a `super().__init__()`:**
  * *Error:* Ejecutar `super().__init__(id_empleado)` y `super().__init__(nombre)` en líneas separadas. Esto causaba un fallo de tipo `TypeError` porque el constructor base esperaba ambos argumentos simultáneamente en la primera llamada.
  * *Solución:* Consolidé la invocación en una única instrucción: `super().__init__(id_empleado, nombre)`.
* **Omisión de información base en métodos condicionales:**
  * *Error:* Condicionar todo el bloque de `mostrar_detalles()` a la presencia de la lista `self.empleados_a_cargo`, haciendo que los empleados sin subordinados no imprimieran su ID o nombre.
  * *Solución:* Reestructuré el método para imprimir siempre los datos del empleado y evaluar la lista de subordinados de forma secundaria y condicional.