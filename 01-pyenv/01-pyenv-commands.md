# 🚀 Instalación de pyenv en Pop!_OS / Ubuntu 22.04

Tener varios proyectos que requieren diferentes versiones de Python es muy común, y la mejor práctica es usar herramientas que te permitan aislar ambientes por proyecto y gestionar múltiples versiones de Python.

Usar `pyenv` + `venv` por proyecto

## Instalar dependencias necesarias

```bash
sudo apt update

sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev git
```

## Instalar pyenv

```bash
curl https://pyenv.run | bash
```

## Modificar archivo ~/.bashrc o ~/.zshrc

Agrega estas líneas al final de tu archivo ~/.bashrc o ~/.zshrc, para asegurar que `pyenv` se cargue automáticamente en todos los tipos de terminal que uses.

```text
# Load pyenv automatically by appending
# the following to 
# ~/.bash_profile if it exists, otherwise ~/.profile (for login shells)
# and ~/.bashrc (for interactive shells) :

export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init - bash)"

# Restart your shell for the changes to take effect.

# Load pyenv-virtualenv automatically by adding
# the following to ~/.bashrc:

eval "$(pyenv virtualenv-init -)"
```

En detalle, esto lo que hace es lo siguiente:

```text
export PYENV_ROOT="$HOME/.pyenv"
```

- Define la carpeta donde pyenv almacena sus versiones de Python y shims.
- Por defecto, ~/.pyenv.
- $PYENV_ROOT se usa después para referirse a esa ruta.

```text
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
```

- Verifica si existe el directorio $PYENV_ROOT/bin.
- Si existe, lo agrega al PATH de tu sistema, para que los comandos de pyenv (pyenv, python, etc.) sean reconocidos en la terminal.
- :$PATH mantiene las rutas existentes sin sobrescribirlas.

```text
eval "$(pyenv init - bash)"
 ```

- pyenv init - bash genera un bloque de código shell que:
  - Configura los shims de pyenv para redirigir los comandos python, pip, etc., a la versión correcta.
  - Permite que pyenv cambie automáticamente la versión cuando entras en un proyecto con .python-version.
- eval ejecuta ese bloque en tu sesión actual del shell.

## Reiniciar terminal

Y luego reinicia la terminal o ejecuta:

```bash
source ~/.bashrc
```

## Listar las versiones de Python

Así podrás ver la versiones disponibles para instalar

```bash
pyenv install --list
```

```text
3.13.5
3.13.5t
3.14.0rc1
3.14.0rc1t
3.14-dev
3.14t-dev
```

- 🧾 Versión normal (ej: 3.13.5)
- ✅ Es la versión oficial y estable de Python 3.13.5.
- Usada para proyectos de producción o desarrollo general.
- Es la que usarías normalmente si no necesitas nada especial.
- 🔒 Sufijo t (ej: 3.13.5t, 3.14.0rc1t, 3.15t-dev)
- La t significa que esa versión de Python está compilada con soporte para la biblioteca tcl/tk, que se usa para interfaces gráficas como Tkinter.
- Esto es útil si planeas usar librerías como Tkinter o quieres asegurarte de tener soporte visual en tu instalación.
- ⚠️ Sufijo rc (ej: 3.14.0rc1, 3.14.0rc1t)
- rc = Release Candidate.
- Es una versión preliminar que puede contener bugs.
- Útil para probar nuevas funciones antes del lanzamiento oficial.
- 🔬 Sufijo -dev (ej: 3.14-dev, 3.14t-dev, 3.15t-dev)
- Versiones de desarrollo de futuras versiones de Python.
- Generalmente apuntan al código más reciente en desarrollo.
- ⚠️ No son estables y no se recomienda usarlas para producción.

## Usar pyenv para instalar versiones específicas de Python

Instala diferentes versiones de Python con `pyenv`:

```bash
pyenv install 3.13.5         # versión estable sin GUI
pyenv install 3.13.5t        # versión estable con soporte Tkinter
pyenv install 3.14.0rc1t     # versión candidata con soporte GUI
pyenv install 3.15t-dev      # versión en desarrollo con soporte GUI
```

Esto puede tardar unos minutos, ya que compila Python desde el código fuente.

## Ver versiones instaladas

Con el siguiente comando se verán las versiones de Python instaladas en el sistema

```bash
pyenv versions
```

En mi sistema, las versiones instaladas se ven así:

```text
* system (set by /home/wiltrovira/.pyenv/version)
  3.11.13
  3.12.11
  3.13.5
```

