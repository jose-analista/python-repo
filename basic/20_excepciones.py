# ==========================================
# EXCEPCIONES EN PYTHON
# ==========================================


# ==========================================
# ¿QUÉ ES UNA EXCEPCIÓN?
# ==========================================

# Una excepción es un error que ocurre
# mientras el programa está ejecutándose.


# ==========================================
# ERROR BÁSICO
# ==========================================

# Este código produciría un error:

# numero = 10 / 0

# Error:
# ZeroDivisionError


# ==========================================
# TRY / EXCEPT
# ==========================================

try:

    numero = 10 / 0

except ZeroDivisionError:

    print("No se puede dividir por cero.")


# ==========================================
# EJEMPLO CON INPUT
# ==========================================

try:

    edad = int(input("\nIngresa tu edad: "))

    print("Tu edad es:", edad)

except ValueError:

    print("Debes ingresar un número.")


# ==========================================
# VARIOS TIPOS DE ERRORES
# ==========================================

try:

    numero = int(input("\nIngresa un número: "))

    resultado = 100 / numero

    print("Resultado:", resultado)

except ValueError:

    print("Debes ingresar un número válido.")

except ZeroDivisionError:

    print("No puedes dividir por cero.")


# ==========================================
# EXCEPTION
# ==========================================

try:

    numero = int(input("\nIngresa otro número: "))

    resultado = 100 / numero

    print("Resultado:", resultado)

except Exception as error:

    print("Ocurrió un error:")
    print(error)


# ==========================================
# ELSE
# ==========================================

try:

    numero = int(input("\nIngresa un número: "))

except ValueError:

    print("Número inválido.")

else:

    print("Número válido:")
    print(numero)


# ==========================================
# TRY + EXCEPT + ELSE
# ==========================================

try:

    numero = int(input("\nIngresa un número: "))

    resultado = 100 / numero

except ValueError:

    print("Debes ingresar un número.")

except ZeroDivisionError:

    print("No puedes dividir por cero.")

else:

    print("La operación fue exitosa.")
    print("Resultado:", resultado)


# ==========================================
# FINALLY
# ==========================================

try:

    numero = int(input("\nIngresa un número: "))

    print("Número:", numero)

except ValueError:

    print("Entrada inválida.")

finally:

    print("Este bloque siempre se ejecuta.")


# ==========================================
# EJEMPLO CON ARCHIVOS
# ==========================================

try:

    archivo = open(
        "archivo.txt",
        "r"
    )

    contenido = archivo.read()

    print("\nContenido:")
    print(contenido)

    archivo.close()

except FileNotFoundError:

    print("\nEl archivo no existe.")


# ==========================================
# VARIOS ERRORES
# ==========================================

try:

    numero = int("abc")

except (ValueError, TypeError):

    print("\nEl valor no puede convertirse.")


# ==========================================
# RAISE
# ==========================================

edad = 15

try:

    if edad < 18:

        raise ValueError(
            "La persona debe ser mayor de edad."
        )

except ValueError as error:

    print("\nError:")
    print(error)


# ==========================================
# FUNCIÓN CON EXCEPCIONES
# ==========================================

def dividir(a, b):

    try:

        return a / b

    except ZeroDivisionError:

        return "No se puede dividir por cero."


print("\nDivisión:")

print(dividir(10, 2))

print(dividir(10, 0))


# ==========================================
# FUNCIÓN CON VALIDACIÓN
# ==========================================

def validar_edad(edad):

    if edad < 0:

        raise ValueError(
            "La edad no puede ser negativa."
        )

    if edad < 18:

        return False

    return True


try:

    resultado = validar_edad(25)

    print("\n¿Es mayor de edad?")
    print(resultado)

except ValueError as error:

    print("Error:")
    print(error)


# ==========================================
# DICCIONARIO + EXCEPCIONES
# ==========================================

usuario = {

    "nombre": "José",
    "edad": 25

}

try:

    nombre = usuario["nombre"]

    telefono = usuario["telefono"]

except KeyError:

    print("\nEl dato solicitado no existe.")

else:

    print(nombre)
    print(telefono)


# ==========================================
# GET() COMO ALTERNATIVA
# ==========================================

telefono = usuario.get(
    "telefono",
    "No registrado"
)

print("\nTeléfono:")
print(telefono)


# ==========================================
# EJEMPLO PRÁCTICO:
# DATOS DE UNA API
# ==========================================

respuesta_api = {

    "success": True,

    "usuario": {

        "id": 1,
        "nombre": "José"

    }

}

try:

    usuario = respuesta_api["usuario"]

    nombre = usuario["nombre"]

    email = usuario["email"]

except KeyError:

    print("\nFalta información en la respuesta de la API.")

else:

    print("\nUsuario:")
    print(nombre)
    print(email)


# ==========================================
# EJEMPLO PRÁCTICO:
# PROCESAR USUARIOS
# ==========================================

usuarios = [

    {
        "nombre": "José",
        "edad": 25
    },

    {
        "nombre": "Pedro",
        "edad": 30
    },

    {
        "nombre": "Ana"
    }

]


for usuario in usuarios:

    try:

        nombre = usuario["nombre"]
        edad = usuario["edad"]

        print(
            nombre,
            "-",
            edad
        )

    except KeyError:

        print(
            "El usuario no tiene todos los datos."
        )