# Variables en Python

## ¿Qué es una variable?

Una **variable** en Python es un **contenedor que almacena un valor** que puede cambiar durante la ejecución de un programa. Es una forma de **nombrar y guardar información** para poder usarla más adelante.

Por ejemplo:

```python
edad = 25
nombre = "Ana"
pi = 3.1416
```

En este ejemplo:

* `edad` es una variable que almacena un número entero.
* `nombre` es una variable que almacena una cadena de texto (string).
* `pi` es una variable que almacena un número decimal (float).

## Tipos de variables en Python

Python es un lenguaje **dinámicamente tipado**, lo que significa que no necesitas declarar explícitamente el tipo de una variable. Sin embargo, es importante conocer los principales tipos de datos:

### 1. Números enteros (`int`)

Almacenan números sin decimales.

```python
edad = 25
año = 2025
```

### 2. Números decimales (`float`)

Almacenan números con decimales.

```python
pi = 3.1416
precio = 49.99
```

### 3. Cadenas de texto (`str`)

Almacenan texto.

```python
nombre = "Ana"
mensaje = "Hola, mundo!"
```

### 4. Valores booleanos (`bool`)

Almacenan `True` o `False`, útil para condiciones.

```python
es_adulto = True
tiene_mascota = False
```

### 5. Listas (`list`)

Almacenan colecciones de elementos, que pueden ser de diferentes tipos.

```python
numeros = [1, 2, 3, 4, 5]
nombres = ["Ana", "Luis", "Pedro"]
```

### 6. Tuplas (`tuple`)

Similares a las listas, pero **inmutables** (no se pueden cambiar después de crear).

```python
coordenadas = (10.0, 20.0)
```

### 7. Conjuntos (`set`)

Almacenan colecciones de elementos **únicos** y no tienen un orden específico.

```python
frutas = {"manzana", "banana", "pera"}
```

### 8. Diccionarios (`dict`)

Almacenan pares de **clave: valor**.

```python
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Bogotá"
}
```

## Tipos dinámicos

En Python puedes cambiar el tipo de una variable asignándole un nuevo valor de otro tipo:

```python
x = 10      # int
x = "diez"  # str
```

Con esto tienes una base clara de **qué son las variables** y **los tipos de datos más comunes en Python**.