- system (set by /home/wiltrovira/.pyenv/version)
  - La * indica que esta es la versión activa actualmente.
  - system significa que estás usando la versión de Python que viene con tu sistema operativo, no una instalada por `pyenv`.
  - (set by /home/wiltrovira/.pyenv/version) indica que hay un archivo .python-version en tu home que fuerza a `pyenv` a usar la versión system de manera global.

- 3.11.13, 3.12.11, 3.13.5
  - Estas son versiones de Python instaladas por `pyenv` en tu sistema.
  - Ninguna de estas está activa actualmente porque no tienen la * al lado.
  - Puedes cambiar a cualquiera de ellas usando `pyenv` global <versión> (para todo el sistema) o `pyenv` local <versión> (solo en un proyecto específico).

## Desinstalar una versión de Python con `pyenv`

En este ejemplo, desinstalaré la versión 3.11.13

```bash
pyenv uninstall 3.11.13
```

Se confirma que desea desinstalar

```text
pyenv: remove /home/usuario/.pyenv/versions/3.11.13? (y/N) y
pyenv: 3.11.13 uninstalled
```

Luego, se consultan las versiones disponibles

```bash
pyenv versions
```

```text
* system (set by /home/plinterbryan/.pyenv/version)
  3.12.11
  3.13.5
```

La versión 3.11.13 fue desinstalada con éxito.

## Cambiar la versión de Python del sistema global

Al consultar la versión de Python en mi sistema

```bash
python3 --version
```

Mi sistema muestra la versión 3.10.12

```text
Python 3.10.12
```

Ahora, opcionalmente, puedo cambiar la versión de Python que usa mi sistema de manera global.

```bash
pyenv global 3.13.5 # En todo el sistema
```

Luego, al comprobar las versiones nuevamente, puedes utilizar los siguientes 2 comandos:

```bash
pyenv versions
```

El resultado: La versión del sistema es 3.13.5

```text
system
3.11.13
3.12.11
* 3.13.5 (set by /home/usuario/.pyenv/version)
```

Otra forma de comprobar la versión actual usada en el sistema es

```bash
python3 --version
```

El resultado es

```text
Python 3.10.12
```

También puedo usar un alias de python que apunta python3, el cual  tengo configurado en mi archivo ~/.bashrc

```bash
# Alias para usar python como python3 en archivo ~/.bashrc
alias python=python3
```

💡 Tip: Esto es muy útil en Ubuntu 22.04 / Pop!_OS, porque el sistema solo instala python3 por defecto.

Al ejecutar

```bash
python --version
```

El resultado es

```text
Python 3.10.12
```

Si quiero volver a utilizar la versión del sistema predeterminada:

```bash
pyenv global system
```

## Cambiar la versión de Python local a un proyecto

Cuando tienes un proyecto,

```bash
pyenv local 3.8.18  # Solo en el proyecto actual
```

## Cambiar temporalmente la versiónde Python en la terminal

Este comando le dice a pyenv que use temporalmente la versión 3.10.14 de Python solo en la terminal actual.

```bash
pyenv shell 3.10.14
```

✅ Esto es útil si quieres probar algo sin afectar tu configuración global o local. Cambia la versión solo en la sesión actual de terminal (temporal).

## 💡 Tip extra (VS Code)

Si usas Visual Studio Code, y tienes `.venv` en tu carpeta del proyecto:

- Abre el proyecto en VS Code.
- Presiona Ctrl+Shift+P → Python: Select Interpreter
- Elige la que diga .venv/bin/python

## 🏗️ Ejemplo: Crear Proyecto 1 con Python 3.8

### Crea una carpeta para el proyecto

```bash
mkdir ~/proyecto1-python38
cd ~/proyecto1-python38
```

### Establece la versión de Python local

```bash
pyenv local 3.8.18
```

📌 Esto crea un archivo .python-version en la carpeta, que hace que siempre uses Python 3.8.18 dentro de este proyecto.

### Crea un entorno virtual con venv:

```bash
python -m venv .venv
```

- venv es el módulo de Python para crear entornos virtuales aislados.
- .venv es la carpeta donde se creará el entorno virtual.
- Lo que hace este comando:
  - Crea un directorio .venv dentro de tu proyecto.
  - Copia binarios de Python y pip de la versión activa (3.10.14) al entorno.
  - Permite instalar paquetes sin afectar Python del sistema ni otras versiones de pyenv.

### Activa el entorno virtual

```bash
source .venv/bin/activate
```

- Este comando activa el entorno virtual que acabas de crear.
- Cambia algunas variables del shell, principalmente:
- $PATH → para usar los binarios de .venv/bin primero.
- Prompt de la terminal → ahora aparece algo como (.venv) indicando que estás dentro del entorno.

### Verifica

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
