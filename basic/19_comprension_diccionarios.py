# ==========================================
# COMPRENSIÓN DE DICCIONARIOS EN PYTHON
# ==========================================


# ==========================================
# DICCIONARIO NORMAL
# ==========================================

numeros = [1, 2, 3, 4, 5]

cuadrados = {}

for numero in numeros:

    cuadrados[numero] = numero ** 2

print("Cuadrados:")
print(cuadrados)


# ==========================================
# DICTIONARY COMPREHENSION
# ==========================================

cuadrados = {
    numero: numero ** 2
    for numero in numeros
}

print("\nCuadrados con comprensión:")
print(cuadrados)


# ==========================================
# ESTRUCTURA BÁSICA
# ==========================================

# {
#     clave: valor
#     for elemento in lista
# }


# ==========================================
# CREAR DICCIONARIO DE NÚMEROS
# ==========================================

numeros = [1, 2, 3, 4, 5]

dobles = {
    numero: numero * 2
    for numero in numeros
}

print("\nDobles:")
print(dobles)


# ==========================================
# ELEVAR AL CUADRADO
# ==========================================

cuadrados = {
    numero: numero ** 2
    for numero in numeros
}

print("\nCuadrados:")
print(cuadrados)


# ==========================================
# ELEVAR AL CUBO
# ==========================================

cubos = {
    numero: numero ** 3
    for numero in numeros
}

print("\nCubos:")
print(cubos)


# ==========================================
# TRABAJAR CON TEXTOS
# ==========================================

nombres = [
    "José",
    "Pedro",
    "Ana"
]

longitudes = {
    nombre: len(nombre)
    for nombre in nombres
}

print("\nLongitud de nombres:")
print(longitudes)


# ==========================================
# CONDICIÓN
# ==========================================

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = {
    numero: numero ** 2
    for numero in numeros
    if numero % 2 == 0
}

print("\nCuadrados de números pares:")
print(pares)


# ==========================================
# FILTRAR VALORES
# ==========================================

edades = {

    "José": 25,
    "Pedro": 30,
    "Ana": 22,
    "Carlos": 28

}

mayores = {
    nombre: edad
    for nombre, edad in edades.items()
    if edad >= 25
}

print("\nPersonas de 25 años o más:")
print(mayores)


# ==========================================
# TRANSFORMAR VALORES
# ==========================================

precios = {

    "notebook": 500000,
    "mouse": 15000,
    "teclado": 25000

}

precios_iva = {

    producto: precio * 1.19
    for producto, precio in precios.items()

}

print("\nPrecios con IVA:")
print(precios_iva)


# ==========================================
# FILTRAR PRODUCTOS
# ==========================================

productos_caros = {

    producto: precio
    for producto, precio in precios.items()
    if precio >= 30000
}

print("\nProductos de $30.000 o más:")
print(productos_caros)


# ==========================================
# CONDICIONAL IF / ELSE
# ==========================================

numeros = [1, 2, 3, 4, 5]

resultado = {

    numero: "Par" if numero % 2 == 0 else "Impar"

    for numero in numeros

}

print("\nPar o impar:")
print(resultado)


# ==========================================
# DICCIONARIO DE PRODUCTOS
# ==========================================

productos = {

    "Notebook": 500000,
    "Mouse": 15000,
    "Teclado": 25000,
    "Monitor": 180000

}

productos_con_descuento = {

    nombre: precio * 0.9

    for nombre, precio in productos.items()

}

print("\nProductos con 10% de descuento:")

for nombre, precio in productos_con_descuento.items():

    print(nombre, ":", precio)


# ==========================================
# DICCIONARIO DE USUARIOS
# ==========================================

usuarios = {

    1: "José",
    2: "Pedro",
    3: "Ana",
    4: "Carlos"

}

usuarios_formateados = {

    id_usuario: nombre.upper()

    for id_usuario, nombre in usuarios.items()

}

print("\nUsuarios en mayúsculas:")
print(usuarios_formateados)


# ==========================================
# DICCIONARIO ANIDADO
# ==========================================

usuarios = {

    1: {
        "nombre": "José",
        "edad": 25
    },

    2: {
        "nombre": "Pedro",
        "edad": 30
    },

    3: {
        "nombre": "Ana",
        "edad": 22
    }

}


# ==========================================
# FILTRAR DICCIONARIO ANIDADO
# ==========================================

usuarios_mayores = {

    id_usuario: datos

    for id_usuario, datos in usuarios.items()

    if datos["edad"] >= 25

}

print("\nUsuarios mayores:")
print(usuarios_mayores)


# ==========================================
# OBTENER SOLO NOMBRES
# ==========================================

nombres = {

    id_usuario: datos["nombre"]

    for id_usuario, datos in usuarios.items()

}

print("\nNombres:")
print(nombres)


# ==========================================
# EJEMPLO PRÁCTICO:
# PRODUCTOS CON STOCK
# ==========================================

productos = {

    "notebook": {
        "precio": 500000,
        "stock": 5
    },

    "mouse": {
        "precio": 15000,
        "stock": 20
    },

    "teclado": {
        "precio": 25000,
        "stock": 0
    }

}


# ==========================================
# PRODUCTOS DISPONIBLES
# ==========================================

disponibles = {

    nombre: datos

    for nombre, datos in productos.items()

    if datos["stock"] > 0

}

print("\nProductos disponibles:")
print(disponibles)


# ==========================================
# PRODUCTOS SIN STOCK
# ==========================================

agotados = {

    nombre: datos

    for nombre, datos in productos.items()

    if datos["stock"] == 0

}

print("\nProductos agotados:")
print(agotados)


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
# CREAR DICCIONARIO DE USUARIOS ACTIVOS
# ==========================================

usuarios_activos = {

    usuario["id"]: usuario["nombre"]

    for usuario in respuesta_api["usuarios"]

    if usuario["activo"]

}

print("\nUsuarios activos:")
print(usuarios_activos)