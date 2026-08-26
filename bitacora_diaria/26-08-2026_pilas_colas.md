# Bitácora de Aprendizaje: Reto 07 - Pilas (Stacks) y Colas (Queues)

### 1. 🎯 Lo que dominé hoy (El clic mental)

* **Comportamiento LIFO vs. FIFO:**
  * **Pila (Stack - LIFO):** El último elemento en entrar es el primero en salir (como la pila de platos o la navegación web). Se implementa con `.append()` para insertar y `.pop()` para extraer el último elemento.
  * **Cola (Queue - FIFO):** El primer elemento en entrar es el primero en salir (como la fila de un banco o una impresora). Se implementa con `.append()` para encolar y `.pop(0)` para desencolar el primer elemento.
* **Comportamiento dual del método `.pop()`:** Entendí que `.pop()` o `.pop(0)` realiza dos acciones simultáneas: elimina el elemento de la lista y al mismo tiempo lo devuelve. Para no perder ese dato en el aire, se debe asignar directamente a una variable (ej. `pagina_actual = historial_atras.pop()`).
* **Manejo de estados en el Navegador Web (Pilas):**
  * La `pagina_actual` se gestiona de forma independiente y nunca debe estar dentro de las listas de historial.
  * Al ingresar a una nueva web, se guarda la actual en `historial_atras` y se vacía por completo el `historial_adelante` usando `.clear()`.

---

### 2. ⚠️ Tropezones, errores y cómo los solucioné

* **Llamada a `.pop()` sin capturar el retorno:**
  * *Error:* Ejecutar `historial_atras.pop()` suelto al ir "atrás". Esto eliminaba el elemento de la lista, pero `pagina_actual` no cambiaba y el dato extraído se perdía.
  * *Solución:* Asignar el retorno directamente a la variable: `pagina_actual = historial_atras.pop()`.
* **Riesgo de `IndexError` en listas vacías (Impresora compartida):**
  * *Error:* Intentar ejecutar `.pop(0)` directamente cuando el usuario ingresaba `"imprimir"`, sin verificar si `cola_impresion` tenía elementos, provocando un colapso del programa por `IndexError: pop from empty list`.
  * *Solución:* Validar la existencia de elementos antes de extraer mediante `if not cola_impresion:` e informar al usuario si la cola está vacía.
* **Falta de control de flujo tras entradas vacías:**
  * *Error:* Olvidar el `continue` dentro del bloque de validación para entradas vacías (`if not instruccion:`), lo que permitía que la ejecución continuara hacia los bloques de abajo.
  * *Solución:* Agregar `continue` para reiniciar el ciclo `while True` inmediatamente ante un `input` en blanco.