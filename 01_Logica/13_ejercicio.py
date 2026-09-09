# =============================================================================
# RETO 13: PRUEBAS UNITARIAS (UNIT TESTING)
#
# CONCEPTOS CLAVE:
# 1. Pruebas Unitarias: Pruebas automatizadas que verifican el correcto 
#    funcionamiento de un componente individual de código (función o clase).
# 2. Módulo 'unittest': Framework integrado en Python para crear y ejecutar 
#    suites de pruebas basadas en clases de prueba y métodos de aserción.
# 3. Aserciones (Assertions): Métodos que comprueban si una condición se cumple
#    (ej. assertEqual, assertIn, assertIsInstance, assertTrue).
# =============================================================================

import unittest

# =============================================================================
# 1. FUNCIÓN A PROBAR Y SU TEST UNITARIO
# =============================================================================
# Enunciado: Crea una función que se encargue de sumar dos números y retornar
# su resultado. Crea un test que determine si esa función se ejecuta correctamente.

# --- FUNCIÓN A EVALUAR ---
# Pasos sugeridos:
# - Define una función 'sumar' con type hints que reciba dos parámetros (int/float)
#   y retorne su suma.
def sumar (numero1: int | float, numero2: int | float) -> int | float:
    return numero1 + numero2


# --- TEST UNITARIO DE LA FUNCIÓN ---
# Pasos sugeridos:
# - Crea una clase de prueba que herede de 'unittest.TestCase'.
# - Define un método de prueba (debe empezar obligatoriamente con el prefijo 'test_').
# - Utiliza 'self.assertEqual()' para comprobar que el retorno de 'sumar(a, b)' 
#   coincida con el resultado esperado.

class TestSumar(unittest.TestCase):
    def test_sumar_positivos(self):
        self.assertEqual(sumar(10, 20), 30)
        
    def test_sumar_decimales(self):
        self.assertEqual(sumar(2.5, 3.5), 6.0)


# =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# =============================================================================
# Enunciado: Crea un diccionario con las claves: "name", "age", "birth_date" y
# "programming_languages". Crea dos test:
# - El primero determina que existen todos los campos (claves).
# - El segundo determina que los datos introducidos son del tipo correcto o válidos.

# --- ESTRUCTURA DE DATOS A EVALUAR ---
# Pasos sugeridos:
# - Define el diccionario 'datos_usuario' con la estructura requerida.
datos_usuario = {
    "nombre" : "Javier",
    "edad" : 26,
    "fecha_nacimiento" : "20-06-2000",
    "lenguajes_programacion" : ["Python","SQL","Javascript"]
}

# --- TEST UNITARIO DEL DICCIONARIO ---
# Pasos sugeridos:
# - Crea una clase de prueba 'TestDatosUsuario' que herede de 'unittest.TestCase'.
class TestDatosUsuario(unittest.TestCase):

# - TEST 1: VERIFICAR EXISTENCIA DE CAMPOS:
#   * Define 'test_existencia_campos(self)'.
#   * Obtén las claves del diccionario.
#   * Comprueba con 'self.assertIn()' o 'self.assertTrue()' que las 4 claves requeridas
#     existan dentro del diccionario.
    def test_existencia_campos(self):
        campos_requeridos = {"nombre", "edad", "fecha_nacimiento", "lenguajes_programacion"}
        self.assertTrue(campos_requeridos.issubset(datos_usuario.keys()))

# - TEST 2: VERIFICAR TIPOS DE DATOS Y VALIDEZ:
#   * Define 'test_validez_datos(self)'.
#   * Usa 'self.assertIsInstance()' para validar que 'name' sea str, 'age' sea int,
#     'birth_date' sea str y 'programming_languages' sea list.
#   * Opcional: Verifica con 'self.assertGreater()' que la edad sea mayor a 0 y que
#     la lista de lenguajes no esté vacía.
    def test_validez_datos(self):
        self.assertIsInstance(datos_usuario["nombre"], str)
        self.assertIsInstance(datos_usuario["edad"], int)
        self.assertIsInstance(datos_usuario["fecha_nacimiento"], str)
        self.assertIsInstance(datos_usuario["lenguajes_programacion"], list)

        self.assertGreater(datos_usuario["edad"], 0)
        self.assertGreater(len(datos_usuario["lenguajes_programacion"]), 0)

# =============================================================================
# EJECUCIÓN DE LOS TESTS
# =============================================================================
# Pasos sugeridos:
# - Agrega el bloque 'if __name__ == "__main__":' y llama a 'unittest.main()' 
#   para ejecutar las pruebas automáticamente al correr el script.

if __name__ == "__main__":
    unittest.main()