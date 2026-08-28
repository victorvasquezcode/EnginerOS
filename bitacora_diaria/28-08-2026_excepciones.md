# Bitácora de Aprendizaje: Reto 10 - Manejo de Excepciones

### 1. 🎯 Lo que dominé hoy (El clic mental)

* **Estructura Defensiva `try / except / else / finally`:**
  * Comprendí el flujo completo del control de errores: el bloque `try` aísla el código de riesgo; los bloques `except` específicos capturan errores concretos; `else` ejecuta la ruta feliz solo si no hubo fallos; y `finally` actúa como cierre garantizado que se ejecuta siempre.
* **Separación de Responsabilidades y Delegación de Parámetros:**
  * Entendí la diferencia entre la función "motor" (`procesar_parametros`), encargada de operar y provocar errores, y la función "escudo" (`probar_procesamiento`), que recibe los parámetros del usuario y los reenvía dentro de un bloque protector para controlar la ejecución.
* **Creación y Lanzamiento de Excepciones de Negocio:**
  * Utilicé `pass` en clases vacías heredadas de `Exception` para crear tipos de errores personalizados (`MiExcepcionPersonalizadaError`) aprovechando la infraestructura nativa de Python.
  * Aprendí a forzar salidas controladas con la palabra clave `raise` enviando mensajes descriptivos cuando no se cumplen las reglas de negocio (ej. parámetros negativos).

---

### 2. ⚠️ Tropezones, errores y cómo los solucioné

* **Confusión entre imprimir y retornar en la función principal:**
  * *Error:* Usar `return print(...)` al final de la función procesadora, lo que devolvía implícitamente `None` e impedía aprovechar la respuesta en el bloque `else`.
  * *Solución:* Retorné directamente la cadena con formato (`return f"..."`) para enviar el dato limpio a la función invocadora.
* **Incertidumbre sobre cómo identificar el tipo de error en consola:**
  * *Error:* Capturar la excepción pero solo imprimir el mensaje en texto sin conocer la clase exacta que la generó.
  * *Solución:* Utilicé la introspección con `type(e).__name__` para extraer dinámicamente el nombre de la clase del error (`ZeroDivisionError`, `IndexError`, etc.).