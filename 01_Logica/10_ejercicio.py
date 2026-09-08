# =============================================================================
# RETO 10: MANEJO DE EXCEPCIONES Y ERRORES
# =============================================================================

# -----------------------------------------------------------------------------
# 1. EJERCICIO PRINCIPAL: CAPTURA DE ERRORES BÁSICOS
# -----------------------------------------------------------------------------

print("=== MANEJO BÁSICO DE EXCEPCIONES ===")

# --- Prueba 1: División entre cero ---
try:
    resultado = 10/0
except ZeroDivisionError as error:
    print(f"Error capturado correctamente {error}")


# --- Prueba 2: Índice fuera de rango en lista ---
try:
    lista = [10, 20, 30]
    elemento = lista[5]
except IndexError as error:
    print(f"Error capturado correctamente {error}")
    pass

print("El programa continuó su ejecución sin colapsar.\n")


# =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# =============================================================================

print("=== DIFICULTAD EXTRA ===")

# --- 1. Tu Excepción Personalizada ---
class MiExcepcionPersonalizadaError(Exception):
    pass


# --- 2. Función procesadora de parámetros ---
def procesar_parametros(a: int, b: int, lista: list):
    """
    Debe lanzar 3 excepciones distintas:
    1. MiExcepcionPersonalizadaError (lanzada manualmente con 'raise' si a < 0)
    2. ZeroDivisionError (si b == 0)
    3. IndexError (si intentas acceder a un índice fuera de rango en 'lista')
    """
    # TODO 1: Si 'a' es menor a 0, lanza con 'raise' tu excepción personalizada
    if a < 0:
        raise MiExcepcionPersonalizadaError("El valor de 'a' no puede ser negativo.")
    # TODO 2: Realiza la división a / b (esto provocará ZeroDivisionError si b es 0)
    resultado = a/b
    # TODO 3: Accede a lista[a] (esto provocará IndexError si el índice no existe)
    acceder_lista = lista[a]
    # TODO 4: Retorna un mensaje exitoso con los resultados si todo salió bien
    return f"Division: {resultado}, Elemento: {acceder_lista}"


# --- 3. Invocación y captura completa ---
def probar_procesamiento(a, b, lista):
    try:
        prueba_division = procesar_parametros(a,b,lista)
    except ZeroDivisionError as e:
        print(f"Error de tipo [{type(e).__name__}]: {e}")
    except IndexError as e:
        print(f"Error de tipo [{type(e).__name__}]: {e}")
    except MiExcepcionPersonalizadaError as e:
        print(f"Error de tipo [{type(e).__name__}]: {e}")
    else:
        # TODO: Se ejecuta si NO hubo ningún error (Imprime éxito)
        print(f"Todo Salio Con Exito: {prueba_division}")
    finally:
        # TODO: Se ejecuta SIEMPRE (Imprime que la ejecución ha finalizado)
        print("La ejecucion a terminado")



#--- Casos de Prueba (Descomenta conforme vayas programando) ---
print("Caso 1: Ejecución limpia")
probar_procesamiento(1, 2, ["a", "b", "c"])

print("\nCaso 2: Provocando ZeroDivisionError")
probar_procesamiento(10, 0, [1, 2])

print("\nCaso 3: Provocando IndexError")
probar_procesamiento(5, 2, [1, 2])

print("\nCaso 4: Provocando MiExcepcionPersonalizadaError")
probar_procesamiento(-5, 2, [1, 2])