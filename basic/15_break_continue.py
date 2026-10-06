# ==========================================
# BREAK Y CONTINUE EN PYTHON
# ==========================================

# break y continue sirven para controlar
# el comportamiento de los ciclos.


# ==========================================
# BREAK CON FOR
# ==========================================

print("BREAK CON FOR:")

for numero in range(1, 11):

    print(numero)

    if numero == 5:
        break


# ==========================================
# BREAK CON WHILE
# ==========================================

print("\nBREAK CON WHILE:")

contador = 1

while contador <= 10:

    print(contador)

    if contador == 5:
        break

    contador += 1


# ==========================================
# CONTINUE CON FOR
# ==========================================

print("\nCONTINUE CON FOR:")

for numero in range(1, 11):

    if numero == 5:
        continue

    print(numero)


# ==========================================
# CONTINUE CON WHILE
# ==========================================

print("\nCONTINUE CON WHILE:")

contador = 0

while contador < 10:

    contador += 1

    if contador == 5:
        continue

    print(contador)


# ==========================================
# BUSCAR UN ELEMENTO CON BREAK
# ==========================================

print("\nBUSCAR CON BREAK:")

lenguajes = [
    "PHP",
    "Java",
    "Python",
    "JavaScript",
    "C++"
]

for lenguaje in lenguajes:

    print("Revisando:", lenguaje)

    if lenguaje == "Python":

        print("Python encontrado.")

        break


# ==========================================
# IGNORAR ELEMENTOS CON CONTINUE
# ==========================================

print("\nIGNORAR ELEMENTOS:")

lenguajes = [
    "Python",
    "PHP",
    "JavaScript",
    "Java",
    "C++"
]

for lenguaje in lenguajes:

    if lenguaje == "Java":
        continue

    print("Lenguaje:", lenguaje)


# ==========================================
# SOLO NÚMEROS PARES
# ==========================================

print("\nNÚMEROS PARES:")

for numero in range(1, 11):

    if numero % 2 != 0:
        continue

    print(numero)


# ==========================================
# DETENER CUANDO ENCUENTRE UN NÚMERO
# ==========================================

print("\nBUSCANDO EL NÚMERO 7:")

for numero in range(1, 11):

    if numero == 7:

        print("Número encontrado:", numero)

        break


# ==========================================
# BREAK CON LISTA DE PRODUCTOS
# ==========================================

print("\nBUSCAR PRODUCTO:")

productos = [
    "Notebook",
    "Mouse",
    "Teclado",
    "Monitor",
    "Audífonos"
]

for producto in productos:

    print("Revisando:", producto)

    if producto == "Monitor":

        print("Producto encontrado.")

        break


# ==========================================
# CONTINUE CON PRODUCTOS
# ==========================================

print("\nIGNORAR UN PRODUCTO:")

for producto in productos:

    if producto == "Mouse":
        continue

    print("Producto:", producto)


# ==========================================
# VALIDAR DATOS
# ==========================================

print("\nVALIDANDO EDADES:")

edades = [15, 20, 17, 25, 30]

for edad in edades:

    if edad < 18:
        continue

    print("Edad válida:", edad)


# ==========================================
# BUSCAR USUARIO
# ==========================================

print("\nBUSCAR USUARIO:")

usuarios = [
    {
        "nombre": "Pedro",
        "activo": False
    },
    {
        "nombre": "José",
        "activo": True
    },
    {
        "nombre": "Ana",
        "activo": True
    }
]

for usuario in usuarios:

    if not usuario["activo"]:
        continue

    print("Usuario activo:", usuario["nombre"])


# ==========================================
# BREAK Y CONTINUE JUNTOS
# ==========================================

print("\nBREAK Y CONTINUE JUNTOS:")

for numero in range(1, 11):

    if numero % 2 != 0:
        continue

    if numero > 8:
        break

    print(numero)


# ==========================================
# EJEMPLO PRÁCTICO:
# PROCESAR PEDIDOS
# ==========================================

print("\nPROCESANDO PEDIDOS:")

pedidos = [
    {"id": 1, "estado": "completado"},
    {"id": 2, "estado": "cancelado"},
    {"id": 3, "estado": "completado"},
    {"id": 4, "estado": "pendiente"},
    {"id": 5, "estado": "completado"}
]

for pedido in pedidos:

    # Ignoramos pedidos cancelados.

    if pedido["estado"] == "cancelado":
        continue

    print(
        "Procesando pedido:",
        pedido["id"]
    )


# ==========================================
# DETENER PROCESAMIENTO
# ==========================================

print("\nDETENER PROCESAMIENTO:")

for pedido in pedidos:

    if pedido["estado"] == "cancelado":

        print("Pedido cancelado encontrado.")

        break

    print("Pedido:", pedido["id"])