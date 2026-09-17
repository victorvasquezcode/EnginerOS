# =============================================================================
# PARTE 1: MANEJO BÁSICO DE EXCEPCIONES (try - except - else - finally)
# =============================================================================
# Las excepciones permiten gestionar errores en tiempo de ejecución sin que
# el programa se detenga de manera abrupta (crash).


# 1. Provocar y Capturar Error de División por Cero (ZeroDivisionError):
# - Estructura 'try': Bloque de código donde se intenta ejecutar la operación riesgosa (10 / 0).
# - Estructura 'except ZeroDivisionError as e':
#     - Capturar específicamente la excepción de división por cero.
#     - Imprimir el mensaje de error capturado sin detener el programa.
try:
    division = 10/0
except ZeroDivisionError as e:
    print(f"Error capturado {e}")


# 2. Provocar y Capturar Error de Índice Fuera de Rango (IndexError):
# - Definir una lista de prueba (ej. numeros = [1, 2, 3]).
# - Estructura 'try': Intentar acceder a un índice inexistente (ej. numeros[5]).
# - Estructura 'except IndexError as e':
#     - Capturar la excepción de índice fuera de límites.
#     - Imprimir el error correspondiente.
numero = [1, 2, 3]
try:
    numero[5]
except IndexError as e:
    print(f"Error capturado {type(e).__name__}")


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
    if not isinstance(param1, (int,float)):
        raise TypeError("El primer parametro debe ser un numero entero o decimal.")
    if param2 < 0:
        raise ValueError("El segundo parametro no puede ser un numero negativo")
    if param1 == 0 and param2 == 0:
        raise MiExcepcionPersonalizadaError("Ambos parametros son cero")
    return param1 / param2


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

def probrar(p1,p2):
    print(f"\n--- Probando con: param1= {p1}, param2= {p2} ---")
    try:
        resultado = procesar_parametros(p1,p2)
    except MiExcepcionPersonalizadaError as e:
        print(f"⚠️ Error Personalizado [{type(e).__name__}]: {e}")
    except TypeError as e:
        print(f"⚠️ Error de Tipo [{type(e).__name__}]: {e}")
    except ValueError as e:
        print(f"⚠️ Error de Valor [{type(e).__name__}]: {e}")
    except Exception as e:
        print(f"⚠️ Error Generico [{type(e).__name__}]: {e}")
    else:
        print(f"✅ Procesamiento exitoso. Resultado: {resultado}")
    finally:
        print("🔒 La ejecucion ha finalizado.")

probrar("5", -10)
probrar(10, -5)
probrar(0, 0)
probrar(10, 2)