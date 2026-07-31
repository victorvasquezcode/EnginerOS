# Glosario de Conceptos Generales de Software

* **REFACTORIZACIÓN:** Proceso de modificar el código existente para hacerlo más limpio, eficiente o legible sin alterar su comportamiento o funcionalidad externa.
* **MODULARIZAR:** Dividir un programa complejo en partes pequeñas, independientes y reutilizables (módulos o funciones) para facilitar su mantenimiento.

---

# Glosario de Tipos de Datos en Python

* **String (`str`):** Cadena de texto plano delimitada entre comillas (`"hola"` o `'hola'`).
* **Integer (`int`):** Números enteros, ya sean positivos o negativos (`10`, `-5`).
* **Float (`float`):** Números con punto decimal (`3.14`, `-0.5`).
* **Boolean (`bool`):** Valores lógicos de verdad: solo pueden ser `True` o `False` (siempre con la primera letra en mayúscula).

---

# Sintaxis y Conceptos Generales

## Formato y Salida de Texto
* **Salto de línea (`\n`):** Carácter de escape especial que inserta una nueva línea dentro de un string.
* **Separación con coma en `print()`:** Permite imprimir múltiples variables y textos. Python agrega automáticamente un espacio entre cada elemento.
* **f-Strings (Formato de Cadenas):** Cadenas antepuestas por `f` (ej. `f"Hola {variable}"`) que permiten incrustar expresiones y variables directamente entre llaves.
* **Mapeo / Personalización de Respuestas:** Uso de diccionarios `{True: "Mensaje True", False: "Mensaje False"}` para traducir evaluadores booleanos a texto personalizado sin necesidad de condicionales.

---

# Tipos de Operadores

* **Operadores de Asignación Abreviada (`+=`, `-=`, `*=`, `/=`):** Modifican el valor de una variable aplicando una operación sobre sí misma. Requieren que la variable haya sido declarada previamente.
* **Operadores Lógicos (`and`, `or`, `not`):**
  * `and`: Devuelve `True` solo si **ambas** condiciones son verdaderas.
  * `or`: Devuelve `True` si **al menos una** condición es verdadera.
  * `not`: Invierte el valor lógico (`True` se vuelve `False` y viceversa).
* **Operadores de Pertenencia (`in`, `not in`):**
  * `in`: Busca si un elemento o subcadena existe dentro de una secuencia (string, lista, tupla). Es sensible a mayúsculas/minúsculas.
  * `not in`: Verifica que un elemento NO exista dentro de la secuencia.
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
* **`else`:** Es el camino de respaldo; se ejecuta únicamente cuando ninguna condición anterior se cumplió.

### Reglas de Sintaxis y Buenas Prácticas (PEP 8)
1. **Sin paréntesis:** En Python no se encierran las condiciones entre paréntesis `()`.
   * *Correcto:* `if edad >= 18:`
   * *Incorrecto:* `if (edad >= 18):`
2. **Uso de operadores lógicos:** Utilizar siempre `and` / `or` dentro del `if`, nunca operadores bitwise (`&` / `|`).
3. **Encadenamiento de rangos:** Se pueden simplificar rangos de manera matemática:
   * `if 16 <= edad < 18:` (equivale a `16 <= edad and edad < 18`).
4. **Prioridad de evaluación:** En cadenas `if/elif`, las condiciones compuestas o más restrictivas (ej. `múltiplo de 3 y 5`) deben evaluarse **primero** que las condiciones simples.

---

## Bucles de Iteración (`for`)
Permiten ejecutar un bloque de código de forma repetitiva para cada elemento de una secuencia o rango.

* **Sintaxis básica:** `for variable in secuencia:`
* **Iteración sobre cadenas de texto (Strings):** Recorre el texto carácter por carácter (`for letra in "Texto":`).
* **Desempaquetado de Variables (Unpacking):** Permite asignar múltiples variables en cada vuelta si el elemento recorrido contiene sub-elementos agrupados (ej. `for clave, valor in diccionario.items():`).

### La Función `range(inicio, fin, paso)`
Genera una secuencia de números enteros. El valor de `fin` nunca se incluye en el resultado.

* `range(8)` $\rightarrow$ Genera del `0` al `7` (8 elementos en total).
* `range(1, 10)` $\rightarrow$ Genera del `1` al `9` (especifica inicio y fin).
* `range(1, 10, 2)` $\rightarrow$ Genera `1, 3, 5, 7, 9` (el tercer parámetro indica el incremento o paso).

## Bucle Indefinido (`while`)
Ejecuta un bloque de código repetidamente **mientras** una condición lógica devuelva `True`.

```python
contador = 0
while contador < 5:
    contador += 1
    print(contador)
```

---

# Estructuras de Datos

Python cuenta con cuatro tipos de datos integrados para almacenar colecciones de elementos:

## 1. Listas (`list`)
Colecciones mutables, ordenadas y que permiten elementos duplicados.
* **Creación:** `frutas = ["manzana", "pera"]`
* **Inserción:** `lista.append("uva")` (al final) | `lista.insert(1, "platano")` (en índice)
* **Borrado:** `lista.remove("pera")` (por valor) | `lista.pop(0)` (por índice, retorna valor)
* **Ordenación:** `lista.sort()` (modifica original) | `sorted(lista)` (retorna copia ordenada)

## 2. Tuplas (`tuple`)
Colecciones inmutables, ordenadas y que permiten elementos duplicados. Ideal para proteger datos.
* **Creación:** `coordenadas = (10, 20)`
* **Inmutabilidad:** Intentar `tupla[0] = 5` lanza un `TypeError`.
* **Desempaquetado (Unpacking):** `x, y = coordenadas`

## 3. Diccionarios (`dict`)
Colecciones mutables, estructuradas mediante pares `Clave: Valor`. Las claves deben ser únicas.
* **Creación:** `perfil = {"nombre": "Victor", "edad": 26}`
* **Inserción / Actualización:** `perfil["cargo"] = "Admin"`
* **Borrado:** `perfil.pop("edad")` o `del perfil["edad"]`
* **Métodos de Iteración:**
  * `perfil.keys()` $\rightarrow$ Retorna solo las claves.
  * `perfil.values()` $\rightarrow$ Retorna solo los valores.
  * `perfil.items()` $\rightarrow$ Retorna tuplas `(clave, valor)` para desempaquetar en bucles `for`.

## 4. Conjuntos (`set`)
Colecciones mutables, no ordenadas y de elementos únicos (filtra duplicados automáticamente).
* **Creación:** `numeros = {1, 2, 2, 3}` $\rightarrow$ Resultado: `{1, 2, 3}`
* **Inserción:** `conjunto.add(5)`
* **Borrado:** `conjunto.remove(2)` (lanza error si no existe) | `conjunto.discard(2)` (seguro)
* **Eliminación de duplicados en listas:** `lista_limpia = list(set(lista_con_duplicados))`