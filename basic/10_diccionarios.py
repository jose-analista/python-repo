# ==========================================
# DICCIONARIOS EN PYTHON
# ==========================================

# Un diccionario almacena información mediante
# una relación CLAVE -> VALOR.

persona = {
    "nombre": "José",
    "edad": 25,
    "profesion": "Analista Programador",
    "activo": True
}

print("Datos de la persona:")
print(persona)

# ==========================================
# ACCEDER A VALORES
# ==========================================

print("\nNombre:")
print(persona["nombre"])

print("\nEdad:")
print(persona["edad"])

print("\nProfesión:")
print(persona["profesion"])

# ==========================================
# AGREGAR UN NUEVO DATO
# ==========================================

persona["ciudad"] = "Santiago"

print("\nPersona con ciudad:")
print(persona)

# ==========================================
# MODIFICAR UN DATO
# ==========================================

persona["edad"] = 26

print("\nEdad modificada:")
print(persona["edad"])

# ==========================================
# ELIMINAR UN DATO
# ==========================================

del persona["activo"]

print("\nDespués de eliminar 'activo':")
print(persona)

# ==========================================
# COMPROBAR SI EXISTE UNA CLAVE
# ==========================================

if "nombre" in persona:
    print("\nLa clave 'nombre' existe.")

if "telefono" not in persona:
    print("La clave 'telefono' no existe.")

# ==========================================
# OBTENER TODAS LAS CLAVES
# ==========================================

print("\nClaves del diccionario:")

for clave in persona:
    print("-", clave)

# ==========================================
# OBTENER CLAVE Y VALOR
# ==========================================

print("\nClaves y valores:")

for clave, valor in persona.items():
    print(clave, ":", valor)

# ==========================================
# OBTENER SOLO LOS VALORES
# ==========================================

print("\nValores:")

for valor in persona.values():
    print("-", valor)

# ==========================================
# OBTENER SOLO LAS CLAVES
# ==========================================

print("\nClaves:")

for clave in persona.keys():
    print("-", clave)

# ==========================================
# LONGITUD DEL DICCIONARIO
# ==========================================

cantidad = len(persona)

print("\nCantidad de datos:")
print(cantidad)

# ==========================================
# USAR get()
# ==========================================

telefono = persona.get("telefono")

print("\nTeléfono:")
print(telefono)

# Como 'telefono' no existe,
# get() devuelve None en lugar
# de producir un error.

# ==========================================
# get() CON VALOR POR DEFECTO
# ==========================================

telefono = persona.get("telefono", "No registrado")

print("\nTeléfono:")
print(telefono)

# ==========================================
# DICCIONARIO DE UN PRODUCTO
# ==========================================

producto = {
    "nombre": "Notebook",
    "precio": 500000,
    "stock": 10
}

print("\nProducto:")
print(producto)

print("Nombre:", producto["nombre"])
print("Precio:", producto["precio"])
print("Stock:", producto["stock"])

# ==========================================
# MODIFICAR PRODUCTO
# ==========================================

producto["precio"] = 450000
producto["stock"] = 8

print("\nProducto actualizado:")
print(producto)

# ==========================================
# DICCIONARIOS DENTRO DE UNA LISTA
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

print("\nLista de productos:")

for producto in productos:
    print(producto["nombre"], "-", producto["precio"])

# ==========================================
# DICCIONARIO ANIDADO
# ==========================================

usuario = {
    "nombre": "José",
    "contacto": {
        "email": "jose@email.com",
        "telefono": "123456789"
    }
}

print("\nEmail del usuario:")
print(usuario["contacto"]["email"])

print("\nTeléfono del usuario:")
print(usuario["contacto"]["telefono"])