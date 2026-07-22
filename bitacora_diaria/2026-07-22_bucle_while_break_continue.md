# Bitácora de Aprendizaje - Lógica de Programación
## Concepto del día: [Estructuas de Control - Bucle While, Break y Continue]

### 1. ¿Qué problema resuelve exactamente?
* **`while`:** Permite repetir un bloque de codigo **mientras** una condicion sea `True`, cuando no sabemos cuantas vuelvas dara por ejemplo la contraseña si se equivoca no sabemos cuantas vuelvas dara
* **`break`:** Detiene y destruye la ejecucion del bucle inmediatamente.
* **`continue`:** Salta el resto de las lineas de la vuelta actual y sigue con el bulce saltandose esa linea

### 2. ¿Cuáles son sus límites o cuándo NO debo usarlo?
* No debo olvidar modificar o incrementar la varible de control dentro del bucle evitando el bucle infinito
* Al usar `continue` el incremeento de la variable **debe ir antes de la condicion** sino se hara un bucle infinito
* No debo usar punto y coma al final de `break` o `continue`
* No debo colocar el inremento dentro de un bloque `else`

### 3. Explicación simple (Técnica Feynman):
* `while` es un portero preguntando a la entrada de una discoteca: "mientras tengas entrada (`True`), puedes volver a pasar".
* `break` es un botón de emergencia: al presionarlo, rompe el ciclo y salimos del lugar inmediatamente.
* `continue` es un "pase al siguiente": ignora lo que falta por hacer en la vuelta actual y vuelve a la fila para la siguiente inspección.

### 4. ¿Cómo lo rompí y qué error dio?
* **Puse el incremento dentro de un bloque `else`:** Escribí `if i == 3: break; else: print(i); i += 1`. Al evaluarse `i == 3`, el bloque `else` no se ejecutaba y la variable no incrementaba.
  * *Solución:* Ubicar el incremento de la variable de forma estratégica dentro del flujo para asegurar que cambie en cada vuelta.
* **Uso de punto y coma `;`:** Escribí `break;` por costumbre de otros lenguajes.
  * *Solución:* Eliminar el punto y coma `;` para mantener la sintaxis estándar de Python.