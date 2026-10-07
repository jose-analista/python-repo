# ==========================================
# MÓDULO PROPIO: utilidades.py
# ==========================================

# Este archivo es un módulo.
# Se importa desde 23_modulos.py con:
#
# import utilidades

PI = 3.1416


def saludar(nombre):

    return f"Hola, {nombre}."


def area_circulo(radio):

    return PI * radio ** 2


def es_par(numero):

    return numero % 2 == 0


# ==========================================
# __name__ == "__main__"
# ==========================================

# Este bloque solo se ejecuta si ejecutas
# ESTE archivo directamente:
#
# python basic/utilidades.py
#
# Si otro archivo lo importa, no se ejecuta.

if __name__ == "__main__":

    print("Probando utilidades.py directamente:")
    print(saludar("José"))
    print(area_circulo(2))
    print(es_par(4))