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