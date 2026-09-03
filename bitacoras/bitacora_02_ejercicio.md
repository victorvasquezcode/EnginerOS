# Bitácora de Aprendizaje: Reto 02

### 1. 🎯 Lo que dominé hoy (El clic mental)
* **Tipos de Parámetros y Flexibilidad:** Aprendí a declarar funciones desde lo más básico hasta variantes avanzadas con valores predeterminados, orden posicional y retorno múltiple (que Python maneja implícitamente como tuplas).
* **Empaquetamiento con `*args` y `**kwargs`:** Hice clic mental en cómo recibir argumentos de cantidad variable. `*args` empaqueta valores posicionales en una tupla, mientras que `**kwargs` empaqueta pares clave-valor en un diccionario.
* **Manejo del Scope (Local vs. Global):** Comprendí cómo Python busca variables en memoria (regla LEGB). Entendí que para **leer** una variable global no se requiere sintaxis extra, pero para **modificarla** dentro de una función es obligatorio declarar `global`, aunque la buena práctica dicta retornar nuevos valores.
* **Lógica del FizzBuzz Personalizado:** Logré resolver la Dificultad Extra estructurando correctamente la prioridad condicional (evaluar primero el caso compuesto `numero % 15 == 0` o `múltiplo de 3 Y 5`) y aislando el contador únicamente dentro de la cláusula `else`.

---

### 2. ⚠️ Tropezones, errores y cómo los solucioné
* **Parámetros por Defecto vs. Reasignación Local:**
  * *Error:* Al intentar asignar un parámetro por defecto, reasignaba la variable dentro del cuerpo de la función (`nombre = "Victor"`), lo que causaba un `TypeError` al llamar a la función sin argumentos.
  * *Solución:* Entendí que los valores por defecto deben definirse directamente en la firma de la función (`def funcion(param: str = "Valor"):`).
* **Delimitación de Comillas en f-strings:**
  * *Error:* Crucé comillas dobles al invocar la función dentro de un f-string: `f"{obtener_nombre("Javier")}"`.
  * *Solución:* Alterné el uso de comillas dobles en el f-string externo y comillas simples en la cadena interna para evitar romper el intérprete.