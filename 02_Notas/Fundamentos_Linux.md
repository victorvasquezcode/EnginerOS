# Glosario de Fundamentos de Linux y Terminal

Guía rápida de comandos esenciales para la gestión de archivos, directorios y navegación desde la consola (Git Bash / Linux / macOS).

---

## 1. Navegación e Inspección del Sistema

* **`pwd` (Print Working Directory):** Muestra la ruta absoluta de la carpeta en la que te encuentras ubicado actualmente.
* **`ls` (List):** Lista todos los archivos y carpetas dentro del directorio actual.
  * `ls -a`: Muestra también los archivos ocultos (los que empiezan con punto, ej. `.gitignore`).
  * `ls -l`: Muestra información detallada (permisos, tamaño, fecha de modificación).
* **`cd` (Change Directory):** Cambia de carpeta en el sistema de archivos.
  * `cd nombre_carpeta`: Entra a la carpeta especificada.
  * `cd ..`: Sube un nivel (regresa a la carpeta padre).
  * `cd ~` o solo `cd`: Regresa directamente a la carpeta raíz de tu usuario.

---

## 2. Creación y Manipulación de Archivos

* **`touch`:** Crea un archivo vacío si este no existe (ej. `touch index.html`). Si el archivo ya existe, actualiza su fecha de última modificación sin alterar su contenido.
* **`mv` (Move / Rename):** Mueve archivos o carpetas de una ubicación a otra, o les cambia el nombre en el mismo lugar.
  * *Renombrar:* `mv nombre_viejo.txt nombre_nuevo.txt`
  * *Mover:* `mv archivo.txt mi_carpeta/`
* **`cp` (Copy):** Duplica/copia un archivo o carpeta.
  * *Copiar archivo:* `cp origen.txt destino.txt`
  * *Copiar carpeta completa:* `cp -r carpeta_origen carpeta_destino` (la opción `-r` significa recursivo).
* **`cat` (Concatenate):** Imprime en pantalla el contenido completo de un archivo de texto de forma rápida sin abrir un editor.

---

## 3. Eliminación de Archivos y Directorios

> ⚠️ **CUIDADO:** Los comandos de eliminación en la terminal de Linux **borran de forma permanente** (no envían el archivo a la Papelera de Reciclaje).

* **`rm` (Remove):** Elimina uno o varios archivos (ej. `rm archivo.txt`).
* **`rmdir` (Remove Directory):** Elimina una carpeta, pero **solo si está completamente vacía**.
* **`rm -rf`:** Elimina una carpeta y todo su contenido (subcarpetas y archivos) de forma forzada y definitiva.

---

## 4. Gestión de Carpetas (Directorios)

* **`mkdir` (Make Directory):** Crea una nueva carpeta en la ubicación actual (ej. `mkdir proyecto_reto05`).
  * `mkdir -p ruta/de/carpetas`: Crea una estructura completa de carpetas anidadas de un solo paso si no existen.

---

## 5. Edición de Archivos desde la Terminal

* **`nano`:** Editor de texto liviano que funciona directamente dentro de la interfaz de la consola.
  * *Abrir/Crear:* `nano nombre_archivo.txt`
  * *Guardar:* `Ctrl + O` y luego `Enter`.
  * *Salir:* `Ctrl + X`.
* **`code`:** Abre el archivo o la carpeta directamente en Visual Studio Code.
  * `code .`: Abre la carpeta actual completa dentro de VS Code.
  * `code archivo.py`: Abre un archivo específico en VS Code.

---

## 6. Productividad y Atajos en la Terminal

* **Tecla `Tab` (Autocompletado):** Presiona `Tab` mientras escribes el nombre de una carpeta o archivo para que la terminal lo complete automáticamente.
* **Flecha Arriba (`↑`) / Flecha Abajo (`↓`):** Navega por el historial de comandos ejecutados recientemente para reusarlos sin tipear de nuevo.
* **`clear` (o `Ctrl + L`):** Limpia el texto de la pantalla de la consola para dejar la vista despejada.