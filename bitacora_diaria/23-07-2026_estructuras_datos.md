# Bitácora de Aprendizaje: Reto 04 - Estructuras de Datos y Algoritmos de Búsqueda

### 1. 🎯 Lo que dominé hoy (El clic mental)
* Comprendí la naturaleza de cada estructura: **Listas** (dinámicas/mutables), **Tuplas** (inmutables), **Sets** (únicos/sin orden) y **Diccionarios** (clave-valor).
* Entendí cómo el extractor `for` abre automáticamente los paquetes de `.items()` en variables independientes (`clave` y `valor`) en cada vuelta.
* Aprendí la arquitectura de **bucles `while True` aislados** para crear validaciones independientes por campo (UX profesional).

### 2. ⚠️ Tropezones, errores y cómo los solucioné
1. **Intentar renombrar la clave de un diccionario directamente:**
   * *Por qué pasó:* Creía que las claves de los diccionarios se podían mutar directamente.
   * *Solución:* Usar la técnica de extracción e inyección en una sola línea: `agenda[nueva] = agenda.pop(vieja)`.
2. **Buscar valores de teléfono usando `if numero in agenda:`:**
   * *Por qué pasó:* El operador `in` sobre un diccionario solo busca en las **claves** (nombres).
   * *Resultado:* Decía que el número no existía aunque estuviera guardado.
   * *Solución:* Buscar explícitamente en los valores con `in agenda.values()` o recorrer el diccionario con `for nombre, numero in agenda.items():`.
3. **Acoplamiento de validaciones en un solo bucle `while`:**
   * *Por qué pasó:* Pedir nombre y número en el mismo bloque `while True`.
   * *Resultado:* Un error en el formato del teléfono obligaba al usuario a volver a escribir el nombre desde cero (mala UX).
   * *Solución:* Asignar un bucle `while True` independiente a cada entrada de datos.
4. **Asignar métodos in-situ de listas a variables:** Intentar `resultado = lista.remove('a')`.
   * *Resultado:* La variable guardaba `None` porque `.remove()` modifica la lista directamente en memoria sin retornar nada.
   * *Solución:* Ejecutar el método directamente sobre la lista sin asignarlo a variables.