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