# Archivo: main.py
# Descripción: Script principal para un proyecto de Python usando Poetry
# Autor: Wilt Rovira
# Fecha: 2025-09-08
# Versión: 1.0.0
# Licencia: MIT
def suma(a: int, b: int) -> int:
    """
    Suma dos números enteros.
    Argumentos:
        a (int): Primer número a sumar.
        b (int): Segundo número a sumar.
    Retorna:
        int: La suma de a y b.
    """
    return a + b


# Función principal
def main():
    """
    Función principal del script.
    Argumentos:
        Ninguno.
    Retorna:
        Ninguno.
    """
    # Comentario de ejemplo para probar flake8 y black
    # Esta línea está intencionadamente larga para verificar que las
    # herramientas de linting
    # y formateo de código funcionan correctamente en este proyecto.
    # Puedes descomentar las siguientes líneas para probar:
    # mensaje1 = "Este es un ejemplo de una línea de código que claramente
    # excede el límite de 88 caracteres para probar flake8 y black"

    numeros = [1, 2, 3, 4, 5]
    total = 0
    for n in numeros:
        total += n
    resultado = suma(total, 10)
    print("El resultado es:", resultado)


# Punto de entrada del script
if __name__ == "__main__":
    """Ejecuta la función principal si el script es ejecutado directamente."""
    main()


# Este es un ejemplo simple de un proyecto en Python usando Poetry
# que define una función de suma y la utiliza en el bloque principal.
# Puedes ejecutar este script directamente para ver el resultado.
# Asegúrate de tener Poetry instalado y de haber creado un entorno virtual
# para gestionar las dependencias si decides agregar alguna en el futuro.
