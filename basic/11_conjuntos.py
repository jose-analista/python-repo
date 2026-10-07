# ==========================================
# CONJUNTOS (SETS) EN PYTHON
# ==========================================

# Un set almacena varios valores,
# pero NO permite elementos duplicados.

lenguajes = {"Python", "PHP", "JavaScript", "Java"}

print("Lenguajes:")
print(lenguajes)

# ==========================================
# LOS DUPLICADOS SE ELIMINAN
# ==========================================

lenguajes_repetidos = {
    "Python",
    "Python",
    "PHP",
    "Java",
    "PHP"
}

print("\nLenguajes con duplicados:")
print(lenguajes_repetidos)

# Python y PHP aparecerán una sola vez.

# ==========================================
# AGREGAR ELEMENTOS
# ==========================================

lenguajes.add("C++")

print("\nDespués de agregar C++:")
print(lenguajes)

# ==========================================
# AGREGAR UN ELEMENTO QUE YA EXISTE
# ==========================================

lenguajes.add("Python")

print("\nDespués de agregar Python nuevamente:")
print(lenguajes)

# No se crea un segundo Python.

# ==========================================
# ELIMINAR ELEMENTOS
# ==========================================

lenguajes.remove("Java")

print("\nDespués de eliminar Java:")
print(lenguajes)

# ==========================================
# DISCARD
# ==========================================

# discard() también elimina un elemento,
# pero no produce error si no existe.

lenguajes.discard("Ruby")

print("\nDespués de intentar eliminar Ruby:")
print(lenguajes)

# ==========================================
# COMPROBAR SI EXISTE UN ELEMENTO
# ==========================================

if "Python" in lenguajes:
    print("\nPython está en el conjunto.")

if "Ruby" not in lenguajes:
    print("Ruby no está en el conjunto.")

# ==========================================
# RECORRER UN SET
# ==========================================

print("\nLenguajes disponibles:")

for lenguaje in lenguajes:
    print("-", lenguaje)

# ==========================================
# CANTIDAD DE ELEMENTOS
# ==========================================

cantidad = len(lenguajes)

print("\nCantidad de lenguajes:")
print(cantidad)

# ==========================================
# CONJUNTO DE NÚMEROS
# ==========================================

numeros = {10, 20, 30, 40, 50}

print("\nNúmeros:")
print(numeros)

# ==========================================
# ELIMINAR DUPLICADOS DE UNA LISTA
# ==========================================

numeros_lista = [10, 20, 10, 30, 20, 40, 10]

print("\nLista original:")
print(numeros_lista)

numeros_unicos = set(numeros_lista)

print("\nConvertida a set:")
print(numeros_unicos)

# ==========================================
# CONVERTIR SET NUEVAMENTE A LISTA
# ==========================================

numeros_lista = list(numeros_unicos)

print("\nConvertida nuevamente a lista:")
print(numeros_lista)

# ==========================================
# UNION DE CONJUNTOS
# ==========================================

backend = {"Python", "PHP", "Java"}
frontend = {"JavaScript", "React", "HTML", "CSS"}

todos = backend.union(frontend)

print("\nTecnologías de backend:")
print(backend)

print("\nTecnologías de frontend:")
print(frontend)

print("\nTodas las tecnologías:")
print(todos)

# ==========================================
# INTERSECCIÓN
# ==========================================

lenguajes_a = {"Python", "Java", "PHP", "JavaScript"}
lenguajes_b = {"Python", "Java", "C++", "C#"}

comunes = lenguajes_a.intersection(lenguajes_b)

print("\nLenguajes del primer conjunto:")
print(lenguajes_a)

print("\nLenguajes del segundo conjunto:")
print(lenguajes_b)

print("\nLenguajes que tienen en común:")
print(comunes)

# ==========================================
# DIFERENCIA
# ==========================================

solo_a = lenguajes_a.difference(lenguajes_b)

print("\nLenguajes que están solamente en A:")
print(solo_a)

# ==========================================
# DIFERENCIA INVERSA
# ==========================================

solo_b = lenguajes_b.difference(lenguajes_a)

print("\nLenguajes que están solamente en B:")
print(solo_b)

# ==========================================
# SUBCONJUNTO
# ==========================================

backend = {"Python", "PHP"}

tecnologias = {
    "Python",
    "PHP",
    "JavaScript",
    "React",
    "Java"
}

if backend.issubset(tecnologias):
    print("\nBackend está contenido dentro de tecnologías.")

# ==========================================
# SUPERCONJUNTO
# ==========================================

if tecnologias.issuperset(backend):
    print("Tecnologías contiene todos los elementos de backend.")

# ==========================================
# EJEMPLO PRÁCTICO
# ==========================================

clientes_visitantes = {
    "José",
    "Pedro",
    "Ana",
    "Carlos"
}

clientes_registrados = {
    "José",
    "Ana",
    "Luis"
}

# Personas que visitaron pero no están registradas.

no_registrados = clientes_visitantes.difference(clientes_registrados)

print("\nVisitantes no registrados:")
print(no_registrados)

# Personas que están en ambos grupos.

registrados_visitantes = clientes_visitantes.intersection(
    clientes_registrados
)

print("\nRegistrados que también visitaron:")
print(registrados_visitantes)

# Todas las personas conocidas.

todas_personas = clientes_visitantes.union(clientes_registrados)

print("\nTodas las personas:")
print(todas_personas)