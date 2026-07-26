# Bitácora de Aprendizaje - Lógica de Programación
## Concepto del día: [Funciones Basico - Declaraciones, Parametros y Retorno]

### 1. ¿Qué problema resuelve exactamente?
Permite empaquetar un bloque de codigo reusable bajo un nombre especifico para no repetir las lineas de codigo varias veces esto ayuda a modularizar el programa dividiendo algo complejo en pequeñas partes

### 2. ¿Cuáles son sus límites o cuándo NO debo usarlo?
* **No abusar para operaciones de una sola linea simple:** Crear una funcion para algo que solo se utiliza una vez no requiere operaciones
* **No confundir `print()` con `return`: ** Un `print()` solo muestra texto pero no devuelve nada utilizable, el return si devuelve un valor que se puede almacenar en una variable o utilizarse en otro calculo
* **Respetar el orden de los argumentos:** Si una funcion espera `def saludar (nombre, apellido):`, si se envia los argumentos en un orden que no es altera el resultado final a menos que se utilize argumentos nombrados
* **Evitar el uso de `global`:** Modificar variables globales desde dentro de las funciones genera codigo inestable y dificil de rastrear

### 3. Explicación simple (Técnica Feynman):
* **`def nombre_funcion():`** Es como un programar un boton en un control remoto le dice a python que instrucciones debe ejecutar cada vez que presione el boton
* **Parametros (`def funcion(parametro):`)**: Son las ranuras o entradas del boton le pasa la materia prima para que pueda trabajar
    * `*args` recibe una cantidad indeterminada de valores sueltos (como una **tupla**).
    * `**kwargs` recibe pares de `clave = valor` (como un **diccionario**).
* **`return`**: Es la ranura de salida. Cuando la funcion termina su trabajo se entrega el producto final para que lo guarde o se use en otra parte
* **Desempaquetado en `for`**: El número de variables en un bucle `for` no depende de la cantidad total de elementos, sino de la cantidad de sub-elementos que componen cada ítem (ej. `for clave, valor in dict.items():`).

### 4. ¿Cómo lo rompí y qué error dio?
* **Olvidar los parentesis al llamar la funcion** Escribir solo `saludar` en lugar de `saludar()`.
    * *Resultado* Python no ejecuta la funcion solo devuelve la direccion en memoria
    * *Solucion* Usar siempre los `()` para invocar la ejecucion de la funcion
2. ** Orden incorrecto en condicionales multiples (`if/elif`):** Poner condiciones generales antes que condiciones compuestas en el FizzBuzz
    * **Resultado:* Las condiciones complejas no se ejecutaban por las simples consumian el flujo
    * **Solucion:* Evaluar siempre la condicion mas especifica/restrictiva en el primer `if`