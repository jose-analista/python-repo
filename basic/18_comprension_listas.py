# ==========================================
# COMPRENSIÓN DE LISTAS EN PYTHON
# ==========================================


# ==========================================
# LISTA NORMAL
# ==========================================

numeros = [1, 2, 3, 4, 5]

dobles = []

for numero in numeros:

    dobles.append(numero * 2)

print("Dobles:")
print(dobles)


# ==========================================
# LIST COMPREHENSION
# ==========================================

dobles = [numero * 2 for numero in numeros]

print("\nDobles con comprensión:")
print(dobles)


# ==========================================
# ESTRUCTURA BÁSICA
# ==========================================

# [expresión for elemento in lista]

cuadrados = [numero ** 2 for numero in numeros]

print("\nCuadrados:")
print(cuadrados)


# ==========================================
# TRABAJAR CON TEXTOS
# ==========================================

nombres = [
    "José",
    "Pedro",
    "Ana",
    "Carlos"
]

nombres_mayusculas = [
    nombre.upper()
    for nombre in nombres
]

print("\nNombres en mayúsculas:")
print(nombres_mayusculas)


# ==========================================
# FILTRAR ELEMENTOS
# ==========================================

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [
    numero
    for numero in numeros
    if numero % 2 == 0
]

print("\nNúmeros pares:")
print(pares)


# ==========================================
# FILTRAR IMPARES
# ==========================================

impares = [
    numero
    for numero in numeros
    if numero % 2 != 0
]

print("\nNúmeros impares:")
print(impares)


# ==========================================
# CONDICIÓN + OPERACIÓN
# ==========================================

cuadrados_pares = [
    numero ** 2
    for numero in numeros
    if numero % 2 == 0
]

print("\nCuadrados de números pares:")
print(cuadrados_pares)


# ==========================================
# LISTA DE PRECIOS
# ==========================================

precios = [
    10000,
    25000,
    50000,
    75000
]

precios_con_iva = [
    precio * 1.19
    for precio in precios
]

print("\nPrecios con IVA:")
print(precios_con_iva)


# ==========================================
# FILTRAR PRECIOS
# ==========================================

precios_altos = [
    precio
    for precio in precios
    if precio >= 30000
]

print("\nPrecios mayores o iguales a $30.000:")
print(precios_altos)


# ==========================================
# LISTA DE DICCIONARIOS
# ==========================================

usuarios = [

    {
        "nombre": "José",
        "edad": 25
    },

    {
        "nombre": "Pedro",
        "edad": 30
    },

    {
        "nombre": "Ana",
        "edad": 22
    }

]


# ==========================================
# OBTENER NOMBRES
# ==========================================

nombres = [
    usuario["nombre"]
    for usuario in usuarios
]

print("\nNombres de usuarios:")
print(nombres)


# ==========================================
# FILTRAR USUARIOS
# ==========================================

usuarios_mayores = [
    usuario
    for usuario in usuarios
    if usuario["edad"] >= 25
]

print("\nUsuarios mayores o iguales a 25:")
print(usuarios_mayores)


# ==========================================
# OBTENER EDADES
# ==========================================

edades = [
    usuario["edad"]
    for usuario in usuarios
]

print("\nEdades:")
print(edades)


# ==========================================
# CONDICIONAL IF / ELSE
# ==========================================

numeros = [1, 2, 3, 4, 5]

resultados = [
    "Par" if numero % 2 == 0 else "Impar"
    for numero in numeros
]

print("\nResultado:")
print(resultados)


# ==========================================
# TRANSFORMAR DATOS
# ==========================================

nombres = [
    "jose",
    "pedro",
    "ana"
]

nombres_formateados = [
    nombre.capitalize()
    for nombre in nombres
]

print("\nNombres formateados:")
print(nombres_formateados)


# ==========================================
# EJEMPLO PRÁCTICO:
# PRODUCTOS
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
        "nombre": "Teclado",
        "precio": 25000
    }

]


# ==========================================
# OBTENER NOMBRES DE PRODUCTOS
# ==========================================

nombres_productos = [
    producto["nombre"]
    for producto in productos
]

print("\nProductos:")
print(nombres_productos)


# ==========================================
# OBTENER PRECIOS
# ==========================================

precios = [
    producto["precio"]
    for producto in productos
]

print("\nPrecios:")
print(precios)


# ==========================================
# PRODUCTOS CAROS
# ==========================================

productos_caros = [
    producto
    for producto in productos
    if producto["precio"] >= 30000
]

print("\nProductos caros:")

for producto in productos_caros:

    print(producto)


# ==========================================
# EJEMPLO PRÁCTICO:
# DATOS DE UNA API
# ==========================================

respuesta_api = {

    "usuarios": [

        {
            "id": 1,
            "nombre": "José",
            "activo": True
        },

        {
            "id": 2,
            "nombre": "Pedro",
            "activo": False
        },

        {
            "id": 3,
            "nombre": "Ana",
            "activo": True
        }

    ]

}


# ==========================================
# USUARIOS ACTIVOS
# ==========================================

usuarios_activos = [

    usuario
    for usuario in respuesta_api["usuarios"]
    if usuario["activo"]
]

print("\nUsuarios activos:")

for usuario in usuarios_activos:

    print(usuario)


# ==========================================
# SOLO NOMBRES DE USUARIOS ACTIVOS
# ==========================================

nombres_activos = [

    usuario["nombre"]
    for usuario in respuesta_api["usuarios"]
    if usuario["activo"]

]

print("\nNombres de usuarios activos:")
print(nombres_activos)