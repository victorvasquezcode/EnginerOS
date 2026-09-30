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
import json
import xml.etree.ElementTree as ET
import os
class Persona():
    def __init__(self, nombre, edad, fecha_nacimiento, lenguajes):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.lenguajes = lenguajes
    def __str__(self):
        return f"\nNombre: {self.nombre}\nEdad: {self.edad}\nFecha de nacimiento: {self.fecha_nacimiento}\nLenguajes: {self.lenguajes}"
persona_1 = Persona("Victor",26,"2000-06-28",["Python","SQL"])
#Guardar JSON
ARCHIVO_1 = 'datos.json'
with open(ARCHIVO_1, "w") as archivo:
    json.dump(persona_1.__dict__,archivo,indent=4)

#Guardar XML
ARCHIVO_2 = 'datos.xml'
raiz = ET.Element("persona")
ET.SubElement(raiz, "nombre").text = persona_1.nombre
ET.SubElement(raiz, "edad").text = str(persona_1.edad)
ET.SubElement(raiz, "fecha_nacimiento").text = persona_1.fecha_nacimiento
lenguaje_nodo = ET.SubElement(raiz, "lenguajes") 
for lenguaje in persona_1.lenguajes:
    ET.SubElement(lenguaje_nodo, "lenguaje").text = lenguaje

arbol = ET.ElementTree(raiz)
arbol.write(ARCHIVO_2, encoding="utf-8",xml_declaration=True)


# - LECTURA Y PARSEO DE JSON A LA CLASE:
#   * Abre el JSON con 'json.load()' para obtener el diccionario.
#   * Instancia un objeto 'Persona' pasando los datos leídos del diccionario.
#   * Muestra la información de la instancia en consola.


# - LECTURA Y PARSEO DE XML A LA CLASE:
#   * Parsea el XML con 'ET.parse("datos.xml")' y obtén la raíz con '.getroot()'.
#   * Extrae los textos de los nodos hijo (ej. 'raiz.find("nombre").text').
#   * Iterar sobre el nodo de lenguajes para reconstruir la lista de cadenas.
#   * Instancia un objeto 'Persona' pasando los datos extraídos del XML.
#   * Muestra la información de la instancia en consola.

#
# - LIMPIEZA FINAL:
#   * Elimina ambos archivos ('datos.json' y 'datos.xml') del sistema con 'os.remove()'.
