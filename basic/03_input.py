# ==========================================
# RECIBIR DATOS DEL USUARIO
# ==========================================

# input() permite recibir información desde el teclado.
nombre = input("¿Cuál es tu nombre?: ")

print("Hola,", nombre)


# ==========================================
# INPUT SIEMPRE DEVUELVE TEXTO (str)
# ==========================================

edad = input("¿Cuál es tu edad?: ")

print("Tu edad es:", edad)
print("Tipo de dato:", type(edad))


# ==========================================
# CONVERTIR TEXTO A ENTERO
# ==========================================

edad = int(input("Ingresa nuevamente tu edad: "))

print("El próximo año tendrás:", edad + 1)


# ==========================================
# RECIBIR UN NÚMERO DECIMAL
# ==========================================

salario = float(input("¿Cuál es tu salario esperado?: "))

print("Salario ingresado:", salario)


# ==========================================
# OPERACIONES CON DATOS INGRESADOS
# ==========================================

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

suma = numero1 + numero2

print("Resultado:", suma)