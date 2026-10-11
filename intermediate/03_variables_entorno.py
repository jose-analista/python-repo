# ==========================================
# VARIABLES DE ENTORNO Y ARCHIVOS .ENV
# ==========================================

# Requisito: instalar python-dotenv en tu
# entorno virtual:
#
# pip install python-dotenv
# pip freeze > requirements.txt

import os

from dotenv import load_dotenv


# ==========================================
# ¿QUÉ ES UNA VARIABLE DE ENTORNO?
# ==========================================

# Es un dato de configuración que vive FUERA
# de tu código, en el sistema o en un archivo.
#
# Se usa para guardar:
#
# - claves de API (API keys)
# - contraseñas de bases de datos
# - tokens
# - configuración que cambia según el equipo
#   (desarrollo, pruebas, producción)
#
# Regla de oro: NUNCA escribas una clave
# directamente en el código ni la subas a Git.
# Si se sube a GitHub, cualquiera puede
# usarla, aunque la borres después.


# ==========================================
# LO QUE NO DEBES HACER
# ==========================================

# API_KEY = "sk-1234567890abcdef"
#
# Esa línea queda guardada en el historial de
# Git para siempre.


# ==========================================
# LEER VARIABLES DEL SISTEMA (os.environ)
# ==========================================

# os.environ funciona como un diccionario.

print("Usuario del sistema:")

print(
    os.environ.get("USERNAME")
    or os.environ.get("USER")
    or "No disponible"
)

print("\nCantidad de variables de entorno:")
print(len(os.environ))


# ==========================================
# GETENV() CON VALOR POR DEFECTO
# ==========================================

print("\nVariable que no existe:")
print(os.getenv("VARIABLE_INEXISTENTE"))

print("\nCon valor por defecto:")
print(os.getenv("VARIABLE_INEXISTENTE", "valor por defecto"))


# ==========================================
# os.environ[...] vs os.getenv(...)
# ==========================================

# os.environ["X"] → lanza KeyError si no existe
# os.getenv("X")  → devuelve None si no existe

try:

    valor = os.environ["VARIABLE_INEXISTENTE"]

except KeyError:

    print("\nKeyError: la variable no existe.")


# ==========================================
# DEFINIR UNA VARIABLE (SOLO EN ESTE PROGRAMA)
# ==========================================

# Esto solo vive mientras el programa corre.

os.environ["MODO_PRUEBA"] = "true"

print("\nMODO_PRUEBA:", os.getenv("MODO_PRUEBA"))


# ==========================================
# TODAS LAS VARIABLES SON TEXTO
# ==========================================

# Aunque escribas PUERTO=8000 o DEBUG=true,
# Python las lee como str. Hay que convertir.

os.environ["PUERTO"] = "8000"

puerto = int(os.getenv("PUERTO", "3000"))

print("\nPuerto:", puerto)
print("Tipo:", type(puerto))

debug = os.getenv("MODO_PRUEBA", "false").lower() == "true"

print("\nDebug:", debug)

# Ojo: bool("false") es True, porque
# cualquier texto no vacío es True.
# Por eso se compara con "true".


# ==========================================
# ¿QUÉ ES UN ARCHIVO .ENV?
# ==========================================

# Un archivo de texto llamado .env en la raíz
# del proyecto, con una variable por línea:
#
# API_KEY=mi_clave_secreta
# API_URL=https://jsonplaceholder.typicode.com
# DEBUG=true
# PUERTO=8000
#
# Reglas:
#
# - Sin espacios alrededor del =
# - Sin comillas (normalmente)
# - Los comentarios empiezan con #
#
# python-dotenv lee ese archivo y carga cada
# línea como variable de entorno.


# ==========================================
# CARGAR EL .ENV
# ==========================================

# load_dotenv() busca un archivo .env y
# devuelve True si lo encontró.

encontrado = load_dotenv()

print("\n¿Se encontró un archivo .env?")
print(encontrado)

if not encontrado:

    print("No hay .env. Más abajo se crea un ejemplo.")


# ==========================================
# .GITIGNORE Y .ENV.EXAMPLE
# ==========================================

