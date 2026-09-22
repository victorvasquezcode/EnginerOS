# =============================================================================
# PARTE 1: ESTRUCTURAS DE DATOS NATIVAS (REPASO)
# =============================================================================

# LISTAS (Ordenadas, mutables, duplicados)
# 1. Creación: Inicializar lista.
# 2. Inserción: Agregar elementos al final y en posición específica.
# 3. Borrado: Eliminar por valor y por índice/posición.
# 4. Actualización: Modificar el valor de una posición específica.
# 5. Ordenación: Ordenar de forma ascendente, descendente y sin modificar la original.
lista = ["Manzana", "Pera", "Platano"]
lista.append("Mandarina")
lista.insert(1,"Arandano")

lista.remove("Manzana")
fruta_eliminada = lista.pop(1)

lista[1] = ("Tomate")

lista.sort(key=str.lower)
lista.sort(reverse=True)
nueva_lista = sorted(lista)

print(lista,nueva_lista)


# TUPLAS (Ordenadas, inmutables, duplicados)
# 1. Creación: Inicializar tupla.
# 2. Inserción/Borrado/Actualización: Explicar o probar qué ocurre si se intenta modificar.
# 3. Ordenación: Convertir a una estructura mutable o usar funciones globales que devuelvan listas.
tupla = ("Borrador","Lapiz","Cuaderno")

try:
    tupla[0] = "Tajador"
except TypeError as e:
    print(f"Error al intentar modificar la tupla: {e}")

tupla_ordenada = sorted(tupla)
print(f"Ordenada con sorted() (devuelve lista): {tupla_ordenada}")

lista_desde_tupla = list(tupla)
lista_desde_tupla.append("Regla")
tupla_actualizada = tuple(lista_desde_tupla)
print(f"Tupla reconstruida: {tupla_actualizada}")

# CONJUNTOS / SETS (Desordenados, mutables, NO duplicados)
# 1. Creación: Inicializar conjunto.
# 2. Inserción: Agregar elementos individuales y múltiples.
# 3. Borrado: Eliminar elementos (manejo de error si no existe vs borrado seguro).
# 4. Actualización: Explicar por qué no hay acceso por índice (remover e insertar).
# 5. Ordenación: Convertir a lista si se requiere un orden visual temporal.
conjuntos = {"Manzana", "Pera", "Platano"}
set_vacio = set()

conjuntos.add("Mandarina")
conjuntos.update(["Uva", "Ciruela", "Pera"])

try:
    conjuntos.remove("Platano")
except KeyError:
    print("El elemento no existe en el conjunto.")

conjuntos.discard("Manzana")

if "Pera" in conjuntos:
    conjuntos.remove("Pera")
    conjuntos.add("Mango")

conjuntos_ordenados = sorted(conjuntos)

print(f"Conjunto final (sin duplicados): {conjuntos}")
print(f"Lista ordenada generada desde el set: {conjuntos_ordenados}")

# DICCIONARIOS (Pares Clave-Valor, mutables, claves únicas)
# 1. Creación: Inicializar diccionario.
# 2. Inserción: Añadir nueva clave con su valor.
# 3. Borrado: Eliminar por clave.
# 4. Actualización: Cambiar el valor asociado a una clave existente.
# 5. Ordenación: Ordenar por claves o por valores (devuelve vistas o listas).
usuarios = {
    "nombre": "Javier",
    "edad"  : 26,
    "carrera" : "Sistemas"
}

usuarios["cargo"] = "Admin"

usuarios.pop("edad")
del usuarios["carrera"]

usuarios["nombre"] = "Victor"

claves_ordenadas = sorted(usuarios.keys())
print(f"Claves ordenadas: {claves_ordenadas}")

valor_ordenados = sorted(usuarios.values())
print(f"Valores ordenados: {valor_ordenados}")

diccionario_ordenado = dict(sorted(usuarios.items()))
print(f"Diccionario ordenado: {diccionario_ordenado}")