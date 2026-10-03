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