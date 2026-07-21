# Glosario de Conceptos de Git y GitHub

* **Git:** Sistema de control de versiones local que rastrea los cambios en el código mediante puntos de restauración.
* **GitHub:** Plataforma en la nube que aloja repositorios de Git remotos para tener respaldos y sincronizar proyectos.
* **Repositorio (Repo):** Carpeta administrada por Git que contiene todo el código y su historial de cambios (`.git`).
* **Commit:** Un "punto de guardado" o fotografía del estado del proyecto en un momento específico con un mensaje explicativo.
* **Staging Area:** Zona intermedia donde se eligen los archivos modificados (`git add`) antes de confirmarlos en un commit.
* **Main:** Nombre estándar de la rama principal de desarrollo del proyecto.
* **Personal Access Token (PAT):** Clave de seguridad generada en GitHub para autenticar la terminal en lugar de usar contraseñas tradicionales.

---

# Comandos Esenciales de Git

## Diagnóstico y Configuración
* `git status`: Muestra el estado actual de los archivos (modificados, agregados o sin seguimiento).
* `git log`: Muestra el historial completo de commits realizados (se sale presionando la tecla `q`).
* `git config --global user.name "Nombre"`: Establece la firma del autor para los commits en el equipo.
* `git config --global user.email "correo@ejemplo.com"`: Asigna el correo asociado a la cuenta de GitHub.
* `git config --global credential.helper store`: Guarda las credenciales/tokens localmente para no ingresarlos en cada push.

## Flujo Diario de Guardado (Ciclo de 3 Pasos)
* `git add .`: Agrega todos los archivos modificados a la zona de preparación (Staging Area).
* `git commit -m "mensaje"`: Crea el punto de guardado local con un mensaje explicativo.
* `git push`: Envía los commits locales al repositorio remoto en GitHub.