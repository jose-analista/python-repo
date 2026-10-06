# ==========================================
# CONDICIONALES EN PYTHON
# ==========================================

edad = 25


# ==========================================
# IF
# ==========================================

if edad >= 18:
    print("Eres mayor de edad.")


# ==========================================
# IF / ELSE
# ==========================================

if edad >= 18:
    print("Puedes acceder.")
else:
    print("No puedes acceder.")


# ==========================================
# IF / ELIF / ELSE
# ==========================================

nota = 75

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
elif nota >= 60:
    print("Suficiente")
else:
    print("Reprobado")


# ==========================================
# OPERADORES DE COMPARACIÓN
# ==========================================

numero1 = 10
numero2 = 20

print("\nComparaciones:")

print("¿Son iguales?:", numero1 == numero2)
print("¿Son diferentes?:", numero1 != numero2)
print("¿Es mayor?:", numero1 > numero2)
print("¿Es menor?:", numero1 < numero2)
print("¿Es mayor o igual?:", numero1 >= numero2)
print("¿Es menor o igual?:", numero1 <= numero2)


# ==========================================
# COMPARAR VARIABLES
# ==========================================

usuario = "Jose"
usuario_registrado = "Jose"

if usuario == usuario_registrado:
    print("\nUsuario correcto.")
else:
    print("\nUsuario incorrecto.")


# ==========================================
# CONDICIONES CON INPUT()
# ==========================================

edad_usuario = int(input("\nIngresa tu edad: "))

if edad_usuario < 0:
    print("La edad no puede ser negativa.")

elif edad_usuario < 18:
    print("Eres menor de edad.")

elif edad_usuario == 18:
    print("Tienes exactamente 18 años.")

else:
    print("Eres mayor de edad.")


# ==========================================
# COMPARAR NÚMEROS
# ==========================================

numero = float(input("\nIngresa un número: "))

if numero > 0:
    print("El número es positivo.")

elif numero < 0:
    print("El número es negativo.")

else:
    print("El número es cero.")