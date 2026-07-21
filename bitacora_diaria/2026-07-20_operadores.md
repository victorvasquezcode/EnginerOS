#Bitácora de Aprendizaje - Lógica de Programación
## Concepto del día: [operadores]
### 1. ¿Que problema resuelve exactamente?
Manipulacion de Variables
Calculos matematicos
Evaluacion de condiciones logicas
Actualizacion en memoria y Busqueda
Verificacion dentro del codigo
Bitwise

### 2.¿Cuales son sus limites o cuando No debo usarlo?
* **Aritméticos:** Un `/` siempre devuelve un `float`, mientras que `//` realiza una división entera y devuelve un `int`.
* **Lógicos:** `and`, `or` y `not` trabajan mayormente con booleanos (`True` y `False`).
* **Asignación:** Operadores como `+=` o `-=` solo se aplican a variables que ya fueron declaradas previamente con un valor inicial.
* **Identidad:** NO debo usar `is` para comparar números o texto por su valor (para eso es `==`). `is` solo se usa para corroborar si dos variables comparten la misma posición física en memoria RAM o si una variable está vacía (`None`).
* **Salida por consola:** En `print()`, al separar texto y variables con comas `,`, Python agrega un espacio automáticamente; no hace falta agregarlo manualmente en el texto.
* **Flujo:** La declaración de la variable debe ir **antes** de llamar a `print()`.
* No debo usar operadores de bits en operaciones logicas
* El operador `~` da numeros negativos

### 3. Explicación simple(Técnica Feyman):
* Los operadores son las acciones o verbos del código.
* El operador `in` funciona como un `Ctrl + F` (o buscador): escanea un texto para ver si existe una letra o palabra clave dentro de él.
* `in` es estricto y distingue entre mayúsculas y minúsculas (case-sensitive).
* Los bits son representaciones de apagado (`0`) y encendido (`1`)

### 4. ¿Como lo rompi y que error dio?
* Intenté hacer un `not` comparando dos números directamente (`30 not 20`) y dio `SyntaxError`.
* Intenté hacer `b += a` sin declarar la variable `b` primero y me salió `NameError: name 'b' is not defined`.
* Al colocar `print()` por encima de la variable declarada, dio error porque Python lee de arriba a abajo y no encuentra la variable.
* Usé `is` con números directos (`20 is 40`) y Python arrojó un `SyntaxWarning` recomendando usar `==`.
* Olvidé poner la coma en un `print()` al separar texto y variable, dando un error de sintaxis.
* Invertí el orden al usar `in` (`apellido in "Vasquez"` en lugar de `"Vas" in apellido`). El estándar es poner primero la subcadena que buscas y luego la variable principal.