# 01 ==========================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# =============================================================================
# Enunciado: Crea un programa que imprima por consola todos los números
# comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16
# ni múltiplos de 3.
#
# Pasos sugeridos:
# - Genera un bucle que recorra los números desde 10 hasta 55 (inclusive).
# - Aplica las condiciones en un 'if':
#   1. Que sea par -> (numero % 2 == 0)
#   2. Que sea diferente de 16 -> (numero != 16)
#   3. Que NO sea múltiplo de 3 -> (numero % 3 != 0)
# - Imprime únicamente los números que cumplan TODAS las condiciones simultáneamente.

# 02 ==========================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# =============================================================================
# Enunciado: Crea una función que reciba dos parámetros de tipo cadena de texto
# y retorne un número.
# - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#   * Si el número es múltiplo de 3, muestra la cadena del primer parámetro.
#   * Si el número es múltiplo de 5, muestra la cadena del segundo parámetro.
#   * Si es múltiplo de 3 y de 5 (múltiplo de 15), muestra ambas concatenadas.
#   * Si no cumple ninguna, imprime el número.
#   * La función retorna el número de veces que se ha impreso el NÚMERO en lugar de los textos.
#
# Pasos sugeridos:
# - Define la función con type hints -> def fizz_buzz_custom(texto1: str, texto2: str) -> int:
# - Inicializa un contador para llevar el registro de cuántas veces se imprime un número.
# - Genera un bucle del 1 al 100 inclusive.
# - Implementa la lógica condicional priorizando el caso compuesto (múltiplo de 3 Y de 5).
# - En el caso base de la condición (else), imprime el número e incrementa el contador.
# - Retorna el contador final y muestra el resultado del retorno en consola.

# 13 ==========================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# =============================================================================
# Enunciado: Crea un diccionario con las claves: "name", "age", "birth_date" y
# "programming_languages". Crea dos test:
# - El primero determina que existen todos los campos (claves).
# - El segundo determina que los datos introducidos son del tipo correcto o válidos.

# --- ESTRUCTURA DE DATOS A EVALUAR ---
# Pasos sugeridos:
# - Define el diccionario 'datos_usuario' con la estructura requerida.


# --- TEST UNITARIO DEL DICCIONARIO ---
# Pasos sugeridos:
# - Crea una clase de prueba 'TestDatosUsuario' que herede de 'unittest.TestCase'.
#
# - TEST 1: VERIFICAR EXISTENCIA DE CAMPOS:
#   * Define 'test_existencia_campos(self)'.
#   * Obtén las claves del diccionario.
#   * Comprueba con 'self.assertIn()' o 'self.assertTrue()' que las 4 claves requeridas
#     existan dentro del diccionario.
#
# - TEST 2: VERIFICAR TIPOS DE DATOS Y VALIDEZ:
#   * Define 'test_validez_datos(self)'.
#   * Usa 'self.assertIsInstance()' para validar que 'name' sea str, 'age' sea int,
#     'birth_date' sea str y 'programming_languages' sea list.
#   * Opcional: Verifica con 'self.assertGreater()' que la edad sea mayor a 0 y que
#     la lista de lenguajes no esté vacía.


# =============================================================================
# EJECUCIÓN DE LOS TESTS
# =============================================================================
# Pasos sugeridos:
# - Agrega el bloque 'if __name__ == "__main__":' y llama a 'unittest.main()' 
#   para ejecutar las pruebas automáticamente al correr el script.