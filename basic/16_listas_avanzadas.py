# ==========================================
# LISTAS AVANZADAS EN PYTHON
# ==========================================

# ==========================================
# APPEND()
# ==========================================

# append() agrega un elemento al final.

lenguajes = [
    "Python",
    "PHP",
    "JavaScript"
]

print("Lista original:")
print(lenguajes)

lenguajes.append("Java")

print("\nDespués de append():")
print(lenguajes)


# ==========================================
# INSERT()
# ==========================================

# insert(posición, elemento)
# permite insertar un elemento en una posición.

lenguajes.insert(1, "C++")

print("\nDespués de insert():")
print(lenguajes)


# ==========================================
# EXTEND()
# ==========================================

# extend() permite agregar varios elementos.

lenguajes.extend([
    "C#",
    "Ruby"
])

print("\nDespués de extend():")
print(lenguajes)


# ==========================================
# MODIFICAR ELEMENTOS
# ==========================================

lenguajes[0] = "Laravel"

print("\nDespués de modificar el primer elemento:")
print(lenguajes)


# ==========================================
# REMOVE()
# ==========================================

# remove() elimina un elemento por su valor.

lenguajes.remove("Ruby")

print("\nDespués de remove():")
print(lenguajes)


# ==========================================
# POP()
# ==========================================

# pop() elimina un elemento por posición
# y además devuelve el elemento eliminado.

eliminado = lenguajes.pop()

print("\nElemento eliminado:")
print(eliminado)

print("\nLista después de pop():")
print(lenguajes)


# ==========================================
# POP CON POSICIÓN
# ==========================================

eliminado = lenguajes.pop(1)

print("\nElemento eliminado de posición 1:")
print(eliminado)

print("\nLista actual:")
print(lenguajes)


# ==========================================
# CLEAR()
# ==========================================

# clear() elimina todos los elementos.

temporal = [
    "Python",
    "PHP",
    "JavaScript"
]

temporal.clear()

print("\nLista después de clear():")
print(temporal)


# ==========================================
# INDEX()
# ==========================================

lenguajes = [
    "Python",
    "PHP",
    "JavaScript",
    "Java"
]

posicion = lenguajes.index("JavaScript")

print("\nPosición de JavaScript:")
print(posicion)


# ==========================================
# COUNT()
# ==========================================

numeros = [
    10,
    20,
    10,
    30,
    10,
    40
]

cantidad = numeros.count(10)

print("\nCantidad de veces que aparece 10:")
print(cantidad)


# ==========================================
# SORT()
# ==========================================

numeros = [
    50,
    10,
    40,
    20,
    30
]

numeros.sort()

print("\nNúmeros ordenados:")
print(numeros)


# ==========================================
# SORT DESCENDENTE
# ==========================================

numeros.sort(reverse=True)

print("\nNúmeros descendentes:")
print(numeros)


# ==========================================
# SORT CON TEXTOS
# ==========================================

lenguajes = [
    "Python",
    "Java",
    "C++",
    "PHP",
    "JavaScript"
]

lenguajes.sort()

print("\nLenguajes ordenados:")
print(lenguajes)


# ==========================================
# REVERSE()
# ==========================================

numeros = [
    1,
    2,
    3,
    4,
    5
]

numeros.reverse()

print("\nLista invertida:")
print(numeros)


# ==========================================
# LEN()
# ==========================================

lenguajes = [
    "Python",
    "PHP",
    "JavaScript"
]

print("\nCantidad de lenguajes:")
print(len(lenguajes))


# ==========================================
# COPIAR UNA LISTA
# ==========================================

original = [
    "Python",
    "PHP",
    "JavaScript"
]

copia = original.copy()

copia.append("Java")

print("\nLista original:")
print(original)

print("\nCopia:")
print(copia)


# ==========================================
# IMPORTANTE: REFERENCIA
# ==========================================

original = [
    "Python",
    "PHP"
]

referencia = original

referencia.append("JavaScript")

print("\nOriginal:")
print(original)

print("\nReferencia:")
print(referencia)

# Ambas listas muestran JavaScript porque
# referencia apunta a la misma lista.


# ==========================================
# SLICING
# ==========================================

numeros = [
    10,
    20,
    30,
    40,
    50
]

print("\nPrimeros tres:")
print(numeros[0:3])

print("\nDesde el segundo:")
print(numeros[1:])

print("\nÚltimos dos:")
print(numeros[-2:])


# ==========================================
# COMPROBAR SI EXISTE
# ==========================================

lenguajes = [
    "Python",
    "PHP",
    "JavaScript"
]

if "Python" in lenguajes:
    print("\nPython existe en la lista.")


# ==========================================
# LISTA DE PRODUCTOS
# ==========================================

productos = [
    "Notebook",
    "Mouse",
    "Teclado"
]

productos.append("Monitor")

print("\nProductos:")
print(productos)


# ==========================================
# ELIMINAR PRODUCTO
# ==========================================

productos.remove("Mouse")

print("\nProductos después de eliminar Mouse:")
print(productos)


# ==========================================
# LISTA DE PRECIOS
# ==========================================

precios = [
    500000,
    15000,
    25000,
    300000
]

print("\nPrecio mínimo:")
print(min(precios))

print("\nPrecio máximo:")
print(max(precios))

print("\nSuma de precios:")
print(sum(precios))


# ==========================================
# FILTRAR UNA LISTA CON FOR
# ==========================================

numeros = [
    10,
    15,
    20,
    25,
    30,
    35
]

pares = []

for numero in numeros:

    if numero % 2 == 0:
        pares.append(numero)

print("\nNúmeros pares:")
print(pares)


# ==========================================
# LISTA DE DICCIONARIOS
# ==========================================

productos = [
    {
        "nombre": "Notebook",
        "precio": 500000
    },
    {
        "nombre": "Mouse",
        "precio": 15000
    },
    {
        "nombre": "Monitor",
        "precio": 300000
    }
]

productos_caros = []

for producto in productos:

    if producto["precio"] > 100000:

        productos_caros.append(producto)


print("\nProductos sobre $100.000:")

for producto in productos_caros:

    print(
        producto["nombre"],
        "-",
        producto["precio"]
    )