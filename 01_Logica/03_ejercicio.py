# =============================================================================
# RETO 03: ESTRUCTURAS DE DATOS
# Enunciado:
# 1. Muestra ejemplos de creación de todas las estructuras soportadas por defecto en Python:
#    - Listas (list)
#    - Tuplas (tuple)
#    - Diccionarios (dict)
#    - Conjuntos (set)
# 2. Operaciones principales: Inserción, Borrado, Actualización y Ordenación en cada una.
# =============================================================================

# -----------------------------------------------------------------------------
# 1. LISTAS (List) - Mutables, ordenadas y permiten duplicados
# Pista: Usa append(), insert(), remove(), pop(), ordenación con sort() o sorted().
# -----------------------------------------------------------------------------
print("--- 1. LISTAS ---")
mercado = ['manzana','zanahoria','tomate','berengena']
mercado.append('pera')
mercado.insert(1,'uva')
mercado.remove('manzana')
elemento_eliminado = mercado.pop()
mercado[2] = 'lechuga'
mercado.sort()
mercado_ordenado = sorted(mercado, reverse=True)
print(f"Lista modificada: {mercado}")
print(f"Lista modificada al revez: {mercado_ordenado}")
print(f"Elemento sacado con pop: {elemento_eliminado}")



# -----------------------------------------------------------------------------
# 2. TUPLAS (Tuple) - Inmutables, ordenadas y permiten duplicados
# Pista: No se pueden modificar directamente. ¿Qué pasa si intentas alterar un valor?
# -----------------------------------------------------------------------------
print("\n--- 2. TUPLAS ---")
componentes = ("memoria","gpu","cpu")
print (f"Primer componenete: {componentes[0]}")

#componentes[0] = "fuente"
# Tener en cuenta que una tupla es inmutable no se puede cambiar el valor

ram , grafica , procesador = componentes
print(f"Tengo una GPU: {grafica} y una CPU: {procesador}")


# -----------------------------------------------------------------------------
# 3. DICCIONARIOS (Dict) - Mutables, mapeo Clave-Valor, claves únicas
# Pista: Usa dict[clave] = valor, pop(), del, keys(), values(), items().
# -----------------------------------------------------------------------------
print("\n--- 3. DICCIONARIOS ---")
perfil = {
    "nombre" :"victor", 
    "apellido" : "Vasquez",
    "edad" : 26
    } 
print(f"Nombre de usuario: {perfil['nombre']}")
perfil["cargo"] = "Asistente"
perfil["edad"] = 27
perfil.pop("apellido")
print("\nDatos actuales del perfil:")
for clave, valor in perfil.items():
    print(f"- {clave.capitalize()}: {valor}")



# -----------------------------------------------------------------------------
# 4. CONJUNTOS (Set) - Mutables, no ordenados, NO permiten duplicados
# Pista: Usa add(), remove(), discard(). Útil para eliminar duplicados de listas.
# -----------------------------------------------------------------------------
print("\n--- 4. CONJUNTOS (SETS) ---")
numeros = {1,2,3,4,4,4,4,4,4}
numeros.add(5)
numeros.remove(2)
numeros.discard(1)
print(list(numeros))


# =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# Enunciado: Crea una agenda de contactos por terminal.
# - Funcionalidades: Búsqueda, inserción, actualización y eliminación de contactos.
# - Datos: Cada contacto tiene Nombre y Teléfono.
# - Validaciones: El teléfono debe ser numérico (.isdigit()) y tener máximo 11 dígitos (len() <= 11).
### - Incluye opción para salir/finalizar el programa. 
# =============================================================================
agenda={
    "victor" : "916487419"
}

