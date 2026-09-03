# Bitácora de Aprendizaje: Reto 01

### 1. 🎯 Lo que dominé hoy (El clic mental)
* **Optimización en Bucle y Rango:** Hice un clic mental clave en la dificultad extra al usar `range(10, 56, 2)`. Al pasarle el paso `2`, filtré los números pares directamente desde la generación del rango, reduciendo a la mitad las iteraciones del bucle en lugar de evaluar cada número.
* **Flujo con Cláusula de Guarda (`continue`):** Dominé la estructura para descartar casos no deseados (`numero == 16 or numero % 3 == 0`) al inicio de cada iteración. Esto evita anidar múltiples `if` y mantiene la lógica del código más limpia.
* **Identidad (`is`) vs. Igualdad (`==`):** Entendí que `==` compara si dos variables contienen el mismo valor, mientras que `is` evalúa si apuntan al mismo bloque físico en memoria RAM.
* **Operadores Bitwise:** Aprendí que los operadores a nivel de bits (`&`, `|`, `^`, `~`, `<<`, `>>`) operan sobre la representación binaria de números enteros.

---

### 2. ⚠️ Tropezones, errores y cómo los solucioné
* **Escape de Comillas en f-strings:**
  * *Error:* Al probar el operador de pertenencia escribí `f"{cadena_texto in "Hola"}"`, cruzando comillas dobles externas con internas y rompiendo la sintaxis.
  * *Solución:* Aprendí a alternar comillas dobles en el exterior y comillas simples en el interior (o viceversa) para no confundir al intérprete: `f"{'Hola' in cadena_texto}"`.
* **Sintaxis de Pertenencia (`in`):**
  * *Error:* Inicialmente busqué la variable dentro de la cadena literal en lugar de buscar el elemento dentro de la variable.
  * *Solución:* Reorganicé la expresión colocando primero el elemento que se busca y después la secuencia donde se buscará: `busqueda in contenedor`.