# 1. El archivo .env va en .gitignore:
#
#    .env
#
# 2. En su lugar, subes un archivo
#    .env.example con los NOMBRES de las
#    variables pero sin los valores reales.
#    Así quien clone el repo sabe qué debe
#    configurar.
#
# Flujo para otra persona (o tú en otro PC):
#
#    1. git clone <repositorio>
#    2. Copiar .env.example a .env
#    3. Rellenar los valores reales


# ==========================================
# CREAR UN .ENV.EXAMPLE DESDE PYTHON
# ==========================================

def crear_env_example(archivo=".env.example"):

    if os.path.exists(archivo):

        print(f"\n{archivo} ya existe. No se modifica.")

        return

    contenido = (

        "# Copia este archivo como .env y completa los valores\n"
        "API_KEY=tu_clave_aqui\n"
        "API_URL=https://jsonplaceholder.typicode.com\n"
        "DEBUG=true\n"
        "PUERTO=8000\n"

    )

    with open(archivo, "w", encoding="utf-8") as f:

        f.write(contenido)

    print(f"\n{archivo} creado.")


crear_env_example()


# ==========================================
# VALIDAR VARIABLES OBLIGATORIAS
# ==========================================

def exigir(nombre):

    valor = os.getenv(nombre)

    if not valor:

        raise RuntimeError(
            f"Falta la variable de entorno {nombre}. "
            "Revisa tu archivo .env."
        )

    return valor


try:

    clave = exigir("API_KEY")

    print("\nAPI_KEY cargada.")

except RuntimeError as error:

    print("\nError:")
    print(error)


# ==========================================
# NO IMPRIMIR CLAVES COMPLETAS
# ==========================================

# Ni en pantalla ni en logs. Si necesitas
# comprobar que existe, muestra solo el final.

def ocultar(secreto):

    if not secreto:

        return "(vacía)"

    if len(secreto) <= 4:

        return "****"

    return "****" + secreto[-4:]


print("\nEjemplos de ocultar():")
print(ocultar("sk-1234567890abcdef"))
print(ocultar(None))


# ==========================================
# CLASE DE CONFIGURACIÓN
# ==========================================

# Centralizar la configuración en un solo
# lugar evita repetir os.getenv() por todo
# el código.

class Config:

    def __init__(self):

        self.api_key = os.getenv("API_KEY")

        self.api_url = os.getenv(
            "API_URL",
            "https://jsonplaceholder.typicode.com"
        )

        self.debug = (
            os.getenv("DEBUG", "false").lower() == "true"
        )

        self.puerto = int(os.getenv("PUERTO", "8000"))

    def cabeceras(self):

        # Muchas APIs piden la clave en una
        # cabecera (header) de la petición.

        return {

            "Authorization": f"Bearer {self.api_key}"

        }

    def __repr__(self):

        return (

            f"Config(api_url={self.api_url!r}, "
            f"debug={self.debug}, "
            f"puerto={self.puerto}, "
            f"api_key={ocultar(self.api_key)!r})"

        )


config = Config()

print("\nConfiguración:")
print(config)


# ==========================================
# USO CON REQUESTS (EJEMPLO)
# ==========================================

# Así se usaría la clave en una petición real
# a una API que la exija:
#
# import requests
#
# respuesta = requests.get(
#     f"{config.api_url}/recurso",
#     headers=config.cabeceras(),
#     timeout=10
# )
#
# JSONPlaceholder no pide clave, por eso
# aquí solo se muestra como ejemplo.


# ==========================================
# EJEMPLO PRÁCTICO:
# REVISAR LA CONFIGURACIÓN DEL PROYECTO
# ==========================================

requeridas = ["API_KEY", "API_URL"]

print("\nEstado de la configuración:")

faltantes = []

for nombre in requeridas:

    if os.getenv(nombre):

        print("✔", nombre)

    else:

        print("✘", nombre, "(falta)")

        faltantes.append(nombre)

if faltantes:

    print("\nCrea un archivo .env con:")

    for nombre in faltantes:

        print(f"{nombre}=...")

else:

    print("\nConfiguración completa.")


# ==========================================
# SI SUBISTE UN .ENV POR ERROR
# ==========================================

# Dejar de rastrear el archivo (no lo borra
# de tu disco):
#
# git rm --cached .env
# git commit -m "Deja de rastrear .env"
#
# Pero OJO: la clave sigue en el historial.
# Si ya estaba en GitHub, considérala
# comprometida y GENERA UNA NUEVA en el
# panel del servicio.