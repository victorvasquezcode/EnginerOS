# 🔴 / 🟡 ACTIVOS

### 🟡 [11] CRUD Ventas
- **Fallas:**
  1. Invertí la condición lógica al evaluar líneas vacías usando `if lista.strip(): continue`.
  2. Dupliqué paréntesis al castear la tupla creando un anidamiento incorrecto `(nombre,(int(cantidad),(float(precio))))`.
  3. Redundé agregando `return None` dentro del `except ValueError` cuando la función ya retornaba `None` por defecto.
  4. Intenté aplicar el método `.strip()` a una tupla `(nombre, cantidad, precio)` provocando un error de atributo `AttributeError`.
  5. Omití el salto de línea `\n` al final de la cadena de formato dentro de `archivo.write()`.
- **Soluciones:**
  1. Negué la condición con `if not lista.strip():` continue para saltar únicamente las líneas vacías.
  2. Simplifiqué el formateo a una sola tupla limpia `((nombre,int(cantidad),float(precio)))`.
  3. Removí el `return None` explícito dejando solo el mensaje de error en el bloque de excepción.
  4. Removí la validación `if not lista.strip(): continue` al iterar sobre elementos que ya venían deserializados como tuplas estructuradas.
  5. Agregué `\n` al final del formato `f"{nombre_producto},{cantidad},{precio:.2f}\n"` para evitar que los nuevos registros se concatenen en la misma línea del archivo.
- **Revisar:** Mañana 5 AM.

### 🟡 [12] XML y JSON
- **Fallas:**
  1. .
  2. .
- **Soluciones:**
  1. .
  2. .
- **Revisar:** .

### 🟡 [13] Pruebas Unitarias
- **Fallas:**
  1. .
  2. .
- **Soluciones:**
  1. .
  2. .
- **Revisar:** .

### 🟡 [14] Manejo Fechas
- **Fallas:**
  1. .
  2. .
- **Soluciones:**
  1. .
  2. .
- **Revisar:**.

### 🟡 [15] Asincronia
- **Fallas:**
  1. .
  2. .
- **Soluciones:**
  1. .
  2. .
- **Revisar:**.

### 🟡 [16] Regex Validaciones 
- **Fallas:**
  1. .
  2. .
- **Soluciones:**
  1. .
  2. .
- **Revisar:**.

---

### 🔴 [17] 
- **Notas / Conceptos aprendidos:**
  1. .
  2. .
- **Falla principal:** .
- **Revisar:**

---

# 🟢 DOMINADOS (VERDES)
- [01 al 10] Conceptos básicos


# 📌 MODO DE TRABAJO DIARIO (EL 1%)

1. 🌅 MAÑANA (5:00 AM - 1 hora) -> AMARILLO
   - Leer esta bitácora (1 min).
   - Resolver 1 ejercicio Amarillo SIN ayuda.
   - Si sale BIEN -> Poner fecha a 3 días para prueba de fuego (cambiando enunciado).
   - Si sale MAL / Pido ayuda -> Anotar las fallas aquí y se queda en Amarillo.

2. ☀️ TARDE/NOCHE -> ROJO + TEORÍA
   - Estudiar y resolver el ROJO del día con ayuda/tutoriales (Pasa a Amarillo).
   - Si fallaste en el AMARILLO de la mañana, estudiar la teoría de los puntos débiles anotados.
   - Registrar fallas/soluciones nuevas en esta bitácora (30 segundos).

3. 🗓️ SÁBADOS -> AUDITORÍA DE VERDES
   - Hacer prueba rápida a 3 o 4 ejercicios Verdes (cambiando reglas o refactorizando).
   - Si aprueban -> Siguen en Verde.
   - Si fallan -> Bajan a Amarillo para repasarlos en la semana.