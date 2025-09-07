# Archivo: main.py
# Descripción: Script principal para un proyecto de Python usando Poetry
def suma(a, b):
    return a + b


# Función principal
def main():
    # a = 9
    # mensaje1 = "Este es un ejemplo de una línea de código que claramente excede el límite de 88 caracteres para probar flake8 y black"

    numeros = [1, 2, 3, 4, 5]
    total = 0
    for n in numeros:
        total += n
    resultado = suma(total, 10)
    print("El resultado es:", resultado)


# Punto de entrada del script
if __name__ == "__main__":
    main()


# Este es un ejemplo simple de un proyecto en Python usando Poetry
# que define una función de suma y la utiliza en el bloque principal.
# Puedes ejecutar este script directamente para ver el resultado.
# Asegúrate de tener Poetry instalado y de haber creado un entorno virtual
# para gestionar las dependencias si decides agregar alguna en el futuro.
