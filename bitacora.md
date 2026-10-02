# 🔴 / 🟡 ACTIVOS

### 🟡 [11] CRUD Ventas
- **Fallas:**
  1. Invertí la condición lógica al evaluar líneas vacías usando `if lista.strip(): continue`.
     1. Negué la condición con `if not lista.strip(): continue` para saltar únicamente las líneas vacías.
   
  2. Dupliqué paréntesis al castear la tupla creando un anidamiento incorrecto `(nombre,(int(cantidad),(float(precio))))`.
     1. Simplifiqué el formateo a una sola tupla limpia `((nombre,int(cantidad),float(precio)))`.
   
  3. Redundé agregando `return None` dentro del `except ValueError` cuando la función ya retornaba `None` por defecto.
     1. Removí el `return None` explícito dejando solo el mensaje de error en el bloque de excepción.
   
  4. Intenté aplicar el método `.strip()` a una tupla `(nombre, cantidad, precio)` provocando un error de atributo `AttributeError`.
     1. Removí la validación `if not lista.strip(): continue` al iterar sobre elementos que ya venían deserializados como tuplas estructuradas.
   
  5. Omití el salto de línea `\n` al final de la cadena de formato dentro de `archivo.write()`.
     1. Agregué `\n` al final del formato `f"{nombre_producto},{cantidad},{precio:.2f}\n"` para evitar que los nuevos registros se concatenen en la misma línea del archivo.
   
- **Revisar:** [05/10/2026].

### 🟡 [12] XML y JSON
- **Fallas:**
  1. .
  2. .
- **Soluciones:**
  1. .
  2. .
- **Revisar:** [03/10/2026].

### 🟡 [13] Pruebas Unitarias
- **Fallas:**
  1. .
  2. .
- **Soluciones:**
  1. .
  2. .
- **Revisar:** .

### 🟡 [14] Manejo Fechas
- **Fallas:**
  1. .
  2. .
- **Soluciones:**
  1. .
  2. .
- **Revisar:**.

### 🟡 [15] Asincronia
- **Fallas:**
  1. .
  2. .
- **Soluciones:**
  1. .
  2. .
- **Revisar:**.

### 🟡 [16] Regex Validaciones 
- **Fallas:**
  1. .
  2. .
- **Soluciones:**
  1. .
  2. .
- **Revisar:**.
- - **Fecha a amarillo:** [30/07/2026]

