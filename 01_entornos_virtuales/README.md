# 🐍 Entornos virtuales en Python con con `pyenv` y `venv`

Este directorio contiene información sobre **`pyenv`** y **`venv`**, herramientas para gestionar múltiples versiones de Python y entornos virtuales en Ubuntu/Pop!_OS

## 📚 Contenido

- [Comandos de `pyenv`](./01_01_pyenv-commands.md) → Comandos para instalar y usar `pyenv`.
- [Preguntas frecuentes](./01_01_pyenv-faq.md) → Preguntas frecuentes de `pyenv`.
- [Comandos de `venv`](./01_02_venv-commands.md) → Comandos para usar `venv`.

## 🎯 Resumen rápido

- `pyenv` permite instalar varias versiones de Python.
- Cambiar versiones por proyecto o globalmente.
- Combinar con `venv` para entornos virtuales aislados.

Tener varios proyectos que requieren diferentes versiones de Python es muy común, y la mejor práctica es usar herramientas que te permitan aislar ambientes por proyecto y gestionar múltiples versiones de Python.

Usar `pyenv` + `venv` por proyecto

## 🎯 ¿Qué es pyenv?

`pyenv` es una herramienta de línea de comandos que te permite instalar, gestionar y cambiar fácilmente entre múltiples versiones de Python en tu sistema.

Sirve para:

- Instalar versiones específicas: pyenv install 3.8.18, 3.10.14, etc.
- Tener varias versiones de Python en tu máquina (por ejemplo: 3.7, 3.8, 3.10, 3.12).
- Cambiar la versión de Python global o por proyecto.
- Combinar con `pyenv` y `venv` para aislar ambientes fácilmente.
- Elegir una versión diferente para cada proyecto.
- Evitar conflictos con el Python del sistema operativo.
- Trabajar con proyectos antiguos o nuevos sin problemas de compatibilidad.

### 🔧 ¿Qué problemas resuelve `venv`?

Supón que:

- Un proyecto requiere Python 3.8.
- Otro requiere Python 3.12.
- Tu sistema tiene preinstalado Python 3.10.

👉 Sin pyenv, es difícil cambiar entre versiones o incluso tenerlas todas instaladas sin errores.

### 📁 ¿Cómo funciona `pyenv`?

- Descarga e instala versiones de Python en una carpeta local (~/.pyenv).
- Usa "shims" (enlaces) para redirigir comandos como python, pip a la versión correcta.
- Se integra con tu shell (bash, zsh, fish) para cambiar de versión automáticamente al entrar en una carpeta de proyecto.

## 🎯 ¿Qué es `venv`?

`venv` es una herramienta incluida en Python (a partir de la versión 3.3) que permite crear **entornos virtuales**.  
Un entorno virtual es una carpeta aislada que contiene su propio **intérprete de Python**, así como sus propios paquetes y dependencias.

¿Para qué sirve?
El objetivo de `venv` es permitir que cada proyecto tenga sus propias librerías y versiones de Python, **sin interferir** con otros proyectos o con la instalación global del sistema.

Ejemplo:

- Proyecto A usa **Django 3.2**
- Proyecto B usa **Django 5.0**

Con `venv`, ambos proyectos pueden coexistir en la misma máquina sin generar conflictos.

### 🛠️ Problemas que resuelve `venv`

- **Conflictos de dependencias:** evita que distintos proyectos usen versiones incompatibles de las mismas librerías.
- **Reproducibilidad:** facilita compartir el mismo entorno entre equipos de trabajo.
- **Seguridad:** no necesitas instalar librerías de forma global, reduciendo riesgos en el sistema.

### ⚙️ ¿Cómo funciona `venv`?

Cuando creas un entorno con `venv`, Python genera una carpeta con:

- Una copia (o enlace) del intérprete de Python.
- Un directorio propio para instalar paquetes (`site-packages`).
- Scripts de activación para usar el entorno.

Esto permite que, al **activar el entorno**, Python y `pip` trabajen únicamente dentro de esa carpeta, ignorando la instalación global.

## 🧪 Diferencia entre pyenv y venv

| Herramienta | ¿Para qué sirve? |
| ----------- | ---------------- |
| pyenv       | Gestiona versiones de Python |
| venv        | Crea entornos virtuales con una versión específica |
