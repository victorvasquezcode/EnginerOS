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

#Guardar JSON

#Guardar XML

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