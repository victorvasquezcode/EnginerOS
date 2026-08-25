# =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# Enunciado: Crea un programa que imprima por consola todos los números
# comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16
# ni múltiplos de 3.
# =============================================================================
# for numeros in range(10,56,2):
#     if numeros != 16 and  numeros % 3 != 0:
#         print(numeros)

# =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# Enunciado: Crea una función que reciba dos parámetros de tipo cadena de texto
# y retorne un número.
# - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#   - Si el número es múltiplo de 3, muestra la cadena del primer parámetro.
#   - Si el número es múltiplo de 5, muestra la cadena del segundo parámetro.
#   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas concatenadas.
#   - La función retorna el número de veces que se ha impreso el número en lugar
#     de los textos.
# =============================================================================
# def dificultad_extra(parametro1, parametro2):
#     contador = 0
#     for numero in range(1,101):
#         if numero % 3 == 0 and numero % 5 == 0:
#             print(f"{parametro1} {parametro2}")
#         elif numero % 3 == 0:
#             print(parametro1)
#         elif numero % 5 == 0:
#             print(parametro2)
#         else:
#             contador += 1
#             print(numero)
#     return contador

# resultado = dificultad_extra("Victor","Javier")
# print(f"El numero de veces que se imprimio el numero es : {resultado} ")


# =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# Enunciado: Crea una agenda de contactos por terminal.
# - Funcionalidades: Búsqueda, inserción, actualización y eliminación de contactos.
# - Datos: Cada contacto tiene Nombre y Teléfono.
# - Validaciones: El teléfono debe ser numérico (.isdigit()) y tener máximo 11 dígitos (len() <= 11).
# ## - Incluye opción para salir/finalizar el programa. 
# =============================================================================

# agenda = {
#     "Victor" : "916487419",
#     "Javier" : "916487420",
#     "Trauco" : "916487421"
# }
# while True:
#     print("Bienvenido a la agenda de contactos")
#     print("1. Buscar contacto")
#     print("2. Insertar contacto")
#     print("3. Actualizar contacto")
#     print("4. Eliminar contacto")
#     print("5. Salir del menu de agenda")
#     opcion = input("Ingrese un numero del (1-5): ")

#     if opcion == "1":
#         while True:
#             opcion_buscar = input("Desea buscar por nombre o numero de contacto (Nombre - 1 o Numero - 2): ")

#             if opcion_buscar == "1":
#                 opcion_buscar_nombre = input("El nombre del contacto que desea buscar: ")

#                 if not opcion_buscar_nombre.strip():
#                     print("No se ingreso un nombre esta vacio")
#                     continue
                    
#                 if opcion_buscar_nombre.capitalize() in agenda:
#                     print(f"Se encontro el contacto '{opcion_buscar_nombre.capitalize()}' con el numero '{agenda[opcion_buscar_nombre.capitalize()]}'")
#                 else:
#                     print("No se encontro el contacto")
                    
#             if opcion_buscar == "2":
#                 opcion_buscar_numero = input("El numero del contacto que desea buscar: ")

#                 if not opcion_buscar_numero.strip():
#                     print("No se ingreso un numero esta vacio")
#                     continue

#                 encontrado = False
#                 for clave , valor in agenda.items():
                
#                     if valor == opcion_buscar_numero:
#                         print(f"El numero {opcion_buscar_numero} es del contacto {clave}")
#                         encontrado = True
#                         break
                    
#                 if not encontrado:
#                     print("No se encontro el numero del contacto.")
#                     continue
#             else:
#                 print("Seleecione un valor valido")
#             opcion_salida_buscar = input("Desea buscar otro contacto ? (1 - Si o 2 - No): ")

#             if opcion_salida_buscar == "1":
#                 continue

#             if opcion_salida_buscar == "2":
#                 break

#     if opcion == "2":
#         while True:
#             while True:
#                 opcion_ingresar_nombre = input("Nombre del contacto que desea agregar: ")

#                 if not opcion_ingresar_nombre.strip():
#                     print("Ingrese el nombre del contacto no puede estar vacio")
#                     continue

#                 if opcion_ingresar_nombre.capitalize() in agenda:
#                     print("Contacto ya existe en la agenda")
#                     continue

#                 break

#             while True:    
#                 opcion_ingresar_numero = input("Numero del contacto que desea agregar: ")

#                 if not opcion_ingresar_numero.strip():
#                     print("Ingrese el numero del contacto no puede estar vacio")
#                     continue

#                 if opcion_ingresar_numero in agenda.values():
#                     print("Numero ya existe en la agenda")
#                     continue

#                 if opcion_ingresar_numero.isdigit() and len(opcion_ingresar_numero) <= 11:
#                     agenda[opcion_ingresar_nombre.capitalize()] = opcion_ingresar_numero
#                     print(f"Contacto agregado exitosamente '{opcion_ingresar_nombre}' con el numero '{opcion_ingresar_numero}'")

#                 break

#             opcion_salida_insertar = input("Desea agregar otro contacto? (Si-1,No-2): ")

#             if opcion_salida_insertar == "1":
#                 continue

#             elif opcion_salida_insertar == "2":
#                 break

#             else:
#                 print("Seleccione una opcion valida")

#     if opcion == "3":

#         if not agenda:
#             print("La agenda esta vacia no hay nada para actualizar")

#         while True:
#             print("\n¿Que desea Actualizar?")
#             print("1. Nombre del contacto")
#             print("2. Numero del contacto")

#             opcion_actualizar = input("Seleccion una opcion (1-2): ")

