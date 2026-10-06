# ==========================================
# TUPLAS EN PYTHON
# ==========================================

# Una tupla permite almacenar varios valores,
# igual que una lista.

lenguajes = ("Python", "PHP", "JavaScript", "Java")

print("Lenguajes:")
print(lenguajes)

# ==========================================
# ACCEDER A ELEMENTOS
# ==========================================

print("\nPrimer lenguaje:")
print(lenguajes[0])

print("\nÚltimo lenguaje:")
print(lenguajes[-1])

# ==========================================
# LONGITUD DE UNA TUPLA
# ==========================================

cantidad = len(lenguajes)

print("\nCantidad de lenguajes:")
print(cantidad)

# ==========================================
# COMPROBAR SI EXISTE UN ELEMENTO
# ==========================================

if "Python" in lenguajes:
    print("\nPython está en la tupla.")

# ==========================================
# RECORRER UNA TUPLA
# ==========================================

print("\nLenguajes disponibles:")

for lenguaje in lenguajes:
    print("-", lenguaje)

# ==========================================
# UNA TUPLA NO SE PUEDE MODIFICAR
# ==========================================

# Esto produciría un error:
#
# lenguajes[0] = "Laravel"

# Las tuplas son INMUTABLES.
# Es decir, después de crearlas,
# no podemos cambiar sus elementos.

# ==========================================
# TUPLA DE NÚMEROS
# ==========================================

numeros = (10, 20, 30, 40, 50)

print("\nNúmeros:")
print(numeros)

print("Suma:", sum(numeros))
print("Mínimo:", min(numeros))
print("Máximo:", max(numeros))

# ==========================================
# SLICING
# ==========================================

print("\nPrimeros tres números:")
print(numeros[0:3])

print("\nDesde el segundo número:")
print(numeros[1:])

# ==========================================
# CONTAR ELEMENTOS
# ==========================================

numeros_repetidos = (10, 20, 10, 30, 10, 40)

cantidad_diez = numeros_repetidos.count(10)

print("\nCantidad de veces que aparece 10:")
print(cantidad_diez)

# ==========================================
# BUSCAR POSICIÓN
# ==========================================

posicion = numeros_repetidos.index(30)

print("\nPosición del número 30:")
print(posicion)

# ==========================================
# TUPLA CON DIFERENTES TIPOS DE DATOS
# ==========================================

persona = ("José", 25, "Analista Programador", True)

print("\nDatos de la persona:")
print(persona)

print("Nombre:", persona[0])
print("Edad:", persona[1])
print("Profesión:", persona[2])
print("¿Busca trabajo?:", persona[3])