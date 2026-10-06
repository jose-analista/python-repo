# ==========================================
# OPERADORES ARITMÉTICOS EN PYTHON
# ==========================================

numero1 = 20
numero2 = 6


# ==========================================
# SUMA
# ==========================================

suma = numero1 + numero2

print("Suma:", suma)


# ==========================================
# RESTA
# ==========================================

resta = numero1 - numero2

print("Resta:", resta)


# ==========================================
# MULTIPLICACIÓN
# ==========================================

multiplicacion = numero1 * numero2

print("Multiplicación:", multiplicacion)


# ==========================================
# DIVISIÓN
# ==========================================

division = numero1 / numero2

print("División:", division)


# ==========================================
# DIVISIÓN ENTERA
# ==========================================

division_entera = numero1 // numero2

print("División entera:", division_entera)


# ==========================================
# MÓDULO (%)
# Obtiene el resto de una división
# ==========================================

resto = numero1 % numero2

print("Resto:", resto)


# ==========================================
# POTENCIA
# ==========================================

potencia = numero1 ** 2

print("Potencia:", potencia)


# ==========================================
# OPERACIONES COMBINADAS
# ==========================================

resultado = (numero1 + numero2) * 2

print("Resultado combinado:", resultado)


# ==========================================
# USANDO INPUT()
# ==========================================

numero_a = float(input("\nIngresa un número: "))
numero_b = float(input("Ingresa otro número: "))

print("\nResultados:")

print("Suma:", numero_a + numero_b)
print("Resta:", numero_a - numero_b)
print("Multiplicación:", numero_a * numero_b)

# Evitamos dividir por cero
if numero_b != 0:
    print("División:", numero_a / numero_b)
    print("División entera:", numero_a // numero_b)
    print("Resto:", numero_a % numero_b)
else:
    print("No se puede dividir por cero.")