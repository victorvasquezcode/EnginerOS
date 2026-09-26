# =============================================================================
# RETO 12: MANEJO DE ARCHIVOS XML Y JSON
#
# CONCEPTOS CLAVE:
# 1. Formato JSON (JavaScript Object Notation): Formato ligero de intercambio 
#    de datos estructurado en pares clave-valor y listas (módulos 'json').
# 2. Formato XML (Extensible Markup Language): Formato basado en etiquetas 
#    anidadas para jerarquizar información (módulo 'xml.etree.ElementTree').
# 3. Serialización / Deserialización: Proceso de convertir objetos de memoria 
#    a texto estructurado en disco y viceversa.
# =============================================================================

import os
import json
import xml.etree.ElementTree as ET

# =============================================================================
# 1. CREACIÓN, LECTURA Y ELIMINACIÓN DE JSON Y XML
# =============================================================================
# Enunciado: Desarrolla un programa capaz de crear un archivo XML y JSON que 
# guarde los siguientes datos: Nombre, Edad, Fecha de nacimiento, Listado de 
# lenguajes de programación. Muestra el contenido y luego borra los archivos.

# --- PARTE A: MANEJO DE JSON ---
# Pasos sugeridos:
# - Define una estructura de datos en memoria (diccionario en Python) con la 
#   información requerida (nombre, edad, fecha_nacimiento, lenguajes).
# - Abre un archivo 'datos.json' en modo escritura ("w") y usa 'json.dump()' 
#   para serializar la información con sangría ('indent=4') para buena legibilidad.
# - Abre y lee el archivo 'datos.json' ("r") imprimiendo su contenido por consola.
# - Elimina el archivo 'datos.json' utilizando 'os.remove()'.
NOMBRE_ARCHIVO = "datos.json"

persona = {
    "nombre":"Victor",
    "edad":18,
    "fecha_nacimiento":"28-06-2000",
    "lenguaje": ["Python","Javascript","SQL"]
}

with open (NOMBRE_ARCHIVO, "w",encoding="utf-8") as archivo:
    json.dump(persona, archivo,indent= 4 , ensure_ascii= False)

with open (NOMBRE_ARCHIVO, "r",encoding="utf-8") as archivo:
    contenido = archivo.read()
    print("--- Contenido de datos.json ---")
    print(contenido)

if os.path.exists(NOMBRE_ARCHIVO):
    os.remove(NOMBRE_ARCHIVO)
    print("Archivo datos.json eliminado con exito")


# --- PARTE B: MANEJO DE XML ---
# Pasos sugeridos:
# - Crea el nodo raíz del XML usando 'ET.Element("persona")'.
# - Agrega subelementos hijo con 'ET.SubElement()' para nombre, edad y fecha de nacimiento,
#   asignándoles su respectivo texto con '.text'.
# - Crea un nodo contenedor para los lenguajes y agrega cada lenguaje como un nodo hijo.
# - Convierte el árbol a un objeto 'ET.ElementTree' y guárdalo en 'datos.xml' 
#   mediante el método '.write()' (especificando 'encoding="utf-8"' y 'xml_declaration=True').
# - Abre y lee el archivo 'datos.xml' ("r") imprimiendo su contenido por consola.
# - Elimina el archivo 'datos.xml' utilizando 'os.remove()'.
NOMBRE_ARCHIVO_XML = "datos.xml"

raiz = ET.Element("persona")

nodo_nombre = ET.SubElement(raiz,"nombre")
nodo_nombre.text = "Victor"

nodo_edad = ET.SubElement(raiz,"edad")
nodo_edad.text = "18"

nodo_fecha_nacimiento = ET.SubElement(raiz, "fecha_nacimiento")
nodo_fecha_nacimiento.text = "28-06-2000"

nodo_lenguajes = ET.SubElement(raiz, "lenguajes")
lenguaje_programacion = ["Python", "Javascript", "SQL"]

for lenguaje in lenguaje_programacion:
    sub_lenguaje = ET.SubElement(nodo_lenguajes,"lenguaje")
    sub_lenguaje.text = lenguaje

arbol = ET.ElementTree(raiz)
arbol.write(NOMBRE_ARCHIVO_XML, encoding="utf-8", xml_declaration= True)

with open (NOMBRE_ARCHIVO_XML,"r" , encoding="utf-8") as archivo:
    print ("--- Contenido de datos.xml ---")
    print (archivo.read())

if os.path.exists(NOMBRE_ARCHIVO_XML):
    os.remove(NOMBRE_ARCHIVO_XML)
    print("Archivo datos.xml eliminado con exito.")