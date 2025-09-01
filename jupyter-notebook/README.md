# 📓 Jupyter Notebooks de Aprendizaje en Python

Este directorio contiene los **notebooks de Jupyter** que utilizo para documentar el proceso de aprendizaje en Python.  
Aquí encontrarás ejercicios, ejemplos prácticos y experimentos que ayudarán a comprender mejor la sintaxis y conceptos del lenguaje.

## 🎯 Objetivo

- Practicar Python desde cero utilizando un entorno interactivo.
- Documentar ejercicios y ejemplos de estudio.
- Tener un registro organizado y versionado de mi progreso.
- Usar los notebooks como referencia rápida en el futuro.

## 🛠️ Tecnologías usadas

- **Python** 🐍
- **Jupyter Notebook** y **JupyterLab** ✨
- Entorno virtual gestionado con **venv/pyenv**
- Control de versiones con **Git + GitHub**

## 📂 Estructura

Cada notebook está orientado a un tema o bloque de ejercicios:

```text
notebooks/
├── 01_basicos.ipynb
├── 02_control_flujo.ipynb
├── 03_funciones.ipynb
```

## 📒 Introducción a Jupyter Notebook y JupyterLab

Esta carpeta contiene ejemplos y notas sobre el uso de **Jupyter Notebook** y **JupyterLab**, dos entornos interactivos muy populares en el ecosistema de Python.

### 📌 ¿Qué es Jupyter Notebook?

- Es una herramienta que permite combinar **código Python**, **texto en Markdown**, **imágenes**, **ecuaciones matemáticas** y **resultados interactivos** en un mismo documento.
- Los archivos tienen extensión `.ipynb` (*IPython Notebook*).
- Es muy usado en:
  - Aprendizaje y práctica de Python.
  - Análisis y visualización de datos.
  - Documentación de experimentos.
  - Prototipado rápido de código.

Ejemplo de celda en un Notebook:

```python
print("Hola, mundo 👋")
```

### 📌 ¿Qué es JupyterLab?

Es la evolución de Jupyter Notebook: un entorno más avanzado y flexible.

Permite trabajar con:

- Múltiples notebooks al mismo tiempo.
- Archivos de Python (.py), Markdown (.md), CSV (.csv), entre otros.
- Consolas, terminales y gráficos en una sola interfaz.
- Ideal para proyectos más grandes o cuando necesitas mayor organización.

### Diferencias entre Jupyter Notebook y JupterLab

| Jupyter Notebook                                | JupyterLab                                                |
| ----------------------------------------------- | --------------------------------------------------------- |
| Interfaz clásica y simple.                      | Interfaz moderna tipo IDE (múltiples pestañas y paneles). |
| Fácil de usar para principiantes.               | Más flexible y poderosa para proyectos complejos.         |
| Perfecto para aprender y hacer pruebas rápidas. | Perfecto para análisis de datos, ML y colaboración.       |

## 🚀 Instalación básica en un entorno virtual (recomendado)

Para mayor información: [Instalación de pyenv en Pop!_OS / Ubuntu 22.04](../01-pyenv/01-pyenv-commands.md)

### Crear entorno virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Instalar Jupyter Notebook y JupyterLab

```bash
pip install notebook jupyterlab
```

### Iniciar Notebook

jupyter notebook

### Iniciar JupyterLab

jupyter lab

✍️ Nota: Los notebooks aquí incluidos pueden abrirse tanto en la interfaz clásica de Jupyter Notebook como en JupyterLab o directamente desde Visual Studio Code con la extensión de Jupyter.

## ⚙️ El Kernel en Jupyter

### 🔎 Definición

El kernel es el motor de ejecución que corre detrás de Jupyter Notebook o JupyterLab.

Es el proceso que:

- Recibe el código que escribes en una celda.
- Lo ejecuta en el lenguaje correspondiente (ej. Python).
- Devuelve el resultado al notebook para que lo veas.

👉 Piensa en Jupyter Notebook como el cuaderno (interfaz), y el kernel como el “cerebro” que realmente entiende y ejecuta el código.

En otras palabras:

- Un kernel es un proceso en segundo plano que corre tu código.
- Cada notebook se conecta a un kernel específico.
- Ese kernel es realmente un intérprete de Python (u otro lenguaje) + todas las librerías que tenga disponibles.

👉 Si piensas en un notebook como un cuaderno, el kernel es el profesor que te responde las preguntas: cada cuaderno puede elegir qué profesor lo atiende (qué kernel usar).

### 📌 Características principales

- Cada notebook se conecta a un kernel.
- Un kernel solo ejecuta un lenguaje a la vez.
  - Normalmente es Python, pero también hay kernels de R, Julia, JavaScript, etc.
- Puedes tener varios kernels instalados (por ejemplo, uno por cada entorno virtual).
- Si cierras o matas el kernel, el notebook ya no puede ejecutar código.

### 🧩 Relación entre kernel y entorno

Un entorno virtual (venv, conda, pyenv, etc.) define:

- Una versión específica de Python.
- Un conjunto de librerías instaladas.

Cuando registras un entorno como kernel, lo que le dices a Jupyter es:
> “Este notebook no debe usar el Python global ni sus librerías, sino el Python y los paquetes de este entorno virtual”.

De esa forma:

