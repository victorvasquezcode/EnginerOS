# ==============================================================================
# PARTE 1: DEFINICIÓN DE ENUMERADOS (ENUM) Y MAPPING SIMPLE
# ==============================================================================

# Importar el módulo 'enum' nativo de Python para trabajar con la clase 'Enum'.

# Definir la clase enumerada 'DiaSemana' heredando de 'Enum':
# - Asignar a cada día de la semana (LUNES a DOMINGO) un valor entero consecutivo del 1 al 7.

# Definir una función que reciba un número entero (1 al 7):
# - Validar si el número está dentro del rango permitido (1-7).
# - Encontrar el miembro correspondiente del Enum mediante su valor numérico: DiaSemana(numero).
# - Retornar o imprimir el nombre del día (.name).
# - Capturar posibles errores (ValueError) si se ingresa un número fuera del rango.
from enum import Enum

class DiaSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

def numero_entero(n: int) -> str:
    try:
        return DiaSemana(n).name
    except ValueError as e:
        return "Numero fuera de rango"

# Pruebas de la Parte 1:
# - Probar la función de día de la semana con números válidos (ej. 1, 5) e inválidos (ej. 8).

print("--- PRUEBAS PARTE 1: Enum DiaSemana ---")
print(numero_entero(1))  # Salida: LUNES
print(numero_entero(5))  # Salida: VIERNES
print(numero_entero(8))  # Salida: Número fuera de rango