# ==========================================
# CONSUMIR UNA API CON REQUESTS
# ==========================================

# Requisito: instalar requests dentro de tu
# entorno virtual (lo viste en basic/26):
#
# pip install requests
# pip freeze > requirements.txt
#
# Usaremos JSONPlaceholder, una API pública
# de prueba (no necesita registro ni clave):
#
# https://jsonplaceholder.typicode.com
#
# Sus datos son falsos: sirve para practicar.

import json

import requests


URL_BASE = "https://jsonplaceholder.typicode.com"

ARCHIVO_API = "tareas_api.json"


# ==========================================
# ¿QUÉ ES UNA API?
# ==========================================

# Una API es una forma de pedirle datos a
# otro programa a través de internet.
#
# Mandas una petición (request) a una URL y
# recibes una respuesta (response), casi
# siempre en formato JSON.
#
# Métodos HTTP principales:
#
# GET    → obtener datos
# POST   → crear datos
# PUT    → reemplazar datos
# PATCH  → modificar parte de los datos
# DELETE → eliminar datos


# ==========================================
# PRIMERA PETICIÓN (GET)
# ==========================================

respuesta = requests.get(
    f"{URL_BASE}/todos/1",
    timeout=10
)

print("Código de estado:", respuesta.status_code)

print("\nTexto crudo:")
print(respuesta.text)

print("\nComo diccionario de Python:")
datos = respuesta.json()
print(datos)

print("\nTítulo:", datos["title"])


# ==========================================
# CÓDIGOS DE ESTADO
# ==========================================

# 200 → OK
# 201 → creado
# 400 → petición mal hecha
# 401 → no autenticado
# 404 → no encontrado
# 500 → error del servidor

respuesta = requests.get(
    f"{URL_BASE}/todos/99999",
    timeout=10
)

print("\nTarea inexistente:", respuesta.status_code)


# ==========================================
# OBTENER UNA LISTA
# ==========================================

respuesta = requests.get(
    f"{URL_BASE}/todos",
    timeout=10
)

todos = respuesta.json()

print("\nCantidad de tareas:", len(todos))

print("\nPrimeras 3:")

for tarea in todos[:3]:

    estado = "✔" if tarea["completed"] else "○"

    print(estado, tarea["id"], "-", tarea["title"])


# ==========================================
# PARÁMETROS (params)
# ==========================================

# Equivale a escribir ?userId=1&completed=false
# al final de la URL.

respuesta = requests.get(
    f"{URL_BASE}/todos",
    params={

        "userId": 1,
        "completed": "false"

    },
    timeout=10
)

pendientes = respuesta.json()

print("\nPendientes del usuario 1:", len(pendientes))

print("URL final:", respuesta.url)


# ==========================================
# ENVIAR DATOS (POST)
# ==========================================

# JSONPlaceholder simula la creación:
# responde con el dato, pero no lo guarda.

nueva = {

    "title": "Aprender a consumir APIs",
    "completed": False,
    "userId": 1

}

respuesta = requests.post(
    f"{URL_BASE}/todos",
    json=nueva,
    timeout=10
)

print("\nPOST:", respuesta.status_code)
print(respuesta.json())


# ==========================================
# MANEJO DE ERRORES
# ==========================================

# Una API puede fallar de varias maneras:
#
# - Sin internet     → ConnectionError
# - Tarda demasiado  → Timeout
# - Respuesta 4xx/5xx → HTTPError
#                       (con raise_for_status())
# - Respuesta no JSON → ValueError

def obtener_json(ruta, params=None):

    try:

        respuesta = requests.get(
            f"{URL_BASE}{ruta}",
            params=params,
            timeout=10
        )

        respuesta.raise_for_status()

        return respuesta.json()

    except requests.exceptions.ConnectionError:

        print("Error: no hay conexión a internet.")

    except requests.exceptions.Timeout:

        print("Error: la API tardó demasiado en responder.")

    except requests.exceptions.HTTPError as error:

        print("Error HTTP:", error)

    except ValueError:

        print("Error: la respuesta no es un JSON válido.")

    return None


print("\nPrueba con ruta válida:")

dato = obtener_json("/todos/2")

print(dato)

print("\nPrueba con ruta inexistente:")

dato = obtener_json("/ruta_que_no_existe")

print(dato)


# ==========================================
# GUARDAR LO DESCARGADO EN JSON
# ==========================================

def guardar_json(datos, archivo):

    with open(archivo, "w", encoding="utf-8") as f:

        json.dump(
            datos,
            f,
            indent=4,
            ensure_ascii=False
        )


def cargar_json(archivo):

    try:

        with open(archivo, "r", encoding="utf-8") as f:

            return json.load(f)

    except (FileNotFoundError, json.JSONDecodeError):

        return []


# ==========================================
# CLASE PARA TRABAJAR CON LA API
# ==========================================

class ClienteTareas:

    def __init__(self, url_base):

        self.url_base = url_base

    def descargar(self, usuario_id):

        datos = obtener_json(
            "/todos",
            params={"userId": usuario_id}
        )

        if datos is None:

            return []

        # Nos quedamos solo con los campos
        # que necesitamos, con nombres propios.

        return [

            {
                "id": item["id"],
                "titulo": item["title"],
                "completada": item["completed"]
            }
            for item in datos

        ]


# ==========================================
# EJEMPLO PRÁCTICO:
# DESCARGAR TAREAS Y GUARDARLAS
# ==========================================

cliente = ClienteTareas(URL_BASE)

tareas = cliente.descargar(usuario_id=1)

print("\nTareas descargadas:", len(tareas))

if tareas:

    guardar_json(tareas, ARCHIVO_API)

    print(f"Guardadas en {ARCHIVO_API}")


# ==========================================
# EJEMPLO PRÁCTICO:
# RESUMEN DE LO GUARDADO
# ==========================================

guardadas = cargar_json(ARCHIVO_API)

completadas = [

    t for t in guardadas
    if t["completada"]

]

print("\nResumen:")
print("Total:", len(guardadas))
print("Completadas:", len(completadas))
print("Pendientes:", len(guardadas) - len(completadas))

print("\nPrimeras 5:")

for tarea in guardadas[:5]:

    estado = "✔" if tarea["completada"] else "○"

    print(estado, tarea["id"], "-", tarea["titulo"])