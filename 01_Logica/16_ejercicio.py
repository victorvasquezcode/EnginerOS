# --- EJERCICIO PRINCIPAL: BÚSQUEDA Y EXTRACCIÓN CON EXPRESIONES REGULARES ---

# Pasos sugeridos para el ejercicio principal:
# 1. Importa el módulo nativo de expresiones regulares de tu lenguaje (ej. 're' en Python).
import re
# 2. Define una cadena de texto de prueba que contenga varios números intercalados (enteros, positivos, etc.).
cadena_texto = "Tengo 35 manzanas, 2 perros y naci el año 2000"
# 3. Diseña el patrón de Expresión Regular (Regex):
#    - Debe coincidir con secuencias de uno o más dígitos numéricos (usando meta-caracteres como '\d' y cuantificadores como '+').
patron = r"\d+"
# 4. Aplica el método de búsqueda/extracción global sobre la cadena:
#    - Utiliza la función correspondiente para encontrar todas las coincidencias globales (ej. 're.findall()' en Python).
numeros_extraidos = re.findall(patron,cadena_texto)
# 5. Imprime el texto original y la lista con todos los números extraídos.
print(f"Texto original: {cadena_texto}\nLista de numeros extraidos: {numeros_extraidos}")