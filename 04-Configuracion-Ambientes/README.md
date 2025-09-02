# 🌍 Configuración de Ambientes en Python (Desarrollo, Pruebas y Producción)

Cuando trabajamos con **Python** en proyectos que usan **bases de datos, APIs o credenciales**, normalmente necesitamos **diferentes configuraciones** para cada ambiente:

- **Desarrollo (local)** → pruebas en tu máquina.  
- **Pruebas (testing/staging)** → simulación antes de salir a producción.  
- **Producción** → donde la aplicación está en uso real por los usuarios.  

El reto principal es **no subir información sensible (contraseñas, tokens, cadenas de conexión, etc.) al repositorio de GitHub**.

## 📌 1. Usar archivos de configuración y variables de entorno

La práctica recomendada es **guardar las credenciales en un archivo `.env`** (o en variables de entorno del sistema) y **no subir ese archivo a GitHub**.

Para manejar `.env` podemos usar la librería [**python-dotenv**](https://pypi.org/project/python-dotenv/).

## 📌 2. Usar entornos virtuales (`venv`)

Los entornos virtuales permiten **aislar las dependencias** de cada proyecto en Python. Así evitas conflictos entre versiones de librerías.

### Crear un entorno virtual

```bash
# Crear el entorno
python -m .venv venv
```

Esto genera una carpeta llamada .venv/ con todo lo necesario para ejecutar tu proyecto.

⚠️ Importante: La carpeta .venv/ nunca debe subirse a GitHub, así que debe estar en el .gitignore.

### Activar el entorno virtual

En Linux/Mac:

```bash
source .venv/bin/activate
```

En Windows (PowerShell):

```PowerShell
venv\Scripts\activate
```

Verás el prefijo (.venv) en tu terminal indicando que está activo.

### Instalación de `python-dotenv` en el entorno virtual

```bash
pip install python-dotenv
```

Puedes verificar los paquetes instalados con:

```bash
pip list
```

## 📌 3. Generar y usar `requirements.txt`

El archivo `requirements.txt` sirve para documentar y compartir las dependencias de tu proyecto.

Generar requirements.txt (Nota: El entorno local del proyecto todavía debe estar activo)

```bash
pip freeze > requirements.txt
```

Esto crea un archivo con todas las librerías y versiones instaladas en el proyecto.

Ejemplo de `requirements.txt`:

```text
python-dotenv==1.0.1
requests==2.31.0
```

Si alguien clona tu proyecto, puede instalar las dependencias desde `requirements.txt`

```bash
pip install -r requirements.txt
```

### Desactivar el entorno virtual

```bash
deactivate
```

Con esto, el entorno virtual está desactivado.

## 📌 4. Usar archivos de configuración y variables de entorno

La práctica recomendada es guardar las credenciales en un archivo .env (o en variables de entorno del sistema) y no subir ese archivo a GitHub.

Para manejar .env podemos usar la librería `python-dotenv`.

Ya instalada en el paso anterior con:

```bash
pip install python-dotenv
```

## 📌 5. Crear archivos `.env` por cada ambiente

Ejemplo de estructura del proyecto:

```text
mi_proyecto/
│── app.py
│── .env.development
│── .env.testing
│── .env.production
│── .env.example
│── .gitignore
```

### Ejemplo de `.env.development`

```env
# Variables de ambiente para DESARROLLO
DB_HOST=localhost
DB_USER=admin
DB_PASSWORD=12345
DB_NAME=mi_base_dev
DEBUG=True
```

⚠️ Muy importante: Esto archivo NO se debe subir a GitHub.

### Ejemplo de `.env.testing`

```env
# Variables de ambiente para PRUEBAS
DB_HOST=test-db.example.com
DB_USER=test_user
DB_PASSWORD=test123
DB_NAME=mi_base_test
DEBUG=True
```

⚠️ Muy importante: Esto archivo NO se debe subir a GitHub.

### Ejemplo de `.env.production`

```env
# Variables de ambiente para PRODUCCIÓN
DB_HOST=prod-db.example.com
DB_USER=prod_user
DB_PASSWORD=superSecreta123
DB_NAME=mi_base_prod
DEBUG=False

```

⚠️ Muy importante: Esto archivo NO se debe subir a GitHub.

En su lugar, sube un **archivo de ejemplo**:

### `.env.example`

```env
# Copia este archivo como .env.development, .env.testing o .env.production
# y completa con tus datos reales.

DB_HOST=your_host
DB_USER=your_user
DB_PASSWORD=your_password
DB_NAME=your_db
```

⚠️ Muy importante: Esto archivo Sí se puede/debe subir a GitHub, sin datos reales. Esto servirá como plantilla.

## 📌 6. Configurar `.gitignore`

En tu archivo `.gitignore` debes agregar:

```gitignore
# ------------------------------
# Ignorar archivos .env
# ------------------------------
.env*
!*.example

# ------------------------------
# Entornos virtuales
# ------------------------------
# Ignora venv local
**/venv/
**/ENV/
**/env/
**/.venv/
**/.env/
```

👉 Esto significa:

- Ignorar cualquier archivo `.env...`  
- **Pero NO ignorar** el archivo `.env.example` (ya que sirve de guía).  

## 📌 7. Código en Python para leer las variables

Archivo `app.py`:

```python
import os
from dotenv import load_dotenv

# Seleccionar el ambiente (puede venir de una variable del sistema)
AMBIENTE = os.getenv("APP_ENV", "development")

# Cargar el archivo correspondiente
if AMBIENTE == "development":
    load_dotenv(".env.development")
elif AMBIENTE == "testing":
    load_dotenv(".env.testing")
elif AMBIENTE == "production":
    load_dotenv(".env.production")

# Leer variables
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DEBUG = os.getenv("DEBUG")

print(f"Conectando a {DB_NAME} en {DB_HOST} con usuario {DB_USER}")
```

👉 Explicación:

- `APP_ENV` define el ambiente actual (`development`, `testing`, `production`).  
- Según el valor, carga un archivo `.env` diferente.  
- Nunca ponemos las credenciales en el código directamente.  

## 📌 8. Cómo definir el ambiente actual

Puedes definir el ambiente desde la terminal antes de ejecutar tu aplicación:

```bash
# En Linux/Mac
export APP_ENV=testing

# En Windows (PowerShell)
setx APP_ENV testing
```

Y luego ejecutas:

```bash
python app.py
```

## 🚀 9. En la práctica

Cuando inicies tu app, la configuración dependerá automáticamente del ambiente:

### En desarrollo

```bash
export APP_ENV=development
python app.py   # Usará .env.development
```

### En pruebas

```bash
export APP_ENV=test
python app.py   # Usará .env.test
```

### En producción

```bash
export APP_ENV=production
python app.py   # Usará .env.production
```

De esta forma:

- No necesitas cambiar el código para cada ambiente.
- Todo depende de la configuración en variables de entorno y los .env.

## 📌 10. Buenas prácticas

- Nunca subas credenciales reales a GitHub.  
- Usa `.env.example` como referencia para tu equipo.  
- Usa **un gestor de secretos** en producción (ej. AWS Secrets Manager, Azure Key Vault).  
- Controla los accesos a tus bases de datos con permisos mínimos necesarios.  
- Configura tu `.gitignore` correctamente desde el inicio del proyecto.  
- Documenta siempre tus dependencias en requirements.txt.

## 🚀 11. Conclusión

- Cada ambiente (desarrollo, pruebas, producción) debe tener su propio archivo `.env`.  
- Usa `.gitignore` para proteger tus credenciales.  
- Comparte solo `.env.example` como guía.  
- Usa `python-dotenv` para cargar variables según el ambiente.  
- Maneja dependencias con venv y requirements.txt.

De esta forma tu proyecto será **seguro, ordenado y profesional**.  
