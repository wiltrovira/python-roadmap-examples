# 📓 🚀 Instalación básica en un entorno virtual (recomendado)

Para mayor información: [Instalación de pyenv en Pop!_OS / Ubuntu 22.04](../01-pyenv/01-pyenv-commands.md)

## Crear entorno virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Instalar Jupyter Notebook y JupyterLab

```bash
pip install notebook jupyterlab
```

## Iniciar Notebook

jupyter notebook

## Iniciar JupyterLab

jupyter lab

✍️ Nota: Los notebooks aquí incluidos pueden abrirse tanto en la interfaz clásica de Jupyter Notebook como en JupyterLab o directamente desde Visual Studio Code con la extensión de Jupyter.

## Cómo registrar un venv como kernel en Jupyter

### 1️⃣ Crea (o activa) tu entorno virtual

Si no lo tienes todavía, lo creas en tu proyecto:

```bash
python -m venv .venv
```

Actívalo (Linux/Mac):

```bash
source .venv/bin/activate
```

### 2️⃣ Instala ipykernel en ese entorno

Con el entorno activado, instala la librería que permite a Jupyter reconocerlo:

```bash
pip install ipykernel
```

### 3️⃣ Registra el kernel

Ejecuta (con el entorno activado):

```bash
python -m ipykernel install --user --name=py3135_roadmap_examples --display-name "Python 3.13.5 (Roadmap Examples)"
```

- `--name`: es el identificador interno del kernel (no debe tener espacios).
  - Es el identificador interno.
  - No admite espacios ni caracteres raros.
  - Es el que verás en la salida de jupyter kernelspec list.
  - Ejemplo: mi_proyecto_env, datascience, py311_venv, py3135_roadmap_examples.

- `--display-name`: es el nombre amigable que verás en Jupyter al seleccionarlo.
  - Es el nombre amigable que verás en Jupyter Notebook/Lab en el menú “Select Kernel”.
  - Puede tener espacios, mayúsculas, símbolos.
  - Ejemplo: "PPython 3.13.5 (Roadmap Examples)".

  📌 Buenas prácticas para nombrarlos

1. Incluye la versión de Python (muy útil si trabajas con varios entornos diferentes):

   - `--name=py311_projectx`  
   - `--display-name="Python 3.11 (Project X)"`

2. Refleja el proyecto o propósito.  
   Ejemplo para un proyecto de *machine learning*:  

   - `--name=ml_env`  
   - `--display-name="Python (ML Env)"`

3. Mantén consistencia entre entornos:  

   - Siempre usa minúsculas y guiones bajos en `--name`.  
   - Usa formato uniforme en `--display-name`.  

   Ejemplo para distintos proyectos:  

   - `--name=py310_proyectoA` → `"Python 3.10 (Proyecto A)"`  
   - `--name=py311_proyectoB` → `"Python 3.11 (Proyecto B)"`

4. No uses nombres genéricos como `env` o `venv` → se vuelven ambiguos en la lista.

### 4️⃣ Verifica que está registrado

Ahora revisa qué kernels conoce Jupyter:

```bash
jupyter kernelspec list
```

Verás algo como:

```text
Available kernels:
  py3135_roadmap_examples    /home/usuario/.local/share/jupyter/kernels/py3135_roadmap_examples
  python3                    /home/usuario/.pyenv/versions/3.13.5/share/jupyter/kernels/python3
```

### Borrar el kernel

```bash
jupyter kernelspec uninstall py3135_roadmap_examples
```

Luego confirma que quieres borrar el kernel especificado.

### 5️⃣ Úsalo en Jupyter Notebook / Lab

Cuando abras un notebook, podrás elegirlo desde el menú Select Kernel → "Python 3.13.5 (Roadmap Examples)".

✅ Beneficio: cada proyecto puede tener su propio kernel, con sus dependencias aisladas, y tú seleccionas cuál usar en cada Notebook sin mezclar librerías.
