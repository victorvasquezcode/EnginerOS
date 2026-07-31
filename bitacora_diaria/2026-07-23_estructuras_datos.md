# Bitácora de Aprendizaje - Lógica de Programación
## Concepto del día: [Estructuras de Datos - Listas, Tuplas, Diccionarios y Sets]

### 1. ¿Qué problema resuelve exactamente?
Permite agrupar, organizar y manipular colecciones de datos en memoria segun su naturaleza

### 2. ¿Cuáles son sus límites o cuándo NO debo usarlo?
* **Listas** No usar cuando se requiere asegurar que los datos permanezcan inmutables `Tuplas` o cuando se permitan elementos repetidos `Sets`
* **Tuplas** No usar si los datos van a cambiar a lo largo del tiempo ya que son inmutable
* **Diccionarios** No usar si solo necesitas una secuencia simple sin identificadores clave-valor.
* **Sets:** No usar si el orden de los elementos importa o si necesitas acceder a ellos mediante el indice numero `set[0]`

### 3. Explicación simple (Técnica Feynman):
* **Lista (`[]`)** Es una caja con comportamientos numeros (`0,1,2,....`) donde se puede meter sacar y ordenar lo que se quiera
* **Tupla (`()`)** Es un bloque de cemento con datos guardados nadie lo puede modificar
* **Diccionario (`{}`)** Es un casillero etiquetado no se busca por numero se busca por la etiqueta clave para saber el valor adentro
* **Set (`{}`)** Es un colador anti-duplicados todo pierde su orden pero elimina automaticamente las copias repetidas
* **Extractor `for` con `.items()`:** Al iterar `for clave, valor in dict.items():` el bucle extrae y desempaqueta automaticamente la clave y el valor en cada vuelta.
* **Aislamiento de validacion en bucle:** Usar bucles `while True` independientes para cada campo evita pedir nuevamente datos que el usuario ya ingreso correctamente.

### 4. ¿Cómo lo rompí y qué error dio?
1. **Asignar métodos de lista a variables:** Intentar `remove = lista.remove('a')`.
   * *Resultado:* La variable guarda `None` porque modifica la lista directamente.
   * *Solución:* Aplicar el metodo directo a la lista sin asignarlo a una variable.
2. **Intentar modificar la clave de un diccionario directamente:** Intentar renombrar una clave existente.
   * *Resultado:* Incompatibilidad logica, las claves no se renombran directamente.
   * *Solucion:* Asignar el valor a la nueva clave y eliminar la anterior mediante `agenda[nueva] = agenda.pop(vieja)`
3. **Buscar valores directamente sobre la estructura del diccionario:** Usar `if numero in agenda:`
   * *Resultado:* `in` solo busca en las **claves** (nombres)
   * *Solucion:* Buscar en los valores con `in agenda.values()` o iterar los pares con `for nombre, numero in agenda.items():`
4. **Acoplamiento de validaciones en un solo bucle:** Validar nombre y numero dentro del mismo `while True`
   * *Resultado:* Un error en el numero obligada al usuario a reescribir el nombre desde cero (mala UX)
   * *Solucion:* Anidar bucles `while True` separados para cada dato a recolectar