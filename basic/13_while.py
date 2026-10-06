# ==========================================
# CICLO WHILE EN PYTHON
# ==========================================

# while significa:
# "mientras se cumpla esta condición,
# ejecuta este código."

contador = 1

while contador <= 5:

    print("Contador:", contador)

    contador = contador + 1


# ==========================================
# CONTADOR
# ==========================================

numero = 1

while numero <= 10:

    print("\nNúmero:", numero)

    numero += 1


# ==========================================
# CUENTA REGRESIVA
# ==========================================

contador = 5

while contador >= 1:

    print("\nCuenta:", contador)

    contador -= 1

print("\n¡Despegue!")


# ==========================================
# WHILE CON CONDICIÓN
# ==========================================

edad = 15

while edad < 18:

    print("\nEdad actual:", edad)

    edad += 1

print("\nAhora tienes 18 años.")


# ==========================================
# RECORRER UNA LISTA CON WHILE
# ==========================================

lenguajes = [
    "Python",
    "PHP",
    "JavaScript",
    "Java"
]

indice = 0

while indice < len(lenguajes):

    print("\nLenguaje:", lenguajes[indice])

    indice += 1


# ==========================================
# SUMAR NÚMEROS
# ==========================================

numero = 1
total = 0

while numero <= 5:

    total = total + numero

    numero += 1

print("\nSuma total:")
print(total)


# ==========================================
# BREAK
# ==========================================

contador = 1

while contador <= 10:

    print("\nNúmero:", contador)

    if contador == 5:
        break

    contador += 1


# ==========================================
# CONTINUAR CON CONTINUE
# ==========================================

contador = 0

while contador < 10:

    contador += 1

    if contador == 5:
        continue

    print("\nNúmero:", contador)


# ==========================================
# WHILE CON BANDERA
# ==========================================

activo = True

contador = 1

while activo:

    print("\nProceso:", contador)

    if contador == 3:
        activo = False

    contador += 1


# ==========================================
# VALIDAR UN VALOR
# ==========================================

numero = 0

while numero <= 0:

    print("\nEl número debe ser mayor que 0.")

    numero = 5

print("\nNúmero válido:")
print(numero)


# ==========================================
# MENÚ
# ==========================================

opcion = 1

while opcion != 0:

    print("\n===== MENÚ =====")
    print("1. Ver perfil")
    print("2. Ver proyectos")
    print("3. Salir")

    opcion = 3

    if opcion == 1:

        print("Mostrando perfil.")

    elif opcion == 2:

        print("Mostrando proyectos.")

    elif opcion == 3:

        print("Saliendo...")
        opcion = 0

    else:

        print("Opción no válida.")


# ==========================================
# EJEMPLO PRÁCTICO
# ==========================================

intentos = 0
max_intentos = 3

while intentos < max_intentos:

    intentos += 1

    print("\nIntento:", intentos)

    if intentos == 3:
        print("Máximo de intentos alcanzado.")