- El notebook siempre corre con la versión correcta de Python.
- Usa solo las librerías que instalaste en ese entorno.
- Evitas conflictos entre proyectos.

### ✅ Beneficio de registrar un kernel desde el ambiente

1. Aislamiento de proyectos

    - Proyecto A (Python 3.10, numpy==1.24)
    - Proyecto B (Python 3.12, numpy==2.0)

      Si no registras kernels separados, Jupyter no sabrá qué librerías/versiones usar.

2. Reproducibilidad

    Si alguien más abre tu notebook y selecciona el kernel correcto (Python (mi_proyecto)), podrá instalar el mismo entorno (requirements.txt) y ejecutar el notebook sin errores.

3. Compatibilidad con VS Code y JupyterLab

    Podrás elegir el kernel correcto desde el menú desplegable. Sin esto, VS Code podría usar el Python global, y dar errores tipo:

    > ModuleNotFoundError: No module named 'pandas'

### 📚 Ejemplo práctico

Cuando ejecutas en Jupyter:

```python
x = 5
x + 2
```

- El notebook envía estas instrucciones al kernel de Python.
- El kernel procesa la operación → 7.
- Devuelve el resultado → se muestra justo debajo de la celda.

### 🧠 Kernels y entornos virtuales

Cuando trabajas con entornos virtuales (venv, conda, pyenv, etc.), cada entorno puede tener su propio kernel.

Esto permite:

- Un proyecto con Python 3.10 y librerías específicas.
- Otro proyecto con Python 3.12 y otras librerías.
- En Jupyter, al abrir un notebook, puedes elegir el kernel en el menú:
  - 👉 Kernel > Change kernel

### ⚠️ Importante

Si ejecutas una celda que depende de una librería no instalada en el kernel actual, dará error (ModuleNotFoundError).

Por eso, es recomendable instalar Jupyter dentro del entorno virtual del proyecto, o registrar ese entorno como un kernel disponible en Jupyter.

### ✅ En resumen

El kernel de Jupyter es el proceso que ejecuta el código en un notebook.

- El kernel = el proceso que ejecuta el código del notebook.
- El entorno = el conjunto de Python + librerías.
- Registrar un entorno como kernel = decirle a Jupyter “usa este Python y estas librerías para ejecutar este notebook”.
- Sin kernel, tu notebook es solo texto.
- Cada kernel puede ser de un lenguaje diferente o de un entorno virtual diferente.
- La buena práctica es: un entorno virtual = un kernel, así cada proyecto mantiene sus dependencias separadas.

### 🔎 ¿Qué pasa si no registraste ningún kernel?

Cuando instalas Jupyter Notebook o JupyterLab con pip install notebook jupyterlab, ese paquete necesita un kernel por defecto para poder ejecutar el código.

Lo que ocurre es:

- Jupyter instala ipykernel automáticamente en el mismo lugar donde fue instalado.
- Ese ipykernel registra un kernel base que apunta al intérprete de Python con el que instalaste Jupyter.
- Ese kernel aparece como Python 3 (o similar) en la lista de kernels de Jupyter.

🚩 Lo importante

- Aunque no hayas registrado un kernel propio, sí tienes un kernel: el que se creó junto con la instalación de Jupyter.
- Ese kernel está ligado al Python desde donde corriste pip install notebook.
- Si luego cambias de proyecto y no registras un kernel de ese proyecto, todos los notebooks seguirán corriendo con el mismo Python global, lo que rompe el aislamiento entre proyectos.

✅ Por eso conviene registrar kernels

De lo contrario, pasa lo típico:

- Proyecto A necesita pandas==1.3.
- Proyecto B necesita pandas==2.0.
- Si ambos dependen del mismo kernel (Python global), tendrás conflictos.

Con kernels separados (Python (A), Python (B)), cada notebook sabe exactamente qué motor de Python debe usar.

### 🔎 Desde dentro de un Notebook

Abre una celda nueva en tu .ipynb y ejecuta:

```python
import sys
print(sys.executable)
print(sys.version)
```

- `sys.executable` → te dice la ruta exacta del intérprete de Python que usa el kernel.
- `sys.version` → te muestra la versión de Python.

Ejemplo de salida:

```text
/home/usuario/.pyenv/versions/3.13.5/bin/python3
3.13.5 (main, Aug  7 2025, 13:14:15) [GCC 11.4.0]
```

✅ Con este comando sabrás qué kernel está usando tu notebook actual.

### 🔎 Desde la terminal

Para ver qué kernels reconoce Jupyter:

```bash
jupyter kernelspec list
```

Esto devuelve algo así:

```text
Available kernels:
  py3135_roadmap_examples    /home/usuario/.local/share/jupyter/kernels/py3135_roadmap_examples
  python3                    /home/usuario/.pyenv/versions/3.13.5/share/jupyter/kernels/python3
```

Ese python3 apunta al kernel por defecto (el Python donde instalaste Jupyter).

✅ Con este comando sabrás qué otros kernels tienes disponibles.

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

### 5️⃣ Úsalo en Jupyter Notebook / Lab

Cuando abras un notebook, podrás elegirlo desde el menú Select Kernel → "Python 3.13.5 (Roadmap Examples)".

✅ Beneficio: cada proyecto puede tener su propio kernel, con sus dependencias aisladas, y tú seleccionas cuál usar en cada Notebook sin mezclar librerías.
