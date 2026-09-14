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


# =============================================================================
# PARTE 2: DIFICULTAD EXTRA - AGENDA DE CONTACTOS
# =============================================================================

# --- 1. ESTRUCTURA DE DATOS PRINCIPAL ---
# Razonar: ¿Qué estructura native es ideal para buscar rápido un contacto por su NOMBRE?
# Pista: Un diccionario donde la "clave" sea el nombre y el "valor" sea el teléfono.
agenda = {}

# --- 2. FUNCIONES DE VALIDACIÓN ---
# Crear una función para validar el teléfono según las reglas:
# - ¿El valor ingresado contiene solo dígitos numéricos?
# - ¿La longitud está dentro del límite permitido (ej. mayor a 0 y menor o igual a 11)?
# - Retornar un booleano (True/False) para saber si pasa la prueba.
def es_telefono_valido (telefono: str) -> bool:
    paso_prueba = False
    if telefono.isdigit() and 0 < len(telefono) <= 11:
        paso_prueba = True
    return paso_prueba


# --- 3. FUNCIONES DE OPERACIONES DE LA AGENDA ---

# Función: BÚSQUEDA
# - Pedir el nombre a buscar.
# - Verificar si existe en la estructura.
# - Si existe: mostrar nombre y teléfono.
# - Si no existe: mostrar mensaje de error.
def buscar_contacto(nombre: str):
    if nombre in agenda:
        print(f"Contacto: {nombre} | Telefono: {agenda[nombre]}")
    else:
        print(f"El contacto '{nombre}' no existe en la agenda.")

# Función: INSERCIÓN
# - Pedir el nombre del nuevo contacto.
# - Pedir el teléfono y usar la función de validación dentro de un bucle hasta que sea válido.
# - Si el nombre ya existe, avisar al usuario o redirigir a actualización.
# - Guardar la relación nombre -> teléfono.
def insertar_contacto():
    nombre = input("Ingresar el nombre del contacto: ").strip().capitalize()

    if nombre in agenda:
        print(f"El contacto {nombre} ya existe en la agenda")
        opcion = input(f"Desea actualizar el contacto '{nombre}'? (si/no): ").strip().lower()

        if opcion in ("si", "sí", "s"):
            actualizar_contacto()
            return
        else:
            print("Operacion cancelada.")
            return
    
    while True:
        telefono = input("Ingresar el numero del contacto (max. 11 digitos): ").strip()
        if es_telefono_valido(telefono):
            break
        print("Numero invalido. Debe contener solo digitos y tenerhasta 11 caracteres.")

    agenda[nombre] = telefono
    print(f"Contacto '{nombre}' guardado exitosamente.")


# Función: ACTUALIZACIÓN
# - Pedir el nombre del contacto a actualizar.
# - Verificar si existe.
# - Si existe: pedir el nuevo teléfono (validándolo) y actualizar el valor.
# - Si no existe: informar que no se encontró el contacto.

def actualizar_contacto():
    nombre = input("Ingresar el nombre del contacto para actualizar: ").strip().capitalize()
    if nombre in agenda:
        while True:
            nuevo_telefono = input("Ingresar el nuevo telefono: ").strip()
            if es_telefono_valido(nuevo_telefono):
                break
            print("Numero invalido.")
        agenda[nombre] = nuevo_telefono
        print("Telefono actualizado correctamente.")
    else:
        print(f"El contacto '{nombre}' no existe.")

# Función: ELIMINACIÓN
# - Pedir el nombre a eliminar.
# - Verificar si existe.
# - Si existe: borrar el registro de la estructura y confirmar al usuario.
# - Si no existe: informar que no se encontró.
def eliminar_contacto():
    nombre = input("Ingresa el nombre del contacto para eliminar: ").strip().capitalize()
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto '{nombre}' eliminado.")
    else:
        print(f"El contacto '{nombre}' no existe.")


# --- 4. BUCLE PRINCIPAL Y MENÚ DE INTERACCIÓN ---
# - Definir una variable de control para mantener el programa activo (ej. ejecutable = True).
# - Iniciar bucle while:
#     - Mostrar las opciones del menú (1. Buscar, 2. Insertar, 3. Actualizar, 4. Eliminar, 5. Salir).
#     - Leer la opción seleccionada por el usuario.
#     - Evaluar la opción (usar estructuras condicionales if / elif / else o match/case):
#         - Caso 1: Llamar función de Búsqueda.
#         - Caso 2: Llamar función de Inserción.
#         - Caso 3: Llamar función de Actualización.
#         - Caso 4: Llamar función de Eliminación.
#         - Caso 5: Cambiar variable de control para romper el bucle y despedir al usuario.
#         - Caso Default: Notificar que la opción elegida no es válida.

def menu_principal():
    while True:
        print("\n--- AGENDA DE CONTACTOS ---")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion_seleccionada = input("Ingrese una opcion (1-5): ").strip()

        match opcion_seleccionada:
            case "1":
                nombre = input("Ingrese el nombre de contacto a buscar: ").strip().capitalize()
                buscar_contacto(nombre)
            case "2":
                insertar_contacto()
            case "3":
                actualizar_contacto()
            case "4":
                eliminar_contacto()
            case "5":
                print("¡Hasta Luego! Gracias por usar la agenda.")
                break
            case _:
                print("Opcion no valida. Por favor, ingrese un numero del 1 al 5.")

if __name__ == "__main__":
    menu_principal()