# Bitácora de Aprendizaje: Reto 08 - Clases y Objetos (POO)

### 1. 🎯 Lo que dominé hoy (El clic mental)

* **Fundamentos de POO (Clases y Objetos):**
  * La **Clase** actúa como el molde o plantilla (define atributos y métodos), mientras que el **Objeto** es la instancia concreta creada a partir de ella.
  * El constructor `__init__` se ejecuta automáticamente al instanciar el objeto y el parámetro `self` permite hacer referencia a las variables internas de la propia instancia (`self.atributo`).
* **Encapsulamiento de Estructuras (Pilas y Colas con Clases):**
  * Diseñé las clases `Pila` (LIFO) y `Cola` (FIFO) encapsulando una lista interna (`self.elementos`) y aislando sus métodos operacionales (`push`, `pop`, `enqueue`, `dequeue`).
* **Diferencia técnica entre `print()` y `return`:**
  * `print()` es solo un canal visual para el usuario en consola; no entrega datos procesables al programa.
  * `return` finaliza la ejecución de la función y entrega un valor en memoria que puede ser asignado a variables o utilizado en operaciones posteriores.
* **Patrón de Diseño *Early Return* (Salida Temprana):**
  * Si una condición de error o freno de mano se cumple (ej. `if not self.elementos:`), se ejecuta un `return` inmediato para cortar la función, eliminando la necesidad de usar bloques `else` redundantes e identación innecesaria.

---

### 2. ⚠️ Tropezones, errores y cómo los solucioné

* **Confundir la impresión con el retorno en métodos informativos:**
  * *Error:* En el método `contar()`, utilizaba `print(len(self.elementos))`, lo que provocaba que al llamarlo fuera de la clase no devolviera un tipo `int`, sino `None`.
  * *Solución:* Reemplacé el `print()` por `return len(self.elementos)` para cumplir con el contrato de retorno y permitir que el entero sea operable desde fuera.
* **Falta de retorno en los métodos de extracción (`pop` / `dequeue`):**
  * *Error:* Ejecutar `self.elementos.pop()` de forma aislada sin usar la palabra clave `return`. Aunque el elemento se eliminaba de la lista, se perdía en el aire y no se entregaba al invocador.
  * *Solución:* Modifiqué la instrucción a `return self.elementos.pop()` para eliminar y retornar el valor simultáneamente.