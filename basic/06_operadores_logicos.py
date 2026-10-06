# ==========================================
# OPERADORES LÓGICOS EN PYTHON
# ==========================================

# and
# Ambas condiciones deben ser verdaderas.

edad = 25
tiene_documento = True

if edad >= 18 and tiene_documento:
    print("Puede ingresar.")
else:
    print("No puede ingresar.")


# ==========================================
# OR
# ==========================================

# or
# Al menos una condición debe ser verdadera.

tiene_efectivo = False
tiene_tarjeta = True

if tiene_efectivo or tiene_tarjeta:
    print("\nPuede realizar el pago.")
else:
    print("\nNo puede realizar el pago.")


# ==========================================
# NOT
# ==========================================

# not invierte el resultado de una condición.

usuario_bloqueado = False

if not usuario_bloqueado:
    print("\nEl usuario puede acceder.")
else:
    print("\nEl usuario está bloqueado.")


# ==========================================
# COMBINAR AND, OR Y NOT
# ==========================================

edad = 25
tiene_experiencia = True
esta_estudiando = False

if edad >= 18 and tiene_experiencia:
    print("\nCumple los requisitos principales.")

if edad >= 18 and (tiene_experiencia or esta_estudiando):
    print("Puede postular al puesto.")


# ==========================================
# EJEMPLO CON INPUT()
# ==========================================

edad_usuario = int(input("\nIngresa tu edad: "))

tiene_cedula = input(
    "¿Tienes cédula vigente? (si/no): "
).lower()

tiene_cedula = tiene_cedula == "si"


if edad_usuario >= 18 and tiene_cedula:
    print("Puedes realizar el trámite.")

else:
    print("No cumples todos los requisitos.")


# ==========================================
# EJEMPLO CON OR
# ==========================================

dia = input(
    "\nIngresa el día de la semana: "
).lower()

if dia == "sábado" or dia == "domingo":
    print("Es fin de semana.")

else:
    print("Es un día laboral.")


# ==========================================
# EJEMPLO CON NOT
# ==========================================

esta_matriculado = True

if not esta_matriculado:
    print("\nEl usuario no está matriculado.")

else:
    print("\nEl usuario está matriculado.")