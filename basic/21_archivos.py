# ==========================================
# ARCHIVOS EN PYTHON
# ==========================================


# ==========================================
# ¿QUÉ ES TRABAJAR CON ARCHIVOS?
# ==========================================

# Python puede crear, leer, escribir y
# modificar archivos del computador.
#
# Se usa la función open():
#
# open("nombre", "modo", encoding="utf-8")
#
# Modos principales:
#
# "r" → leer (el archivo debe existir)
# "w" → escribir (crea el archivo o BORRA el contenido anterior)
# "a" → agregar al final (no borra nada)


# ==========================================
# ESCRIBIR UN ARCHIVO (w)
# ==========================================

archivo = open(
    "datos.txt",
    "w",
    encoding="utf-8"
)

archivo.write("Hola, soy José.\n")
archivo.write("Estoy aprendiendo Python.\n")

archivo.close()

print("Archivo creado.")


# ==========================================
# LEER UN ARCHIVO (r)
# ==========================================

archivo = open(
    "datos.txt",
    "r",
    encoding="utf-8"
)

contenido = archivo.read()

archivo.close()

print("\nContenido:")
print(contenido)


# ==========================================
# WITH (FORMA RECOMENDADA)
# ==========================================

# with cierra el archivo automáticamente,
# incluso si ocurre un error.

with open("datos.txt", "r", encoding="utf-8") as archivo:

    contenido = archivo.read()

print("Leído con with:")
print(contenido)


# ==========================================
# AGREGAR AL FINAL (a)
# ==========================================

with open("datos.txt", "a", encoding="utf-8") as archivo:

    archivo.write("Esta línea fue agregada después.\n")

print("Línea agregada.")


# ==========================================
# LEER LÍNEA POR LÍNEA
# ==========================================

print("\nLínea por línea:")

with open("datos.txt", "r", encoding="utf-8") as archivo:

    for linea in archivo:

        # strip() elimina el salto de línea
        print(linea.strip())


# ==========================================
# READLINE() Y READLINES()
# ==========================================

with open("datos.txt", "r", encoding="utf-8") as archivo:

    primera = archivo.readline()

    print("\nPrimera línea:")
    print(primera.strip())

with open("datos.txt", "r", encoding="utf-8") as archivo:

    lineas = archivo.readlines()

print("\nreadlines() devuelve una lista:")
print(lineas)

print("\nCantidad de líneas:", len(lineas))


# ==========================================
# ESCRIBIR UNA LISTA
# ==========================================

frutas = ["manzana", "pera", "uva"]

with open("frutas.txt", "w", encoding="utf-8") as archivo:

    for fruta in frutas:

        archivo.write(fruta + "\n")

print("\nfrutas.txt creado.")


# ==========================================
# LEER A UNA LISTA
# ==========================================

with open("frutas.txt", "r", encoding="utf-8") as archivo:

    frutas_leidas = [

        linea.strip()
        for linea in archivo

    ]

print("Frutas leídas:")
print(frutas_leidas)


# ==========================================
# ARCHIVO QUE NO EXISTE
# ==========================================

try:

    with open("no_existe.txt", "r", encoding="utf-8") as archivo:

        print(archivo.read())

except FileNotFoundError:

    print("\nEl archivo no existe.")


# ==========================================
# COMPROBAR SI EXISTE (os)
# ==========================================

import os

if os.path.exists("datos.txt"):

    print("\ndatos.txt existe.")

else:

    print("\ndatos.txt no existe.")


# ==========================================
# ELIMINAR UN ARCHIVO
# ==========================================

if os.path.exists("frutas.txt"):

    os.remove("frutas.txt")

    print("frutas.txt eliminado.")


# ==========================================
# CONTAR PALABRAS DE UN ARCHIVO
# ==========================================

with open("datos.txt", "r", encoding="utf-8") as archivo:

    texto = archivo.read()

palabras = texto.split()

print("\nCantidad de palabras:", len(palabras))


# ==========================================
# EJEMPLO PRÁCTICO:
# GUARDAR Y LEER USUARIOS
# ==========================================

usuarios = [

    {"nombre": "José", "edad": 25},
    {"nombre": "Pedro", "edad": 30},
    {"nombre": "Ana", "edad": 28}

]

with open("usuarios.txt", "w", encoding="utf-8") as archivo:

    for usuario in usuarios:

        archivo.write(
            f"{usuario['nombre']},{usuario['edad']}\n"
        )

print("\nusuarios.txt creado.")

print("Usuarios leídos:")

with open("usuarios.txt", "r", encoding="utf-8") as archivo:

    for linea in archivo:

        nombre, edad = linea.strip().split(",")

        print(nombre, "-", edad)


# ==========================================
# EJEMPLO PRÁCTICO:
# LISTA DE TAREAS CON ARCHIVO
# ==========================================

def guardar_tarea(tarea):

    with open("tareas.txt", "a", encoding="utf-8") as archivo:

        archivo.write(tarea + "\n")


def leer_tareas():

    try:

        with open("tareas.txt", "r", encoding="utf-8") as archivo:

            return [

                linea.strip()
                for linea in archivo

            ]

    except FileNotFoundError:

        return []


guardar_tarea("Estudiar Python")
guardar_tarea("Hacer commit")

print("\nTareas guardadas:")

for numero, tarea in enumerate(leer_tareas(), start=1):

    print(numero, "-", tarea)