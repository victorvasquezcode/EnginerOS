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
class Persona:
    def __init__(self, nombre, edad, fecha_nacimiento, lenguajes):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.lenguajes = lenguajes
    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nFecha nacimiento: {self.fecha_nacimiento}\nLenguaje: {self.lenguajes}"
    
#Guardar JSON
DATOS_1 = 'datos.json'
persona1 = Persona("Victor",26,"28-06-2000",["Python","SQL"])

with open (DATOS_1, "w") as archivo:
    json.dump(persona1.__dict__, archivo)

#Guardar XML
DATOS_2 = 'datos.xml'
persona2 = Persona("Javier",25,"26-03-2000",["Java","Javascript"])

raiz = ET.Element("persona")
ET.SubElement(raiz, "nombre").text = persona2.nombre
ET.SubElement(raiz, "edad").text = str(persona2.edad)
ET.SubElement(raiz, "fecha_nacimiento").text = persona2.fecha_nacimiento
for lenguaje in persona2.lenguajes:
    ET.SubElement(raiz, "lenguaje").text = lenguaje

arbol = ET.ElementTree(raiz)
arbol.write(DATOS_2,encoding="utf-8", xml_declaration=True)

# - LECTURA Y PARSEO DE JSON A LA CLASE:
#   * Abre el JSON con 'json.load()' para obtener el diccionario.
#   * Instancia un objeto 'Persona' pasando los datos leídos del diccionario.
#   * Muestra la información de la instancia en consola.
with open(DATOS_1, "r") as archivo:
    datos = json.load(archivo)
persona3 = Persona(**datos)
print(persona3)

# - LECTURA Y PARSEO DE XML A LA CLASE:
#   * Parsea el XML con 'ET.parse("datos.xml")' y obtén la raíz con '.getroot()'.
#   * Extrae los textos de los nodos hijo (ej. 'raiz.find("nombre").text').
#   * Iterar sobre el nodo de lenguajes para reconstruir la lista de cadenas.
#   * Instancia un objeto 'Persona' pasando los datos extraídos del XML.
#   * Muestra la información de la instancia en consola.
arbol = ET.parse(DATOS_2)
raiz = arbol.getroot()
nombre = raiz.find("nombre").text
edad = int(raiz.find("edad").text)
fecha_nacimiento = raiz.find("fecha_nacimiento").text
lenguajes = [l.text for l in raiz.findall("lenguaje")]
persona4 = Persona(nombre,edad,fecha_nacimiento,lenguajes)
print(persona4)
#
# - LIMPIEZA FINAL:
#   * Elimina ambos archivos ('datos.json' y 'datos.xml') del sistema con 'os.remove()'.
if os.path.exists(DATOS_1):
    os.remove(DATOS_1)

if os.path.exists(DATOS_2):
    os.remove(DATOS_2)