# 📄 El archivo `requirements.txt` en Python

El archivo **`requirements.txt`** es un documento de texto muy utilizado en proyectos de Python para **gestionar las dependencias** (paquetes externos) que el proyecto necesita para ejecutarse correctamente. Es un estándar de facto en la comunidad y forma parte de las buenas prácticas de desarrollo.

## ✅ ¿Qué es y para qué sirve?

- Contiene la **lista de librerías y sus versiones** necesarias para el proyecto.  
- Permite que cualquier persona (o servidor) pueda **recrear el mismo entorno** de ejecución sin tener que instalar manualmente cada paquete.  
- Facilita la **portabilidad, reproducibilidad y colaboración** en proyectos Python.

Ejemplo de un `requirements.txt`:

```text
requests==2.31.0
numpy>=1.26.0
pandas~=2.2.0
```

## 📌 Casos de uso

1. **Compartir proyectos**: otros desarrolladores pueden instalar las dependencias con un solo comando.  
2. **Despliegue en producción**: servidores y contenedores (ej. Docker, Heroku) usan este archivo para configurar el entorno.  
3. **Control de versiones de librerías**: garantiza que todos trabajen con las mismas versiones y evita errores de compatibilidad.  
4. **Automatización**: herramientas de CI/CD leen `requirements.txt` para instalar dependencias en los pipelines.

## ⚙️ Cómo generar el archivo `requirements.txt`

Si ya tienes instalado todo en tu entorno virtual:

```bash
pip freeze > requirements.txt
```

Esto captura todas las dependencias actuales con sus versiones exactas.

## 🚀 Cómo utilizarlo

Para instalar las dependencias listadas:

```bash
pip install -r requirements.txt
```

Esto asegura que el entorno tenga todas las librerías necesarias.

## 📂 Uso con entornos virtuales

El `requirements.txt` se suele usar junto con entornos virtuales (`venv`, `virtualenv`, `pipenv`, `poetry`):

1. Crear y activar un entorno virtual:  

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .venv\Scripts\activate      # Windows
   ```

2. Instalar dependencias desde `requirements.txt`:  

   ```bash
   pip install -r requirements.txt
   ```

3. Exportar cambios (si instalas una nueva librería):  

   ```bash
   pip freeze > requirements.txt
   ```

Esto permite que cada proyecto tenga sus propias librerías sin interferir con otros.

## 📝 Recomendaciones y buenas prácticas

- **Versionar siempre**: incluir `requirements.txt` en el repositorio.  
- **Fijar versiones críticas**: usar `==` para librerías que puedan romper compatibilidad si se actualizan.  
- **Flexibilidad controlada**: usar `>=` o `~=` cuando quieras permitir ciertas actualizaciones menores.  
- **Mantener actualizado**: regenerar el archivo si se añaden o eliminan dependencias.  
- **No mezclar entornos**: genera `requirements.txt` desde el entorno virtual del proyecto, no desde el Python global.  
- **Usar un archivo base y otro de desarrollo**: por ejemplo:
  - `requirements.txt` → solo dependencias necesarias en producción.  
  - `requirements-dev.txt` → dependencias adicionales (testing, linters, etc.).  

## 🔎 Aspectos adicionales relevantes

- En proyectos grandes, puedes tener **múltiples archivos de requisitos** organizados:
  - `requirements.txt` (producción)
  - `requirements-dev.txt` (desarrollo)
  - `requirements-test.txt` (pruebas automatizadas)

- En **Docker**, es habitual copiar el archivo y usarlo para instalar dependencias en la imagen:  

  ```dockerfile
  COPY requirements.txt .
  RUN pip install -r requirements.txt
  ```

- Alternativas modernas: herramientas como **Pipenv** o **Poetry** reemplazan `requirements.txt` con archivos más avanzados (`Pipfile.lock`, `poetry.lock`), pero `requirements.txt` sigue siendo el estándar más compatible.

## 🛠️ Ejemplo práctico paso a paso

Imagina que quieres crear un proyecto llamado **mi_proyecto**.  

### 1. Crear carpeta y entorno virtual

```bash
mkdir mi_proyecto
cd mi_proyecto
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate    # Windows
```

### 2. Instalar librerías necesarias

```bash
pip install requests pandas
```

### 3. Exportar dependencias a `requirements.txt`

```bash
pip freeze > requirements.txt
```

Esto generará un archivo parecido a:

```text
pandas==2.2.0
python-dateutil==2.9.0.post0
pytz==2024.1
requests==2.31.0
six==1.16.0
urllib3==2.2.2
```

### 4. Compartir el proyecto

Cuando alguien más descargue tu código, podrá ejecutar:

```bash
pip install -r requirements.txt
```

y tendrá el mismo entorno configurado.

## 📌 Resumen

El archivo `requirements.txt` es la forma más sencilla y estandarizada de **compartir dependencias en proyectos Python**.  
Usado correctamente junto con entornos virtuales, garantiza que el proyecto sea reproducible, portable y mantenible en cualquier entorno.
