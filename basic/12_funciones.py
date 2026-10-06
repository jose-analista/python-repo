# ==========================================
# FUNCIONES EN PYTHON
# ==========================================

# Una función es un bloque de código que podemos
# reutilizar varias veces.

def saludar():
    print("Hola, bienvenido a Python.")


# ==========================================
# LLAMAR A UNA FUNCIÓN
# ==========================================

saludar()
saludar()


# ==========================================
# FUNCIÓN CON PARÁMETRO
# ==========================================

def saludar_persona(nombre):
    print("Hola", nombre)


saludar_persona("José")
saludar_persona("Pedro")
saludar_persona("Ana")


# ==========================================
# VARIOS PARÁMETROS
# ==========================================

def presentar_persona(nombre, edad):
    print("Nombre:", nombre)
    print("Edad:", edad)


presentar_persona("José", 25)


# ==========================================
# FUNCIÓN CON RETURN
# ==========================================

def sumar(a, b):

    resultado = a + b

    return resultado


resultado = sumar(10, 20)

print("\nResultado de la suma:")
print(resultado)


# ==========================================
# RETURN DIRECTAMENTE
# ==========================================

def restar(a, b):
    return a - b


resultado = restar(30, 10)

print("\nResultado de la resta:")
print(resultado)


# ==========================================
# MULTIPLICAR
# ==========================================

def multiplicar(a, b):
    return a * b


resultado = multiplicar(5, 4)

print("\nResultado de la multiplicación:")
print(resultado)


# ==========================================
# DIVIDIR
# ==========================================

def dividir(a, b):

    if b == 0:
        return None

    return a / b


resultado = dividir(20, 5)

print("\nResultado de la división:")
print(resultado)


# ==========================================
# PARÁMETRO CON VALOR POR DEFECTO
# ==========================================

def saludar_usuario(nombre="Usuario"):
    print("Hola", nombre)


saludar_usuario("José")

saludar_usuario()


# ==========================================
# VARIOS PARÁMETROS CON VALORES POR DEFECTO
# ==========================================

def crear_usuario(nombre, edad=18, activo=True):

    print("\nUsuario:")
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Activo:", activo)


crear_usuario("José")

crear_usuario("Pedro", 30)

crear_usuario("Ana", 25, False)


# ==========================================
# ARGUMENTOS POR NOMBRE
# ==========================================

def registrar_persona(nombre, edad, ciudad):

    print("\nPersona registrada:")
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Ciudad:", ciudad)


registrar_persona(
    nombre="José",
    edad=25,
    ciudad="Santiago"
)


# ==========================================
# FUNCIÓN QUE TRABAJA CON UNA LISTA
# ==========================================

def mostrar_lenguajes(lenguajes):

    print("\nLenguajes:")

    for lenguaje in lenguajes:
        print("-", lenguaje)


lenguajes = [
    "Python",
    "PHP",
    "JavaScript",
    "Java"
]

mostrar_lenguajes(lenguajes)


# ==========================================
# FUNCIÓN QUE CALCULA EL PROMEDIO
# ==========================================

def calcular_promedio(numeros):

    total = sum(numeros)

    cantidad = len(numeros)

    return total / cantidad


notas = [5.5, 6.0, 4.8, 6.5]

promedio = calcular_promedio(notas)

print("\nPromedio:")
print(promedio)


# ==========================================
# FUNCIÓN QUE COMPRUEBA LA EDAD
# ==========================================

def puede_ingresar(edad):

    if edad >= 18:
        return True

    return False


edad = 25

if puede_ingresar(edad):
    print("\nPuede ingresar.")
else:
    print("\nNo puede ingresar.")


# ==========================================
# FUNCIÓN QUE DEVUELVE UN DICCIONARIO
# ==========================================

def crear_persona(nombre, edad, profesion):

    persona = {
        "nombre": nombre,
        "edad": edad,
        "profesion": profesion
    }

    return persona


persona = crear_persona(
    "José",
    25,
    "Analista Programador"
)

print("\nPersona creada:")
print(persona)


# ==========================================
# FUNCIÓN PARA BUSCAR EN UNA LISTA
# ==========================================

def buscar_lenguaje(lenguajes, lenguaje_buscado):

    if lenguaje_buscado in lenguajes:
        return True

    return False


lenguajes = [
    "Python",
    "PHP",
    "JavaScript"
]

if buscar_lenguaje(lenguajes, "Python"):
    print("\nPython está disponible.")

if not buscar_lenguaje(lenguajes, "C++"):
    print("C++ no está disponible.")


# ==========================================
# FUNCIÓN CON CÁLCULO
# ==========================================

def calcular_precio_final(precio, descuento):

    monto_descuento = precio * descuento / 100

    precio_final = precio - monto_descuento

    return precio_final


precio = 100000
descuento = 20

precio_final = calcular_precio_final(
    precio,
    descuento
)

print("\nPrecio original:")
print(precio)

print("Descuento:")
print(descuento, "%")

print("Precio final:")
print(precio_final)