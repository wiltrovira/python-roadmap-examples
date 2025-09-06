# Guía completa: Crear un proyecto en Python con Poetry, pipx y VS Code

## 1. Introducción

Esta guía tiene como objetivo enseñar a los desarrolladores, especialmente principiantes, a crear proyectos en Python utilizando herramientas modernas que facilitan la gestión de dependencias, entornos virtuales y versiones de Python. Usar **Poetry**, **pipx** y **VS Code** permite mantener un flujo de trabajo limpio, reproducible y organizado.

### Beneficios

- **Aislamiento de proyectos**: Cada proyecto tiene su propio entorno virtual, evitando conflictos entre dependencias.
- **Gestión de versiones de Python**: Con pyenv se puede usar diferentes versiones de Python en distintos proyectos sin afectar el sistema.
- **Reproducibilidad**: Gracias a `pyproject.toml` y `poetry.lock`, todos los miembros de un equipo pueden tener exactamente las mismas versiones de paquetes.
- **Herramientas globales seguras**: pipx permite instalar herramientas como Poetry, Black y Flake8 de forma aislada, sin ensuciar el sistema.
- **Integración con VS Code**: Facilita el desarrollo, linting y formateo automático.

### Problemas que resuelve

- Conflictos de dependencias entre proyectos.
- Problemas con diferentes versiones de Python en el sistema.
- Necesidad de mantener el sistema limpio y sin modificaciones globales innecesarias.
- Inconsistencias de versiones de paquetes entre desarrolladores.

Esta guía explica cómo configurar un entorno moderno de desarrollo en Python, usando:

- **pyenv**: para manejar múltiples versiones de Python sin tocar el sistema.
- **pipx**: para instalar herramientas globales aisladas.
- **Poetry**: para manejar dependencias y entornos virtuales por proyecto.
- **VS Code**: como editor de código con integración al entorno virtual.

## 2. Instalar pyenv

**Concepto:** `pyenv` permite instalar y manejar múltiples versiones de Python sin modificar el Python del sistema.

- [Comandos de `pyenv`](./01_01_pyenv-commands.md) → Comandos para instalar y usar `pyenv`.

## 3. Instalar versiones de Python con pyenv

**Concepto:** Puedes tener varias versiones de Python instaladas y cambiar entre ellas globalmente (`pyenv global`) o por proyecto (`pyenv local`).

```bash
pyenv install 3.13.5
pyenv install 3.12.11
```

Verifica:

```bash
pyenv versions
```

## 4. Configurar versión global mínima

Esto asegura que los comandos de Python y Poetry encuentren un intérprete válido.

```bash
pyenv global 3.13.5
python --version
which python
```

## 5. Instalar pipx

**Concepto:** `pipx` permite instalar herramientas globales en entornos virtuales aislados, evitando mezclar paquetes con tu sistema o proyectos.

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

## 6. Instalar Poetry con pipx

**Concepto:** Poetry gestiona dependencias y entornos virtuales por proyecto, reemplazando la necesidad de `requirements.txt`.

```bash
pipx install poetry
poetry --version
```

## 7. Crear un proyecto nuevo con Poetry

**Concepto:** `pyproject.toml` contiene todas las dependencias y configuración del proyecto.

```bash
cd ~/Dev/python-roadmap-examples/proyectos
poetry new proyecto3-poetry
cd proyecto3-poetry
```

Estructura creada:

```text
proyecto3-poetry/
├── pyproject.toml
├── README.md
├── proyecto3_poetry/
│   └── __init__.py
└── tests/
    └── __init__.py
```

## 8. Configurar Python por proyecto con pyenv

```bash
pyenv local 3.13.5
```

Crea un archivo `.python-version` en el proyecto para usar esa versión automáticamente.

## 9. Configurar el entorno virtual de Poetry

**Concepto:** Poetry crea un entorno virtual aislado y lo asocia a la versión de Python definida por pyenv.

```bash
poetry env use $(pyenv which python)
poetry run python --version
```

## 10. Instalar herramientas de desarrollo (flake8 y black)

```bash
poetry add --dev flake8 black
```

- `--dev` indica que son dependencias solo para desarrollo.  
- No necesitas activar el entorno virtual; Poetry maneja la instalación automáticamente.

## 11. Configuración opcional de Flake8 y Black

### `.flake8`

```ini
[flake8]
max-line-length = 88
exclude = .venv,__pycache__,build,dist
ignore = E203,W503
```

### `pyproject.toml` para Black

```toml
[tool.black]
line-length = 88
target-version = ['py310']
```

## 12. Ejecutar comandos dentro del proyecto

### Con `poetry shell`

```bash
poetry shell
flake8 ruta_del_codigo/
black ruta_del_codigo/
```

### Sin activar el shell

```bash
poetry run flake8 ruta_del_codigo/
poetry run black ruta_del_codigo/
```

## 13. Flujo recomendado de trabajo

1. Instalar versiones de Python con pyenv.  
2. Definir versión global mínima: `pyenv global X.Y.Z`.  
3. Crear un proyecto con `poetry new`.  
4. Configurar versión local de Python: `pyenv local X.Y.Z`.  
5. Configurar entorno de Poetry: `poetry env use $(pyenv which python)`.  
6. Instalar dependencias: `poetry add paquete` o `poetry add --dev paquete`.  
7. Ejecutar scripts o comandos con `poetry run` o `poetry shell`.  
8. Integrar con VS Code usando el intérprete del entorno virtual de Poetry.

## 14. Integración con VS Code

1. Instala la extensión oficial de Python.  
2. Abre la carpeta del proyecto.  
3. Selecciona el **intérprete de Python** que apunta al entorno virtual de Poetry:

    ```bash
    poetry env info -p
    ```

4. Configura el formateador (Black) y linter (Flake8) en VS Code.

✅ Con este procedimiento tendrás un entorno moderno, reproducible y aislado para cada proyecto, sin tocar el Python del sistema.
