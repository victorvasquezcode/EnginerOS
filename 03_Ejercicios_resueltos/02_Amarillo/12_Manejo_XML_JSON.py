# =============================================================================
# DIFICULTAD EXTRA (OPCIONAL)
# =============================================================================
# Enunciado: Utilizando la lógica de creación de los archivos anteriores, crea un
# programa capaz de leer y transformar en una misma clase custom de tu lenguaje
# los datos almacenados en el XML y el JSON. Borra los archivos al finalizar.
#
# Pasos sugeridos:
# - Define una clase 'Persona' con su constructor '__init__' para almacenar
#   las propiedades: nombre, edad, fecha_nacimiento y lenguajes.✅
# - Implementa un método de representación '__str__' o un método 'mostrar_datos()'
#   para imprimir la instancia de forma clara.✅
# - Crea de nuevo en disco los archivos 'datos.json' y 'datos.xml' con la información. ❌
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
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nFecha de nacimiento: {self.fecha_nacimiento}\nLenguajes: {self.lenguajes}"
    
persona1 = Persona("Victor",26,"2000-06-28",["Java","SQL","Python"])

# JSON
DATOS_JSON = 'datos.json'
with open(DATOS_JSON, "w") as archivo:
    json.dump(persona1.__dict__, archivo)

# XML    
DATOS_XML = 'datos.xml'
raiz = ET.Element("persona")
ET.SubElement(raiz,"nombre").text = persona1.nombre
ET.SubElement(raiz,"edad").text = str(persona1.edad)
ET.SubElement(raiz,"fecha_nacimiento").text = persona1.fecha_nacimiento
nodo_lenguajes = ET.SubElement(raiz,"lenguajes")
for lenguaje in persona1.lenguajes:
    ET.SubElement(nodo_lenguajes, "lenguaje").text = lenguaje

arbol = ET.ElementTree(raiz)
arbol.write(DATOS_XML)

# - LECTURA Y PARSEO DE JSON A LA CLASE: 
#   * Abre el JSON con 'json.load()' para obtener el diccionario. ❌
#   * Instancia un objeto 'Persona' pasando los datos leídos del diccionario. ❌
#   * Muestra la información de la instancia en consola. ❌
with open(DATOS_JSON, 'r') as archivo:
    diccionario_1 = json.load(archivo)

persona2 = Persona(**diccionario_1)

print(persona2)

# - LECTURA Y PARSEO DE XML A LA CLASE:
#   * Parsea el XML con 'ET.parse("datos.xml")' y obtén la raíz con '.getroot()'. ❌
#   * Extrae los textos de los nodos hijo (ej. 'raiz.find("nombre").text'). ❌
#   * Iterar sobre el nodo de lenguajes para reconstruir la lista de cadenas. ❌
#   * Instancia un objeto 'Persona' pasando los datos extraídos del XML. ❌
#   * Muestra la información de la instancia en consola. ❌
arbol = ET.parse(DATOS_XML)
raiz = arbol.getroot()

nombre = raiz.find("nombre").text
edad = int(raiz.find("edad").text)
fecha_nacimiento = raiz.find("fecha_nacimiento").text

lenguajes = [nodo.text for nodo in raiz.find("lenguajes")]

persona3 = Persona(nombre, edad, fecha_nacimiento, lenguajes)
print(persona3)

# - LIMPIEZA FINAL:
#   * Elimina ambos archivos ('datos.json' y 'datos.xml') del sistema con 'os.remove()'. ✅
if os.path.exists(DATOS_JSON):
    os.remove(DATOS_JSON)

if os.path.exists(DATOS_XML):
    os.remove(DATOS_XML)
