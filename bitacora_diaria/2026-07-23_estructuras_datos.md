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
* **Mecanismo del `for`:** El `for` no es solo un contador; es un extractor. Al usar `for clave, valor in dict.items():`, el `for` abre la tupla de cada vuelta y guarda automáticamente el primer dato en `clave` y el segundo en `valor`.

### 4. ¿Cómo lo rompí y qué error dio?
1. **Asignar métodos de lista a variables:** Intentar `remove = lista.remove('a')`.
   * *Resultado:* La variable guarda `None` porque los métodos de listas modifican la lista *in-situ*.
   * *Solución:* Aplicar el método directo a la lista sin asignar a variable, a menos que sea `sorted(lista)`.
2. **Sintaxis incorrecta en Diccionarios:** Usar `=` en lugar de `:` dentro de `{}`.
   * *Resultado:* `SyntaxError` en Python.
   * *Solución:* Las claves llevan comillas y se separan del valor con `:`.
