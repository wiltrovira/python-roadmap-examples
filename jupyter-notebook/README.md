# 📒 Introducción a Jupyter Notebook y JupyterLab

Esta carpeta contiene ejemplos y notas sobre el uso de **Jupyter Notebook** y **JupyterLab**, dos entornos interactivos muy populares en el ecosistema de Python.

---

## 📌 ¿Qué es Jupyter Notebook?

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

## 📌 ¿Qué es JupyterLab?

Es la evolución de Jupyter Notebook: un entorno más avanzado y flexible.

Permite trabajar con:

- Múltiples notebooks al mismo tiempo.
- Archivos de Python (.py), Markdown (.md), CSV (.csv), entre otros.
- Consolas, terminales y gráficos en una sola interfaz.
- Ideal para proyectos más grandes o cuando necesitas mayor organización.

## Diferencia principal

| Jupyter Notebook                                | JupyterLab                                                |
| ----------------------------------------------- | --------------------------------------------------------- |
| Interfaz clásica y simple.                      | Interfaz moderna tipo IDE (múltiples pestañas y paneles). |
| Fácil de usar para principiantes.               | Más flexible y poderosa para proyectos complejos.         |
| Perfecto para aprender y hacer pruebas rápidas. | Perfecto para análisis de datos, ML y colaboración.       |

## 🚀 Instalación básica en un entorno virtual (recomendado)

### Crear entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### Instalar Jupyter Notebook y JupyterLab

```bash
pip install notebook jupyterlab
```

## Iniciar Notebook

jupyter notebook

## Iniciar JupyterLab

jupyter lab

✍️ Nota: Los notebooks aquí incluidos pueden abrirse tanto en la interfaz clásica de Jupyter Notebook como en JupyterLab o directamente desde Visual Studio Code con la extensión de Jupyter.
