# ==========================================
# PARTE PRINCIPAL: OPERACIONES SOBRE LA ESTRUCTURA
# ==========================================

# 1. Creación e inicialización del conjunto de datos original.
lista = ["Lapicero","Cuaderno","Borrador","Tajador"]

# 2. Operación 1: Añadir un elemento al final de la estructura.
lista.append("Mochila")

# 3. Operación 2: Añadir un elemento al principio (índice 0).
lista.insert(0,"Regla")

# 4. Operación 3: Añadir varios elementos en bloque al final (extensión).
extension = ["Hoja","Botella"]
lista.extend(extension)

# 5. Operación 4: Añadir varios elementos en bloque en una posición concreta.
lista[2:2] = ["Agua","Frasco"]

# 6. Operación 5: Eliminar un elemento en una posición concreta (por índice).
lista.pop(2)

# 7. Operación 6: Actualizar el valor de un elemento en una posición concreta.
lista[0] = "Mouse"

# 8. Operación 7: Comprobar si un elemento está presente en la estructura (búsqueda booleana).
if "Mouse" in lista:
    print("Aqui esta el mouse")

# 9. Operación 8: Eliminar todo el contenido (vaciar la estructura por completo).
lista.clear()