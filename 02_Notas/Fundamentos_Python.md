# Glosario de Conceptos Generales de Software

* **REFACTORIZACIÓN:** Cuando el código funciona, pero se modifica para hacerlo más limpio, eficiente o legible sin cambiar su comportamiento.
* **MODULARIZAR:** Dividir un código complejo en partes pequeñas e independientes que se puedan reutilizar en distintas ocasiones.

---

# Glosario de Tipos de Datos en Python

* **String (str):** Texto plano delimitado entre comillas (`"hola"` o `'hola'`).
* **Integer (int):** Números enteros, ya sean positivos o negativos (`10`, `-5`).
* **Float (float):** Números con punto decimal (`3.14`, `-0.5`).
* **Boolean (bool):** Valores lógicos de verdad: solo pueden ser `True` o `False` (siempre con la primera letra en mayúscula).

---

# Sintaxis y Conceptos Generales

## Formato y Salida de Texto
* **Salto de línea (`\n`):** Carácter especial que inserta un salto de línea dentro de un string.
* **Separación con coma en `print()`:** Permite imprimir múltiples variables y textos. Python agrega automáticamente un espacio entre cada elemento.
* **Mapeo / Personalización de Respuestas:** Uso de diccionarios `{True: "Mensaje si sale True", False: "Mensaje si sale False"}` para traducir evaluadores booleanos a texto personalizado sin necesidad de condicionales.

---

# Tipos de Operadores

* **Operadores de Asignación Abreviada (`+=`, `-=`, `*=`, `/=`):** Modifican el valor de una variable existente aplicando una operación sobre sí misma. Requieren que la variable haya sido declarada previamente.
* **Operadores Lógicos (`and`, `or`, `not`):**
  * `and`: Devuelve `True` solo si **ambas** condiciones son verdaderas.
  * `or`: Devuelve `True` si **al menos una** condición es verdadera.
  * `not`: Invierte el valor lógico (`True` se vuelve `False` y viceversa).
* **Operadores de Pertenencia (`in`, `not in`):**
  * `in`: Busca si una subcadena o elemento existe dentro de un string o lista (es sensible a mayúsculas/minúsculas).
  * `not in`: Verifica que un elemento NO exista dentro del string o lista.
* **Operadores de Identidad (`is`, `is not`):** Evalúan si dos variables apuntan exactamente a la misma posición en la memoria RAM o si una variable es `None`. No deben usarse para comparar valores numéricos o texto (para eso se usa `==`).
* **Operadores a Nivel de Bits (Bitwise):**
  * `<<` (Izquierda): Desplaza bits a la izquierda (multiplica el número por 2).
  * `>>` (Derecha): Desplaza bits a la derecha (divide el número entre 2 de forma entera).
  * `&` (AND): Devuelve `1` solo si ambos bits son `1`.
  * `|` (OR): Devuelve `1` si al menos uno de los bits es `1`.
  * `^` (XOR): Devuelve `1` si los bits comparados son diferentes.
  * `~` (NOT): Invierte los bits (fórmula en decimal: `-(n + 1)`).

---

# Estructuras de Control de Flujo

## Condicionales (`if`, `elif`, `else`)
Evalúan expresiones booleanas para decidir qué bloque de código ejecutar.

* **`if`:** Evalúa la primera condición. Si es `True`, ejecuta su bloque identado.
* **`elif` (Else If):** Evalúa una nueva condición únicamente si las condiciones anteriores resultaron `False`. Se pueden usar múltiples `elif`.
* **`else`:** Es el camino de respaldo; se ejecuta cuando ninguna condición anterior se cumplió.

### Reglas de Sintaxis y Buenas Prácticas (PEP 8)
1. **Sin paréntesis:** En Python no se encierran las condiciones entre paréntesis `()`.
   * *Correcto:* `if edad >= 18:`
   * *Incorrecto:* `if (edad >= 18):`
2. **Uso de operadores lógicos:** Utilizar siempre `and` / `or` dentro del `if`, nunca operadores bitwise (`&` / `|`).
3. **Encadenamiento de rangos:** Se pueden simplificar rangos de manera matemática:
   * `if 16 <= edad < 18:` (equivale a `16 <= edad and edad < 18`).

---

## Bucles de Iteración (`for`)
Permiten ejecutar un bloque de código de forma repetitiva para cada elemento de una secuencia o rango.

* **Sintaxis básica:** `for variable in secuencia:`
* **Iteración sobre cadenas de texto (Strings):** Recorre el texto carácter por carácter (`for letra in "Texto":`).

### La Función `range(inicio, fin, paso)`
Genera una secuencia de números enteros. El valor de `fin` nunca se incluye en el resultado.

* `range(8)` $\rightarrow$ Genera del `0` al `7` (8 elementos en total).
* `range(1, 10)` $\rightarrow$ Genera del `1` al `9` (especifica inicio y fin).
* `range(1, 10, 2)` $\rightarrow$ Genera `1, 3, 5, 7, 9` (el tercer parámetro indica el incremento o paso).