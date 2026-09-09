# 🐍 Glosario y Guía de Fundamentos de Python

> **Propósito:** *reunir los conceptos aprendidos en una referencia única, ordenada y fácil de consultar.*
>
> **Criterio:** *cada tema sigue, cuando corresponde, este orden:* **qué es → sintaxis → ejemplo → idea clave**.

---

## 📚 Índice

1. [Conceptos generales de software](#1-conceptos-generales-de-software)

2. [Tipos de datos básicos](#2-tipos-de-datos-básicos)

3. [Sintaxis y salida de texto](#3-sintaxis-y-salida-de-texto)

4. [Operadores](#4-operadores)

5. [Estructuras de control de flujo](#5-estructuras-de-control-de-flujo)

6. [Estructuras de datos](#6-estructuras-de-datos)

7. [Métodos de cadenas](#7-métodos-de-cadenas)

8. [Control de bucles](#8-control-de-bucles)

9. [Validación y UX defensiva](#9-validación-y-ux-defensiva)

10. [Manejo de excepciones](#10-manejo-de-excepciones)

11. [Funciones y modularidad](#11-funciones-y-modularidad)

12. [Buenas prácticas de diseño](#12-buenas-prácticas-de-diseño)

13. [Variables, objetos y mutabilidad](#13-variables-objetos-y-mutabilidad)

14. [Desempaquetado e intercambio de variables](#14-desempaquetado-e-intercambio-de-variables)

15. [Recursividad](#15-recursividad)

16. [Pilas y colas](#16-pilas-y-colas)

17. [Programación orientada a objetos](#17-programación-orientada-a-objetos)

18. [Herencia y polimorfismo](#18-herencia-y-polimorfismo)

19. [Manejo de archivos JSON y XML](#19-manejo-de-archivos-json-y-xml)

20. [Pruebas unitarias](#20-pruebas-unitarias)

21. [Atajos de teclado](#21-atajos-de-teclado)

22. [Chuleta rápida](#22-chuleta-rápida)

23. [Mapa mental de lo aprendido](#23-mapa-mental-de-lo-aprendido)

---

# 1. Conceptos generales de software

## Refactorización

La **refactorización** consiste en modificar la estructura interna del código para hacerlo más limpio, legible, mantenible o eficiente **sin cambiar su comportamiento observable**.

**Idea clave:** mejorar cómo está construido el programa sin cambiar lo que hace.

## Modularización

**Modularizar** significa dividir un programa complejo en partes pequeñas y reutilizables, como funciones, módulos o clases.

**Beneficios principales:**

- Menor duplicación de código.

- Mantenimiento más sencillo.

- Mejor organización.

- Reutilización de lógica.

- Pruebas más fáciles.

---

# 2. Tipos de datos básicos

Python proporciona distintos tipos para representar información.

| Tipo | Ejemplo | Descripción |

|---|---|---|

| *`str`* | *`"hola"`* | Texto |

| *`int`* | *`10`*, *`-5`* | Número entero |

| *`float`* | *`3.14`*, *`-0.5`* | Número decimal |

| *`bool`* | *`True`*, *`False`* | Valor lógico |

## *`str`* — String

Cadena de texto delimitada normalmente por comillas simples o dobles.

```python

nombre = "Víctor"

mensaje = 'Hola'

```

## *`int`* — Integer

Números enteros positivos, negativos o cero.

```python

edad = 26

saldo = -5

```

## *`float`* — Float

Números que representan valores decimales.

```python

precio = 3.14

peso = 95.5

```

## *`bool`* — Boolean

Solo admite dos valores:

```python

True

False

```

Se utiliza principalmente para representar resultados lógicos y condiciones.

---

# 3. Sintaxis y salida de texto

## 3.1 Salto de línea: *`\n`*

Es un carácter especial que introduce una nueva línea dentro de un string.

```python

print("Hola\nVíctor")

```

Resultado:

```text

Hola

Víctor

```

## 3.2 *`print()`* con varios argumentos

*`print()`* puede recibir varios valores separados por comas.

```python

nombre = "Víctor"

edad = 26

print(nombre, edad)

```

Python separa automáticamente los argumentos con un espacio, salvo que se especifique otro separador mediante *`sep`*.

## 3.3 f-Strings

Permiten insertar variables y expresiones directamente dentro de una cadena.

```python

nombre = "Víctor"

edad = 26

print(f"Mi nombre es {nombre} y tengo {edad} años.")

```

**Idea clave:** cuando necesitas construir texto con variables, las f-Strings suelen ser la opción más clara.

## 3.4 Mapeo de valores booleanos a mensajes

Un diccionario puede utilizarse para traducir un resultado booleano a un texto personalizado.

```python

mensajes = {

    True: "Operación correcta",

    False: "Operación incorrecta"

}

resultado = True

print(mensajes[resultado])

```

Esto puede ser útil cuando existen pocos estados conocidos y no se necesita un *`if/else`* completo.

---

# 4. Operadores

## 4.1 Asignación abreviada

Permiten modificar una variable utilizando su valor actual.

| Operador | Equivale a |

|---|---|

| *`+=`* | *`x = x + valor`* |

| *`-=`* | *`x = x - valor`* |

| *`*=`* | *`x = x * valor`* |

| *`/=`* | *`x = x / valor`* |

Ejemplo:

```python

contador = 5

contador += 1

print(contador)  # 6*

```

La variable debe existir antes de aplicar estas operaciones.

## 4.2 Operadores lógicos

### *`and`*

Devuelve *`True`* solamente cuando **todas** las condiciones son verdaderas.

```python

edad >= 18 and tiene_documento

```

### *`or`*

Devuelve *`True`* cuando **al menos una** condición es verdadera.

```python

es_admin or es_supervisor

```

### *`not`*

Invierte un valor booleano.

```python

not True   # False*

not False  # True*

```

## 4.3 Operadores de pertenencia

### *`in`*

Comprueba si un elemento o subcadena existe dentro de una colección o secuencia.

```python

"a" in "casa"       # True*

3 in [1, 2, 3]       # True*

```

En strings la comparación distingue mayúsculas y minúsculas.

### *`not in`*

Comprueba que un elemento **no** pertenezca a una colección o secuencia.

```python

"z" not in "casa"   # True*

```

## 4.4 Operadores de identidad

### *`is`* / *`is not`*

Comprueban identidad de objeto, no igualdad de valor.

Su uso más habitual en código cotidiano es comparar con *`None`*:

```python

resultado is None

resultado is not None

```

Para comparar valores se utiliza normalmente *`==`* o *`!=`*.

```python

nombre == "Víctor"

numero != 16

```

> **Regla práctica:** *`is` → identidad. `==` → igualdad de valores.*

## 4.5 Operadores a nivel de bits

Estos operadores trabajan sobre la representación binaria de los enteros.

| Operador | Función |

|---|---|

| *`<<`* | Desplazamiento de bits a la izquierda |

| *`>>`* | Desplazamiento de bits a la derecha |

| *`&`* | AND bit a bit |

| *`|`* | OR bit a bit |

| *`^`* | XOR bit a bit |

| *`~`* | NOT bit a bit |

Ejemplos conceptuales:

```python

8 << 1   # 16*

8 >> 1   # 4*

```

> **Importante:** *no confundir operadores bitwise (`&`, `|`) con operadores lógicos (`and`, `or`).*

---

# 5. Estructuras de control de flujo

## 5.1 Condicionales: *`if`*, *`elif`*, *`else`*

Permiten decidir qué bloque de código se ejecuta según una condición.

```python

if edad >= 18:

    print("Mayor de edad")

elif edad >= 16:

    print("Menor de edad, pero dentro del segundo rango")

else:

    print("Menor de edad")

```

### *`if`*

Evalúa la primera condición.

### *`elif`*

Evalúa otra condición solamente cuando las anteriores fueron *`False`*.

### *`else`*

Se ejecuta cuando ninguna condición anterior se cumple.

## 5.2 Buenas prácticas para condiciones

### Evitar paréntesis innecesarios

```python

if edad >= 18:

    print("Puede ingresar")

```

Los paréntesis pueden utilizarse cuando aportan claridad a una expresión compleja, pero no son necesarios para la sintaxis básica de *`if`*.

### Utilizar operadores apropiados

Para condiciones lógicas utiliza:

```python

and

or

not

```

No los sustituyas por sus equivalentes bitwise en expresiones booleanas comunes.

### Encadenamiento de comparaciones

Python permite escribir rangos de forma natural:

```python

if 16 <= edad < 18:

    print("Dentro del rango")

```

Equivale conceptualmente a:

```python

if 16 <= edad and edad < 18:

    print("Dentro del rango")

```

### Orden de las condiciones

En una cadena *`if/elif`*, evalúa primero las condiciones más específicas cuando unas condiciones puedan incluir a otras.

Ejemplo:

```python

if numero % 3 == 0 and numero % 5 == 0:

    print("Múltiplo de 3 y 5")

elif numero % 3 == 0:

    print("Múltiplo de 3")

elif numero % 5 == 0:

    print("Múltiplo de 5")

```

---

## 5.3 Bucle *`for`*

*`for`* permite recorrer los elementos de una secuencia o rango.

```python

for letra in "Python":

    print(letra)

```

## Desempaquetado durante un *`for`*

Cuando cada elemento contiene varios valores, pueden asignarse directamente a variables.

```python

perfil = {

    "nombre": "Víctor",

    "edad": 26

}

for clave, valor in perfil.items():

    print(clave, valor)

```

## *`range(inicio, fin, paso)`*

Genera una secuencia de números enteros. El valor de *`fin`* **no se incluye**.

```python

range(8)

```

Genera conceptualmente:

```text

0 1 2 3 4 5 6 7

```

```python

range(1, 10)

```

Genera:

```text

1 2 3 4 5 6 7 8 9

```

Con un paso:

```python

range(1, 10, 2)

```

Genera:

```text

1 3 5 7 9

```

---

## 5.4 Bucle *`while`*

*`while`* repite un bloque mientras una condición sea *`True`*.

```python

contador = 0

while contador < 5:

    contador += 1

    print(contador)

```

### Idea clave

*`for`* suele utilizarse cuando sabes qué colección o rango vas a recorrer.

*`while`* suele utilizarse cuando la repetición depende de una condición y no sabes de antemano cuántas iteraciones serán necesarias.

---

# 6. Estructuras de datos

Python incluye varias estructuras fundamentales para almacenar colecciones.

| Estructura | Orden | Mutable | Duplicados | Acceso principal |

|---|---|---|---|---|

| *`list`* | Sí | Sí | Sí | Índice |

| *`tuple`* | Sí | No | Sí | Índice |

| *`dict`* | Mantiene orden de inserción | Sí | Claves únicas | Clave |

| *`set`* | No indexado | Sí | No | Pertenencia |

*> La tabla resume el uso conceptual. Cada estructura tiene características y casos de uso más amplios.*

---

## 6.1 Listas — *`list`*

Colecciones ordenadas, mutables y que permiten elementos duplicados.

### Crear

```python

frutas = ["manzana", "pera"]

```

### Insertar

```python

frutas.append("uva")

frutas.insert(1, "plátano")

```

- *`append()`* → agrega al final.

- *`insert()`* → agrega en el índice indicado.

### Eliminar

```python

frutas.remove("pera")

fruta = frutas.pop(0)

```

- *`remove(valor)`* → elimina por valor.

- *`pop(indice)`* → elimina por posición y **devuelve** el elemento eliminado.

### Ordenar

```python

lista.sort()

```

Modifica la lista original.

```python

nueva_lista = sorted(lista)

```

Devuelve una nueva lista ordenada.

---

## 6.2 Tuplas — *`tuple`*

Colecciones ordenadas e inmutables que permiten elementos duplicados.

### Crear

```python

coordenadas = (10, 20)

```

### Inmutabilidad

No puedes modificar directamente uno de sus elementos:

```python

coordenadas[0] = 5

```

Esto produce *`TypeError`*.

### Desempaquetado

```python

x, y = coordenadas

```

---

## 6.3 Diccionarios — *`dict`*

Almacenan información mediante pares *`clave: valor`*.

```python

perfil = {

    "nombre": "Víctor",

    "edad": 26

}

```

Las claves deben ser únicas.

### Insertar o actualizar

```python

perfil["cargo"] = "Admin"

```

Si la clave existe, se actualiza. Si no existe, se crea.

### Eliminar

```python

perfil.pop("edad")

del perfil["edad"]

```

### Recorrer un diccionario

```python

perfil.keys()

```

Obtiene las claves.

```python

perfil.values()

```

Obtiene los valores.

```python

perfil.items()

```

Obtiene pares *`(clave, valor)`*.

Ejemplo:

```python

for clave, valor in perfil.items():

    print(clave, valor)

```

---

## 6.4 Conjuntos — *`set`*

Colecciones de elementos únicos. Son útiles para eliminar duplicados y realizar operaciones de conjuntos.

### Crear

```python

numeros = {1, 2, 2, 3}

```

El conjunto resultante contiene conceptualmente:

```text

{1, 2, 3}

```

### Insertar

```python

numeros.add(5)

```

### Eliminar

```python

numeros.remove(2)

```

*`remove()`* produce un error si el elemento no existe.

```python

numeros.discard(2)

```

*`discard()`* no produce error si el elemento no existe.

### Eliminar duplicados de una lista

```python

lista_limpia = list(set(lista_con_duplicados))

```

> **Advertencia:** *convertir una lista a `set` no conserva necesariamente el orden original. Usa otra estrategia cuando el orden sea importante.*

---

# 7. Métodos de cadenas

Los strings tienen numerosos métodos para validar, limpiar y transformar texto.

## 7.1 *`.strip()`*

Elimina espacios en blanco al principio y al final.

```python

texto = "   hola   "

print(texto.strip())

```

Muy útil para validar *`input()`*:

```python

if not texto.strip():

    print("El campo no puede estar vacío")

```

## 7.2 *`.isdigit()`*

Devuelve *`True`* si todos los caracteres de la cadena son dígitos según las reglas del método.

```python

"12345".isdigit()  # True*

"12a45".isdigit()  # False*

```

## 7.3 *`.capitalize()`*

Convierte la primera letra de la cadena en mayúscula y el resto a minúsculas.

```python

"vÍCTOR".capitalize()

```

## 7.4 *`.lower()`* y *`.upper()`*

```python

texto.lower()

texto.upper()

```

Convierten el texto a minúsculas o mayúsculas.

## 7.5 *`.title()`*

Convierte a mayúscula inicial cada palabra.

```python

"hola mundo".title()

# "Hola Mundo"*

```

### Diferencia importante

```text

capitalize() → primera letra de toda la cadena

 title()     → primera letra de cada palabra

```

## 7.6 *`.replace(viejo, nuevo)`*

Reemplaza una subcadena por otra.

```python

texto = "hola mundo"

texto = texto.replace(" ", "-")

```

Resultado:

```text

hola-mundo

```

A diferencia de *`strip()`*, *`replace()`* puede modificar caracteres que se encuentran en medio del texto.

## 7.7 *`.split(separador)`*

Divide una cadena y devuelve una lista.

```python

"a,b,c".split(",")

```

Resultado:

```python

['a', 'b', 'c']

```

## 7.8 *`.join(iterable)`*

Une varios strings utilizando como separador el string sobre el que se llama.

```python

lista = ["a", "b", "c"]

resultado = ", ".join(lista)

```

Resultado:

```text

a, b, c

```

## 7.9 *`.startswith()`* y *`.endswith()`*

Comprueban el inicio o final de una cadena.

```python

nombre.startswith("Vi")

nombre.endswith("z")

```

Devuelven *`True`* o *`False`*.

## 7.10 *`.isalpha()`*

Comprueba si todos los caracteres de la cadena son letras.

```python

"Hola".isalpha()      # True*

"Hola Mundo".isalpha()  # False*

"Hola123".isalpha()   # False*

```

Los espacios y números hacen que el resultado sea *`False`*.

## 7.11 Slicing

Permite extraer partes de una secuencia.

```python

texto[inicio\:fin\:paso]

```

### Invertir una cadena

```python

cadena[::-1]

```

Ejemplo:

```python

palabra = "radar"

invertida = palabra[::-1]

```

Esto puede utilizarse como parte de una solución para comprobar palíndromos.

---

# 8. Control de bucles

## 8.1 *`break`*

Interrumpe inmediatamente el bucle actual.

```python

while True:

    dato = input("Dato: ")

    if dato == "salir":

        break

```

La ejecución continúa después del bucle.

## 8.2 *`continue`*

Salta el resto de la iteración actual y pasa a la siguiente iteración.

```python

for numero in range(10):

    if numero % 2 == 0:

        continue

    print(numero)

```

Aquí se imprimen los números impares.

---

# 9. Validación y UX defensiva

La validación evita que el programa continúe con datos incorrectos.

## 9.1 Patrón *`while True`* + validación + *`break`*

Este patrón permite insistir hasta obtener un dato válido.

```python

while True:

    dato = input("Ingrese dato: ")

    if es_valido(dato):

        break

    print("Dato inválido. Intente nuevamente.")

```

### Flujo mental

```text

Pedir dato

   ↓

¿Es válido?

   ├── Sí → break → continuar

   └── No → mostrar error → volver a pedir

```

## 9.2 Bucles aislados por campo

Cuando un formulario tiene varios datos, puede utilizarse un *`while True`* independiente para cada campo.

Esto evita que, si el usuario comete un error en un campo posterior, tenga que volver a ingresar los datos anteriores.

Ejemplo conceptual:

```python

while True:

    nombre = input("Nombre: ")

    if nombre.strip():

        break

    print("El nombre no puede estar vacío.")

while True:

    telefono = input("Teléfono: ")

    if telefono.isdigit() and len(telefono) <= 11:

        break

    print("Teléfono inválido.")

```

### Idea clave

**Un campo → una validación → un estado válido.**

Esto hace que la interacción sea más resistente a errores y más cómoda para el usuario.

---

# 10. Manejo de excepciones

Las excepciones permiten gestionar errores que ocurren durante la ejecución sin dejar que el programa termine de forma inesperada.

## 10.1 *`try / except / else / finally`*

```python

try:

    numero = int(input("Ingrese un número: "))

    resultado = 10 / numero

except ValueError:

    print("Error: debe ingresar un número entero válido.")

except ZeroDivisionError as error:

    print(f"Error matemático: {error}")

else:

    print(f"Operación exitosa. Resultado: {resultado}")

finally:

    print("Finalizando verificación.")

```

## *`try`*

Contiene el código que puede producir una excepción.

## *`except`*

Captura y gestiona una excepción concreta.

```python

except ValueError:

    ...

```

También puedes conservar la excepción en una variable:

```python

except ZeroDivisionError as error:

    print(error)

```

## *`else`*

Se ejecuta únicamente cuando el bloque *`try`* termina sin lanzar una excepción.

## *`finally`*

Se ejecuta siempre, haya ocurrido un error o no. Es especialmente útil para tareas de limpieza o liberación de recursos.

### Regla práctica

Captura excepciones **específicas** cuando conozcas qué errores esperas manejar.

---

# 11. Funciones y modularidad

Una función encapsula una tarea concreta bajo un nombre reutilizable.

Esto ayuda a reducir duplicación de código y facilita la organización.

## 11.1 Anatomía básica de una función

```python

def calcular_total(precio: float, impuesto: float = 0.18) -> float:

    total = precio + (precio * impuesto)

    return total

```

### Partes principales

| Elemento | Función |

|---|---|

| *`def`* | Declara la función |

| *`calcular_total`* | Nombre de la función |

| *`precio`* | Parámetro |

| *`float`* | Anotación de tipo |

| *`impuesto = 0.18`* | Valor por defecto |

| *`-> float`* | Tipo esperado del retorno |

| *`return`* | Devuelve el resultado |

### Principio DRY

**DRY — Don't Repeat Yourself** significa evitar duplicar la misma lógica en diferentes lugares.

*> Una buena función debería tener una responsabilidad clara y reutilizable.*

---

# 12. Buenas prácticas de diseño

## 12.1 Comparar desigualdad

Para comprobar que dos valores son diferentes, utiliza *`!=`*.

```python

if numero != 16:

    print("Es diferente")

```

Aunque *`not numero == 16`* puede expresar una negación, *`!=`* es más directo y legible.

## 12.2 Encadenamiento de métodos

El **method chaining** consiste en aplicar varios métodos consecutivamente.

```python

texto.strip().lower()

```

El resultado de un método se convierte en la entrada del siguiente.

## 12.3 Diseño defensivo en funciones

Una función puede normalizar sus entradas para reducir errores y hacer explícito qué formato espera.

```python

def normalizar_nombre(nombre: str) -> str:

    return nombre.strip().lower()

```

Esto evita depender por completo de que el código externo ya haya limpiado el dato.

## 12.4 Técnica del flag

Un **flag** es una variable, normalmente booleana, utilizada para recordar un estado mientras se recorre una colección o se ejecuta un proceso.

```python

encontrado = False

for numero in numeros:

    if numero == objetivo:

        encontrado = True

        break

if encontrado:

    print("Encontrado")

else:

    print("No encontrado")

```

### Idea clave

El flag permite guardar una decisión tomada durante el recorrido para utilizarla posteriormente.

---

# 13. Variables, objetos y mutabilidad

> **Nota conceptual:** *en Python es más preciso pensar en que las variables son nombres que hacen referencia a objetos. Al pasar un objeto a una función, se comparte esa referencia al objeto. El comportamiento observable depende de si el objeto es mutable o inmutable.*

## 13.1 Tipos inmutables

Entre los tipos inmutables habituales se encuentran:

```text

int

float

str

bool

tuple

```

Su contenido no puede modificarse después de crear el objeto.

Ejemplo:

```python

def cambiar(numero):

    numero = 100

valor = 10

cambiar(valor)

print(valor)  # 10*

```

La reasignación local no modifica el objeto original al que apuntaba *`valor`*.

### Para conservar un resultado

Se captura el valor devuelto:

```python

def cambiar(a, b):

    return a + 1, b + 1

nueva_a, nueva_b = cambiar(a, b)

```

## 13.2 Tipos mutables

Entre los tipos mutables habituales están:

```text

list

dict

set

```

Su contenido puede modificarse.

```python

def agregar_elemento(lista):

    lista.append(10)

numeros = [1, 2, 3]

agregar_elemento(numeros)

print(numeros)

# [1, 2, 3, 10]*

```

La función modificó el mismo objeto lista.

## 13.3 Reasignación vs. mutación

Estas dos operaciones no son equivalentes.

### Reasignar

```python

lista = [1, 2]

```

Hace que el nombre *`lista`* pase a apuntar a otro objeto.

### Mutar

```python

lista.append(3)

```

Modifica el contenido del objeto existente.

## 13.4 Copiar para evitar mutaciones externas

Si necesitas trabajar con una copia independiente de una lista:

```python

copia = lista.copy()

```

---

# 14. Desempaquetado e intercambio de variables

Python permite asignar varios valores en una sola instrucción.

## 14.1 Swap de variables

```python

a, b = b, a

```

Intercambia los valores sin necesidad de una variable temporal explícita.

## 14.2 Desempaquetado del retorno de una función

```python

def intercambiar(a, b):

    return b, a

nueva_a, nueva_b = intercambiar(var1, var2)

```

### Idea clave

El mismo mecanismo permite trabajar con tuplas y otros iterables de manera compacta.

---

# 15. Recursividad

La **recursividad** ocurre cuando una función se llama a sí misma para resolver un problema dividiéndolo en subproblemas del mismo tipo.

## 15.1 Los dos pilares

Una función recursiva necesita una estructura que permita detenerse.

### Caso base

Es la condición que detiene la recursión.

### Caso recursivo

Es la llamada a la misma función con un problema reducido o más cercano al caso base.

## 15.2 Pila de llamadas

Las llamadas recursivas se almacenan en la **call stack**.

### Descenso

Las llamadas se van acumulando hasta llegar al caso base.

### Ascenso

Una vez alcanzado el caso base, las llamadas pendientes se resuelven en sentido inverso.

## 15.3 Ejemplo: factorial

```python

def factorial(n: int) -> int:

# Caso base*

    if n <= 1:

        return 1

# Caso recursivo*

    return n * factorial(n - 1)

```

Flujo conceptual para *`factorial(4)`*:

```text

factorial(4)

    ↓

4 * factorial(3)

    ↓

4 * 3 * factorial(2)

    ↓

4 * 3 * 2 * factorial(1)

    ↓

4 * 3 * 2 * 1

    ↓

24

```

*> Una recursión mal definida puede provocar llamadas infinitas y terminar en `RecursionError`.*

---

# 16. Pilas y colas

Son estructuras lineales que establecen reglas específicas para insertar y extraer elementos.

## 16.1 Pila — Stack — LIFO

**LIFO: Last In, First Out**

El último elemento que entra es el primero que sale.

### Analogías

- Pila de platos.

- Historial de navegación.

- Operaciones de deshacer.

### Implementación sencilla con *`list`*

```python

pila = []

pila.append("A")

pila.append("B")

pila.append("C")

```

Extraer:

```python

elemento = pila.pop()

```

Resultado conceptual:

```text

entra: A → B → C

sale : C

```

---

## 16.2 Cola — Queue — FIFO

**FIFO: First In, First Out**

El primer elemento que entra es el primero que sale.

### Analogías

- Fila de un banco.

- Cola de impresión.

- Personas esperando atención.

### Implementación educativa con *`list`*

```python

cola = []

cola.append("A")

cola.append("B")

cola.append("C")

```

Extraer el primero:

```python

elemento = cola.pop(0)

```

### Nota de eficiencia

Para colas reales y operaciones frecuentes en ambos extremos, suele ser más apropiado utilizar *`collections.deque`*:

```python

from collections import deque

cola = deque()

cola.append("A")

cola.append("B")

elemento = cola.popleft()

```

---

## 16.3 *`pop()`* y asignación directa

*`pop()`* realiza dos acciones:

1. Elimina el elemento de la colección.

2. Devuelve el elemento eliminado.

Por eso puedes conservarlo:

```python

elemento_extraido = pila.pop()

```

---

# 17. Programación orientada a objetos

La **Programación Orientada a Objetos (POO)** organiza el código alrededor de objetos que combinan estado y comportamiento.

## 17.1 Conceptos fundamentales

### Clase

Plantilla o molde que define las características y comportamiento de un tipo de objeto.

### Objeto / instancia

Un elemento concreto creado a partir de una clase.

### Atributo

Dato asociado al estado de un objeto.

### Método

Función definida dentro de una clase que representa un comportamiento.

### *`self`*

Referencia al objeto actual en los métodos de instancia.

---

## 17.2 Anatomía de una clase

```python

class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self) -> None:
        print(f"Nombre: {self.nombre} | Edad: {self.edad}")

usuario = Persona("Víctor", 26)

usuario.mostrar_datos()

```

## 17.3 *`__init__`*

Es el inicializador que normalmente se ejecuta cuando se crea una instancia.

```python

usuario = Persona("Víctor", 26)

```

Durante la creación se ejecuta el inicializador definido en la clase.

---

# 18. Herencia y polimorfismo

La herencia permite crear clases especializadas a partir de otras clases.

## 18.1 Superclase y subclase

- **Superclase / clase padre:** define características generales.

- **Subclase / clase hija:** hereda y puede ampliar o especializar el comportamiento.

## 18.2 Ejemplo de herencia

```python

class Empleado:

    def __init__(self, id_empleado: int, nombre: str):

self.id_empleado = id_empleado

self.nombre = nombre

class Programador(Empleado):

    def __init__(self, id_empleado: int, nombre: str, lenguaje: str):

        super().__init__(id_empleado, nombre)

self.lenguaje = lenguaje

```

## 18.3 *`super()`*

Permite acceder a métodos de la clase padre desde la subclase.

En el ejemplo:

```python

super().__init__(id_empleado, nombre)

```

se ejecuta el inicializador de *`Empleado`* para reutilizar la lógica que crea *`id_empleado`* y *`nombre`*.

## 18.4 Polimorfismo

El **polimorfismo** permite que diferentes objetos respondan al mismo mensaje o llamada de acuerdo con su propia implementación.

Ejemplo conceptual:

```python

class Perro:

    def hablar(self):

        return "Guau"

class Gato:

    def hablar(self):

        return "Miau"

animales = [Perro(), Gato()]

for animal in animales:

    print(animal.hablar())

```

Ambos objetos responden a *`hablar()`*, pero cada uno produce un resultado diferente.

---

# 19. Manejo de archivos JSON y XML

Esta sección reúne dos formatos muy utilizados para **guardar, intercambiar y transportar datos estructurados** desde Python.

## 19.1 Conceptos clave

| Concepto | Significado |
|---|---|
| **JSON** | Formato ligero y estructurado basado en objetos (clave-valor) y listas. |
| **XML** | Formato estructurado mediante etiquetas anidadas. |
| **Serialización** | Convertir datos de Python a un formato que pueda almacenarse o transmitirse. |
| **Deserialización** | Reconstruir datos de Python a partir de un formato almacenado o recibido. |
| `json.dump()` | Escribe un objeto Python directamente en un archivo JSON. |
| `json.load()` | Lee un archivo JSON y reconstruye el objeto Python. |
| `ElementTree` | API de Python para crear y procesar documentos XML. |
| `os.remove()` | Elimina un archivo del sistema de archivos. |

### Idea clave

> **JSON/XML = datos en memoria ↔ formato estructurado en disco.**

---

## 19.2 JSON: creación, lectura y eliminación

### Enunciado

Crear un archivo `datos.json` con nombre, edad, fecha de nacimiento y lenguajes de programación; mostrar su contenido y eliminarlo al finalizar.

### Código

```python
import json
import os

ARCHIVO_JSON = "datos.json"

persona = {
    "nombre": "Victor",
    "edad": 18,
    "fecha_nacimiento": "28-06-2000",
    "lenguajes": ["Python", "JavaScript", "SQL"]
}

# 1. Serializar y guardar.
with open(ARCHIVO_JSON, "w", encoding="utf-8") as archivo:
    json.dump(persona, archivo, indent=4, ensure_ascii=False)

# 2. Leer y mostrar.
with open(ARCHIVO_JSON, "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print("--- Contenido de datos.json ---")
    print(contenido)

# 3. Eliminar.
if os.path.exists(ARCHIVO_JSON):
    os.remove(ARCHIVO_JSON)
    print("Archivo datos.json eliminado con éxito.")
```

### ¿Qué ocurre en cada paso?

1. `persona` contiene los datos en memoria como diccionario.
2. `json.dump()` convierte ese diccionario a JSON y lo escribe en disco.
3. `open(..., "r")` permite leer el archivo como texto.
4. `os.path.exists()` comprueba que el archivo exista antes de eliminarlo.
5. `os.remove()` elimina el archivo.

---

## 19.3 XML: creación, lectura y eliminación

### Estructura conceptual

```text
persona
├── nombre
├── edad
├── fecha_nacimiento
└── lenguajes
    ├── lenguaje
    ├── lenguaje
    └── lenguaje
```

### Código

```python
import os
import xml.etree.ElementTree as ET

ARCHIVO_XML = "datos.xml"

# 1. Crear el nodo raíz.
raiz = ET.Element("persona")

# 2. Crear nodos hijos.
ET.SubElement(raiz, "nombre").text = "Victor"
ET.SubElement(raiz, "edad").text = "18"
ET.SubElement(raiz, "fecha_nacimiento").text = "28-06-2000"

# 3. Crear el contenedor de lenguajes.
nodo_lenguajes = ET.SubElement(raiz, "lenguajes")

lenguajes = ["Python", "JavaScript", "SQL"]

for lenguaje in lenguajes:
    ET.SubElement(nodo_lenguajes, "lenguaje").text = lenguaje

# 4. Crear el árbol XML y guardarlo.
arbol = ET.ElementTree(raiz)
arbol.write(
    ARCHIVO_XML,
    encoding="utf-8",
    xml_declaration=True
)

# 5. Leer y mostrar.
with open(ARCHIVO_XML, "r", encoding="utf-8") as archivo:
    print("--- Contenido de datos.xml ---")
    print(archivo.read())

# 6. Eliminar.
if os.path.exists(ARCHIVO_XML):
    os.remove(ARCHIVO_XML)
    print("Archivo datos.xml eliminado con éxito.")
```

### Métodos importantes de XML

| Método / atributo | Uso |
|---|---|
| `ET.Element("persona")` | Crea el nodo raíz. |
| `ET.SubElement(...)` | Crea un nodo hijo. |
| `.text` | Define el texto contenido en un nodo. |
| `ET.ElementTree(raiz)` | Construye el árbol XML. |
| `.write(...)` | Guarda el árbol en un archivo. |
| `ET.parse(...)` | Lee y analiza un archivo XML. |
| `.getroot()` | Obtiene la raíz del documento. |
| `.find("nombre")` | Busca un nodo hijo. |

---

## 19.4 JSON y XML hacia una misma clase

Una aplicación importante de la serialización es poder obtener datos desde diferentes formatos y convertirlos a una misma estructura de Python.

### Clase `Persona`

```python
class Persona:
    def __init__(
        self,
        nombre: str,
        edad: int,
        fecha_nacimiento: str,
        lenguajes: list[str]
    ):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.lenguajes = lenguajes

    def mostrar_datos(self) -> None:
        lenguajes_str = ", ".join(self.lenguajes)
        print(
            f"Nombre: {self.nombre} | "
            f"Edad: {self.edad} | "
            f"Fecha de nacimiento: {self.fecha_nacimiento} | "
            f"Lenguajes: {lenguajes_str}"
        )
```

### Datos compartidos

```python
ARCHIVO_JSON = "datos.json"
ARCHIVO_XML = "datos.xml"

persona_data = {
    "nombre": "Victor",
    "edad": 18,
    "fecha_nacimiento": "28-06-2000",
    "lenguajes": ["Python", "JavaScript", "SQL"]
}
```

### Guardar JSON

```python
with open(ARCHIVO_JSON, "w", encoding="utf-8") as archivo:
    json.dump(persona_data, archivo, indent=4, ensure_ascii=False)
```

### Guardar XML

```python
raiz = ET.Element("persona")

ET.SubElement(raiz, "nombre").text = persona_data["nombre"]
ET.SubElement(raiz, "edad").text = str(persona_data["edad"])
ET.SubElement(raiz, "fecha_nacimiento").text = persona_data["fecha_nacimiento"]

nodo_lenguajes = ET.SubElement(raiz, "lenguajes")

for lenguaje in persona_data["lenguajes"]:
    ET.SubElement(nodo_lenguajes, "lenguaje").text = lenguaje

arbol = ET.ElementTree(raiz)
arbol.write(ARCHIVO_XML, encoding="utf-8", xml_declaration=True)
```

### Leer JSON y construir `Persona`

```python
with open(ARCHIVO_JSON, "r", encoding="utf-8") as archivo:
    datos_dict = json.load(archivo)

persona_desde_json = Persona(
    nombre=datos_dict["nombre"],
    edad=int(datos_dict["edad"]),
    fecha_nacimiento=datos_dict["fecha_nacimiento"],
    lenguajes=datos_dict["lenguajes"]
)

print("\n--- Objeto creado desde JSON ---")
persona_desde_json.mostrar_datos()
```

### Leer XML y construir `Persona`

```python
arbol_xml = ET.parse(ARCHIVO_XML)
raiz_xml = arbol_xml.getroot()

nombre_xml = raiz_xml.find("nombre").text
edad_xml = int(raiz_xml.find("edad").text)
fecha_xml = raiz_xml.find("fecha_nacimiento").text

nodo_lenguajes_xml = raiz_xml.find("lenguajes")
lenguajes_xml = [nodo.text for nodo in nodo_lenguajes_xml]

persona_desde_xml = Persona(
    nombre=nombre_xml,
    edad=edad_xml,
    fecha_nacimiento=fecha_xml,
    lenguajes=lenguajes_xml
)

print("\n--- Objeto creado desde XML ---")
persona_desde_xml.mostrar_datos()
```

### Limpieza final

```python
if os.path.exists(ARCHIVO_JSON):
    os.remove(ARCHIVO_JSON)

if os.path.exists(ARCHIVO_XML):
    os.remove(ARCHIVO_XML)

print("\nArchivos temporales eliminados correctamente.")
```

### 🧠 Idea clave del reto

```text
Diccionario Python
       │
       ├──→ JSON ──→ json.load() ──→ Persona
       │
       └──→ XML  ──→ ET.parse() ──→ Persona
```

La idea importante no es memorizar cada línea, sino comprender que **dos formatos diferentes pueden terminar representando la misma entidad dentro del programa**.

---

# 20. Pruebas unitarias (Unit Testing)

Las **pruebas unitarias** verifican automáticamente que una unidad pequeña del programa —por ejemplo, una función o una parte concreta de una clase— produzca el resultado esperado.

## 20.1 Conceptos clave

| Concepto | Significado |
|---|---|
| **Prueba unitaria** | Verificación automatizada de una unidad de código. |
| `unittest` | Framework incluido en la biblioteca estándar de Python para escribir tests. |
| `TestCase` | Clase base que proporciona herramientas para construir pruebas. |
| **Aserción** | Comprobación que determina si una condición esperada se cumple. |
| `assertEqual()` | Comprueba que dos valores sean iguales. |
| `assertIn()` | Comprueba que un valor exista dentro de una colección. |
| `assertIsInstance()` | Comprueba el tipo de un objeto. |
| `assertTrue()` | Comprueba que una expresión sea verdadera. |
| `assertGreater()` | Comprueba que el primer valor sea mayor que el segundo. |

### Regla fundamental

Un método de prueba debe comenzar con `test_` para que `unittest` pueda detectarlo automáticamente.

---

## 20.2 Primera prueba: sumar dos números

### Función a probar

```python
def sumar(numero1: int | float, numero2: int | float) -> int | float:
    return numero1 + numero2
```

### Tests

```python
import unittest

class TestSumar(unittest.TestCase):

    def test_sumar_positivos(self):
        self.assertEqual(sumar(10, 20), 30)

    def test_sumar_decimales(self):
        self.assertEqual(sumar(2.5, 3.5), 6.0)
```

### ¿Qué está comprobando `assertEqual()`?

```python
self.assertEqual(resultado_obtenido, resultado_esperado)
```

En este caso:

```python
self.assertEqual(sumar(10, 20), 30)
```

La prueba pasa cuando el valor retornado por `sumar(10, 20)` es exactamente `30`.

---

## 20.3 Pruebas de una estructura de datos

### Datos a evaluar

```python
datos_usuario = {
    "nombre": "Javier",
    "edad": 26,
    "fecha_nacimiento": "20-06-2000",
    "lenguajes_programacion": ["Python", "SQL", "JavaScript"]
}
```

### Test 1: verificar campos obligatorios

```python
class TestDatosUsuario(unittest.TestCase):

    def test_existencia_campos(self):
        campos_requeridos = {
            "nombre",
            "edad",
            "fecha_nacimiento",
            "lenguajes_programacion"
        }

        self.assertTrue(
            campos_requeridos.issubset(datos_usuario.keys())
        )
```

**¿Qué hace `issubset()`?**

Comprueba que todos los elementos de `campos_requeridos` estén contenidos en las claves de `datos_usuario`.

### Test 2: verificar tipos y valores básicos

```python
    def test_validez_datos(self):
        self.assertIsInstance(datos_usuario["nombre"], str)
        self.assertIsInstance(datos_usuario["edad"], int)
        self.assertIsInstance(datos_usuario["fecha_nacimiento"], str)
        self.assertIsInstance(
            datos_usuario["lenguajes_programacion"],
            list
        )

        self.assertGreater(datos_usuario["edad"], 0)
        self.assertGreater(
            len(datos_usuario["lenguajes_programacion"]),
            0
        )
```

### 🧠 Idea clave

```text
Código
  ↓
Ejecutar prueba
  ↓
Comparar resultado obtenido
  ↓
¿Coincide con lo esperado?
  ├── Sí → ✅ PASS
  └── No → ❌ FAIL
```

---

## 20.4 Ejecutar automáticamente los tests

```python
if __name__ == "__main__":
    unittest.main()
```

Este bloque ejecuta el sistema de pruebas cuando el archivo se ejecuta directamente.

### Ejecución desde terminal

```bash
python archivo_tests.py
```

`unittest` buscará los métodos que comiencen con `test_` y mostrará el resultado de cada prueba.

---

## 20.5 Flujo mental de una prueba unitaria

```text
1. Preparar datos
       ↓
2. Ejecutar función / código
       ↓
3. Obtener resultado
       ↓
4. Compararlo con lo esperado
       ↓
5. PASS o FAIL
```

### Regla práctica

> **Una prueba debe responder una pregunta concreta:** “¿este comportamiento funciona como espero?”

---

# 21. Atajos de teclado

*> Estos atajos corresponden al flujo indicado en el material original y pueden variar según editor, sistema operativo o configuración.*

### Comentar

```text

Ctrl + K

luego

Ctrl + C

```

### Descomentar

```text

Ctrl + K

luego

Ctrl + U

```

---

# 22. Chuleta rápida

## Tipos

```python

str

int

float

bool

list

tuple

dict

set

```

## Condiciones

```python

if condicion:

    ...

elif otra_condicion:

    ...

else:

    ...

```

## Bucles

```python

for elemento in coleccion:

    ...

```

```python

while condicion:

    ...

```

## Control de bucles

```python

break

continue

```

## Validación

```python

while True:

    dato = input("Dato: ")

    if valido(dato):

        break

```

## Excepciones

```python

try:

    ...

except ValueError:

    ...

else:

    ...

finally:

    ...

```

## Funciones

```python

def funcion(parametro: str) -> None:

    ...

    return ...

```

## Métodos de strings frecuentes

```python

.strip()

.lower()

.upper()

.capitalize()

.title()

.replace()

.split()

.join()

.startswith()

.endswith()

.isalpha()

.isdigit()

```

## Colecciones

```python

lista.append(x)

lista.pop()

lista.sort()

clave in diccionario

conjunto.add(x)

conjunto.discard(x)

```

## Identidad y comparación

```python

x == y       # igualdad de valores*

x != y       # desigualdad*

x is None    # identidad*

x is not None

```

## Recursividad

```python

def funcion(n):

    if caso_base:

        return resultado

    return funcion(problema_mas_pequeno)

```

## Pila

```python

pila.append(x)

pila.pop()

```

## Cola

```python

from collections import deque

cola.append(x)

cola.popleft()

```

## POO

```python

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

```

---

# 23. Mapa mental de lo aprendido

```text

PYTHON

│

├── Datos

│   ├── str

│   ├── int

│   ├── float

│   └── bool

│

├── Operadores

│   ├── Asignación

│   ├── Lógicos

│   ├── Pertenencia

│   ├── Identidad

│   └── Bitwise

│

├── Flujo

│   ├── if / elif / else

│   ├── for

│   └── while

│

├── Colecciones

│   ├── list

│   ├── tuple

│   ├── dict

│   └── set

│

├── Strings

│   ├── strip

│   ├── split / join

│   ├── replace

│   ├── lower / upper

│   └── validaciones

│

├── Control

│   ├── break

│   ├── continue

│   └── flags

│

├── Robustez

│   ├── validación

│   ├── while True

│   └── try / except

│

├── Diseño

│   ├── funciones

│   ├── modularización

│   ├── DRY

│   ├── chaining

│   └── diseño defensivo

│

├── Estructuras

│   ├── Stack → LIFO

│   └── Queue → FIFO

│

├── Recursividad

│   ├── caso base

│   └── caso recursivo

│

├── Archivos y formatos

│   ├── JSON

│   ├── XML

│   ├── serialización

│   └── deserialización

│

├── Testing

│   ├── unittest

│   ├── TestCase

│   ├── assertions

│   └── test_

│

└── POO

    ├── clase

    ├── objeto

    ├── atributo

    ├── método

    ├── herencia

    ├── super()

    └── polimorfismo

```
