# ==========================================
# VARIABLES Y TIPOS DE DATOS EN PYTHON
# ==========================================

# String (texto)
nombre = "José"
profesion = "Analista Programador"

# Integer (número entero)
edad = 25
experiencia = 2

# Float (número decimal)
altura = 1.75
salario_esperado = 750000.50

# Boolean (verdadero / falso)
trabajando = False
buscando_empleo = True


# ==========================================
# MOSTRAR VARIABLES
# ==========================================

print("Nombre:", nombre)
print("Profesión:", profesion)
print("Edad:", edad)
print("Experiencia:", experiencia, "años")
print("Altura:", altura)
print("Salario esperado:", salario_esperado)
print("¿Está trabajando?:", trabajando)
print("¿Está buscando empleo?:", buscando_empleo)


# ==========================================
# COMPROBAR TIPOS DE DATOS
# ==========================================

print("\nTipos de datos:")

print(type(nombre))
print(type(edad))
print(type(altura))
print(type(trabajando))


# ==========================================
# OPERACIONES CON VARIABLES
# ==========================================

edad_futura = edad + 1
experiencia_futura = experiencia + 1

print("\nDentro de un año:")
print("Edad:", edad_futura)
print("Experiencia:", experiencia_futura)


# ==========================================
# CAMBIAR EL VALOR DE UNA VARIABLE
# ==========================================

estado = "Buscando trabajo"

print("\nEstado inicial:", estado)

estado = "Trabajando"

print("Estado actualizado:", estado)