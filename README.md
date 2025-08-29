# 🐍 Python Roadmap by Examples (Aprendizaje en Python Progresivo por Ejemplos)

Este roadmap describe el camino de estudio que sigo para aprender Python
desde cero hasta avanzado, organizado en **módulos progresivos** con ejemplos,
ejercicios y proyectos.

---

## 0️⃣ Introducción
- Instalar Python en Windows/Linux/Mac
- Usar un editor o IDE (VS Code, PyCharm, Jupyter Notebook)
- Escribir el primer programa: `print("Hello World")`
- Ejecutar scripts desde la terminal

📚 Recursos:
- [Python.org - Getting Started](https://www.python.org/about/gettingstarted/)

---

## 1️⃣ Sintaxis Básica
- Variables y tipos de datos
- Operadores aritméticos y lógicos
- Condicionales (`if/else`)
- Bucles (`for`, `while`)

🎯 Objetivo: Comprender la estructura básica de un programa en Python.  

📚 Recursos:
- [W3Schools Python Basics](https://www.w3schools.com/python/)

---

## 2️⃣ Estructuras de Datos
- Listas
- Tuplas
- Diccionarios
- Conjuntos (sets)
- Comprensiones de listas

🎯 Objetivo: Aprender a organizar y manipular colecciones de datos.  

📚 Recursos:
- [Python Docs - Data Structures](https://docs.python.org/3/tutorial/datastructures.html)

---

## 3️⃣ Funciones
- Definir funciones (`def`)
- Parámetros y argumentos
- Funciones anónimas (`lambda`)
- Alcance de variables (scope)

🎯 Objetivo: Modularizar el código y reutilizar lógica.  

📚 Recursos:
- [Real Python - Functions](https://realpython.com/defining-your-own-python-function/)

---

## 4️⃣ Programación Orientada a Objetos (POO)
- Clases y objetos
- Atributos y métodos
- Herencia
- Polimorfismo y encapsulación

🎯 Objetivo: Aprender el paradigma orientado a objetos con Python.  

📚 Recursos:
- [Python OOP Tutorial](https://www.programiz.com/python-programming/object-oriented-programming)

---

## 5️⃣ Manejo de Archivos
- Lectura y escritura de archivos (`open`, `with`)
- Archivos JSON
- Archivos CSV

🎯 Objetivo: Guardar y leer datos desde archivos externos.  

---

## 6️⃣ Manejo de Excepciones
- `try`, `except`, `finally`
- Excepciones personalizadas

🎯 Objetivo: Escribir código robusto que maneje errores.  

---

## 7️⃣ Módulos y Paquetes
- Importar módulos estándar
- Crear tus propios módulos
- Instalar librerías externas con `pip`

🎯 Objetivo: Aprender a organizar proyectos y usar librerías externas.  

---

## 8️⃣ Librerías Estándar Útiles
- `os` (sistema de archivos)
- `sys` (argumentos de línea de comandos)
- `datetime`
- `math` y `random`

🎯 Objetivo: Dominar las utilidades más usadas de la librería estándar.  

---

## 9️⃣ Proyectos Pequeños
- Calculadora
- Juego de piedra, papel o tijera
- Generador de contraseñas
- Gestor de tareas simple

🎯 Objetivo: Aplicar lo aprendido en proyectos prácticos.  

---

## 🔟 Python Avanzado
- Decoradores
- Generadores
- Iteradores
- Context Managers (`with`)
- Tipado (type hints, `typing`)

🎯 Objetivo: Escribir código Python más eficiente y profesional.  

---

## 1️⃣1️⃣ Testing
- `unittest` (básico)
- `pytest` (más avanzado)

🎯 Objetivo: Aprender buenas prácticas y garantizar calidad de código.  

---

## 1️⃣2️⃣ Proyectos Medianos
- Agenda de contactos en CLI
- API client usando `requests`
- Web Scraper con `BeautifulSoup`

🎯 Objetivo: Consolidar habilidades construyendo aplicaciones reales.  

---

# 📚 Recursos Adicionales
- [Documentación oficial de Python](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)

---

# ✅ Recomendación
Este roadmap no es lineal rígido: puedes saltar entre módulos según tus necesidades.
Lo importante es **practicar constantemente con proyectos** y documentar tu progreso en este repositorio.

# ✅ Estructura de carpetas
Python-Roadmap-Examples/
│
├── 00-Introduccion/
│   ├── notas.md                 # Qué es Python, instalación, IDEs
│   ├── hello_world.py
│   ├── primer_programa.py
│   └── ejercicios/
│
├── 01-Sintaxis-Basica/
│   ├── variables.py
│   ├── tipos_datos.py
│   ├── operadores.py
│   ├── condicionales.py
│   ├── bucles.py
│   ├── ejercicios.md
│   └── README.md
│
├── 02-Estructuras-Datos/
│   ├── listas.py
│   ├── tuplas.py
│   ├── diccionarios.py
│   ├── sets.py
│   ├── comprensiones_listas.py
│   ├── ejercicios.md
│   └── README.md
│
├── 03-Funciones/
│   ├── funciones_basicas.py
│   ├── argumentos.py
│   ├── funciones_lambda.py
│   ├── alcance_variables.py
│   ├── ejercicios.md
│   └── README.md
│
├── 04-POO/
│   ├── clases_objetos.py
│   ├── metodos.py
│   ├── herencia.py
│   ├── polimorfismo.py
│   ├── encapsulamiento.py
│   ├── ejercicios.md
│   └── README.md
│
├── 05-Manejo-Archivos/
│   ├── abrir_escribir.py
│   ├── leer_json.py
│   ├── leer_csv.py
│   ├── ejercicios.md
│   └── README.md
│
├── 06-Excepciones/
│   ├── try_except.py
│   ├── finally.py
│   ├── excepciones_personalizadas.py
│   ├── ejercicios.md
│   └── README.md
│
├── 07-Modulos-Paquetes/
│   ├── importar_modulos.py
│   ├── crear_paquete/
│   │   ├── __init__.py
│   │   └── operaciones.py
│   ├── uso_librerias_externas.py
│   └── README.md
│
├── 08-Librerias-Standard/
│   ├── datetime_ejemplos.py
│   ├── os_path.py
│   ├── sys_argv.py
│   ├── math_random.py
│   └── README.md
│
├── 09-Proyectos-Pequenos/
│   ├── calculadora.py
│   ├── piedra_papel_tijera.py
│   ├── generador_contrasenas.py
│   ├── gestor_tareas.py
│   └── README.md
│
├── 10-Avanzado/
│   ├── decoradores.py
│   ├── generadores.py
│   ├── context_managers.py
│   ├── iteradores.py
│   ├── anotaciones_tipos.py
│   ├── ejercicios.md
│   └── README.md
│
├── 11-Testing/
│   ├── intro_unittest.py
│   ├── pytest_basico.py
│   ├── test_ejercicios.py
│   └── README.md
│
├── 12-Proyectos-Medianos/
│   ├── cli_agenda_contactos/
│   ├── api_consumo_requests/
│   ├── web_scraper_bs4/
│   └── README.md
│
├── docs/             # Documentación adicional
│   ├── roadmap.md    # Plan de estudio
│   ├── recursos.md   # Libros, cursos, webs útiles
│   ├── cheatsheet.md # Apuntes rápidos
│   └── README.md
│
├── .gitignore
├── LICENSE
└── README.md
