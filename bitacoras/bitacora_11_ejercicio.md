# Bitácora de Aprendizaje: Reto 11 - Manejo de Archivos y Dificultad Extra

### 1. 🎯 Lo que dominé hoy (El clic mental)

* **El puente entre RAM y Disco Duro:** Comprendí que un archivo de texto (`.txt`) solo almacena cadenas de caracteres (`str`). Para operar con datos numéricos en Python, es necesario traducir el texto a estructuras de memoria mediante `cargar_productos()` (usando `.strip()`, `.split(",")`, `int()` y `float()`) y reconvertir las listas a texto formateado con `guardar_todos_los_productos()`.
* **Modos de apertura con `with open()`:**
  * Modo **`"w"` (write):** Sobrescribe todo el archivo desde cero. Ideal para inicializar o actualizar la lista completa tras modificaciones.
  * Modo **`"a"` (append):** Adjunta nuevas líneas al final sin alterar el contenido existente. Perfecto para añadir productos individuales.
  * Modo **`"r"` (read):** Lee el contenido sin modificar el disco.
* **Mutabilidad y persistencia en listas (`enumerate` vs `[i]`):** Entendí que modificar una variable local dentro de un bucle `for` no cambia los datos reales de una lista. Es indispensable usar la posición física `productos[i]` o reconstruir la lista mediante **Comprensión de Listas** (`[p for p in productos if ...]`) para aplicar cambios en memoria antes de guardar en el archivo.
* **Formatos de impresión con f-strings:** Aprendí a usar alineación y columnas fijas (`:<15`, `:<5`) junto con restricciones de decimales (`:.2f`) para presentar tablas tabuladas y legibles en la terminal.

---

### 2. ⚠️ Tropezones, errores y cómo los solucioné

* **Sintaxis incorrecta al escribir en archivo:**
  * *Error:* Intentar guardar datos asignando variables sueltas como `nombre, edad, lenguaje` o envolviéndolas en corchetes `{[nombre]}` dentro de `archivo.write()`.
  * *Solución:* Usar invocaciones explícitas de `.write()` acompañadas de f-strings y saltos de línea explícitos (`f"{nombre}, {cantidad}, {precio}\n"`).
* **Olvidar el salto de línea (`\n`) en modo Append:**
  * *Error:* Guardar productos con `archivo.write(f"{nombre}, {cantidad}, {precio}")` provocaba que el siguiente registro se pegara en la misma línea (`Manzana, 10, 2.5Pera, 5, 3.0`), rompiendo el procesamiento posterior con `.split(",")`.
  * *Solución:* Asegurar siempre un `\n` al final de cada registro escrito.
* **Remplazo por listas vacías al eliminar (`productos[i] = []`):**
  * *Error:* Asignar `[]` a un elemento generaba un `ValueError: not enough values to unpack` al intentar reescribir el archivo.
  * *Solución:* Implementar filtrado con comprensión de listas (`[p for p in productos if p[0].lower() != objetivo.lower()]`) o usar `del productos[i]`.
* **Impresiones repetidas dentro de bucles:**
  * *Error:* Colocar el `print()` del total general dentro del bucle `for` en `calcular_ventas_total()` o dejar fuera de sangría el `print()` de cada producto en `consultar_producto()`.
  * *Solución:* Ajustar la indentación: mantener la lectura dentro del `for` para mostrar filas individuales y sacar las variables acumuladoras fuera del `for` para imprimir resultados consolidados.