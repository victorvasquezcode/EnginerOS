# Bitácora de Aprendizaje: Reto 02 - Funciones Básicas, Parámetros y Retorno

### 1. 🎯 Lo que dominé hoy (El clic mental)
* Entendí la diferencia fundamental entre `print()` y `return`: `print()` solo es una pantalla temporal, mientras que `return` entrega un valor real y útil que se puede guardar en una variable para usarlo en otros cálculos.
* Comprendí que `*args` empaqueta múltiples argumentos sueltos en una Tupla `()`, mientras que `**kwargs` los recibe como un Diccionario `{}` con estructura clave-valor.

### 2. ⚠️ Tropezones, errores y cómo los solucioné
1. **Olvidar los paréntesis al llamar a la función:** Escribir `saludar` en lugar de `saludar()`.
   * *Por qué pasó:* Confundí el nombre/referencia de la función con su orden de ejecución.
   * *Resultado:* Python no ejecutaba el código, solo mostraba la dirección técnica del objeto en memoria RAM.
   * *Solución:* Usar siempre los paréntesis `()` para **invocar** la función.
2. **Orden incorrecto de condicionales múltiples en FizzBuzz:** Poner evaluaciones simples antes que las compuestas.
   * *Por qué pasó:* Colocar `if num % 3 == 0:` antes de `if num % 3 == 0 and num % 5 == 0:`.
   * *Resultado:* Las condiciones complejas nunca se evaluaban porque las simples "atrapaban" el flujo primero.
   * *Solución:* En cadenas de condicionales, la condición más restrictiva o especifica **siempre debe ir en el primer `if`**.