# Bitácora de Aprendizaje: Reto 08 - Programación Orientada a Objetos (POO) y Clases

### 1. 🎯 Lo que dominé hoy (El clic mental)

- **Fundamentos de Clases y POO:**
  - **Sintaxis y Estructura:** Entendí que una clase funciona como un molde o plantilla (`class NombreClase:`) que encapsula datos (**atributos**) y comportamientos (**métodos**).
  - **El Constructor (`__init__`):** Comprendí la función del método especial `__init__` para inicializar el estado del objeto en su instanciación.
  - **El Rol de `self`:** Identifiqué que `self` representa la instancia actual del objeto y debe ser el primer parámetro de los métodos de clase para acceder y mutar sus atributos (`self.atributo`).

- **Abstracción de Estructuras de Datos mediante Clases:**
  - **Clase Pila (`Pila`):** Encapsulé la lógica LIFO en una clase reutilizable utilizando una lista interna (`self.items`), exponiendo una interfaz limpia mediante métodos explícitos (`push`, `pop`, `contar`, `imprimir`).
  - **Clase Cola (`Cola`):** Encapsulé la lógica FIFO en una clase utilizando `collections.deque` internamente para garantizar operaciones de extracción de alto rendimiento $O(1)$ con `popleft()`.

---

### 2. ⚠️ Tropezones, errores y cómo los solucioné

- **Uso Incorrecto de `self` en la Declaración de la Clase:**
  - *Error:* Intentar declarar la clase agregando `self` a la cabecera principal (`class Persona(self, nombre, edad):`).
  - *Solución:* Recordar que `self` únicamente se incluye como primer parámetro en la definición del método constructor `def __init__(self, ...)` y demás métodos internos.

- **Asignación Hardcodeada en Métodos Mutadores:**
  - *Error:* Escribir `self.items.append("Manzana")` en el método `push()` en lugar de utilizar el parámetro recibido por la función.
  - *Solución:* Asignar variables dinámicas (`self.items.append(elemento)`) para permitir que la clase procese cualquier tipo de dato enviado por el usuario.

- **Inversión de Cláusula de Guardia en Extracción de Elementos:**
  - *Error:* Intentar ejecutar `.pop()` dentro de la condición `if not self.items:` (que evalúa si la colección está vacía), provocando errores de ejecución.
  - *Solución:* Corregir la condición para extraer datos únicamente cuando la colección contenga elementos (`if self.items:`), retornando `None` en el bloque `else`.