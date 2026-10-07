# ==========================================
# ENTORNOS VIRTUALES Y PIP EN PYTHON
# ==========================================

# Este archivo mezcla explicación (los comandos
# se escriben en la terminal, NO dentro de
# Python) con código que puedes ejecutar para
# ver en qué entorno estás.


# ==========================================
# ¿QUÉ ES PIP?
# ==========================================

# pip es el instalador de paquetes de Python.
# Descarga librerías externas desde PyPI
# (el repositorio oficial de paquetes).
#
# Comandos (en la terminal):
#
# pip install requests
# pip uninstall requests
# pip list
# pip show requests
# pip install --upgrade requests
# pip install requests==2.31.0   (versión exacta)


# ==========================================
# ¿QUÉ ES UN ENTORNO VIRTUAL?
# ==========================================

# Un entorno virtual es una carpeta aislada
# con su propia copia de Python y sus propios
# paquetes.
#
# Sirve para que cada proyecto tenga sus
# dependencias sin mezclarse con otros
# proyectos ni con el Python del sistema.
#
# Ejemplo: el proyecto A usa una versión de
# una librería y el proyecto B usa otra.


# ==========================================
# CREAR UN ENTORNO VIRTUAL
# ==========================================

# Desde la carpeta de tu proyecto:
#
# python -m venv venv
#
# (el segundo "venv" es el nombre de la carpeta;
# también se usa mucho ".venv")


# ==========================================
# ACTIVAR EL ENTORNO
# ==========================================

# Windows (PowerShell):
#
# venv\Scripts\Activate.ps1
#
# Windows (CMD):
#
# venv\Scripts\activate.bat
#
# Mac / Linux:
#
# source venv/bin/activate
#
# Si se activó bien, verás (venv) al inicio
# de la línea de la terminal.
#
# Si PowerShell bloquea el script, ejecuta:
#
# Set-ExecutionPolicy -Scope CurrentUser RemoteSigned


# ==========================================
# DESACTIVAR EL ENTORNO
# ==========================================

# deactivate


# ==========================================
# REQUIREMENTS.TXT
# ==========================================

# requirements.txt es la lista de paquetes que
# necesita tu proyecto.
#
# Guardar los paquetes instalados:
#
# pip freeze > requirements.txt
#
# Instalar todo en otro computador:
#
# pip install -r requirements.txt
#
# Contenido típico:
#
# requests==2.31.0
# python-dotenv==1.0.1


# ==========================================
# GIT Y EL ENTORNO VIRTUAL
# ==========================================

# La carpeta venv/ NO se sube a Git.
# Pesa mucho y se puede recrear con
# requirements.txt.
#
# Agrega esto a tu archivo .gitignore:
#
# venv/
# .venv/
# __pycache__/
#
# Sí se sube: requirements.txt


# ==========================================
# FLUJO DE TRABAJO COMPLETO
# ==========================================

# 1. python -m venv venv
# 2. Activar el entorno
# 3. pip install requests
# 4. pip freeze > requirements.txt
# 5. Trabajar en el proyecto
# 6. deactivate
#
# Para otra persona (o tú en otro PC):
#
# 1. git clone <repositorio>
# 2. python -m venv venv
# 3. Activar el entorno
# 4. pip install -r requirements.txt


# ==========================================
# AHORA, CÓDIGO PARA EJECUTAR
# ==========================================

import sys
import subprocess


# ==========================================
# VER QUÉ PYTHON ESTÁS USANDO
# ==========================================

print("Ejecutable de Python:")
print(sys.executable)

print("\nVersión:")
print(sys.version)


# ==========================================
# ¿ESTOY DENTRO DE UN ENTORNO VIRTUAL?
# ==========================================

# Dentro de un venv, sys.prefix es distinto
# de sys.base_prefix.

en_entorno = sys.prefix != sys.base_prefix

print("\n¿Entorno virtual activo?")
print(en_entorno)

if en_entorno:

    print("Carpeta del entorno:", sys.prefix)

else:

    print("Estás usando el Python global.")


# ==========================================
# EJECUTAR PIP DESDE PYTHON
# ==========================================

# Usar sys.executable -m pip garantiza que
# se use el pip del Python actual.

resultado = subprocess.run(

    [sys.executable, "-m", "pip", "--version"],
    capture_output=True,
    text=True

)

print("\nVersión de pip:")
print(resultado.stdout.strip())


# ==========================================
# LISTAR PAQUETES INSTALADOS
# ==========================================

from importlib import metadata

paquetes = sorted(

    (
        distribucion.metadata["Name"],
        distribucion.version
    )
    for distribucion in metadata.distributions()

)

print("\nPaquetes instalados:", len(paquetes))

for nombre, version in paquetes[:10]:

    print("-", nombre, version)

if len(paquetes) > 10:

    print("...")


# ==========================================
# COMPROBAR SI UN PAQUETE ESTÁ INSTALADO
# ==========================================

def esta_instalado(nombre):

    try:

        metadata.version(nombre)

        return True

    except metadata.PackageNotFoundError:

        return False


print("\n¿requests instalado?")
print(esta_instalado("requests"))

print("\n¿paquete_inexistente instalado?")
print(esta_instalado("paquete_inexistente"))


# ==========================================
# IMPORT DE UN PAQUETE EXTERNO
# ==========================================

# Si no instalas el paquete, import falla
# con ModuleNotFoundError (un ImportError).

try:

    import requests

    print("\nrequests versión:", requests.__version__)

except ImportError:

    print("\nrequests no está instalado.")
    print("Instálalo con: pip install requests")


# ==========================================
# EJEMPLO PRÁCTICO:
# VERIFICAR DEPENDENCIAS DEL PROYECTO
# ==========================================

dependencias = ["requests", "pytest", "flask"]

print("\nEstado de las dependencias:")

faltantes = []

for dependencia in dependencias:

    if esta_instalado(dependencia):

        print("✔", dependencia, metadata.version(dependencia))

    else:

        print("✘", dependencia, "(falta)")

        faltantes.append(dependencia)

if faltantes:

    print("\nPara instalar lo que falta:")
    print("pip install", " ".join(faltantes))

else:

    print("\nTodas las dependencias están instaladas.")