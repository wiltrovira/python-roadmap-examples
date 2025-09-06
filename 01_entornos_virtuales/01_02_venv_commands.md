# 🚀 Crear un entorno virtual con `venv` en Pop!_OS / Ubuntu 22.04

## Crea un entorno virtual con venv

```bash
python -m venv .venv
```

- venv es el módulo de Python para crear entornos virtuales aislados.
- .venv es la carpeta donde se creará el entorno virtual.
- Lo que hace este comando:
  - Crea un directorio .venv dentro de tu proyecto.
  - Copia binarios de Python y pip de la versión activa (3.10.14) al entorno.
  - Permite instalar paquetes sin afectar Python del sistema ni otras versiones de pyenv.

## Activa el entorno virtual

```bash
source .venv/bin/activate
```

- Este comando activa el entorno virtual que acabas de crear.
- Cambia algunas variables del shell, principalmente:
- $PATH → para usar los binarios de .venv/bin primero.
- Prompt de la terminal → ahora aparece algo como (.venv) indicando que estás dentro del entorno.

## Verifica

```bash
python --version  # Debe mostrar Python 3.8.18
```

Ahora puedes instalar paquetes sin afectar nada fuera del proyecto:

```bash
pip install requests
```

## 🏗️ Ejemplo: Crear Proyecto 2 con Python 3.12

```bash
mkdir ~/proyecto2-python312
cd ~/proyecto2-python312
pyenv local 3.12.3
python -m venv .venv
source .venv/bin/activate
python --version  # Debe mostrar Python 3.12.3
```

## 🔄 Cómo cambiar entre proyectos

Cada vez que cambias de carpeta:

```bash
cd ~/proyecto1-python38
source .venv/bin/activate  # Python 3.8
```

```bash
cd ~/proyecto2-python312
source .venv/bin/activate  # Python 3.12
```

Y cuando termines, puedes desactivar el entorno virtual con:

## 🔄 Salir del entorno y volver al Python normal

Se usa cuando estás dentro de un entorno virtual de Python (por ejemplo, creado con venv) y sirve para salir de ese entorno.

```bash
deactivate
```

- Restaura el $PATH a su estado original antes de activar el entorno.
- Esto significa que los binarios python y pip volverán a ser los del sistema o los de pyenv según la versión activa fuera del entorno virtual.
- Cambia el prompt de la terminal de nuevo a su forma normal.
- Por ejemplo, si tu prompt mostraba (.venv) al activar el entorno, después de deactivate desaparecerá.
- Aísla nuevamente los paquetes: cualquier paquete que instales después de desactivar ya no afectará el entorno virtual que habías activado.
