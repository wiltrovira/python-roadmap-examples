# 🚀 Conceptos básicos de pyenv en Pop!_OS / Ubuntu 22.04

Este directorio contiene información sobre **pyenv**, una herramienta para gestionar múltiples versiones de Python en Ubuntu/Pop!_OS.


## 📚 Contenido

- [Comandos de pyenv](01-pyenv-commands.md) → Comandos para instalar y usar `pyenv`.
- [Preguntas frecuentes](01-pyenv-faq.md) → Preguntas frecuentes de `pyenv`.

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

## 🔧 ¿Qué problemas resuelve?

Supón que:

- Un proyecto requiere Python 3.8.
- Otro requiere Python 3.12.
- Tu sistema tiene preinstalado Python 3.10.

👉 Sin pyenv, es difícil cambiar entre versiones o incluso tenerlas todas instaladas sin errores.

## 📁 ¿Cómo funciona pyenv?

- Descarga e instala versiones de Python en una carpeta local (~/.pyenv).
- Usa "shims" (enlaces) para redirigir comandos como python, pip a la versión correcta.
- Se integra con tu shell (bash, zsh, fish) para cambiar de versión automáticamente al entrar en una carpeta de proyecto.

## 🧪 Diferencia entre pyenv y venv

| Herramienta | ¿Para qué sirve? |
| ----------- | ---------------- |
| pyenv       | Gestiona versiones de Python |
| venv        | Crea entornos virtuales con una versión específica |