#             while True:
#                 if opcion_actualizar == "1":
#                     actualizar_nombre = input ("Cual es el nombre del contacto: ")

#                     if actualizar_nombre in agenda:
#                         print(f"Se encontro el contacto {actualizar_nombre}")
#                         nuevo_nombre = input("Cual es el nuevo nombre del contacto: ")

#                         if not nuevo_nombre.strip():
#                             print("El nuevo nombre esta vacio")
#                             continue
#                         elif nuevo_nombre in agenda:
#                             print("Ya existe un nombre registrado en la agenda")
#                             continue
#                         else:
#                             agenda [nuevo_nombre] = agenda.pop(actualizar_nombre)
#                             print(f"El contacto {actualizar_nombre} ahora se llama {nuevo_nombre}")
#                             break
#                     else:
#                         print(f"El contacto {actualizar_nombre} no existe en la agenda")

#                 elif opcion_actualizar == "2":
#                     actualizar_nombre_numero = input ("Cual es el nombre del contacto: ")

#                     if actualizar_nombre_numero in agenda:
#                         while True:
#                             actualizar_numero = input(f"Ingrese el nuevo numero para el contacto {actualizar_nombre_numero}: ")

#                             if actualizar_numero in agenda.values():
#                                 print("Este numero ya pertence a otro contacto")
#                             elif actualizar_numero.isdigit() and len(actualizar_numero) <= 11:
#                                 agenda[actualizar_nombre_numero] = actualizar_numero
#                                 print(f"Numero de {actualizar_nombre_numero} actualizado a {actualizar_numero}")
#                                 break
#                             else:
#                                 print("El numero debe tener solo digitos y maximo de 11 carateres")
#                         break
#                     else:
#                         print("El contacto {actualizar_nombre_numero} no exite en la agenda")
#                         break
#             else:
#                 print("Debe seleccionar una opcion valida (1-2)")

#         opcion_salida_actualizar = input("Desea actualizar otro contacto ? (1-Si o 2-No)")

#         if opcion_salida_actualizar == "1":
#             continue
#         elif opcion_salida_actualizar == "2":
#             break
#         else:
#             print("Seleccione una opcion valida (1-2)")

#     if opcion == "4":
#         while True:
#             opcion_eliminar = input("Que contacto desea eliminar: ")

#             if opcion_eliminar.capitalize() in agenda:
#                 agenda.pop(opcion_eliminar.capitalize())
#                 print("Se elimino el contacto exitosamente.")
#             else:
#                 print("No se encontro el contacto.")

#             opcion_salida_eliminar = input("Desea eliminar otro contacto? (1-Si,2-No): ")

#             if opcion_salida_eliminar == "1":
#                 continue

#             if opcion_salida_eliminar == "2":
#                 break

#     if opcion == "5":
#         break

# =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# Enunciado: Crea un programa que analice dos palabras diferentes y determine si:
# 1. Palíndromo: Se lee igual de izquierda a derecha que de derecha a izquierda.
#    (Ejemplo: "ana", "radar", "reconocer").
# 2. Anagrama: Tienen exactamente las mismas letras pero en diferente orden.
#    (Ejemplo: "roma" y "amor", "frase" y "fresa").
# 3. Isograma: Una palabra donde ninguna letra se repite.
#    (Ejemplo: "centrifugado", "murciélago").
#
# Pistas:
# - Normaliza los textos a minúsculas y elimina espacios antes de comparar.
# - Para anagramas: ¿Qué pasa si ordenas las letras con sorted()?
# - Para isogramas: ¿Qué pasa si comparas len(palabra) con len(set(palabra))?
# =============================================================================

def Tipo_Palabras(palabra1: str, palabra2: str):
    palabra1_limpia = palabra1.strip().lower().replace(" ","")
    palabra2_limpia = palabra2.strip().lower().replace(" ","")

    print(f"{f'La palabra {palabra1_limpia} es Palindromo' if palabra1_limpia == palabra1_limpia[::-1] else f'La palabra {palabra1_limpia} no es Palindromo'}")
    print(f"{f'La palabra {palabra2_limpia} es Palindromo' if palabra2_limpia == palabra2_limpia[::-1] else f'La palabra {palabra2_limpia} no es Palindromo'}")

    print(f"{f'La palabra {palabra1_limpia} y {palabra2_limpia} son Anagramas' if palabra1_limpia != palabra2_limpia and sorted(palabra1_limpia) == sorted(palabra2_limpia) else f'La palabra {palabra1_limpia} y {palabra2_limpia} no son Anagramas'}")

    print(f"{f'La palabra {palabra1_limpia} es Isograma' if len(palabra1_limpia) == len(set(palabra1_limpia)) else f'La palabra {palabra1_limpia} no es Isograma'}")
    print(f"{f'La palabra {palabra2_limpia} es Isograma' if len(palabra2_limpia) == len(set(palabra2_limpia)) else f'La palabra {palabra2_limpia} no es Isograma'}")

while True:
    ingresar_palabra_1 = input("Primera palabra: ")
    ingresar_palabra_2 = input("Segunda palabra: ")

    if not ingresar_palabra_1 or not ingresar_palabra_2:
        print("Las palabras no pueden estar vacias.")
        continue

    Tipo_Palabras(ingresar_palabra_1,ingresar_palabra_2)

    opcion_valida = False
    while True:
        salida = input("Desea comparar otras palabras ? (1 - SI o 2 - NO)")
        if salida == "1":
            break
        elif salida == "2":
            print("Adios.")
            opcion_valida = True
            break
        else:
            print("Opcion invalida. Ingrese 1 para Si o 2 para No.")
    if opcion_valida:
        break
