# ==========================================
# CLASES Y OBJETOS EN PYTHON
# ==========================================


# ==========================================
# ¿QUÉ ES UNA CLASE?
# ==========================================

# Una clase es un molde para crear objetos.
#
# Una clase define:
#
# - atributos → los datos del objeto
# - métodos   → las acciones del objeto
#
# Ejemplo: la clase Persona es el molde y
# "José" y "Ana" son objetos creados con él.


# ==========================================
# PRIMERA CLASE
# ==========================================

class Persona:

    def __init__(self, nombre, edad):

        self.nombre = nombre
        self.edad = edad

    def saludar(self):

        print(f"Hola, soy {self.nombre}.")


# ==========================================
# CREAR OBJETOS (INSTANCIAS)
# ==========================================

persona1 = Persona("José", 25)
persona2 = Persona("Ana", 28)

print("Nombre:", persona1.nombre)
print("Edad:", persona1.edad)

print("\nSegunda persona:")
print(persona2.nombre, "-", persona2.edad)


# ==========================================
# LLAMAR MÉTODOS
# ==========================================

print()

persona1.saludar()
persona2.saludar()


# ==========================================
# __INIT__ Y SELF
# ==========================================

# __init__ es el constructor: se ejecuta
# automáticamente al crear el objeto.
#
# self representa al objeto actual.
# Con self.nombre = nombre guardas el dato
# dentro del objeto.
#
# Python pasa self automáticamente:
# persona1.saludar() equivale a
# Persona.saludar(persona1)


# ==========================================
# MODIFICAR ATRIBUTOS
# ==========================================

persona1.edad = 26

print("\nNueva edad de José:", persona1.edad)


# ==========================================
# AGREGAR ATRIBUTOS DESDE FUERA
# ==========================================

# Python lo permite, aunque no es lo más
# recomendable. Es mejor definirlos en __init__.

persona1.ciudad = "Santiago"

print("Ciudad:", persona1.ciudad)


# ==========================================
# MÉTODOS CON PARÁMETROS Y RETORNO
# ==========================================

class Rectangulo:

    def __init__(self, base, altura):

        self.base = base
        self.altura = altura

    def area(self):

        return self.base * self.altura

    def perimetro(self):

        return 2 * (self.base + self.altura)


rectangulo = Rectangulo(5, 3)

print("\nÁrea:", rectangulo.area())
print("Perímetro:", rectangulo.perimetro())


# ==========================================
# VALORES POR DEFECTO
# ==========================================

class Usuario:

    def __init__(self, nombre, rol="invitado"):

        self.nombre = nombre
        self.rol = rol


usuario1 = Usuario("Pedro")
usuario2 = Usuario("Laura", "admin")

print("\nUsuarios:")
print(usuario1.nombre, "-", usuario1.rol)
print(usuario2.nombre, "-", usuario2.rol)


# ==========================================
# ATRIBUTOS DE CLASE
# ==========================================

# Un atributo de clase es compartido por
# TODOS los objetos de esa clase.

class Perro:

    especie = "Canis familiaris"

    def __init__(self, nombre):

        self.nombre = nombre


perro1 = Perro("Firulais")
perro2 = Perro("Rex")

print("\nEspecie:")
print(perro1.especie)
print(perro2.especie)


# ==========================================
# CONTADOR DE OBJETOS
# ==========================================

class Producto:

    total = 0

    def __init__(self, nombre, precio):

        self.nombre = nombre
        self.precio = precio

        Producto.total += 1


Producto("Mouse", 8000)
Producto("Teclado", 15000)
Producto("Monitor", 90000)

print("\nProductos creados:", Producto.total)


# ==========================================
# OBJETOS EN UNA LISTA
# ==========================================

personas = [

    Persona("José", 25),
    Persona("Ana", 28),
    Persona("Pedro", 30)

]

print("\nPersonas:")

for persona in personas:

    print(persona.nombre, "-", persona.edad)


# ==========================================
# BUSCAR EN UNA LISTA DE OBJETOS
# ==========================================

mayores = [

    persona.nombre
    for persona in personas
    if persona.edad >= 28

]

print("\nMayores o iguales a 28:")
print(mayores)


# ==========================================
# MÉTODOS QUE MODIFICAN EL OBJETO
# ==========================================

class Contador:

    def __init__(self):

        self.valor = 0

    def incrementar(self):

        self.valor += 1

    def reiniciar(self):

        self.valor = 0


contador = Contador()

contador.incrementar()
contador.incrementar()
contador.incrementar()

print("\nContador:", contador.valor)

contador.reiniciar()

print("Después de reiniciar:", contador.valor)


# ==========================================
# EJEMPLO PRÁCTICO:
# CUENTA BANCARIA
# ==========================================

class CuentaBancaria:

    def __init__(self, titular, saldo=0):

        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):

        if monto <= 0:

            raise ValueError(
                "El monto debe ser mayor a cero."
            )

        self.saldo += monto

    def retirar(self, monto):

        if monto > self.saldo:

            raise ValueError("Saldo insuficiente.")

        self.saldo -= monto

    def mostrar(self):

        print(f"{self.titular}: ${self.saldo}")


cuenta = CuentaBancaria("José", 10000)

cuenta.depositar(5000)
cuenta.mostrar()

try:

    cuenta.retirar(50000)

except ValueError as error:

    print("\nError:")
    print(error)

cuenta.retirar(3000)
cuenta.mostrar()


# ==========================================
# EJEMPLO PRÁCTICO:
# INVENTARIO
# ==========================================

class Inventario:

    def __init__(self):

        self.productos = []

    def agregar(self, nombre, precio):

        self.productos.append({

            "nombre": nombre,
            "precio": precio

        })

    def total(self):

        return sum(
            producto["precio"]
            for producto in self.productos
        )

    def listar(self):

        for producto in self.productos:

            print(
                producto["nombre"],
                "-",
                producto["precio"]
            )


inventario = Inventario()

inventario.agregar("Mouse", 8000)
inventario.agregar("Teclado", 15000)

print("\nInventario:")
inventario.listar()

print("Total:", inventario.total())