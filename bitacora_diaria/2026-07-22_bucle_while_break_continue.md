# Bitácora de Aprendizaje: Reto 01 - Bucle While, Break y Continue

### 1. 🎯 Lo que dominé hoy (El clic mental)
* Entendí la utilidad de cada herramienta de control de flujo:
  * **`while`:** Ideal para iteraciones indefinidas donde no sabemos de antemano cuántas vueltas dará el programa (ej. reintento de contraseñas).
  * **`break`:** Rompe y aborta el bucle de inmediato.
  * **`continue`:** Salta el resto del código de la iteración actual y regresa al inicio para evaluar la siguiente vuelta.

### 2. ⚠️ Tropezones, errores y cómo los solucioné
1. **Bucle infinito al usar `continue` antes de incrementar la variable:**
   * *Por qué pasó:* Colocar el incremento `i += 1` después de la sentencia `continue`.
   * *Resultado:* El programa saltaba el incremento, la variable no cambiaba y se quedaba atrapado en un bucle infinito.
   * *Solución:* En bucles `while` con `continue`, la variable de control **siempre debe incrementarse antes** de activar el salto.
2. **Incremento aislado dentro de un bloque `else`:** Escribir el incremento únicamente dentro del `else` en un `if/else`.
   * *Resultado:* Al cumplirse la condición del `if`, el bloque `else` se omitía, la variable dejaba de actualizarse y el ciclo colapsaba.
   * *Solución:* Colocar el incremento en una posición estratégica donde se garantice su ejecución en cada vuelta.
3. **Uso de punto y coma `;` por inercia de otros lenguajes (`break;`):**
   * *Solución:* Eliminar el `;` para respetar la sintaxis idiomática de Python (PEP 8).