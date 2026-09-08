# 📘 Glosario de Git y GitHub

> Guía de referencia rápida para comprender Git, GitHub y el flujo básico de trabajo con repositorios.

---

## 📑 Índice

1. [Conceptos fundamentales](#1-conceptos-fundamentales)
2. [Git vs. GitHub](#2-git-vs-github)
3. [Estados y flujo de trabajo](#3-estados-y-flujo-de-trabajo)
4. [Comandos esenciales](#4-comandos-esenciales)
   - [Diagnóstico](#41-diagnóstico)
   - [Configuración](#42-configuración)
   - [Flujo diario](#43-flujo-diario)
5. [Commits y convenciones](#5-commits-y-convenciones)
6. [Flujo mental de trabajo](#6-flujo-mental-de-trabajo)
7. [Chuleta rápida](#7-chuleta-rápida)

---

# 1. Conceptos fundamentales

## Git

**Git** es un sistema de control de versiones distribuido que permite registrar los cambios realizados en un proyecto y consultar su historial.

### Idea clave

Git permite volver a estados anteriores del proyecto, comparar cambios y trabajar de manera organizada sobre el código.

---

## GitHub

**GitHub** es una plataforma que permite alojar repositorios Git de forma remota y colaborar con otras personas.

### Idea clave

Git trabaja principalmente con el historial del proyecto; GitHub facilita almacenar ese repositorio en línea, compartirlo y sincronizarlo entre equipos.

---

## Repositorio (Repository / Repo)

Un **repositorio** es un proyecto administrado por Git que contiene los archivos del proyecto y su historial de versiones.

Dentro del proyecto existe una carpeta especial llamada **`.git`**, donde Git almacena la información necesaria para controlar las versiones.

```text
proyecto/
├── archivo1.py
├── archivo2.py
└── .git/
```

> ⚠️ No se debe modificar manualmente el contenido de `.git` salvo que sepas exactamente lo que estás haciendo.

---

## Commit

Un **commit** es un registro del estado del proyecto en un momento determinado.

Puede entenderse como un **punto de guardado con nombre**, porque incluye un mensaje que describe qué cambio se realizó.

```bash
git commit -m "agregar validacion del telefono"
```

### Buen commit

Debe explicar de manera breve y clara **qué cambió**.

---

## Staging Area

La **Staging Area** o **zona de preparación** es el área intermedia donde seleccionas qué cambios quieres incluir en el próximo commit.

El comando principal para pasar cambios a esta zona es:

```bash
git add archivo.py
```

O para preparar todos los cambios del directorio actual:

```bash
git add .
```

### Flujo conceptual

```text
Archivos modificados
        ↓
    git add
        ↓
  Staging Area
        ↓
  git commit
        ↓
 Historial de Git
```

---

## Main

**`main`** es el nombre utilizado habitualmente para la rama principal de un repositorio.

```text
main
```

> 💡 `main` es un nombre de rama, no significa que Git obligatoriamente deba usarlo como rama principal. La configuración depende del proyecto y del repositorio.

---

## Personal Access Token (PAT)

Un **Personal Access Token (PAT)** es una credencial generada en GitHub que puede utilizarse para autenticar determinadas operaciones en lugar de una contraseña tradicional.

```text
GitHub
   ↓
Personal Access Token
   ↓
Autenticación de operaciones remotas
```

> ⚠️ Un PAT debe tratarse como una contraseña: no debe publicarse ni subirlo al repositorio.

---

# 2. Git vs. GitHub

| Concepto | Git | GitHub |
|---|---|---|
| Tipo | Sistema de control de versiones | Plataforma de alojamiento y colaboración |
| Funciona localmente | ✅ | No es necesario para usar Git localmente |
| Historial de cambios | ✅ | Aloja el repositorio remoto |
| Repositorios remotos | Se conecta a ellos | Los aloja |
| Colaboración | Posible mediante Git | Facilita colaboración, revisión y trabajo remoto |

### Forma sencilla de recordarlo

```text
Git      → controla las versiones
GitHub   → aloja y comparte repositorios Git
```

---

# 3. Estados y flujo de trabajo

El flujo básico de cambios en Git puede visualizarse así:

```text
┌──────────────────────┐
│ Working Directory    │
│ Archivos modificados │
└──────────┬───────────┘
           │
        git add
           ↓
┌──────────────────────┐
│ Staging Area         │
│ Cambios seleccionados│
└──────────┬───────────┘
           │
      git commit
           ↓
┌──────────────────────┐
│ Repositorio local    │
│ Historial de commits │
└──────────┬───────────┘
           │
        git push
           ↓
┌──────────────────────┐
│ Repositorio remoto   │
│ GitHub               │
└──────────────────────┘
```

### Los 4 conceptos que debes memorizar

1. **Working Directory:** archivos con los que estás trabajando.
2. **Staging Area:** cambios seleccionados para el próximo commit.
3. **Local Repository:** historial guardado en tu repositorio local.
4. **Remote Repository:** copia remota, por ejemplo, en GitHub.

---

# 4. Comandos esenciales

## 4.1 Diagnóstico

### `git status`

Muestra el estado actual del repositorio.

Permite identificar, entre otras cosas:

- archivos modificados;
- archivos preparados para commit;
- archivos sin seguimiento (*untracked*);
- la rama actual;
- información sobre cambios pendientes.

```bash
git status
```

---

### `git log`

Muestra el historial de commits del repositorio.

```bash
git log
```

Para salir de la vista del historial:

```text
q
```

### Uso básico

Sirve para revisar **qué cambios se han registrado y en qué orden**.

---

## 4.2 Configuración

### `git config --global user.name`

Define el nombre que Git utilizará como autor de los commits realizados desde ese equipo.

```bash
git config --global user.name "Nombre"
```

---

### `git config --global user.email`

Define el correo electrónico asociado a la identidad utilizada para los commits.

```bash
git config --global user.email "correo@ejemplo.com"
```

> 💡 El nombre y el correo forman parte de la información de autor del commit. Para que los commits aparezcan correctamente asociados a tu cuenta de GitHub, normalmente conviene utilizar un correo reconocido por esa cuenta.

---

### `git config --global credential.helper store`

Configura Git para almacenar las credenciales utilizadas para autenticarse con repositorios remotos.

```bash
git config --global credential.helper store
```

> ⚠️ **Precaución:** este método puede almacenar las credenciales localmente de una forma que no es adecuada para todos los equipos. En un equipo compartido o sensible, es preferible utilizar un método de autenticación más seguro.

---

## 4.3 Flujo diario

El flujo básico que debes memorizar es:

```text
1. Modificar archivos
2. git add
3. git commit
4. git push
```

### Paso 1 — Preparar cambios

```bash
git add .
```

Agrega al **Staging Area** todos los cambios del directorio actual que Git pueda preparar.

También puedes agregar archivos específicos:

```bash
git add archivo.py
```

---

### Paso 2 — Crear commit

```bash
git commit -m "mensaje"
```

Crea un nuevo commit en el repositorio local.

Ejemplo:

```bash
git commit -m "agregar validacion de telefono"
```

---

### Paso 3 — Enviar a GitHub

```bash
git push
```

Envía los commits locales al repositorio remoto configurado.

```text
Local
  ↓
 git push
  ↓
GitHub
```

---

# 5. Commits y convenciones

Una convención útil para mantener mensajes de commit consistentes es **Conventional Commits**.

La estructura básica es:

```text
tipo: descripcion breve
```

## `docs:`

Se utiliza cuando el cambio afecta únicamente documentación, apuntes o notas.

```bash
git commit -m "docs: agregar bitacora de condicionales"
```

---

## `feat:`

Se utiliza cuando agregas una nueva funcionalidad o capacidad al proyecto.

```bash
git commit -m "feat: completar ejercicio de condicionales"
```

---

## `fix:`

Se utiliza cuando corriges un error o comportamiento incorrecto.

```bash
git commit -m "fix: corregir sintaxis del operador and"
```

---

## `refactor:`

Se utiliza cuando reorganizas, simplificas o limpias el código **sin cambiar su comportamiento esperado**.

```bash
git commit -m "refactor: simplificar validacion de contactos"
```

---

## `style:`

Se utiliza para cambios de formato que no modifican la lógica del programa.

Ejemplos:

- espacios;
- indentación;
- formato;
- limpieza de comentarios.

```bash
git commit -m "style: ordenar formato del archivo"
```

---

## Regla rápida para tus commits

Como regla práctica de estudio:

> **Usa mensajes cortos, claros y específicos.**

Una estructura recomendable es:

```text
tipo: verbo + cambio
```

Ejemplos:

```text
docs: agregar apuntes de funciones
feat: agregar menu de contactos
fix: corregir validacion del telefono
refactor: separar validaciones en funciones
style: ordenar espacios del codigo
```

### ✅ Buen mensaje

```text
feat: agregar validacion del telefono
```

### ❌ Mensaje poco útil

```text
cambios
```

---

# 6. Flujo mental de trabajo

Cada vez que termines una parte pequeña de tu trabajo, piensa:

```text
¿Cambie algo?
    ↓
   Sí
    ↓
¿Quiero incluirlo en el próximo guardado?
    ↓
   Sí
    ↓
git add
    ↓
¿El cambio ya representa una unidad lógica?
    ↓
   Sí
    ↓
git commit
    ↓
¿Quiero sincronizarlo con GitHub?
    ↓
   Sí
    ↓
git push
```

### Idea fundamental

```text
git add     → selecciono lo que quiero guardar

git commit  → guardo ese cambio en el historial local

git push    → envío ese historial al remoto
```

---

# 7. ⚡ Chuleta rápida

## Conceptos

| Concepto | Significado |
|---|---|
| **Git** | Control de versiones |
| **GitHub** | Plataforma para alojar y colaborar con repositorios Git |
| **Repositorio** | Proyecto administrado por Git |
| **Commit** | Registro de un estado del proyecto |
| **Staging Area** | Zona donde preparas cambios para el commit |
| **`main`** | Nombre habitual de la rama principal |
| **PAT** | Credencial de autenticación de GitHub |

## Comandos

| Comando | Función |
|---|---|
| `git status` | Ver estado del repositorio |
| `git log` | Ver historial de commits |
| `git add .` | Preparar cambios |
| `git add archivo.py` | Preparar un archivo específico |
| `git commit -m "mensaje"` | Crear commit |
| `git push` | Enviar commits al remoto |
| `git config --global user.name "Nombre"` | Configurar nombre del autor |
| `git config --global user.email "correo"` | Configurar correo del autor |

## Tipos de commit

| Tipo | Cuándo usarlo |
|---|---|
| `docs:` | Documentación |
| `feat:` | Nueva funcionalidad |
| `fix:` | Corrección de errores |
| `refactor:` | Mejora interna sin cambiar comportamiento |
| `style:` | Formato o estilo |

---

# 🧠 Fórmula para memorizar Git

```text
MODIFICAR
   ↓
git status
   ↓
git add
   ↓
git commit
   ↓
git push
   ↓
GitHub
```

> **Git guarda el historial. GitHub lo aloja y facilita compartirlo.**
