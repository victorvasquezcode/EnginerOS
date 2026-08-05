# Bitácora de Aprendizaje: Reto 00 - Operadores y Manipulación de Variables

### 1. 🎯 Lo que dominé hoy (El clic mental)
* Comprendí la diferencia operativa de las comparaciones: `==` compara **valores**, mientras que `is` evalúa si dos variables apuntan al **mismo espacio de memoria RAM** o si una variable es `None`.
* Entendí la sintaxis del operador de pertenencia `in` (sensible a mayúsculas/minúsculas): funciona como un buscador donde la subcadena buscada va primero y la variable recipiente al final (`"subcadena" in variable`).
* Comprendí el comportamiento de las divisiones: `/` siempre retorna un decimal (`float`), mientras que `//` ejecuta una división entera truncada (`int`).

### 2. ⚠️ Tropezones, errores y cómo los solucioné
1. **Intento de usar `+=` sin inicializar la variable previamente:**
   * *Error:* `NameError: name 'b' is not defined` al hacer `b += a`.
   * *Por qué pasó:* Los operadores de asignación abreviada requieren que la variable de destino ya exista en memoria.
   * *Solución:* Inicializar la variable con un valor por defecto (ej. `b = 0`) antes de aplicar `+=`.
2. **Sintaxis incorrecta combinando `not` con números (`30 not 20`):**
   * *Error:* `SyntaxError`.
   * *Por qué pasó:* `not` es un operador unario que invierte un booleano (`not True`), no un operador binario de comparación entre dos números.
   * *Solución:* Usar la comparación explícita `30 != 20` o `not (30 == 20)`.
3. **Inversión de orden en el operador de pertenencia `in`:**
   * *Por qué pasó:* Escribir `apellido in "Vasquez"` en lugar de `"Vas" in apellido`.
   * *Resultado:* Incompatibilidad lógica al buscar la variable dentro de un literal estático.
   * *Solución:* Respetar el estándar: `elemento_buscado in contenedor_o_variable`.
4. **Uso de `is` para comparar literales numéricos (`20 is 40`):**
   * *Error:* `SyntaxWarning: "is" with a literal. Did you mean "=="?`.
   * *Solución:* Usar el operador de igualdad `==` para comparar valores numéricos o cadenas de texto.
5. **Invocación de `print()` previa a la declaración de la variable:**
   * *Error:* `NameError` debido al flujo top-down (de arriba a abajo) de Python al interpretar el archivo.
   * *Solución:* Declarar e inicializar las variables siempre por encima de las líneas donde se usen.