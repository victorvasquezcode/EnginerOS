# Bitácora de Aprendizaje: Reto 05 - Asignación por Valor y por Referencia

### 1. 🎯 Lo que dominé hoy (El clic mental)

* **Diferencia fundamental entre Valor y Referencia:**
  * **Tipos Inmutables (Por Valor):** Al igualar una variable a otra (ej. enteros o texto) y modificar una de ellas, la variable original no cambia su valor.
  * **Tipos Mutables (Por Referencia):** Al igualar estructuras como listas o diccionarios (`lista_2 = lista_1`), ambas variables apuntan a la misma dirección de memoria. Cualquier modificación afectará directamente a la variable original.
* **Comportamiento en Funciones:**
  * Las variables inmutables enviadas a una función no se ven alteradas en el ámbito global (afuera), la modificación ocurre únicamente dentro de la función.
  * Las colecciones mutables (listas/diccionarios) modificadas dentro de una función mediante métodos como `.append()` mantienen los cambios fuera de ella.
* **Sintaxis Idiomática:**
  * El truco del desempaquetado de tuplas `a, b = b, a` para intercambiar los valores de dos variables en una sola línea de forma elegante.
* **Manejo de Retornos:**
  * Para conservar los resultados en tipos inmutables o cambios de asignación, es necesario capturar el retorno de la función en **nuevas variables** (ej. `nueva_a, nueva_b = funcion(a, b)`), ya que volver a llamar a las variables originales solo mostrará sus valores iniciales intactos.

---

### 2. ⚠️ Tropezones, errores y cómo los solucioné

* **Confundir la creación de una nueva lista con una modificación por referencia:**
  * *Error:* Usar el operador `+` entre listas (`lista_2 = lista + ["elemento"]`) pensando que se estaba modificando por referencia.
  * *Solución:* Entendí que el operador `+` crea una lista nueva en memoria. Para modificar por referencia real hay que trabajar sobre la variable asignada directamente (`lista_2 = lista_1`) utilizando métodos mutables como `.append()`.
* **Asignación estática dentro de funciones de intercambio:**
  * *Error:* Asignar valores fijos dentro de la función (`a = 20`, `b = 15`) en lugar de procesar los parámetros dinámicos recibidos.
  * *Solución:* Reemplacé los valores fijos por la reasignación de parámetros `a, b = b, a` para que la función acepte y procese cualquier dato de entrada.
* **No capturar los valores retornados por la función:**
  * *Error:* Invocar la función con `intercambiar_por_valor(var1, var2)` esperando que las variables globales cambiaran solas.
  * *Solución:* Entendí que el retorno debe asignarse explícitamente a nuevas variables (`nueva_var1, nueva_var2 = ...`) para visualizar los resultados.