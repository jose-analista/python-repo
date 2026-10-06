# ==========================================
# DICCIONARIOS AVANZADOS EN PYTHON
# ==========================================


# ==========================================
# DICCIONARIO BÁSICO
# ==========================================

persona = {
    "nombre": "José",
    "edad": 25,
    "profesion": "Analista Programador"
}

print("Persona:")
print(persona)


# ==========================================
# ACCEDER A UN VALOR
# ==========================================

print("\nNombre:")
print(persona["nombre"])

print("\nEdad:")
print(persona["edad"])


# ==========================================
# GET()
# ==========================================

# get() permite obtener un valor sin producir
# un error si la clave no existe.

telefono = persona.get("telefono")

print("\nTeléfono:")
print(telefono)


# ==========================================
# GET() CON VALOR POR DEFECTO
# ==========================================

telefono = persona.get(
    "telefono",
    "No registrado"
)

print("\nTeléfono:")
print(telefono)


# ==========================================
# AGREGAR UN ELEMENTO
# ==========================================

persona["ciudad"] = "Santiago"

print("\nDespués de agregar ciudad:")
print(persona)


# ==========================================
# MODIFICAR UN ELEMENTO
# ==========================================

persona["edad"] = 26

print("\nDespués de modificar edad:")
print(persona)


# ==========================================
# UPDATE()
# ==========================================

# update() permite agregar o modificar
# varios elementos al mismo tiempo.

persona.update({
    "edad": 27,
    "telefono": "123456789",
    "activo": True
})

print("\nDespués de update():")
print(persona)


# ==========================================
# POP()
# ==========================================

# pop() elimina una clave y devuelve
# el valor eliminado.

telefono = persona.pop("telefono")

print("\nTeléfono eliminado:")
print(telefono)

print("\nPersona actual:")
print(persona)


# ==========================================
# POP() CON VALOR POR DEFECTO
# ==========================================

email = persona.pop(
    "email",
    "No registrado"
)

print("\nEmail:")
print(email)


# ==========================================
# SETDEFAULT()
# ==========================================

# setdefault() agrega una clave solamente
# si todavía no existe.

persona.setdefault(
    "email",
    "jose@email.com"
)

print("\nDespués de setdefault():")
print(persona)


# Si email ya existe, no lo modifica.

persona.setdefault(
    "email",
    "otro@email.com"
)

print("\nEmail:")
print(persona["email"])


# ==========================================
# KEYS()
# ==========================================

print("\nClaves:")

for clave in persona.keys():

    print("-", clave)


# ==========================================
# VALUES()
# ==========================================

print("\nValores:")

for valor in persona.values():

    print("-", valor)


# ==========================================
# ITEMS()
# ==========================================

print("\nClaves y valores:")

for clave, valor in persona.items():

    print(clave, ":", valor)


# ==========================================
# COMPROBAR CLAVE
# ==========================================

if "nombre" in persona:

    print("\nLa clave nombre existe.")


if "direccion" not in persona:

    print("La clave direccion no existe.")


# ==========================================
# LONGITUD
# ==========================================

print("\nCantidad de datos:")

print(len(persona))


# ==========================================
# DICCIONARIO ANIDADO
# ==========================================

usuario = {

    "nombre": "José",

    "contacto": {

        "email": "jose@email.com",
        "telefono": "123456789"

    },

    "direccion": {

        "ciudad": "Santiago",
        "pais": "Chile"

    }

}

print("\nUsuario:")
print(usuario)


# ==========================================
# ACCEDER A DICCIONARIO ANIDADO
# ==========================================

print("\nEmail:")

print(
    usuario["contacto"]["email"]
)


print("\nCiudad:")

print(
    usuario["direccion"]["ciudad"]
)


# ==========================================
# MODIFICAR DICCIONARIO ANIDADO
# ==========================================

usuario["direccion"]["ciudad"] = "Valparaíso"

print("\nCiudad modificada:")

print(
    usuario["direccion"]["ciudad"]
)


# ==========================================
# LISTA DENTRO DE DICCIONARIO
# ==========================================

usuario = {

    "nombre": "José",

    "lenguajes": [
        "Python",
        "PHP",
        "JavaScript"
    ]

}

print("\nLenguajes del usuario:")

for lenguaje in usuario["lenguajes"]:

    print("-", lenguaje)


# ==========================================
# DICCIONARIO DENTRO DE LISTA
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

print("\nUsuarios:")

for usuario in usuarios:

    print(
        usuario["nombre"],
        "-",
        usuario["edad"]
    )


# ==========================================
# BUSCAR USUARIO
# ==========================================

nombre_buscado = "Pedro"

for usuario in usuarios:

    if usuario["nombre"] == nombre_buscado:

        print("\nUsuario encontrado:")

        print(usuario)

        break


# ==========================================
# MODIFICAR USUARIO
# ==========================================

for usuario in usuarios:

    if usuario["nombre"] == "Ana":

        usuario["edad"] = 23


print("\nUsuarios actualizados:")

for usuario in usuarios:

    print(usuario)


# ==========================================
# FILTRAR USUARIOS
# ==========================================

usuarios_mayores = []

for usuario in usuarios:

    if usuario["edad"] >= 25:

        usuarios_mayores.append(usuario)


print("\nUsuarios de 25 años o más:")

for usuario in usuarios_mayores:

    print(usuario)


# ==========================================
# DICCIONARIO DE PRODUCTOS
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
        "stock": 10
    }

}

print("\nProductos:")

for nombre, datos in productos.items():

    print(
        nombre,
        "- Precio:",
        datos["precio"],
        "- Stock:",
        datos["stock"]
    )


# ==========================================
# ACTUALIZAR STOCK
# ==========================================

productos["mouse"]["stock"] -= 1

print("\nStock del mouse:")

print(
    productos["mouse"]["stock"]
)


# ==========================================
# BUSCAR PRODUCTO
# ==========================================

producto_buscado = "notebook"

if producto_buscado in productos:

    print("\nProducto encontrado:")

    print(
        productos[producto_buscado]
    )


# ==========================================
# CONTAR ELEMENTOS
# ==========================================

print("\nCantidad de productos:")

print(len(productos))


# ==========================================
# COPIAR DICCIONARIO
# ==========================================

original = {

    "nombre": "José",
    "edad": 25

}

copia = original.copy()

copia["edad"] = 30

print("\nDiccionario original:")

print(original)

print("\nCopia:")

print(copia)


# ==========================================
# DICCIONARIO CON LISTA DE PRODUCTOS
# ==========================================

tienda = {

    "nombre": "Caytech",

    "productos": [

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

}

print("\nProductos de la tienda:")

for producto in tienda["productos"]:

    print(
        producto["nombre"],
        "-",
        producto["precio"]
    )


# ==========================================
# EJEMPLO PRÁCTICO:
# DATOS DE UNA API
# ==========================================

respuesta_api = {

    "success": True,

    "usuario": {

        "id": 1,
        "nombre": "José",
        "email": "jose@email.com"

    }

}

if respuesta_api["success"]:

    usuario = respuesta_api["usuario"]

    print("\nUsuario recibido desde API:")

    print("ID:", usuario["id"])
    print("Nombre:", usuario["nombre"])
    print("Email:", usuario["email"])