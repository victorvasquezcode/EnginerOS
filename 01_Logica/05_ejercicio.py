# =============================================================================
# PARTE 1: ASIGNACIÓN Y PASO DE PARÁMETROS EN PYTHON (VALOR VS. REFERENCIA)
# =============================================================================
# Nota conceptual previa para Python:
# En Python todo es un objeto. No existe la asignación por valor o referencia tradicional,
# sino el concepto de "Paso por Asignación de Objeto" (Pass-by-object-reference):
# - Tipos Inmutables (se comportan como "por valor"): int, float, str, bool, tuple.
# - Tipos Mutables (se comportan como "por referencia"): list, dict, set.


# 1. Asignación de Variables por Valor (Tipos Inmutables):
# - Crear una variable original con un tipo inmutable (ej. entero o string).
# - Asignar esa variable a una nueva variable (copia de valor).
# - Modificar la segunda variable y comprobar que la primera permanece inalterada.
variable_original = "Victor Javier Vasquez Trauco"
variable_nueva = variable_original
variable_nueva = "Victor Javier"

print(f"Variable original: {variable_original}")
print(f"Variable nueva: {variable_nueva}")

# 2. Asignación de Variables por Referencia (Tipos Mutables):
# - Crear una variable original con un tipo mutable (ej. una lista).
# - Asignar esa variable a una nueva variable (comparten la misma posición en memoria).
# - Modificar la segunda variable (ej. .append()) y comprobar que la primera también cambia.
variable_original_mutable = ["Pera", "Manzana", "Kiwi"]
nueva_variable_mutable = variable_original_mutable
nueva_variable_mutable.append("Tomate")

print(f"Variable original: {variable_original_mutable}")
print(f"Variable nueva: {nueva_variable_mutable}")

# 3. Funciones con Parámetros Inmutables ("Por Valor"):
# - Definir una función que reciba un argumento inmutable (ej. int).
# - Modificar el valor del parámetro dentro del cuerpo de la función.
# - Demostrar que la variable original fuera de la función NO sufre ningún cambio.
def modificar_valor(numero:int):
    numero+=10
    print(f"Dentro de la funcion: {numero}")

mi_numero = 15
print(f"\nAntes de la funcion: {mi_numero}")
modificar_valor(mi_numero)
print(f"Despues de la funcion: {mi_numero}")

# 4. Funciones con Parámetros Mutables ("Por Referencia"):
# - Definir una función que reciba un argumento mutable (ej. list).
# - Modificar la estructura directamente dentro de la función (ej. .append() o .clear()).
# - Demostrar que la variable original fuera de la función SÍ se modifica.
# - Mostrar la excepción: Reasignar la variable dentro de la función (`lista = [...]`) rompe la referencia.
def modificar_estructura(lista: list):
    lista.append("Lapiz")
    print(f"Dentro de la funcion (modificacion directa): {lista}")

def reasignar_estructura(lista: list):
    lista = ["Borrador", "Tajador"]
    print(f"Dentro de la funcion (reasignacion): {lista}")

lista_colegio = ["Cuaderno", "Regla"]
print(f"\nLista original inicial: {lista_colegio}")

modificar_estructura(lista_colegio)
print(f"Despues de modificar estructura: {lista_colegio}")

reasignar_estructura(lista_colegio)
print(f"Despues de reasignar_estructura: {lista_colegio}")