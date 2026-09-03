# Bitácora de Aprendizaje: Reto 00

### 1. 🎯 Lo que dominé hoy (El clic mental)
* **Tipos Primitivos y Sintaxis:** Consolidé la declaración exacta de los tipos de datos fundamentales en Python: `int`, `float`, `bool`, `str` y `NoneType` (`None`).
* **Convenciones de Nombrado:** Integré el estándar de la comunidad usando `snake_case` para variables convencionales y `UPPERCASE` para denotar "constantes" (ya que Python no bloquea la reasignación a nivel de intérprete, sino por acuerdo de desarrolladores).
* **Comentarios y Docstrings:** Dominé el uso de `#` para anotaciones rápidas en una sola línea y las triples comillas (`"""` / `'''`) para bloques multilínea o documentación.
* **Formateo con F-strings:** Aprendí a inyectar variables de forma dinámica en salidas de consola usando la sintaxis `f"..."`.

---

### 2. ⚠️ Tropezones, errores y cómo los solucioné
* **Reutilización de Variables:** Al inicio usé `cadena_caracteres` directamente dentro del `print()`, lo que funcionaba pero no mostraba explícitamente el nombre del lenguaje guardado en una variable independiente.
* **Solución:** Separé el texto del saludo en una variable de texto y el nombre del lenguaje en otra, combinándolas dinámicamente dentro de la plantilla f-string: `f"¡{cadena_texto}, {mi_variable}!"`.