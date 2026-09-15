# Bitácora de Aprendizaje: Reto 06 - Recursividad y Algoritmos Recursivos

### 1. 🎯 Lo que dominé hoy (El clic mental)

- **Mapeo Mental de la Recursividad:**
  - **Estructura Indispensable:** Comprendí que toda función recursiva requiere obligatoriamente dos componentes: un **Caso Base** (condición de parada para evitar un desbordamiento de pila) y un **Caso Recursivo** (llamada a la misma función modificando el argumento hacia el caso base).
  - **Pila de Llamadas (*Call Stack*):** Entendí cómo Python almacena en memoria cada llamada pendiente hasta alcanzar el caso base, momento en el cual la pila comienza a desapilarse (*unwinding*) retornando los valores hacia arriba.

- **Implementaciones Prácticas:**
  - **Conteo Regresivo:** Control de flujo simple basado en condiciones de parada con `return` implícito (`None`).
  - **Factorial ($n!$):** Estructura de reducción lineal $O(n)$ donde el resultado final se construye mediante la acumulación del producto en la fase de desapilado (`n * factorial(n - 1)`).
  - **Sucesión de Fibonacci:** Aplicación de recursión ramificada o doble ($F(n) = F(n-1) + F(n-2)$) con múltiples casos base ($F(0) = 0$ y $F(1) = 1$).

---

### 2. ⚠️ Tropezones, errores y cómo los solucioné

- **Uso Innecesario de `print()` en Funciones de Efecto Secundario:**
  - *Error:* Ejecutar `print(imprimir_numeros(100))`, lo que provocaba la impresión de un `None` adicional al final de la secuencia debido a la falta de un `return` con valor explícito.
  - *Solución:* Invocar la función directamente (`imprimir_numeros(100)`) cuando su propósito sea únicamente ejecutar acciones en consola sin devolver datos.

- **Omisión de Guardias para Entradas Inválidas:**
  - *Error:* Permitir que argumentos negativos en `factorial(n)` o `fibonacci(posicion)` provocaran una recursión infinita y derivaran en un `RecursionError: maximum recursion depth exceeded`.
  - *Solución:* Incorporar clausulas de guarda iniciales (`if n < 0: return None`) antes de evaluar los casos base estándar.

- **Identificación de Casos Base Múltiples:**
  - *Error:* Tratar de resolver Fibonacci con un solo caso base para $n \le 1$, perdiendo la precisión entre la posición $0$ y $1$.
  - *Solución:* Declarar los dos casos base explícitos e independientes ($n = 0 \to 0$ y $n = 1 \to 1$).