while True:
    print("\nAgenda de Contactos:")
    print("1. Buscar contacto")
    print("2. Insertar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Salir del programa")
    opcion_usuario = input("Selecciona un numero del (1-5): ")

    if opcion_usuario == "1":
        print("Desea buscar por nombre o por numero (1.Nombre , 2.Numero)")
        while True:

            buscar_contacto = input ("Seleccione una opcion (1-2): ")

            if buscar_contacto == "1":
                
                buscar_contacto_nombre = input("Cual es el nombre de la persona que deseas buscar: ")

                if buscar_contacto_nombre in agenda:
                    print(f"La persona es {buscar_contacto_nombre} con el numero {agenda[buscar_contacto_nombre]}")
                else:
                    print("No existe en la agenda")
                break

            elif buscar_contacto == "2":

                buscar_contacto_numero = input("Cual es el numero de la persona que deseas buscar: ")

                if not (buscar_contacto_numero.isdigit() and len(buscar_contacto_numero) <= 11):
                    print("El numero debe ser digito y tener 11 digitos o menos")
                    continue

                encontrado = False
                for nombre,numero in agenda.items():
                    if numero == buscar_contacto_numero:
                        print(f"El numero pertenece a: {nombre}")
                        encontrado = True
                        break

                if not encontrado:
                        print("No hay ninguna contacto registrado con ese numero")
                break
            else:
                print("Debe seleccionar una opcion valida (1-2)")
                continue

    elif opcion_usuario == "2":
        while True:
            while True:

                insertar_nombre = input ("Inserte el nombre del contacto: ")
                
                if not insertar_nombre.strip():
                    print("El nombre no debe estar vacio")
                    continue

                if insertar_nombre in agenda:
                    print("El contacto ya existe puedes cambiarlo en la opcion 3 (Actualizar)")
                    continue

                break

            while True:
                insertar_numero = input ("Inserte el numero del contacto: ")

                if insertar_numero in agenda.values():
                    print("Este numero ya pertenece a otro contacto.")
                    continue

                if insertar_numero.isdigit() and len(insertar_numero) <= 11:
                    agenda[insertar_nombre] = insertar_numero
                    print(f"Contacto {insertar_nombre.capitalize()} guardado correctamente con el numero {insertar_numero}")
                    break
                else:
                    print("El numero debe ser numero y tener maximo de 11 digitos")
                    continue

            while True:
                ingresar_otro_numero = input ("Desea ingresar otro numero ?(1-Si , 2-No): ")

                if ingresar_otro_numero == "1":
                    break
                elif ingresar_otro_numero == "2":
                    break
                else:
                    print("Ingrese un numero entre 1 y 2")

            if ingresar_otro_numero == "2":
                break

    elif opcion_usuario == "3":
        if not agenda:
            print(" La agenda esta vacia. No hay contactos para actualizar.")
        else:
            print("\n¿Que deseas actualizar?")
            print("1. Nombre del contacto")
            print("2. Telefono del contacto")

            while True:
                buscar_contacto_actualizar = input ("Selecciona una opcion (1-2): ")

                if buscar_contacto_actualizar == "1":
                    buscar_nombre_actualizar = input("Cual es el nombre del contacto: ")

                    if buscar_nombre_actualizar in agenda:
                        print(f"Se encontro el nombre '{buscar_nombre_actualizar}' en los contactos")
                        nuevo_nombre_actualizar = input(f"Cual es el nuevo nombre para '{buscar_nombre_actualizar}': ")

                        if not nuevo_nombre_actualizar.strip():
                            print("El nombre no puede estar vacio.")
                        elif nuevo_nombre_actualizar in agenda:
                            print("Ya existe otro contacto con ese nombre.")
                        else:
                            agenda [nuevo_nombre_actualizar] = agenda.pop(buscar_nombre_actualizar)
                            print(f"El contacto '{buscar_nombre_actualizar}' ahora se llama '{nuevo_nombre_actualizar}'")
                            break

                    else:
                        print(f"El contacto {buscar_nombre_actualizar} no existe en la agenda")
                        break

                elif buscar_contacto_actualizar == "2":
                    buscar_nombre_actualizar = input("Ingresa el nombre del contacto cuyo numero deseas que se cambie: ")

                    if buscar_nombre_actualizar in agenda:
                        while True:
                            nuevo_numero_actualizar = input(f"Ingrese el nuevo numero para el contacto '{buscar_nombre_actualizar}' : ")

                            if nuevo_numero_actualizar in agenda.values():
                                print("Este numero ya pertenece a otro contacto.")
                            elif nuevo_numero_actualizar.isdigit() and len(nuevo_numero_actualizar) <= 11:
                                agenda[buscar_nombre_actualizar] = nuevo_numero_actualizar
                                print(f"Numero de '{buscar_nombre_actualizar}' actualizado a '{nuevo_numero_actualizar}'")
                                break
                            else:
                                print("El numero debe contener solo digitos y maximo 11 caracteres.")
                        break
                    else:
                        print(f"El contacto {buscar_nombre_actualizar} no existe en la agenda")
                        break
                else:
                    print("Debe seleccionar una opcion valida (1 - 2)")

    elif opcion_usuario == "4":
        buscar_contacto_eliminar= input("Que contacto desea eliminar: ")

        if buscar_contacto_eliminar in agenda:
            agenda.pop(buscar_contacto_eliminar)
            print(f"El contacto {buscar_contacto_eliminar} a sido eliminado con exito.")

    elif opcion_usuario == "5":
        break
    else:
        print("No se selecciono ninguna opcion selecciones una opcion valida (1-5)")
        continue