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

# =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# =============================================================================
# Enunciado: Utilizando la lógica de creación de los archivos anteriores, crea un
# programa capaz de leer y transformar en una misma clase custom de tu lenguaje
# los datos almacenados en el XML y el JSON. Borra los archivos al finalizar.
#
# Pasos sugeridos:
# - Define una clase 'Persona' con su constructor '__init__' para almacenar
#   las propiedades: nombre, edad, fecha_nacimiento y lenguajes.
# - Implementa un método de representación '__str__' o un método 'mostrar_datos()'
#   para imprimir la instancia de forma clara.
# - Crea de nuevo en disco los archivos 'datos.json' y 'datos.xml' con la información.
class Persona:
    def __init__(self,nombre:str, edad:int, fecha_nacimiento:str, lenguajes:list):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.lenguajes = lenguajes

    def mostrar_datos(self) -> None:
        lenguajes_str = ", ".join(self.lenguajes)
        print(f"Nombre: {self.nombre} | Edad: {self.edad} | Fecha de nacimiento = {self.fecha_nacimiento} | Lenguajes = {lenguajes_str} ")

ARCHIVO_JSON = "datos.json"
ARCHIVO_XML = "datos.xml"

datos_persona = {
    "nombre":"Victor",
    "edad":18,
    "fecha_nacimiento":"28-06-2000",
    "lenguajes": ["Python","Javascript","SQL"]
}

#Guardar JSON
with open (ARCHIVO_JSON, "w", encoding="utf-8") as archivo:
    json.dump(datos_persona, archivo, indent = 4, ensure_ascii = False)

#Guardar XML
raiz = ET.Element("persona")
ET.SubElement(raiz, "nombre").text = datos_persona["nombre"]
ET.SubElement(raiz, "edad").text = str(datos_persona["edad"])
ET.SubElement(raiz, "fecha_nacimiento").text = datos_persona["fecha_nacimiento"]

nodo_lenguajes = ET.SubElement(raiz, "lenguajes")
for lenguaje in datos_persona["lenguajes"]:
    ET.SubElement(nodo_lenguajes, "lenguaje").text = lenguaje

arbol = ET.ElementTree(raiz)
arbol.write(ARCHIVO_XML, encoding="utf-8", xml_declaration=True)


# - LECTURA Y PARSEO DE JSON A LA CLASE:
#   * Abre el JSON con 'json.load()' para obtener el diccionario.
#   * Instancia un objeto 'Persona' pasando los datos leídos del diccionario.
#   * Muestra la información de la instancia en consola.
print("\n--- Objeto creado desde JSON ---")
with open (ARCHIVO_JSON, "r" ,encoding="utf-8") as archivo:
    datos_dict = json.load(archivo)

persona_desde_json = Persona(
    nombre = datos_dict["nombre"],
    edad = int(datos_dict["edad"]),
    fecha_nacimiento=datos_dict["fecha_nacimiento"],
    lenguajes=datos_dict["lenguajes"]
)
persona_desde_json.mostrar_datos()

# - LECTURA Y PARSEO DE XML A LA CLASE:
#   * Parsea el XML con 'ET.parse("datos.xml")' y obtén la raíz con '.getroot()'.
#   * Extrae los textos de los nodos hijo (ej. 'raiz.find("nombre").text').
#   * Iterar sobre el nodo de lenguajes para reconstruir la lista de cadenas.
#   * Instancia un objeto 'Persona' pasando los datos extraídos del XML.
#   * Muestra la información de la instancia en consola.
print("\n--- Objeto creado desde XML ---")
arbol_xml = ET.parse(ARCHIVO_XML)
raiz_xml = arbol_xml.getroot()

nombre_xml = raiz_xml.find("nombre").text
edad_xml = int(raiz_xml.find("edad").text)
fecha_xml = raiz_xml.find("fecha_nacimiento").text

lenguaje_xml = [nodo.text for nodo in raiz_xml.find("lenguajes")]

persona_desde_xml = Persona(
    nombre = nombre_xml,
    edad = edad_xml,
    fecha_nacimiento = fecha_xml,
    lenguajes = lenguaje_xml
)
persona_desde_xml.mostrar_datos()

#
# - LIMPIEZA FINAL:
#   * Elimina ambos archivos ('datos.json' y 'datos.xml') del sistema con 'os.remove()'.

if os.path.exists(ARCHIVO_JSON):
    os.remove(ARCHIVO_JSON)

if os.path.exists(ARCHIVO_XML):
    os.remove(ARCHIVO_XML)

print("\nArchivos temporales eliminados correctamente.")