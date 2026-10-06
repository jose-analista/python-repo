# ==========================================
# LISTAS EN PYTHON
# ==========================================

# Una lista puede almacenar varios valores.
lenguajes = ["Python", "PHP", "JavaScript", "Java"]

print("Lenguajes:")
print(lenguajes)


# ==========================================
# ACCEDER A ELEMENTOS
# ==========================================

print("\nPrimer lenguaje:")
print(lenguajes[0])

print("\nSegundo lenguaje:")
print(lenguajes[1])


# ==========================================
# ÍNDICES NEGATIVOS
# ==========================================

print("\nÚltimo lenguaje:")
print(lenguajes[-1])

print("\nPenúltimo lenguaje:")
print(lenguajes[-2])


# ==========================================
# LONGITUD DE UNA LISTA
# ==========================================

cantidad = len(lenguajes)

print("\nCantidad de lenguajes:", cantidad)


# ==========================================
# MODIFICAR UN ELEMENTO
# ==========================================

lenguajes[1] = "Laravel"

print("\nLista modificada:")
print(lenguajes)


# ==========================================
# AGREGAR ELEMENTOS
# ==========================================

lenguajes.append("SQL")

print("\nDespués de append():")
print(lenguajes)


# ==========================================
# INSERTAR EN UNA POSICIÓN
# ==========================================

lenguajes.insert(1, "HTML")

print("\nDespués de insert():")
print(lenguajes)


# ==========================================
# ELIMINAR ELEMENTOS
# ==========================================

lenguajes.remove("Java")

print("\nDespués de remove():")
print(lenguajes)


# ==========================================
# ELIMINAR POR ÍNDICE
# ==========================================

lenguajes.pop(0)

print("\nDespués de pop():")
print(lenguajes)


# ==========================================
# COMPROBAR SI EXISTE UN ELEMENTO
# ==========================================

if "Python" in lenguajes:
    print("\nPython está en la lista.")
else:
    print("\nPython no está en la lista.")


# ==========================================
# RECORRER UNA LISTA
# ==========================================

print("\nLenguajes disponibles:")

for lenguaje in lenguajes:
    print("-", lenguaje)


# ==========================================
# LISTA DE NÚMEROS
# ==========================================

numeros = [10, 20, 30, 40, 50]

print("\nNúmeros:")

for numero in numeros:
    print(numero)


# ==========================================
# SUMAR ELEMENTOS
# ==========================================

total = sum(numeros)

print("\nSuma total:", total)


# ==========================================
# VALOR MÍNIMO Y MÁXIMO
# ==========================================

print("Valor mínimo:", min(numeros))
print("Valor máximo:", max(numeros))


# ==========================================
# ORDENAR UNA LISTA
# ==========================================

numeros.sort()

print("\nLista ordenada:")
print(numeros)


# ==========================================
# SLICING
# Obtener una parte de la lista
# ==========================================

lenguajes = [
    "Python",
    "PHP",
    "JavaScript",
    "Java",
    "C#"
]

print("\nPrimeros tres lenguajes:")
print(lenguajes[0:3])

print("\nDesde el segundo elemento:")
print(lenguajes[1:])


# ==========================================
# LISTA CON INPUT()
# ==========================================

nombre1 = input("\nIngresa un nombre: ")
nombre2 = input("Ingresa otro nombre: ")

nombres = [nombre1, nombre2]

print("\nNombres ingresados:")

for nombre in nombres:
    print("-", nombre)