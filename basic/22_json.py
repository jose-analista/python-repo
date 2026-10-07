# ==========================================
# JSON EN PYTHON
# ==========================================


# ==========================================
# ¿QUÉ ES JSON?
# ==========================================

# JSON (JavaScript Object Notation) es un
# formato de texto para guardar e
# intercambiar datos.
#
# Es el formato que usan casi todas las APIs.
#
# Se parece mucho a los diccionarios de Python:
#
# {"nombre": "José", "edad": 25}
#
# Python incluye el módulo json para trabajar
# con este formato.

import json


# ==========================================
# EQUIVALENCIAS PYTHON ↔ JSON
# ==========================================

# dict   → objeto  { }
# list   → arreglo [ ]
# str    → texto "..."
# int    → número
# float  → número
# True   → true
# False  → false
# None   → null


# ==========================================
# DICCIONARIO → TEXTO JSON (dumps)
# ==========================================

usuario = {

    "nombre": "José",
    "edad": 25,
    "activo": True,
    "telefono": None

}

texto_json = json.dumps(usuario)

print("Texto JSON:")
print(texto_json)

print("\nTipo:")
print(type(texto_json))


# ==========================================
# JSON BIEN FORMATEADO (indent)
# ==========================================

print("\nCon indent:")
print(json.dumps(usuario, indent=4))


# ==========================================
# TILDES Y Ñ (ensure_ascii)
# ==========================================

# Por defecto, json convierte las tildes
# en códigos como \u00e9.

print("\nSin ensure_ascii=False:")
print(json.dumps({"ciudad": "Concepción"}))

print("\nCon ensure_ascii=False:")
print(
    json.dumps(
        {"ciudad": "Concepción"},
        ensure_ascii=False
    )
)


# ==========================================
# TEXTO JSON → DICCIONARIO (loads)
# ==========================================

texto = '{"nombre": "Ana", "edad": 28, "activo": false}'

datos = json.loads(texto)

print("\nDiccionario:")
print(datos)

print("\nTipo:")
print(type(datos))

print("\nNombre:", datos["nombre"])

print("Activo:", datos["activo"])


# ==========================================
# LISTAS EN JSON
# ==========================================

texto = '["python", "git", "sql"]'

tecnologias = json.loads(texto)

print("\nLista:")
print(tecnologias)

for tecnologia in tecnologias:

    print("-", tecnologia)


# ==========================================
# JSON ANIDADO
# ==========================================

texto = """
{
    "id": 1,
    "nombre": "José",
    "direccion": {
        "ciudad": "Santiago",
        "pais": "Chile"
    },
    "habilidades": ["Python", "Git", "SQL"]
}
"""

persona = json.loads(texto)

print("\nCiudad:")
print(persona["direccion"]["ciudad"])

print("\nPrimera habilidad:")
print(persona["habilidades"][0])


# ==========================================
# GUARDAR JSON EN UN ARCHIVO (dump)
# ==========================================

# dump  → escribe en un archivo
# dumps → devuelve un texto
#
# (la "s" significa "string")

proyecto = {

    "nombre": "python-repo",
    "lenguaje": "Python",
    "lecciones": 22,
    "temas": ["listas", "diccionarios", "excepciones"]

}

with open("proyecto.json", "w", encoding="utf-8") as archivo:

    json.dump(
        proyecto,
        archivo,
        indent=4,
        ensure_ascii=False
    )

print("\nproyecto.json creado.")


# ==========================================
# LEER JSON DESDE UN ARCHIVO (load)
# ==========================================

# load  → lee desde un archivo
# loads → lee desde un texto

with open("proyecto.json", "r", encoding="utf-8") as archivo:

    datos = json.load(archivo)

print("\nDatos leídos:")
print(datos)

print("\nTemas:")

for tema in datos["temas"]:

    print("-", tema)


# ==========================================
# MODIFICAR Y VOLVER A GUARDAR
# ==========================================

datos["lecciones"] = 23

datos["temas"].append("json")

with open("proyecto.json", "w", encoding="utf-8") as archivo:

    json.dump(
        datos,
        archivo,
        indent=4,
        ensure_ascii=False
    )

print("\nproyecto.json actualizado.")


# ==========================================
# JSON INVÁLIDO (JSONDecodeError)
# ==========================================

# En JSON los textos van con comillas dobles.
# Las comillas simples producen error.

texto_malo = "{'nombre': 'José'}"

try:

    datos = json.loads(texto_malo)

except json.JSONDecodeError as error:

    print("\nJSON inválido:")
    print(error)


# ==========================================
# ARCHIVO JSON QUE NO EXISTE
# ==========================================

try:

    with open("no_existe.json", "r", encoding="utf-8") as archivo:

        datos = json.load(archivo)

except FileNotFoundError:

    print("\nEl archivo JSON no existe.")


# ==========================================
# EJEMPLO PRÁCTICO:
# RESPUESTA DE UNA API
# ==========================================

respuesta = """
{
    "success": true,
    "usuarios": [
        {"id": 1, "nombre": "José", "email": "jose@mail.com"},
        {"id": 2, "nombre": "Pedro", "email": "pedro@mail.com"},
        {"id": 3, "nombre": "Ana"}
    ]
}
"""

datos = json.loads(respuesta)

if datos["success"]:

    print("\nUsuarios de la API:")

    for usuario in datos["usuarios"]:

        nombre = usuario["nombre"]

        # get() evita KeyError si falta el dato
        email = usuario.get("email", "Sin email")

        print(nombre, "-", email)


# ==========================================
# EJEMPLO PRÁCTICO:
# LISTA DE TAREAS EN JSON
# ==========================================

def cargar_tareas():

    try:

        with open("tareas.json", "r", encoding="utf-8") as archivo:

            return json.load(archivo)

    except (FileNotFoundError, json.JSONDecodeError):

        return []


def guardar_tareas(tareas):

    with open("tareas.json", "w", encoding="utf-8") as archivo:

        json.dump(
            tareas,
            archivo,
            indent=4,
            ensure_ascii=False
        )


def agregar_tarea(titulo):

    tareas = cargar_tareas()

    tareas.append({

        "id": len(tareas) + 1,
        "titulo": titulo,
        "completada": False

    })

    guardar_tareas(tareas)


agregar_tarea("Estudiar JSON")
agregar_tarea("Hacer commit")

print("\nTareas guardadas:")

for tarea in cargar_tareas():

    estado = "✔" if tarea["completada"] else "○"

    print(estado, tarea["id"], "-", tarea["titulo"])