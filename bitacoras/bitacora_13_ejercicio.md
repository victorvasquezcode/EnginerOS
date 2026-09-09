# Bitácora de Aprendizaje: Reto 21 - Pruebas Unitarias (Unit Testing)

### 1. 🎯 Lo que dominé hoy (El clic mental)
* **Arquitectura de Pruebas con `unittest`:** Hice clic mental en cómo estructurar suites de pruebas automatizadas creando clases de prueba que heredan de `unittest.TestCase` y declarando métodos que inician obligatoriamente con el prefijo `test_`.
* **Uso de Aserciones Específicas:** Aprendí a seleccionar la herramienta de comprobación adecuada según el escenario: `assertEqual` para verificar retornos exactos, `assertIn` para validar existencia de claves o elementos en contenedores, `assertIsInstance` para garantizar la integridad de los tipos de datos (`str`, `int`, `list`) y `assertGreater` para reglas de negocio (ej. edad mayor a 0).
* **Flujo de Ejecución Automatizado:** Entendí el papel de `if __name__ == "__main__":` junto con `unittest.main()` para permitir que el script actúe como un ejecutor de pruebas autónomo únicamente cuando se corre de forma directa.

---

### 2. ⚠️ Tropezones, errores y cómo los solucioné
* **Inconsistencia en los Type Hints de Retorno:**
  * *Error:* Inicialmente definí `sumar(numero1: int, numero2: float) -> int`, lo cual generaba una contradicción de tipos, ya que sumar un `int` y un `float` en Python siempre retorna un `float`.
  * *Solución:* Corregí la firma usando la sintaxis unificada de union tipos `int | float` tanto en los parámetros como en el valor de retorno.
* **Orden de Parámetros en `assertIn`:**
  * *Error:* Al verificar la existencia de claves intenté pasar la lista contenedora como primer argumento y el elemento como segundo (`self.assertIn(clave, lista_claves)`), invirtiendo la lógica del método.
  * *Solución:* Reorganicé la llamada siguiendo la firma estándar `self.assertIn(elemento_buscado, contenedor)`, asegurando que la búsqueda se realizara correctamente en el diccionario `datos_usuario`.
* **Confusión con `.items()` al iterar:**
  * *Error:* Utilicé `datos_usuario.items()` esperando obtener solo las cadenas de los nombres de clave, recibiendo en su lugar tuplas `(clave, valor)`.
  * *Solución:* Modifiqué la iteración para evaluar la lista de claves requeridas directamente contra el contenedor o utilizando `.keys()`.