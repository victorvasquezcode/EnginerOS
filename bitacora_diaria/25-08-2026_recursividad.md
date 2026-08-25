# Bitácora de Aprendizaje: Reto 06 - Recursividad

### 1. 🎯 Lo que dominé hoy (El clic mental)

* **Los Dos Pilares Obligatorios de la Recursividad:**
  * **Caso Base (El freno de mano):** Es la condición de parada con un valor conocido con claridad (ej. en el factorial $1! = 1$, en Fibonacci `posicion <= 1`, o en cuenta atrás `numero < 0`). Evita que la función se llame infinitamente y colapse la memoria.
  * **Caso Recursivo (El problema más pequeño):** Ejecuta la lógica actual combinada con una nueva llamada a la misma función pero reduciendo el problema un paso más (ej. `n * factorial(n - 1)` o `numero - 1`).
* **Flujo de Ejecución (Pila de Llamadas):**
  * **Fase de Descenso:** La función delega el problema reduciéndolo progresivamente hasta alcanzar el caso base.
  * **Fase de Ascenso:** Una vez alcanzado el caso base, los valores devueltos se resuelven de regreso hacia arriba combinando los resultados acumulados.
* **Aplicación en Algoritmos Clásicos:**
  * Estructuración del factorial de un número ($n! = n \times (n-1)!$).
  * Cálculo de la serie de Fibonacci sumando las llamadas de las dos posiciones anteriores ($Fib(n) = Fib(n-1) + Fib(n-2)$).

---

### 2. ⚠️ Tropezones, errores y cómo los solucioné

* **Confundir la recursividad con bucles iterativos (`for` / `while`):**
  * *Error:* Intentar usar un bucle `for` con `range()` dentro de la función `cuenta_atras()`.
  * *Solución:* Comprendí que en la recursividad la propia función reemplaza al bucle al volverse a invocar a sí misma con el parámetro modificado (`numero - 1`).
* **Confusión entre resta simple y llamada recursiva:**
  * *Duda:* ¿Por qué usar `return n * factorial(n - 1)` en lugar de `return n * (n - 1)`?
  * *Solución:* Entendí que `(n - 1)` es solo una operación aritmética aislada que corta la ejecución, mientras que `factorial(n - 1)` obliga a Python a ejecutar toda la función nuevamente para descomponer todo el problema hasta el caso base.
* **Falta de captura del caso base en la llamada inicial:**
  * *Error:* Intentar ejecutar código recursivo sin establecer un `return` claro al cumplirse la condición de parada.
  * *Solución:* Colocar el `if` del caso base al inicio de la función para garantizar una salida limpia del hilo de ejecución.