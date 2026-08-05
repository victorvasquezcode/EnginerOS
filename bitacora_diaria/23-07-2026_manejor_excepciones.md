# Bitácora de Aprendizaje: Reto 06 - Manejo de Excepciones

### 1. 🎯 Lo que dominé hoy (El clic mental)
* Entendí cómo funciona el flujo defensivo completo: `try` aísla el código peligroso, `except` frena el colapso especificando el error, `else` celebra que todo salió bien y `finally` limpia o cierra conexiones sin importar qué pase.

### 2. ⚠️ Tropezones, errores y cómo los solucioné
1. **Confusión con la sintaxis de captura:** No entendía bien qué significaba la estructura `ZeroDivisionError as error`.
   * *Por qué pasó:* Creía que `error` era una palabra clave fija de Python.
   * *Solución:* Entendí que `ZeroDivisionError` es la etiqueta oficial del tipo de falla y `as error` es simplemente la variable que tú eliges para guardar la explicación técnica que devuelve Python.
2. **Peligro de usar `except` "desnudo":** Usar `try/except` sin especificar la excepción.
   * *Solución:* Nunca dejar un `except:` a secas porque oculta errores de lógica o sintaxis. Siempre debo especificar la excepción esperada (ej. `ValueError`, `ZeroDivisionError`).