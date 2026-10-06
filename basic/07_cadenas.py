# ==========================================
# CADENAS DE TEXTO EN PYTHON
# ==========================================

nombre = "José"
profesion = "Analista Programador"

print(nombre)
print(profesion)


# ==========================================
# LONGITUD DE UNA CADENA
# ==========================================

print("\nLongitud del nombre:")

longitud = len(nombre)

print(longitud)


# ==========================================
# CONVERTIR A MAYÚSCULAS
# ==========================================

print("\nMayúsculas:")

print(nombre.upper())


# ==========================================
# CONVERTIR A MINÚSCULAS
# ==========================================

print("\nMinúsculas:")

print(nombre.lower())


# ==========================================
# ELIMINAR ESPACIOS AL PRINCIPIO Y AL FINAL
# ==========================================

texto = "   Hola Python   "

print("\nTexto original:")
print(texto)

print("Texto sin espacios:")
print(texto.strip())


# ==========================================
# REEMPLAZAR TEXTO
# ==========================================

mensaje = "Me gusta Java"

nuevo_mensaje = mensaje.replace("Java", "Python")

print("\nMensaje original:")
print(mensaje)

print("Mensaje modificado:")
print(nuevo_mensaje)


# ==========================================
# COMPROBAR SI UN TEXTO ESTÁ DENTRO DE OTRO
# ==========================================

lenguaje = "Python"

if "Python" in lenguaje:
    print("\nPython está presente.")


# ==========================================
# CONCATENAR TEXTOS
# ==========================================

nombre = "José"
apellido = "Calderón"

nombre_completo = nombre + " " + apellido

print("\nNombre completo:")
print(nombre_completo)


# ==========================================
# F-STRINGS
# ==========================================

edad = 25
profesion = "Analista Programador"

mensaje = f"Mi nombre es {nombre_completo}, tengo {edad} años y soy {profesion}."

print("\nF-string:")
print(mensaje)


# ==========================================
# TRABAJAR CON INPUT()
# ==========================================

nombre_usuario = input("\nIngresa tu nombre: ")

nombre_usuario = nombre_usuario.strip()

print(f"Hola, {nombre_usuario}.")


# ==========================================
# COMPROBAR EL CONTENIDO DE UN TEXTO
# ==========================================

correo = input("Ingresa tu correo: ")

if "@" in correo:
    print("El correo contiene @.")
else:
    print("El correo no parece válido.")


# ==========================================
# CONTAR APARICIONES
# ==========================================

texto = "Python es fácil. Python es potente."

cantidad = texto.count("Python")

print("\nLa palabra Python aparece:", cantidad, "veces.")


# ==========================================
# ENCONTRAR LA POSICIÓN DE UN TEXTO
# ==========================================

texto = "Aprendiendo Python"

posicion = texto.find("Python")

print("\nPython comienza en la posición:", posicion)