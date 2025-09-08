# Introducción a las Cadenas en Python

En Python, una **cadena de caracteres** (*string*) es una secuencia de texto delimitada por comillas simples (`'`), dobles (`"`), o triples (`'''` o `"""`).  
Son uno de los tipos de datos más usados en programación, ya que permiten representar y manipular texto.

## Creación de Cadenas

```python
# Comillas simples
cadena1 = 'Hola'

# Comillas dobles
cadena2 = "Mundo"

# Comillas triples (permite saltos de línea)
cadena3 = """Este es un
texto en varias
líneas"""
```

---

## Operaciones Básicas

### Concatenación

Unir cadenas utilizando el operador `+`:

```python
nombre = "Ana"
saludo = "Hola " + nombre
print(saludo)  # Hola Ana
```

### Repetición

Multiplicar cadenas con el operador `*`:

```python
eco = "Hey! " * 3
print(eco)  # Hey! Hey! Hey!
```

### Indexación y Slicing

Acceder a caracteres individuales o fragmentos de una cadena:

```python
texto = "Python"
print(texto[0])    # P (primer carácter)
print(texto[-1])   # n (último carácter)
print(texto[0:4])  # Pyth (subcadena)
```

## Métodos Útiles

Las cadenas en Python incluyen múltiples métodos para manipular texto:

```python
mensaje = "  hola mundo  "

print(mensaje.upper())     # "  HOLA MUNDO  "
print(mensaje.lower())     # "  hola mundo  "
print(mensaje.strip())     # "hola mundo"
print(mensaje.replace("mundo", "Python"))  # "  hola Python  "
print(mensaje.split())     # ["hola", "mundo"]
```

## f-Strings y Formato

Las **f-strings** (desde Python 3.6) son la forma recomendada de formatear cadenas:

```python
nombre = "Carlos"
edad = 30

print(f"Me llamo {nombre} y tengo {edad} años.")
# Me llamo Carlos y tengo 30 años.
```

## Inmutabilidad de las Cadenas

En Python, las cadenas son **inmutables**: no pueden modificarse directamente.  
Si quieres cambiar una cadena, debes crear una nueva:

```python
texto = "Hola"
# texto[0] = "M"  ❌ Error: las cadenas no son modificables

nuevo_texto = "M" + texto[1:]
print(nuevo_texto)  # "Mola"
```

## Buenas Prácticas y Recomendaciones

1. ✅ **Usa comillas simples o dobles de forma consistente**.  
   Ejemplo: siempre `"` para cadenas en tu proyecto.

2. ✅ **Prefiere f-strings para formatear texto**, son más legibles y eficientes.

3. ✅ **Evita concatenar cadenas dentro de bucles** con `+`; en su lugar, usa `join()` para mayor eficiencia:  
   ```python
   palabras = ["Python", "es", "genial"]
   frase = " ".join(palabras)
   print(frase)  # "Python es genial"
   ```

4. ✅ **Elimina espacios no deseados** con `.strip()` antes de procesar entradas de usuario.

5. ✅ **Documenta bien las cadenas multilínea** si contienen texto extenso.

## Resumen

- Las cadenas en Python son secuencias de caracteres delimitadas por comillas.  
- Son inmutables, por lo que no se pueden modificar directamente.  
- Se pueden concatenar, dividir, transformar y formatear con múltiples métodos.  
- Las **f-strings** son la forma más recomendada para trabajar con texto dinámico.  
- Mantener consistencia en comillas y aplicar buenas prácticas mejora la legibilidad del código.  