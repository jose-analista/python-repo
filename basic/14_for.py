# ==========================================
# CICLO FOR EN PYTHON
# ==========================================

# for permite recorrer elementos uno por uno.

lenguajes = [
    "Python",
    "PHP",
    "JavaScript",
    "Java"
]

for lenguaje in lenguajes:

    print(lenguaje)


# ==========================================
# FOR CON NÚMEROS
# ==========================================

numeros = [10, 20, 30, 40, 50]

for numero in numeros:

    print("Número:", numero)


# ==========================================
# RANGE()
# ==========================================

# range(5) genera números desde 0 hasta 4.

for numero in range(5):

    print("Número:", numero)


# ==========================================
# RANGE CON INICIO Y FIN
# ==========================================

for numero in range(1, 6):

    print("Número:", numero)


# ==========================================
# RANGE CON SALTO
# ==========================================

for numero in range(0, 11, 2):

    print("Número:", numero)


# ==========================================
# CUENTA REGRESIVA
# ==========================================

for numero in range(5, 0, -1):

    print("Cuenta:", numero)

print("¡Despegue!")


# ==========================================
# SUMAR NÚMEROS
# ==========================================

total = 0

for numero in range(1, 6):

    total += numero

print("Suma total:", total)


# ==========================================
# RECORRER UNA CADENA
# ==========================================

nombre = "José"

for letra in nombre:

    print("Letra:", letra)


# ==========================================
# ENUMERATE()
# ==========================================

lenguajes = [
    "Python",
    "PHP",
    "JavaScript",
    "Java"
]

for indice, lenguaje in enumerate(lenguajes):

    print(indice, "-", lenguaje)


# ==========================================
# ENUMERATE() DESDE 1
# ==========================================

for indice, lenguaje in enumerate(lenguajes, start=1):

    print(indice, "-", lenguaje)


# ==========================================
# FOR CON IF
# ==========================================

numeros = [1, 2, 3, 4, 5, 6]

for numero in numeros:

    if numero % 2 == 0:
        print("Par:", numero)


# ==========================================
# FOR CON IF / ELSE
# ==========================================

for numero in numeros:

    if numero % 2 == 0:
        print(numero, "es par")
    else:
        print(numero, "es impar")


# ==========================================
# RECORRER DICCIONARIO
# ==========================================

persona = {
    "nombre": "José",
    "edad": 25,
    "profesion": "Analista Programador"
}

for clave, valor in persona.items():

    print(clave, ":", valor)


# ==========================================
# RECORRER SOLO CLAVES
# ==========================================

for clave in persona.keys():

    print("Clave:", clave)


# ==========================================
# RECORRER SOLO VALORES
# ==========================================

for valor in persona.values():

    print("Valor:", valor)


# ==========================================
# RECORRER UN SET
# ==========================================

tecnologias = {
    "Python",
    "PHP",
    "Laravel",
    "JavaScript"
}

for tecnologia in tecnologias:

    print("Tecnología:", tecnologia)


# ==========================================
# BREAK
# ==========================================

for numero in range(1, 11):

    if numero == 5:
        break

    print(numero)


# ==========================================
# CONTINUE
# ==========================================

for numero in range(1, 6):

    if numero == 3:
        continue

    print(numero)


# ==========================================
# BUSCAR UN ELEMENTO
# ==========================================

lenguajes = [
    "Python",
    "PHP",
    "JavaScript"
]

for lenguaje in lenguajes:

    if lenguaje == "Python":

        print("Python encontrado.")


# ==========================================
# CONTAR ELEMENTOS
# ==========================================

numeros = [10, 20, 30, 40, 50]

contador = 0

for numero in numeros:

    contador += 1

print("Cantidad de números:", contador)


# ==========================================
# CALCULAR PROMEDIO
# ==========================================

notas = [5.5, 6.0, 4.8, 6.5]

total = 0

for nota in notas:

    total += nota

promedio = total / len(notas)

print("Promedio:", promedio)


# ==========================================
# LISTA DE PRODUCTOS
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

for producto in productos:

    print(
        producto["nombre"],
        "-",
        producto["precio"]
    )


# ==========================================
# FOR ANIDADO
# ==========================================

categorias = [
    {
        "nombre": "Backend",
        "tecnologias": ["Python", "PHP", "Java"]
    },
    {
        "nombre": "Frontend",
        "tecnologias": ["HTML", "CSS", "JavaScript"]
    }
]

for categoria in categorias:

    print("\nCategoría:", categoria["nombre"])

    for tecnologia in categoria["tecnologias"]:

        print("-", tecnologia)