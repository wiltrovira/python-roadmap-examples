# Preguntas frecuentes

## 🔧 ¿Qué significa “agregar pyenv al Bash”?

Cuando instalas pyenv, debes modificar tu archivo de configuración del shell (.bashrc, .zshrc, etc.) para que:

El sistema sepa dónde está instalado pyenv (export PATH=...).

Se carguen las funciones necesarias para que los comandos de pyenv funcionen (eval "$(pyenv init ...)").

## 🔍 ¿Por qué es importante hacer esto?

1. 🧭 Para que el comando pyenv funcione en tu terminal

    Si no agregas pyenv al PATH, la terminal no sabrá dónde encontrarlo y te dará un error como:

    ```text
    pyenv: command not found
    ```

2. 🔁 Para que cambie automáticamente la versión de Python al entrar a un proyecto

    Esto lo hace el comando:

    ```bash
    eval "$(pyenv init --path)"
    ```

    Gracias a esto, cuando entras a un directorio con .python-version, `pyenv` cambia automáticamente la versión de Python. Sin eso, siempre usarás la predeterminada del sistema.

3. 🧰 Para que funcionen los “shims” (atajos inteligentes)

    pyenv redirige comandos como python, pip, python3, etc., hacia la versión que hayas seleccionado con:

    pyenv global <versión>
    pyenv local <versión>

    Esto solo funciona si los "shims" de pyenv están al inicio del PATH (por eso usamos export PATH="$HOME/.pyenv/bin:$PATH").

## 🧠 ¿Qué es el comando eval en Bash?

`eval` es un comando de Bash que ejecuta el resultado de una cadena de texto como si fuera un comando.

🔍 Ejemplo sencillo:

```bash
mensaje="echo Hola mundo"
eval $mensaje  # Resultado: Hola mundo
```

🔁 Lo que hace es evaluar la cadena como si tú la hubieras escrito directamente en la terminal.

## 🛠 ¿Y por qué se usa eval con pyenv?

Cuando haces:

```bash
eval "$(pyenv init -)"
```

Estás haciendo lo siguiente:

- Ejecutas pyenv init -, que imprime un bloque de código shell.
- Ese código incluye funciones y configuraciones para que pyenv funcione.
- eval ejecuta ese código dinámicamente dentro de tu sesión del shell.

⚠️ Sin eval, ese código solo se imprimiría en pantalla, no se ejecutaría, y pyenv no funcionaría como debe.

## 🔍 ¿Qué es el comando source?

`source` es un comando de terminal que ejecuta un archivo de comandos (como un script) en el entorno actual del shell.

Cuando usas source, cualquier variable, función o cambio de entorno que se hace dentro del archivo afecta directamente tu sesión de terminal actual, sin abrir una nueva.

🧪 Ejemplo básico:

- Creamos un archivo

```bash
echo 'export SALUDO="Hola mundo"' > mi_script.sh
```

Si ejecutas este script con bash `mi_script.sh`, no se guarda la variable en tu sesión.

Pero si haces:

```bash
source mi_script.sh
echo $SALUDO  # Resultado: Hola mundo
```

✅ Ahora la variable quedó disponible en tu terminal.

## ✅ ¿Para qué se usa source con entornos virtuales?

Cuando activas un entorno virtual de Python, haces:

```bash
source .venv/bin/activate
```

- Lo que estás haciendo es ejecutar el script activate dentro del entorno actual del shell, lo que:
- Cambia la variable $PATH para que el sistema use los binarios del entorno (.venv/bin/python, .venv/bin/pip).
- Cambia el prompt de tu terminal para que veas algo como (.venv).
- Aísla el entorno para instalar paquetes sin tocar el resto del sistema.

⚠️ Si hicieras esto con bash `.venv/bin/activate`, se ejecutaría en un nuevo shell, y los cambios no afectarían tu terminal actual, así que no funcionaría correctamente.

## 🔄 Equivalente corto en Bash

También puedes usar el punto . como forma abreviada de source:

```bash
. .venv/bin/activate
```