### 🟡 [17] Mecanismos de Interacion
- **Notas / Conceptos aprendidos:**
  1. List Comprehension y Side-Effects (Mecanismos 1-2)
     1. La diferencia fundamental entre un bucle tradicional `for` y una List Comprehension es que esta última evalúa una expresión para cada elemento directamente dentro de corchetes `[...]` en una sola línea.
     2. La ejecución de `[print(numero) for numero in range(1, 11)]` logra la iteración deseada mediante el side-effect de la función `print()`, aunque devuelve una lista llena de valores `None`.
  2. Iteradores Manuales y Excepciones (Mecanismos 3-4)
     1. Un iterador creado con `iter()` mantiene un puntero interno para rastrear la posición actual en una secuencia de datos.
     2. La función `next()` extrae el siguiente elemento disponible del iterador y avanza de forma irreversible al siguiente elemento.
     3. La excepción `StopIteration` es lanzada automáticamente por Python para señalar que el iterador ya no tiene más elementos para entregar.
     4. Un bucle `while True` con `try/except StopIteration` replica exactamente la arquitectura interna que utiliza el bucle `for` tradicional en Python.
  3. Módulo itertools y Transmisión Infinita (Mecanismos 5-6)
     1. La función `itertools.count(inicio)` genera un iterador infinito de números enteros sucesivos sin necesidad de mantener un contador manual.
     2. La función `itertools.islice(iterable, alto)` recorta un flujo de datos tomando únicamente la cantidad exacta de elementos indicada por el límite superior.
     3. La función `itertools.takewhile(predicado, iterable)` extrae elementos de una secuencia continua únicamente mientras la condición dada retorne valor verdadero `(True)`.
     4.  Una expresión `lambda x: x <= 10` representa una función anónima compacta en una sola línea que evalúa cada número recibido y devuelve un resultado booleano.
      5.  Consumir un iterador con un bucle desplaza su puntero interno, por lo que requiere crear una nueva instancia de la secuencia para poder reusarla sin agotar sus datos.
  4. Programación Funcional con map() (Mecanismo 7)
     1.  La función de orden superior `map(funcion, iterable)` aplica una función dada a cada uno de los elementos de una secuencia.
     2.  `map()` utiliza evaluación perezosa (lazy evaluation), por lo que no ejecuta la función sobre la secuencia hasta que el objeto resultante sea consumido explícitamente.
     3.  Envolver un objeto `map` dentro de la función `list()` fuerza la iteración completa de la secuencia para ejecutar sus operaciones internas.
     4.  Al transformar un `map()` con efectos secundarios de impresión en una lista, la lista final contendrá valores `None` debido a que la función `print()` no retorna ningún valor.
  5. Generadores con yield (Mecanismo 8)
     1.  La instrucción `yield` transforma una función convencional en un generador pausando su ejecución y conservando su estado interno hasta la siguiente llamada.
     2.  Los generadores aplican evaluación perezosa (lazy evaluation), generando y entregando un único elemento a la vez a medida que se solicita.
     3.  Un generador optimiza de forma drástica el uso de memoria RAM al evitar cargar secuencias masivas o completas simultáneamente en el sistema.
     4.  Consumir un generador mediante un bucle `for` o una función receptora reanuda la función generadora en el punto exacto donde fue pausada por la sentencia `yield`.
  6. Acumulación con reduce() (Mecanismo 9)
     1.  La función `reduce(funcion, iterable)` del módulo `functools` procesa secuencialmente los elementos de una estructura para reducirlos a un único resultado acumulado.
     2.  La función de reducción requiere una firma de dos argumentos en donde el primero almacena el acumulador parcial y el segundo recibe el elemento actual de la iteración.
     3.  A diferencia de `map()` o `filter()`, `reduce()` evalúa la secuencia de forma continua arrastrando el resultado de cada paso al siguiente hasta colapsar toda la secuencia.
     4.  La suma acumulada de los números del 1 al 10 mediante `reduce()` demuestra la capacidad de transformar iteraciones en operaciones aritméticas o lógicas continuas.
  7. Modificación Destructiva de Listas (Mecanismo 10)
     1.  El método `.pop(0)` remueve y devuelve el primer elemento de una lista modificando la estructura original de forma destructiva.
     2.  En Python, las colecciones vacías como una lista `[]` se evalúan automáticamente como `False` en un contexto booleano.
     3.  La condición `while lista:` permite estructurar bucles de consumo destructivo que finalizan de forma limpia al quedar vacía la colección.
     4.  Extraer elementos repetidamente del índice 0 mediante `.pop(0)` tiene un costo de rendimiento $O(n)$ debido a que requiere reordenar los índices restantes en memoria.
- **Fallas:**
  1. .
  2. .
- **Soluciones:**
  1. .
  2. .
- **Revisar:**.
- **Fecha a amarillo:** [01/08/2026]

---

### 🔴 [18] Conjuntos
- **Notas / Conceptos aprendidos:**
  1. .
  2. .

---

# 🟢 DOMINADOS (VERDES)
- [01 al 10] Conceptos básicos


# 📌 MODO DE TRABAJO DIARIO (EL 1%)

1. 🌅 MAÑANA (5:00 AM - 1 hora) -> AMARILLO
   - Leer esta bitácora (1 min).
   - Resolver 1 ejercicio Amarillo SIN ayuda.
   - Si sale BIEN -> Poner fecha a 3 días para prueba de fuego (cambiando enunciado).
   - Si sale MAL / Pido ayuda -> Anotar las fallas aquí y se queda en Amarillo.

2. ☀️ TARDE/NOCHE -> ROJO + TEORÍA
   - Estudiar y resolver el ROJO del día con ayuda/tutoriales (Pasa a Amarillo).
   - Si fallaste en el AMARILLO de la mañana, estudiar la teoría de los puntos débiles anotados.
   - Registrar fallas/soluciones nuevas en esta bitácora (30 segundos).

3. 🗓️ SÁBADOS -> AUDITORÍA DE VERDES
   - Hacer prueba rápida a 3 o 4 ejercicios Verdes (cambiando reglas o refactorizando).
   - Si aprueban -> Siguen en Verde.
   - Si fallan -> Bajan a Amarillo para repasarlos en la semana.