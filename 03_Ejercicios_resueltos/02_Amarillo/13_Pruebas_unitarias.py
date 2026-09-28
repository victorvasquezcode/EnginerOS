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

import unittest


datos_usuario ={
    "nombre": "Victor",
    "edad": 26,
    "fecha_cumpleaños" : "28-06-2000",
    "lenguajes": ["Python", "SQL"]
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
        claves = datos_usuario.keys()
        self.assertIn("nombre", claves)
        self.assertIn("edad", claves)
        self.assertIn("fecha_cumpleaños", claves)
        self.assertIn("lenguajes", claves)

# - TEST 2: VERIFICAR TIPOS DE DATOS Y VALIDEZ:
#   * Define 'test_validez_datos(self)'.
#   * Usa 'self.assertIsInstance()' para validar que 'name' sea str, 'age' sea int,
#     'birth_date' sea str y 'programming_languages' sea list.
#   * Opcional: Verifica con 'self.assertGreater()' que la edad sea mayor a 0 y que
#     la lista de lenguajes no esté vacía.
    def test_validez_datos(self):
        self.assertIsInstance(datos_usuario["nombre"], str)
        self.assertIsInstance(datos_usuario["edad"], int)
        self.assertIsInstance(datos_usuario["fecha_cumpleaños"], str)
        self.assertIsInstance(datos_usuario["lenguajes"], list)
        self.assertGreater(datos_usuario["edad"] , 0)
        self.assertGreater(len(datos_usuario["lenguajes"]) , 0)

# =============================================================================
# EJECUCIÓN DE LOS TESTS
# =============================================================================
# Pasos sugeridos:
# - Agrega el bloque 'if __name__ == "__main__":' y llama a 'unittest.main()' 
#   para ejecutar las pruebas automáticamente al correr el script.

if __name__ == "__main__":unittest.main()