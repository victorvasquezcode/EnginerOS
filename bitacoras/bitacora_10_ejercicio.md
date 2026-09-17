# Bitácora de Aprendizaje: Reto 10 - Manejo de Excepciones

### 1. 🎯 Lo que dominé hoy (El clic mental)

- **Control de Flujo Completo (`try-except-else-finally`):**
  - Comprendí la responsabilidad de cada bloque: `try` aísla el código de riesgo, `except` captura y gestiona fallos específicos, `else` ejecuta la lógica posterior solo si no hubo ningún error, y `finally` actúa como bloque de cierre garantizado.

- **Creación y Disparo Manual de Excepciones (`raise`):**
  - Aprendí a utilizar la palabra clave `raise` dentro de cláusulas de guardia para detener proactivamente la ejecución ante fallos de lógica o reglas de negocio.
  - Comprendí el uso de `isinstance(variable, (int, float))` junto con `not` para validar tipos antes de operar sobre ellos.

- **Diseño de Excepciones Personalizadas:**
  - Aprendí a crear clases de error propias heredando de la superclase `Exception` (`class MiExcepcionPersonalizadaError(Exception): pass`), permitiendo aislar y capturar errores específicos del dominio o negocio.

- **Introspección de Errores:**
  - Utilicé `type(e).__name__` para obtener dinámicamente el nombre exacto de la excepción capturada (`TypeError`, `ValueError`, `IndexError`, etc.), logrando reportes de error más limpios e informativos.

---

### 2. ⚠️ Tropezones, errores y cómo los solucioné

- **Interrupción Prematura del Bloque `try`:**
  - *Error:* Apilar múltiples llamadas que lanzaban excepción (`procesar_parametros("5", -10)`, `procesar_parametros(0, 0)`) seguidas dentro del mismo bloque `try`.
  - *Solución:* Comprendí que cuando la primera llamada falla, la ejecución salta de inmediato al bloque `except` omitiendo las instrucciones restantes del `try`. Solucioné esto aislando cada prueba en su propia función de evaluación (`probar()`) para validar de forma independiente todos los escenarios posibles.

- **Sintaxis de Anotación de Tipos en `isinstance`:**
  - *Duda:* Inseguridad sobre el significado exacto de `not isinstance(param1, (int, float))`.
  - *Solución:* Aclaré que al pasarle una tupla `(int, float)`, `isinstance` valida si la variable pertenece a cualquiera de esos dos tipos numéricos, y la inversión con `not` permite responder directamente si el argumento recibido no cumple esa condición de entrada.