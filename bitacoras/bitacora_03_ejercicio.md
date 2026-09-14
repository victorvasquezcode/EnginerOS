# Bitácora de Aprendizaje: Reto 03 - Estructuras de Datos Nativas y Aplicación de Consola

### 1. 🎯 Lo que dominé hoy (El clic mental)

- **Comportamiento y Detección de Estructuras Nativas:**
  - **Listas (`list`):** Operaciones mutables de inserción con `.append()` (al final) e `.insert(pos, val)` (desplazamiento por índice); borrado específico por valor con `.remove()` o por índice reteniendo el elemento con `.pop()`; y ordenación in-place (`.sort()`) vs. funcional/copia (`sorted()`).
  - **Tuplas (`tuple`):** Naturaleza inmutable que bloquea la modificación directa de índices (lanzando `TypeError`), obligando a reestructurar mediante listas intermedias o el uso de funciones globales como `sorted()`.
  - **Conjuntos (`set`):** Elementos únicos y desordenados donde no existe el índice numérico. Uso de `.add()` y `.update()`, diferenciando el borrado estricto con `.remove()` (KeyError) del borrado seguro con `.discard()`.
  - **Diccionarios (`dict`):** Acceso y modificación eficiente en $O(1)$ asociando claves únicas a valores. Manipulación de registros con `del` y `.pop()`, además de ordenación estructurada mediante `sorted(dicc.items())` reconvertido a `dict`.

- **Arquitectura de Software y UX Defensiva:**
  - **Validación Limpia y Directa:** Retorno explícito de condiciones booleanas (`telefono.isdigit() and 0 < len(telefono) <= 11`) evitando el riesgo de variables no inicializadas (`UnboundLocalError`).
  - **Flujo de Usuario Ágil:** Redirección inteligente dentro del método `insertar_contacto()` hacia `actualizar_contacto()` si el registro ya existe, cortando la ejecución posterior con `return` para no duplicar entradas.
  - **Formateo y Sanitización:** Limpieza de espacios con `.strip()`, estandarización de texto con `.capitalize()` y uso de `match/case` comparando cadenas de texto (`case "1":`) para un menú interactivo robusto.

---

### 2. ⚠️ Tropezones, errores y cómo los solucioné

- **Confusión entre Reemplazo e Inserción:**
  - *Error:* Usar `lista[1] = "Elemento"` creyendo que insertaba una nueva posición.
  - *Solución:* Comprendí que la asignación por índice sobrescribe el valor existente (mantiene la longitud), mientras que `.insert(1, "Elemento")` desplaza los elementos adyacentes hacia la derecha e incrementa el tamaño de la lista.

- **Parámetro Incorrecto en `.pop()`:**
  - *Error:* Intentar borrar un elemento por su texto pasando una cadena (`lista.pop("Manzana")`).
  - *Solución:* Entendí que `.pop()` exige exclusivamente un índice numérico entero. Si se requiere borrar por valor directo, la herramienta adecuada es `.remove("Manzana")`.

- **Bucle Infinito en la Inserción de Teléfono:**
  - *Error:* Usar `while True:` evaluando la variable `telefono` declarada fuera del bucle, haciendo que un primer intento inválido mantuviera el error eternamente (`continue`).
  - *Solución:* Trasladé la lectura del `input()` dentro del cuerpo del bucle `while` para solicitar de nuevo el número en cada iteración hasta superar la validación.

- **Flujo Doble al Redirigir la Inserción:**
  - *Error:* Llamar a `actualizar_contacto()` desde la comprobación de existencia en la inserción, provocando que al terminar la actualización el programa continuara ejecutando la petición del número telefónico.
  - *Solución:* Incorporé la instrucción `return` para abortar de forma limpia el flujo de inserción inmediatamente después de que la actualización tomara el control.