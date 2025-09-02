# 📘 Módulos y Paquetes en Python

Este documento explica de manera sencilla qué son los **módulos** y los **paquetes** en Python, cómo se importan y cómo funcionan.  


## 🔹 1. ¿Qué es un módulo?

Un **módulo** en Python es simplemente un **archivo con extensión `.py`** que contiene código (funciones, clases o variables) que puedes reutilizar en otros programas.

📌 **Ejemplo:**
Archivo `matematicas.py`:

```python
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b
```

Uso en otro archivo:

```python
import matematicas

print(matematicas.sumar(5, 3))   # 8
```

👉 `matematicas` es un **módulo**.

## 🔹 2. ¿Qué es un paquete?

Un **paquete** es una **carpeta** que contiene varios módulos relacionados.  
Para que Python lo reconozca como paquete, la carpeta debe incluir un archivo especial llamado `__init__.py` (puede estar vacío).

📌 **Ejemplo de estructura de un paquete:**

```
mi_proyecto/
│
├── operaciones/              ← Paquete
│   ├── __init__.py
│   ├── suma.py               ← Módulo
│   └── resta.py              ← Módulo
│
└── app.py
```

Contenido de `suma.py`:

```python
def sumar(a, b):
    return a + b
```

Contenido de `resta.py`:

```python
def restar(a, b):
    return a - b
```

Uso en `app.py`:

```python
from operaciones import suma, resta

print(suma.sumar(4, 2))   # 6
print(resta.restar(10, 3)) # 7
```

## 🔹 3. Diferencia entre módulo y paquete

| **Módulo** | **Paquete** |
|------------|-------------|
| Es un **solo archivo** `.py`. | Es una **carpeta** que agrupa módulos. |
| Contiene funciones, clases y variables. | Contiene **módulos y subpaquetes**. |
| Ejemplo: `math` (módulo estándar de Python). | Ejemplo: `numpy` (paquete con muchos submódulos). |

## 🔹 4. Formas de importar módulos

### 1. Importar todo el módulo

```python
import matematicas

print(matematicas.sumar(3, 2))
```

### 2. Importar solo lo necesario

```python
from matematicas import sumar

print(sumar(3, 2))
```

### 3. Usar alias

```python
import matematicas as m

print(m.sumar(3, 2))
```

### 4. Importar varias funciones

```python
from matematicas import sumar, restar
```

### 5. Importar todo con `*` (⚠️ poco recomendado)

```python
from matematicas import *
print(sumar(1, 2))
```

⚠️ Puede causar **conflictos de nombres** si hay funciones repetidas.

---

## 🔹 5. ¿Dónde busca Python los módulos?

Cuando haces un `import`, Python busca en este orden:

1. El **directorio actual** (donde estás ejecutando el script).  
2. La **biblioteca estándar de Python**.  
3. Los directorios listados en `sys.path` (incluye los instalados con `pip`).  

📌 Ver rutas:

```python
import sys
print(sys.path)
```

## 🔹 6. Ejemplo real de paquete estándar

Cuando escribimos:

```python
import xml.etree.ElementTree as ET
```

Esto significa:

- **`xml`** → Paquete de la librería estándar.  
- **`etree`** → Subpaquete dentro de `xml`.  
- **`ElementTree`** → Módulo dentro de `etree`.  
- **`as ET`** → Alias (nombre corto para usar el módulo).  

### Ejemplo práctico:

Archivo XML (`ejemplo.xml`):

```xml
<raiz>
    <saludo>Hola Mundo</saludo>
</raiz>
```

Python:

```python
import xml.etree.ElementTree as ET

tree = ET.parse("ejemplo.xml")
root = tree.getroot()

print(root.tag)       # raiz
print(root[0].tag)    # saludo
print(root[0].text)   # Hola Mundo
```

## 🔹 7. Recomendaciones al importar

✅ Usa `import nombre_modulo` cuando quieras claridad.  
✅ Usa `from modulo import funcion` solo para lo necesario.  
⚠️ Evita `from modulo import *` salvo en casos de pruebas rápidas.  


## 📌 Resumen final

- Un **módulo** es un archivo `.py`.  
- Un **paquete** es una carpeta con módulos + `__init__.py`.  
- Puedes importar módulos de distintas formas (`import`, `from ... import ...`, alias, etc.).  
- Python organiza la librería estándar en **paquetes con submódulos**, como `xml.etree.ElementTree`.  

👉 Con estos conceptos puedes estructurar proyectos más grandes y ordenados en Python.
