# =============================================================================
# DIFICULTAD EXTRA: EXCEPCIONES PERSONALIZADAS Y CONTROL MULTI-ERROR
# =============================================================================

# --- 1. DEFINICIÓN DE EXCEPCIÓN PERSONALIZADA ---
# - Crear una clase que herede de la clase base 'Exception' (o 'ValueError').
# - Sintaxis: class MiExcepcionPersonalizadaError(Exception):
# - Puede contener un constructor o simplemente 'pass'.
class MiExcepcionPersonalizadaError(Exception):
    pass
# --- 2. FUNCIÓN CON MÚLTIPLES DISPAROS DE EXCEPCIÓN ---
# - Definir la función 'procesar_parametros(param1, param2)':
#     - Caso Error 1 (TypeError): Si algún parámetro no es del tipo esperado (ej. no es int/float),
#       lanzar manualmente con 'raise TypeError("Mensaje...")'.
#     - Caso Error 2 (ValueError): Si un valor numérico no cumple un rango o condición (ej. valor negativo),
#       lanzar manualmente con 'raise ValueError("Mensaje...")'.
#     - Caso Error 3 (Custom Exception): Si se cumple una regla de negocio específica (ej. valor igual a cero),
#       lanzar manualmente 'raise MiExcepcionPersonalizadaError("Mensaje...")'.
#     - Si todo es correcto, retornar o procesar el resultado de los parámetros.
def procesar_parametros(param1, param2):
    if not isinstance(param1, (int,float)) or not isinstance(param2, (int,float)):
        raise TypeError("Debe ser entero o decimal")
    if param1 < 0 or param2 < 0:
        raise ValueError("No puede ser negativo")
    if param1 == 0 or param2 == 0:
        raise MiExcepcionPersonalizadaError("No puede ser igual a cero")
    return param1 + param2
# --- 3. BLOQUE PRINCIPAL DE CAPTURA Y CONTROL DE FLUJO ---
# - Crear un bloque 'try' donde se convoque 'procesar_parametros(...)':
#     - Probar llamadas con datos válidos e inválidos para validar cada flujo.
#
# - Múltiples bloques 'except':
#     - except MiExcepcionPersonalizadaError as e: Capturar y mostrar tipo y mensaje.
#     - except TypeError as e: Capturar y mostrar tipo y mensaje.
#     - except ValueError as e: Capturar y mostrar tipo y mensaje.
#     - except Exception as e: Capturar cualquier otra excepción genérica no prevista.
#
# - Cláusula 'else':
#     - Se ejecuta ÚNICAMENTE si el bloque 'try' no lanzó ninguna excepción.
#     - Imprimir mensaje indicando que la procesamiento fue exitoso.
#
# - Cláusula 'finally':
#     - Se ejecuta SIEMPRE, haya ocurrido un error o no.
#     - Imprimir mensaje indicando que la ejecución de la función ha finalizado.
try:
    proceso = procesar_parametros(4,10)
except MiExcepcionPersonalizadaError as e:
    print(e)
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)

else:
    print(f"El proceso fue exitoso {proceso}")

finally:
    print("La ejecucion finalizo")