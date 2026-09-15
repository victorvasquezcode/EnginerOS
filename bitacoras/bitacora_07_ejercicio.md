# Bitácora de Aprendizaje: Reto 07 - Estructuras de Datos: Pilas (Stacks) y Colas (Queues)

### 1. 🎯 Lo que dominé hoy (El clic mental)

- **Pilas (Stack - LIFO: *Last In, First Out*):**
  - **Mecanismo:** El último elemento en ingresar es el primero en salir.
  - **Implementación en Python:** Mediante listas nativas usando `.append()` para *Push* (agregar al final) y `.pop()` sin argumentos para *Pop* (extraer del final), logrando complejidad $O(1)$.
  - **Uso de Inspección (*Peek*):** Acceso al elemento superior mediante indexación negativa (`[-1]`) sin destruir la estructura.
  - **Caso Real:** Historial de navegación Web (pila `atras` vs. pila `adelante`).

- **Colas (Queue - FIFO: *First In, First Out*):**
  - **Mecanismo:** El primer elemento en ingresar es el primero en salir.
  - **Implementación Eficiente:** Uso de `collections.deque` (Double Ended Queue). A diferencia de `list.pop(0)` que requiere reindexar la memoria ($O(n)$), `deque.popleft()` ejecuta la extracción inicial en $O(1)$.
  - **Caso Real:** Gestión de cola de impresión para procesamiento en orden de llegada.

- **Arquitectura de Software y Menú de Selección:**
  - **Encapsulamiento:** Organización de bucles interactivos (`while True`) dentro de funciones contenedoras (`ejecutar_navegador()`, `ejecutar_impresora()`).
  - **Orquestación:** Creación de un menú principal que gestiona el flujo de ejecución sin cerrar el programa al salir de una simulación individual.

---

### 2. ⚠️ Tropezones, errores y cómo los solucioné

- **Uso Erróneo de `.pop()` con Argumentos de Valor:**
  - *Error:* Intentar extraer elementos de la pila mediante `pila.pop(pagina_actual)`, pasando una variable de cadena en lugar de un índice numérico o invocarlo sin argumentos.
  - *Solución:* Usar `.pop()` sin argumentos para extraer por defecto el último elemento de la pila y reasignar el retorno a la variable global `pagina_actual`.

- **Incompatibilidad de Métodos en `deque`:**
  - *Error:* Intentar ejecutar `.pop(0)` en un objeto de tipo `collections.deque`, generando un error de tipo (`TypeError`).
  - *Solución:* Reemplazar la indexación por el método explícito `.popleft()`.

- **Inversión de Lógica en Cláusulas de Guardia:**
  - *Error:* Escribir `if not pila_atras:` para ejecutar la navegación hacia atrás cuando la lista estaba vacía, en lugar de cuando contenía elementos.
  - *Solución:* Evaluar directamente la veracidad de la colección (`if pila_atras:`) antes de realizar la extracción y manejar el estado vacío en el bloque `else`.

- **Ámbitos de Variables Globales (*Scope*):**
  - *Error:* Intentar reasignar `pagina_actual` dentro de funciones auxiliares sin declarar su ámbito global.
  - *Solución:* Incluir la instrucción `global pagina_actual` al inicio de cada función modificadora.