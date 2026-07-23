# Bitácora de Aprendizaje - Lógica de Programación
## Concepto del día: [Manejo Excepciones]

### 1. ¿Qué problema resuelve exactamente?
Evita que un programa colpase de golpe permite capturar ese problema guardarlo en una variable 

### 2. ¿Cuáles son sus límites o cuándo NO debo usarlo?
* **No usar `except`: "desnudo" sin especificar el tipo de error:** Siempre se debe especificar la excepcion esperada `ZeroDivisionError` `ValueError`
* **No usar para ocultar errores de logica:** Si el codigo llegara a fallara por sintaxis o diseño de algoritmo no se debe tapar con un `try/except` se corrige la logica
* **No abusar del bloque `try`:** Dentro del `try` solo va la linea de codigo que puede que este mal o sea peligrosa no todo el script

### 3. Explicación simple (Técnica Feynman):
* **`try` (Intentar):** Es como un cinturon de seguridad encierra el codigo donde hay un posible conflicto
* **`except TipoDeError as error` (Capturar):** Es el colchon de rescate si ocurre ese conflicto deetiene la caida y guarda el reporte del error en una variable `error`
* **`else` (Exito):** Es la confirmacion si no hubo ningun error
* **`finally` (Limpieza final):** Es el cierre garantizado Siempre se ejecuta es para cerrar archivos o conexiones.

### 4. ¿Cómo lo rompí y qué error dio?
* **Confusion con la captura del objeto de error:** No entendia que era `ZeroDivisionError as error`
    * *Solucion:* Entendi que `ZeroDivisionError ` es la etiqueta oficial de Python para el tipo de fallo y `as error` guarda la explicacion tecnica en la variable  `error`
