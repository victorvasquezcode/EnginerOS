# Bitácora de Aprendizaje: Reto 13

### 1. 🎯 Lo que dominé hoy (El clic mental)
* **Serialización y Deserialización en JSON:** Entendí el flujo de guardar datos en memoria (diccionarios/listas) a disco con `json.dump()` y recuperarlos con `json.load()`.
* **Formateo Específico de JSON:** Hice clic mental en los tres parámetros fundamentales para escribir archivos limpios en español: `encoding="utf-8"` (previene errores de acentos/caracteres), `indent=4` (sangría legible para humanos) y `ensure_ascii=False` (imprime texto en español directo en lugar de códigos Unicode).
* **Estructuración de Árboles XML:** Aprendí a manipular la librería `xml.etree.ElementTree` creando nodos raíz (`ET.Element`) y nodos hijos (`ET.SubElement`), asignándoles valor con `.text` (que siempre requiere strings) y respetando las reglas de nombrado sin espacios (ej. `fecha_nacimiento`).
* **Transformación (Mapping) a Clases Custom:** Dominé el proceso de leer datos crudos desde distintos formatos de archivos (JSON y XML) para deserializarlos e instanciarlos directamente como objetos de una clase propia (`Persona`), unificando cómo se consume la información en la aplicación.

---

### 2. ⚠️ Tropezones, errores y cómo los solucioné
* **Firma e Identación en `json.dump()`:**
  * *Error:* Intenté escribir `json.dump(ident = 4)` cometiendo un typo en el parámetro y olvidando pasarle tanto el diccionario como la referencia del archivo abierto.
  * *Solución:* Corregí a `json.dump(persona, archivo, indent=4)`, pasando siempre en orden: el objeto a guardar, el archivo objetivo y la sangría.
* **Manejo de Etiquetas y Tipos de Datos en XML:**
  * *Error:* Intenté usar etiquetas con espacios como `"fecha de nacimiento"` y asignar tipos enteros sin convertir.
  * *Solución:* Cambié las etiquetas a formato `snake_case` (`fecha_nacimiento`) y convertí explícitamente los enteros a texto (`str(edad)`) antes de asignarlos a la propiedad `.text`.
* **Lectura de Nodos Múltiples en XML:**
  * *Error:* Dudas iniciales sobre cómo reconstruir una lista a partir de una etiqueta contenedora en XML.
  * *Solución:* Usé una lista por comprensión iterando sobre el nodo padre: `[nodo.text for nodo in raiz.find("lenguajes")]`.