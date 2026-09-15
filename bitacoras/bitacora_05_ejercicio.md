# Bitácora de Aprendizaje: Reto 05 - Asignación de Variables y Gestión de Memoria

### 1. 🎯 Lo que dominé hoy (El clic mental)

- **Mecanismo de Asignación en Python (*Pass-by-object-reference*):**
  - **Tipos Inmutables (`int`, `float`, `str`, `bool`, `tuple`):** Comportamiento análogo al *paso por valor*. Cualquier reasignación genera un nuevo objeto en una dirección de memoria diferente, dejando intacta la referencia original.
  - **Tipos Mutables (`list`, `dict`, `set`):** Comportamiento análogo al *paso por referencia*. Las variables asignadas comparten la misma posición en memoria (apuntan al mismo objeto).

- **Comportamiento en Funciones:**
  - **Modificación *In-Place* vs. Reasignación:** Las funciones pueden alterar objetos mutables directamente en su dirección de memoria original (p. ej., mediante `.append()`). Sin embargo, reasignar la variable dentro de la función (`lista = [...]`) rompe la referencia, creando un nuevo objeto en un *scope* local.

- **Aislamiento e Intercambio (*Swap*):**
  - **Uso de `.copy()` y Slicing (`[:]`):** Creación de copias explícitas de colecciones mutables dentro de las funciones para permitir transformaciones o intercambios sin alterar las referencias de las variables externas originales.
  - **Empaquetado y Desempaquetado de Tuplas:** Implementación idiómatica del *swap* mediante `a, b = b, a`.

---

### 2. ⚠️ Tropezones, errores y cómo los solucioné

- **Invocación de Objetos Mutables en Pruebas:**
  - *Error:* Pasar literales directos (p. ej., `intercambiar_por_valor(10, 20)`) en lugar de las variables creadas externamente, lo que impedía comprobar si las referencias originales se mantenían inalteradas.
  - *Solución:* Pasar las variables identificadoras (`origin_a`, `origin_b`) y desempaquetar el retorno directamente sobre dos identificadores nuevos.

- **Confusión entre Modificación in-place y Reasignación de Referencia:**
  - *Error:* Asumir que asignar una nueva lista dentro de una función alteraría la lista original del ámbito global.
  - *Solución:* Comprobar experimentalmente la diferencia entre modificar la estructura existente (`lista.append()`) y redefinir el puntero local (`lista = [...]`).

- **Mutabilidad No Deseada en Funciones Swap:**
  - *Error:* Intentar intercambiar elementos de estructuras mutables directamente sin clonarlas, lo que exponía a las listas originales a cambios colaterales.
  - *Solución:* Incorporar `.copy()` en las primeras líneas de la función para desacoplar las referencias del ámbito local respecto al ámbito global.