# ==========================================
# MÓDULOS EN PYTHON
# ==========================================

# IMPORTANTE:
# Este archivo necesita utilidades.py en la
# misma carpeta (basic/).


# ==========================================
# ¿QUÉ ES UN MÓDULO?
# ==========================================

# Un módulo es un archivo .py con código
# (funciones, variables, etc.) que puedes
# reutilizar desde otros archivos.
#
# Python trae muchos módulos incluidos
# (la biblioteca estándar): math, random,
# datetime, os, json, etc.


# ==========================================
# IMPORT
# ==========================================

import math

print("Raíz cuadrada de 16:")
print(math.sqrt(16))

print("\nValor de pi:")
print(math.pi)

print("\nRedondear hacia arriba:")
print(math.ceil(4.2))

print("\nRedondear hacia abajo:")
print(math.floor(4.8))


# ==========================================
# FROM ... IMPORT
# ==========================================

# Importa solo lo que necesitas,
# sin escribir el nombre del módulo.

from math import sqrt, pow

print("\nsqrt(25):", sqrt(25))
print("pow(2, 3):", pow(2, 3))


# ==========================================
# IMPORT ... AS (ALIAS)
# ==========================================

import datetime as dt

ahora = dt.datetime.now()

print("\nFecha y hora actual:")
print(ahora)

print("\nSolo la fecha:")
print(ahora.date())

print("\nFormato personalizado:")
print(ahora.strftime("%d/%m/%Y %H:%M"))


# ==========================================
# MÓDULO RANDOM
# ==========================================

import random

print("\nNúmero aleatorio entre 1 y 10:")
print(random.randint(1, 10))

colores = ["rojo", "verde", "azul"]

print("\nColor aleatorio:")
print(random.choice(colores))

random.shuffle(colores)

print("\nLista mezclada:")
print(colores)


# ==========================================
# MÓDULO OS
# ==========================================

import os

print("\nCarpeta actual:")
print(os.getcwd())

print("\nArchivos de la carpeta:")

for nombre in os.listdir("."):

    print("-", nombre)


# ==========================================
# MÓDULO PROPIO
# ==========================================

import utilidades

print("\nMódulo propio:")

print(utilidades.saludar("José"))

print(utilidades.area_circulo(3))

print(utilidades.es_par(7))

print(utilidades.PI)


# ==========================================
# FROM CON MÓDULO PROPIO
# ==========================================

from utilidades import saludar, es_par

print("\n" + saludar("Ana"))

print(es_par(10))


# ==========================================
# VER QUÉ CONTIENE UN MÓDULO
# ==========================================

print("\nContenido de math (primeros 5):")
print(dir(math)[:5])

# help(math.sqrt) muestra la documentación
# de una función.


# ==========================================
# __name__
# ==========================================

# Python guarda en __name__ el nombre del
# módulo actual.
#
# Si ejecutas el archivo directamente,
# vale "__main__".
# Si lo importan, vale el nombre del archivo.

print("\n__name__ de este archivo:")
print(__name__)

print("__name__ de utilidades:")
print(utilidades.__name__)


# ==========================================
# IMPORT ERROR
# ==========================================

try:

    import modulo_que_no_existe

except ImportError:

    print("\nEl módulo no existe o no está instalado.")


# ==========================================
# EJEMPLO PRÁCTICO:
# CALCULADORA DE FECHAS
# ==========================================

from datetime import date

hoy = date.today()

nacimiento = date(2000, 5, 15)

edad = hoy.year - nacimiento.year

# Si aún no ha cumplido años este año, restar 1
if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):

    edad -= 1

print("\nEdad calculada:", edad)


# ==========================================
# EJEMPLO PRÁCTICO:
# GENERADOR DE CONTRASEÑAS
# ==========================================

import string

caracteres = string.ascii_letters + string.digits

contrasena = "".join(

    random.choice(caracteres)
    for _ in range(10)

)

print("\nContraseña generada:")
print(contrasena)