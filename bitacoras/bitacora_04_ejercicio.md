# Bitácora de Aprendizaje: Reto 04 - Cadenas de Caracteres y Analizador de Texto

### 1. 🎯 Lo que dominé hoy (El clic mental)

- **Manipulación e Inspección Avanzada de Strings:**
  - **Slicing / Rebanado (`[inicio:fin:paso]`):** Uso eficiente de límites excluyentes y pasos negativos (como `[::-1]`) para la inversión instantánea de cadenas sin depender de bucles externos.
  - **Transformación y Búsqueda Nactiva:** Manejo de transformaciones de caso (`.upper()`, `.lower()`, `.title()`, `.swapcase()`), así como la diferencia técnica entre la búsqueda defensiva con `.find()` (retorna `-1`) frente al manejo explícito de errores con `.index()` (`ValueError`).
  - **División, Limpieza y Unión:** Uso combinado de `.strip()` para saneamiento de bordes, `.split()` para deserializar texto a listas y `.join()` invirtiendo la sintaxis estándar (`"separador".join(lista)`).
  - **Verificaciones Booleanas e Iteración:** Inspección con `.isalpha()`, `.isdigit()`, `.isalnum()` y el desempaquetado limpio de índices con `enumerate()`.

- **Lógica Algorítmica y Sanitización:**
  - **Normalización Previa de Datos:** Implementación de funciones de sanitización (`sanitizar_texto`) que filtran caracteres alfanuméricos e ignoran mayúsculas antes de ejecutar comparaciones complejas.
  - **Comprobación Estructurada:**
    - **Palíndromos:** Comparación directa de la cadena limpia frente a su rebanado invertido.
    - **Anagramas:** Ordenación alfabética mediante `sorted()` comprobando igualdad de contenido eliminando la igualdad exacta entre palabras.
    - **Isogramas (Heterogramas):** Comparación rápida de longitud entre la lista de caracteres y la estructura de datos `set()` para detectar letras duplicadas en $O(N)$.

---

### 2. ⚠️ Tropezones, errores y cómo los solucioné

- **Evaluación Global en `len()`:**
  - *Error:* Incluir la frase entera del `f-string` dentro de `len()`, provocando que midiera la longitud acumulada del mensaje formateado en lugar de la variable objetivo.
  - *Solución:* Pasar únicamente la variable `str` aislada a la función `len(cadena_simple)`.

- **Manejo de Iteradores con `enumerate()`:**
  - *Error:* Intentar imprimir directamente el resultado de `enumerate(palabra)`, obteniendo la referencia de memoria del objeto en lugar de los elementos.
  - *Solución:* Consumir el generador iterando con un bucle `for indice, caracter in enumerate(palabra):`.

- **Sintaxis Incompleta en Sanitización:**
  - *Error:* Escribir `caracter.lower` omitiendo los paréntesis `()`, devolviendo la referencia del método en lugar del valor en minúscula.
  - *Solución:* Añadir la invocación completa `caracter.lower()` y acumular las letras filtradas en una lista antes del `.join()`.

- **Redundancia en la Lógica de Anagramas:**
  - *Error:* Agregar una validación explícita `len(p1) == len(p2)` antes de comparar las listas ordenadas por `sorted()`.
  - *Solución:* Remover la verificación de longitud por redundancia, ya que la igualdad de dos listas ordenadas (`sorted(p1) == sorted(p2)`) implica necesariamente que ambas tienen la misma cantidad de elementos.