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

---

# Métodos de Cadenas (String Methods)

Métodos nativos para inspeccionar, transformar y validar texto:

* **`.strip()`:** Elimina los espacios en blanco sobrantes al inicio y al final de un texto. Ideal para detectar si un `input()` se envió en blanco (`if not texto.strip():`).
* **`.isdigit()`:** Evalúa si la cadena está compuesta **exclusivamente por dígitos numéricos**. Retorna `True` o `False`.
* **`.capitalize()`:** Retorna el texto convirtiendo la primera letra en mayúscula y el resto en minúsculas.
* **`.lower()` / `.upper()`:** Convierte todo el texto a minúsculas o mayúsculas, respectivamente.

---

# Control Avanzado de Bucle y Patrones de Interacción

## Control de Ejecución (`break` y `continue`)
* **`break`:** Interrumpe y rompe inmediatamente el bucle en el que está contenido, transfiriendo el control de ejecución a la línea posterior al bucle.
* **`continue`:** Salta el resto de las instrucciones de la vuelta actual y regresa de inmediato al inicio del bucle para evaluar la siguiente iteración.

## Patrones de Interacción y UX Defensiva

### 1. El Bucle Infinito de Validación (`while True`)
Estructura que fuerza al programa a solicitar un dato repetidamente hasta que el usuario ingrese un formato válido.

```python
while True:
    dato = input("Ingrese dato: ")
    if es_valido(dato):
        break  # Se rompe el bucle únicamente cuando el dato es correcto
    print("Dato inválido, intente de nuevo.")
```

---

# Control de Excepciones y Manejo de Errores

Mecanismo para prevenir que el programa colapse ante fallos en tiempo de ejecución (entradas de usuario inválidas, conexiones fallidas, operaciones matemáticas imposibles).

## La Estructura Defensiva (`try / except / else / finally`)

```python
try:
    # Código "peligroso" susceptible a fallar
    numero = int(input("Ingrese un número: "))
    resultado = 10 / numero
except ValueError:
    # Se ejecuta si el usuario ingresa texto en lugar de número
    print("Error: Debe ingresar un número entero válido.")
except ZeroDivisionError as error:
    # Captura la falla específica y guarda la explicación en la variable 'error'
    print(f"Error matemático: {error}")
else:
    # Opcional: Se ejecuta ÚNICAMENTE si NO hubo ningún error en el 'try'
    print(f"Operación exitosa. Resultado: {resultado}")
finally:
    # Opcional: Se ejecuta SIEMPRE, haya habido error o no (ideal para limpiar/cerrar recursos)
    print("Finalizando verificación de seguridad.")
```

---

# Funciones y Modularidad de Código

Permiten encapsular bloques de código reusables bajo un nombre específico para evitar duplicación de lógica (Principio DRY: *Don't Repeat Yourself*).

## Anatomía de una Función (`def`)

```python
def calcular_total(precio: float, impuesto: float = 0.18) -> float:
    # Código o lógica de procesamiento
    total = precio + (precio * impuesto)
    return total  # Entrega el valor operable a quien invocó la función
```

---

### 🛠️ Ajuste menor en "Patrones de Interacción y UX Defensiva":

Añade este segundo patrón debajo del `while True` que ya tienes:

### 2. Bucles Aislados por Campo (UX Profesional)
En lugar de pedir todos los datos en un solo `while`, se asigna un bucle `while True` **independiente para cada campo**. Esto evita que si el usuario comete un error en el segundo dato (ej. teléfono), tenga que volver a ingresar el primero (ej. nombre).

---

* **Comparación de desigualdad (`!=` vs `not ==`):** Para evaluar si dos valores son distintos, el estándar en Python es usar el operador de desigualdad `!=` en lugar de negar una igualdad con `not ==`.
  * *No idiomático:* `if not numero == 16:`
  * *Idiomático (PEP 8):* `if numero != 16:`

# Atajos
* **`ctr+k` luego `ctr+c` para comentar**
* **`ctr+k` luego `ctr+u` para descomentar**