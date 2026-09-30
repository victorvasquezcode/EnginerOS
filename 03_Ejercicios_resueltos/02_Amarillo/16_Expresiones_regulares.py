# --- DIFICULTAD EXTRA (OPCIONAL): VALIDACIÓN DE FORMATOS COMUNES ---

# Pasos sugeridos para la dificultad extra:
# Implementa 3 expresiones regulares para validar patrones específicos mediante funciones de coincidencia completa (ej. 're.match()' o 're.fullmatch()'):
import re
# 1. Validación de Email:
#    - Diseña el patrón Regex:
#      * Nombre de usuario (letras, números, puntos, guiones).
#      * Símbolo obligatorio '@'.
#      * Dominio (letras, números, guiones).
#      * Punto y extensión de dominio (ej. '.com', '.org', '.edu.pe' de 2 a más caracteres).
#    - Crea una función de prueba que reciba un email y devuelva si es válido o no.
def validar_email(email):
    patron = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(patron, email):
        print("Validacion exitosa")
        return bool(re.match(patron,email))
    else: 
        print(f"Correo '{email}' invalido")
        return False

# 2. Validación de Número de Teléfono:
#    - Diseña el patrón Regex:
#      * Código de país opcional (ej. +51 o +1).
#      * Separadores opcionales (espacios, guiones o paréntesis).
#      * Secuencia de dígitos según el estándar elegido (ej. 9 dígitos para celulares).
#    - Crea una función de prueba que reciba un número y devuelva si es válido o no.
def validar_telefono(telefono):
    patron = r"^(\+\d{1,3})?[\s-]?\d{3}[\s-]?\d{3}[\s-]?\d{3}$"
    if re.match(patron,telefono):
        print("Validacion exitosa")
        return bool(re.match(patron,telefono))
    else:
        print(f"Telefono '{telefono}' invalido")
        return False
    
# 3. Validación de URL:
#    - Diseña el patrón Regex:
#      * Protocolo obligatorio u opcional ('http://' o 'https://').
#      * Subdominio opcional ('www.').
#      * Nombre de dominio y TLD (ej. 'github.com').
#      * Ruta, parámetros o puertos opcionales al final.
#    - Crea una función de prueba que reciba una URL y devuelva si es válida o no.
def validar_url(url):
    patron = r"^(https?://)?(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+(/[a-zA-Z0-9#?&=_.-]*)?$"
    if re.match(patron,url):
        print("Validacion exitosa")
        return bool(re.match(patron,url))
    else:
        print(f"Url '{url}' invalido")
        return False
    
# 4. Prueba las 3 funciones con casos válidos e inválidos e imprime los resultados en consola.

if __name__ == "__main__":
    validar_email("javier_2193@live.com")
    validar_email("correo_sin_arroba")
    validar_telefono("+51-916487419")
    validar_telefono("123")
    validar_url("http://")
    validar_url("www.google.com")