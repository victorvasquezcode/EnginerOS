# 🐧 Glosario de Fundamentos de Linux y Terminal

> Guía práctica para aprender a navegar, crear, mover, copiar, eliminar y editar archivos desde la terminal.
>
> Compatible principalmente con **Linux**, **Git Bash** y **macOS**. Algunas instrucciones de administración del sistema son específicas de **Fedora Linux**.

---

## 📚 Índice

1. [Conceptos básicos](#1-conceptos-básicos)
2. [Navegación e inspección](#2-navegación-e-inspección)
3. [Archivos](#3-archivos)
4. [Directorios](#4-directorios)
5. [Mover y copiar](#5-mover-y-copiar)
6. [Eliminar archivos y directorios](#6-eliminar-archivos-y-directorios)
7. [Leer y editar archivos](#7-leer-y-editar-archivos)
8. [Productividad en la terminal](#8-productividad-en-la-terminal)
9. [Rutas importantes](#9-rutas-importantes)
10. [Permisos y `sudo`](#10-permisos-y-sudo)
11. [Mantenimiento de Fedora](#11-mantenimiento-de-fedora)
12. [Actualización de versión mayor de Fedora](#12-actualización-de-versión-mayor-de-fedora)
13. [Flujo mental para usar la terminal](#13-flujo-mental-para-usar-la-terminal)
14. [🧠 Chuleta rápida](#-chuleta-rápida)

---

# 1. Conceptos básicos

## ¿Qué es la terminal?

La **terminal** es una interfaz que permite interactuar con el sistema operativo escribiendo comandos en lugar de utilizar una interfaz gráfica.

Con ella puedes:

- navegar por directorios;
- crear, copiar, mover y eliminar archivos;
- ejecutar programas;
- administrar el sistema;
- instalar y actualizar software;
- trabajar con herramientas como **Git**.

## ¿Qué es un comando?

Un **comando** es una instrucción que escribes en la terminal para pedirle al sistema que realice una acción.

Ejemplo:

```bash
pwd
```

El comando anterior solicita la ruta del directorio actual.

## Estructura general de un comando

```text
comando [opciones] [argumentos]
```

Ejemplo:

```bash
ls -l proyecto
```

- `ls` → comando.
- `-l` → opción.
- `proyecto` → argumento.

> 💡 **Idea clave:** aprende primero qué hace el comando y después sus opciones. No memorices comandos sin entender la acción que realizan.

---

# 2. Navegación e inspección

Estas son las herramientas básicas para saber **dónde estás**, **qué existe** y **cómo desplazarte**.

## `pwd` — Print Working Directory

Muestra la **ruta absoluta** del directorio en el que te encuentras actualmente.

```bash
pwd
```

Ejemplo de salida:

```text
/home/victor/proyectos
```

### Para recordarlo

> `pwd` = **¿Dónde estoy?**

---

## `ls` — List

Muestra los archivos y directorios del lugar actual.

```bash
ls
```

### Opciones importantes

| Comando | Función |
|---|---|
| `ls` | Lista archivos y carpetas visibles. |
| `ls -a` | Incluye archivos ocultos. |
| `ls -l` | Muestra información detallada. |
| `ls -la` | Combina listado detallado + ocultos. |

Ejemplo:

```bash
ls -la
```

> 💡 Los archivos cuyo nombre comienza con `.` suelen considerarse ocultos, por ejemplo `.gitignore`.

---

## `cd` — Change Directory

Permite cambiar de directorio.

### Entrar a una carpeta

```bash
cd proyecto
```

### Subir un nivel

```bash
cd ..
```

### Ir al directorio personal

```bash
cd ~
```

También puedes usar simplemente:

```bash
cd
```

### Encadenar rutas

```bash
cd proyectos/python/retos
```

### Para recordarlo

> `cd` = **moverme a otra carpeta**.

---

# 3. Archivos

## `touch` — Crear un archivo

Crea un archivo vacío si no existe.

```bash
touch index.html
```

Si el archivo ya existe, normalmente no modifica su contenido; actualiza su marca de tiempo de modificación.

### Ejemplos

```bash
touch app.py
```

```bash
touch README.md
```

> 💡 `touch` **no es un editor**. Sirve principalmente para crear el archivo o modificar sus marcas de tiempo.

---

## Identificar un archivo

Puedes combinar `ls` con opciones de listado para inspeccionar rápidamente el contenido de un directorio.

```bash
ls -l
```

---

# 4. Directorios

## `mkdir` — Make Directory

Crea un nuevo directorio.

```bash
mkdir proyecto
```

### Crear varios niveles con `-p`

```bash
mkdir -p proyecto/src/utils
```

La opción `-p` permite crear los directorios intermedios que todavía no existan.

### Ejemplo práctico

```bash
mkdir -p reto01/src
```

Esto puede producir una estructura como:

```text
reto01/
└── src/
```

### Para recordarlo

> `mkdir` = **crear carpeta**.

---

# 5. Mover y copiar

## `mv` — Move / Rename

Se utiliza para **mover** archivos o directorios y también para **renombrarlos**.

### Renombrar un archivo

```bash
mv nombre_viejo.txt nombre_nuevo.txt
```

### Mover un archivo

```bash
mv archivo.txt documentos/
```

### Mover y renombrar al mismo tiempo

```bash
mv archivo.txt documentos/nuevo_nombre.txt
```

> 💡 En Linux, renombrar un archivo es básicamente moverlo a otro nombre dentro de la misma ubicación.

---

## `cp` — Copy

Copia archivos o directorios.

### Copiar un archivo

```bash
cp origen.txt destino.txt
```

### Copiar un archivo a una carpeta

```bash
cp archivo.txt documentos/
```

### Copiar un directorio

```bash
cp -r carpeta_origen carpeta_destino
```

La opción `-r` significa **recursivo** y permite copiar el contenido del directorio y sus subdirectorios.

### Para recordarlo

> `cp` = **duplicar**.

---

# 6. Eliminar archivos y directorios

> ⚠️ **PELIGRO:** los comandos `rm`, `rm -r` y especialmente `rm -rf` pueden eliminar contenido sin enviarlo a la Papelera de Reciclaje. Comprueba siempre la ruta antes de ejecutar el comando.

## `rm` — Remove

Elimina uno o varios archivos.

```bash
rm archivo.txt
```

### Eliminar varios archivos

```bash
rm archivo1.txt archivo2.txt
```

---

## `rmdir` — Remove Directory

Elimina un directorio **vacío**.

```bash
rmdir carpeta_vacia
```

Si el directorio contiene archivos o subdirectorios, el comando no podrá eliminarlo normalmente.

---

## `rm -r` — Eliminar un directorio recursivamente

Elimina un directorio y su contenido de manera recursiva.

```bash
rm -r carpeta
```

---

## `rm -rf` — Eliminación recursiva y forzada

```bash
rm -rf carpeta
```

- `-r` → recursivo.
- `-f` → fuerza la operación y evita algunas confirmaciones o errores por archivos inexistentes.

> 🚨 **Regla profesional:** no uses `rm -rf` sin comprobar primero la ruta. Un error de escritura puede borrar mucho más de lo que pretendías.

---

# 7. Leer y editar archivos

## `cat` — Mostrar contenido

Muestra rápidamente el contenido de un archivo de texto en la terminal.

```bash
cat README.md
```

Es útil para archivos pequeños.

> 💡 Para archivos muy largos, `less` suele ser más cómodo:
>
> ```bash
> less README.md
> ```
>
> Para salir de `less`, presiona `q`.

---

## `nano` — Editor de texto en terminal

Editor sencillo que funciona directamente dentro de la consola.

### Abrir o crear un archivo

```bash
nano archivo.txt
```

### Atajos básicos

| Atajo | Acción |
|---|---|
| `Ctrl + O` | Guardar. |
| `Enter` | Confirmar el nombre del archivo. |
| `Ctrl + X` | Salir. |
|

> 💡 En los atajos de `nano`, `Ctrl` significa mantener presionada la tecla `Ctrl` y pulsar la letra indicada.

---

## `code` — Abrir en Visual Studio Code

Permite abrir archivos o directorios con VS Code cuando el comando `code` está disponible en el `PATH`.

### Abrir la carpeta actual

```bash
code .
```

### Abrir un archivo

```bash
code app.py
```

### Para recordarlo

> `code .` = **abrir este proyecto en VS Code**.

---

# 8. Productividad en la terminal

## `Tab` — Autocompletado

Pulsa `Tab` mientras escribes un comando, archivo o directorio para intentar completarlo automáticamente.

Ejemplo:

```bash
cd pro<Tab>
```

La terminal puede completar `proyecto` si existe y no hay ambigüedad.

> 💡 Además de ahorrar tiempo, el autocompletado ayuda a reducir errores al escribir rutas.

---

## `↑` / `↓` — Historial de comandos

Las flechas permiten recorrer comandos ejecutados anteriormente.

- `↑` → comando anterior.
- `↓` → comando siguiente.

Esto es especialmente útil para repetir comandos largos.

---

## `clear` / `Ctrl + L` — Limpiar pantalla

```bash
clear
```

También puedes usar:

```text
Ctrl + L
```

Esto limpia visualmente la terminal, pero **no elimina el historial de comandos**.

---

# 9. Rutas importantes

Entender las rutas es fundamental para no perderse en Linux.

## Ruta absoluta

Empieza desde la raíz del sistema.

```text
/home/victor/proyecto/app.py
```

La ruta describe exactamente dónde está el archivo.

## Ruta relativa

Parte de la ubicación actual.

```text
proyecto/app.py
```

Su significado depende del directorio en el que estés.

## Símbolos esenciales

| Símbolo | Significado |
|---|---|
| `.` | Directorio actual. |
| `..` | Directorio padre. |
| `~` | Directorio personal del usuario. |
| `/` | Raíz del sistema o separador de rutas. |
|

### Ejemplo

```bash
cd ..
```

Sube un nivel desde el directorio actual.

---

# 10. Permisos y `sudo`

## `sudo`

Permite ejecutar un comando con privilegios administrativos, siempre que tu usuario tenga los permisos necesarios.

Ejemplo:

```bash
sudo dnf upgrade --refresh
```

El sistema puede solicitar tu contraseña.

> ⚠️ **Regla:** usa `sudo` solo cuando sea necesario. No convierte mágicamente un comando peligroso en un comando seguro.

---

## Idea básica de permisos

En Linux, los archivos y directorios tienen permisos asociados al **usuario**, **grupo** y **otros usuarios**.

Un listado como:

```text
-rw-r--r--
```

indica, entre otras cosas, permisos de lectura y escritura para el propietario y permisos de lectura para otros usuarios.

> 📌 Este tema merece un glosario propio cuando avances a permisos, grupos, `chmod`, `chown` y administración del sistema.

---

# 11. Mantenimiento de Fedora

> 🐧 Esta sección es específica de **Fedora Linux** y no forma parte de los comandos portables de Git Bash/Linux/macOS.

## `sudo dnf upgrade --refresh`

Actualiza los paquetes instalados usando `dnf` y refresca la información de los repositorios antes de realizar la actualización.

```bash
sudo dnf upgrade --refresh
```

### Idea mental

> **Actualizar el sistema instalado.**

---

## `flatpak update`

Busca e instala actualizaciones de las aplicaciones administradas mediante Flatpak.

```bash
flatpak update
```

### Idea mental

> **Actualizar aplicaciones Flatpak.**

---

## `sudo dnf clean all`

Limpia los datos almacenados en caché por DNF.

```bash
sudo dnf clean all
```

Puede ser útil para mantenimiento o para solucionar determinados problemas relacionados con cachés, aunque no debe usarse como una rutina obligatoria después de cada actualización.

---

## `dnf check-update`

Comprueba si existen paquetes con actualizaciones disponibles.

```bash
dnf check-update
```

> 📌 Dependiendo del resultado, DNF puede devolver un código de salida distinto de `0` cuando hay actualizaciones disponibles. Eso no significa necesariamente que el comando haya fallado.

---

## `sudo reboot`

Reinicia el equipo desde la terminal.

```bash
sudo reboot
```

Puede ser necesario reiniciar después de determinadas actualizaciones del sistema, especialmente cuando se ha instalado un nuevo kernel y quieres iniciar con él.

---

# 12. Actualización de versión mayor de Fedora

La actualización de una versión de Fedora a otra es diferente de instalar actualizaciones normales de paquetes.

El flujo mostrado aquí sigue el enfoque basado en `dnf system-upgrade` que suele emplearse para estas migraciones.

## Paso 1 — Instalar las herramientas necesarias

```bash
sudo dnf install dnf-plugin-system-upgrade
```

## Paso 2 — Descargar los paquetes de la nueva versión

Ejemplo conceptual:

```bash
sudo dnf system-upgrade download --releasever=40
```

> ⚠️ Sustituye `40` por la **versión de Fedora de destino** que realmente quieras instalar. No copies este número literalmente para una actualización actual.

## Paso 3 — Reiniciar para completar la actualización

```bash
sudo dnf system-upgrade reboot
```

Durante este proceso Fedora reinicia y continúa la instalación de la nueva versión.

> 🚨 **Antes de una actualización mayor:** realiza copias de seguridad, revisa el espacio disponible y comprueba la documentación correspondiente a la versión de Fedora que vas a instalar.

---

# 13. Flujo mental para usar la terminal

Cuando trabajes con archivos, piensa en este orden:

```text
1. ¿Dónde estoy?
        ↓
      pwd
        ↓
2. ¿Qué hay aquí?
        ↓
       ls
        ↓
3. ¿Necesito entrar a otra carpeta?
        ↓
       cd
        ↓
4. ¿Necesito crear algo?
        ↓
   mkdir / touch
        ↓
5. ¿Necesito leerlo o editarlo?
        ↓
  cat / nano / code
        ↓
6. ¿Necesito moverlo o copiarlo?
        ↓
     mv / cp
        ↓
7. ¿Realmente necesito eliminarlo?
        ↓
       rm
```

## Regla de oro

> **Primero inspecciona → después actúa.**

Antes de ejecutar un comando destructivo, comprueba la ruta y el contenido.

Por ejemplo:

```bash
pwd
ls -la
```

Y recién después decide si necesitas `mv`, `cp` o `rm`.

---

# 🧠 Chuleta rápida

## Navegación

```bash
pwd              # ¿Dónde estoy?
ls               # ¿Qué hay aquí?
ls -la           # Ver todo con detalle
cd carpeta       # Entrar
cd ..            # Subir un nivel
cd ~             # Ir al directorio personal
```

## Crear

```bash
mkdir proyecto           # Crear carpeta
touch archivo.txt        # Crear archivo
mkdir -p a/b/c           # Crear carpetas anidadas
```

## Copiar y mover

```bash
cp archivo.txt copia.txt
cp -r carpeta1 carpeta2
mv archivo.txt carpeta/
mv viejo.txt nuevo.txt
```

## Leer y editar

```bash
cat archivo.txt
less archivo.txt
nano archivo.txt
code .
code archivo.py
```

## Eliminar

```bash
rm archivo.txt
rmdir carpeta_vacia
rm -r carpeta
rm -rf carpeta
```

## Productividad

```text
Tab      → autocompletar
↑ / ↓    → historial
Ctrl + L → limpiar pantalla
```

## Fedora

```bash
sudo dnf upgrade --refresh
dnf check-update
flatpak update
sudo dnf clean all
sudo reboot
```

---

# 📌 Mapa mental de comandos

```text
                    TERMINAL
                       │
       ┌───────────────┼────────────────┐
       │               │                │
   NAVEGAR          CREAR            GESTIONAR
       │               │                │
 pwd / ls / cd    mkdir / touch      cp / mv / rm
       │               │                │
       └───────────────┼────────────────┘
                       │
                  LEER / EDITAR
                       │
                cat / less / nano
                       │
                       ▼
                  PRODUCTIVIDAD
                       │
                 Tab / ↑ / ↓ / Ctrl+L
                       │
                       ▼
                    FEDORA
                       │
          dnf / flatpak / reboot
```

---

# ✅ Orden recomendado para memorizar

Aprende los comandos en este orden:

```text
1. pwd       → saber dónde estás
2. ls        → ver qué existe
3. cd        → moverte
4. mkdir     → crear carpetas
5. touch     → crear archivos
6. cat       → leer archivos
7. nano      → editar archivos
8. cp        → copiar
9. mv        → mover / renombrar
10. rm       → eliminar
11. sudo     → ejecutar con privilegios
12. dnf      → administrar paquetes en Fedora
```

> 🎯 **Objetivo inicial:** poder crear una estructura de proyecto, navegar por ella, crear archivos, editarlos, copiarlos, moverlos y eliminarlos sin depender de la interfaz gráfica.
