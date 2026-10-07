# ==========================================
# HERENCIA Y MÁS DE POO EN PYTHON
# ==========================================


# ==========================================
# ¿QUÉ ES LA HERENCIA?
# ==========================================

# La herencia permite crear una clase nueva
# a partir de otra, reutilizando su código.
#
# - Clase padre (base): la original
# - Clase hija (derivada): hereda del padre


# ==========================================
# HERENCIA BÁSICA
# ==========================================

class Animal:

    def __init__(self, nombre):

        self.nombre = nombre

    def comer(self):

        print(f"{self.nombre} está comiendo.")


class Perro(Animal):

    def ladrar(self):

        print(f"{self.nombre} dice: ¡Guau!")


perro = Perro("Rex")

# Método heredado de Animal
perro.comer()

# Método propio de Perro
perro.ladrar()


# ==========================================
# SUPER()
# ==========================================

# super() permite usar el código de la
# clase padre, por ejemplo su __init__.

class Persona:

    def __init__(self, nombre, edad):

        self.nombre = nombre
        self.edad = edad

    def presentarse(self):

        print(f"Soy {self.nombre} y tengo {self.edad} años.")


class Empleado(Persona):

    def __init__(self, nombre, edad, sueldo):

        super().__init__(nombre, edad)

        self.sueldo = sueldo


empleado = Empleado("José", 25, 900000)

print()

empleado.presentarse()

print("Sueldo:", empleado.sueldo)


# ==========================================
# SOBRESCRIBIR MÉTODOS (OVERRIDE)
# ==========================================

# La clase hija puede redefinir un método
# del padre.

class Gato(Animal):

    def comer(self):

        print(f"{self.nombre} come pescado.")


gato = Gato("Michi")

print()

gato.comer()


# ==========================================
# EXTENDER UN MÉTODO CON SUPER()
# ==========================================

class Gerente(Empleado):

    def presentarse(self):

        super().presentarse()

        print("Soy gerente.")


gerente = Gerente("Laura", 40, 2500000)

print()

gerente.presentarse()


# ==========================================
# POLIMORFISMO
# ==========================================

# Objetos distintos responden al mismo
# método de forma diferente.

class Figura:

    def area(self):

        return 0


class Cuadrado(Figura):

    def __init__(self, lado):

        self.lado = lado

    def area(self):

        return self.lado ** 2


class Circulo(Figura):

    def __init__(self, radio):

        self.radio = radio

    def area(self):

        return 3.1416 * self.radio ** 2


figuras = [

    Cuadrado(4),
    Circulo(2)

]

print("\nÁreas:")

for figura in figuras:

    print(type(figura).__name__, "-", figura.area())


# ==========================================
# ISINSTANCE() E ISSUBCLASS()
# ==========================================

print("\n¿perro es Perro?")
print(isinstance(perro, Perro))

print("\n¿perro es Animal?")
print(isinstance(perro, Animal))

print("\n¿perro es Gato?")
print(isinstance(perro, Gato))

print("\n¿Perro hereda de Animal?")
print(issubclass(Perro, Animal))


# ==========================================
# __STR__
# ==========================================

# Sin __str__, print(objeto) muestra algo
# poco útil como <__main__.Libro object at ...>

class Libro:

    def __init__(self, titulo, autor):

        self.titulo = titulo
        self.autor = autor

    def __str__(self):

        return f"{self.titulo} - {self.autor}"


libro = Libro("El principito", "Antoine de Saint-Exupéry")

print("\nLibro:")
print(libro)


# ==========================================
# __REPR__
# ==========================================

# __str__  → texto para el usuario
# __repr__ → texto para el programador
#            (se ve en listas y depuración)

class Punto:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __repr__(self):

        return f"Punto({self.x}, {self.y})"


puntos = [Punto(1, 2), Punto(3, 4)]

print("\nPuntos:")
print(puntos)


# ==========================================
# ENCAPSULACIÓN
# ==========================================

# En Python se usa una convención:
#
# nombre     → público
# _nombre    → "protegido" (uso interno, por convención)
# __nombre   → "privado" (Python cambia su nombre)

class Cuenta:

    def __init__(self, titular, saldo):

        self.titular = titular
        self._saldo = saldo
        self.__clave = "1234"

    def ver_saldo(self):

        return self._saldo

    def validar_clave(self, clave):

        return clave == self.__clave


cuenta = Cuenta("José", 10000)

print("\nSaldo:", cuenta.ver_saldo())

print("Clave correcta:", cuenta.validar_clave("1234"))

try:

    print(cuenta.__clave)

except AttributeError:

    print("No se puede acceder directamente a __clave.")


# ==========================================
# PROPERTY
# ==========================================

# @property permite usar un método como si
# fuera un atributo, y validar al asignar.

class Persona2:

    def __init__(self, nombre, edad):

        self.nombre = nombre
        self.edad = edad

    @property
    def edad(self):

        return self._edad

    @edad.setter
    def edad(self, valor):

        if valor < 0:

            raise ValueError(
                "La edad no puede ser negativa."
            )

        self._edad = valor


p = Persona2("José", 25)

print("\nEdad:", p.edad)

p.edad = 26

print("Nueva edad:", p.edad)

try:

    p.edad = -5

except ValueError as error:

    print("Error:", error)


# ==========================================
# MÉTODOS ESTÁTICOS Y DE CLASE
# ==========================================

class Matematica:

    @staticmethod
    def sumar(a, b):

        return a + b


class Usuario:

    total = 0

    def __init__(self, nombre):

        self.nombre = nombre
        Usuario.total += 1

    @classmethod
    def cantidad(cls):

        return cls.total


print("\nSuma:", Matematica.sumar(3, 4))

Usuario("José")
Usuario("Ana")

print("Usuarios:", Usuario.cantidad())


# ==========================================
# COMPOSICIÓN
# ==========================================

# A veces es mejor que un objeto TENGA otro
# objeto (composición) en vez de HEREDAR.
#
# Un Auto tiene un Motor. No es un Motor.

class Motor:

    def encender(self):

        print("Motor encendido.")


class Auto:

    def __init__(self, marca):

        self.marca = marca
        self.motor = Motor()

    def arrancar(self):

        print(f"Arrancando {self.marca}...")

        self.motor.encender()


auto = Auto("Toyota")

print()

auto.arrancar()


# ==========================================
# EJEMPLO PRÁCTICO:
# EMPLEADOS CON DISTINTOS BONOS
# ==========================================

class Trabajador:

    def __init__(self, nombre, sueldo_base):

        self.nombre = nombre
        self.sueldo_base = sueldo_base

    def sueldo_final(self):

        return self.sueldo_base

    def __str__(self):

        return f"{self.nombre}: ${self.sueldo_final()}"


class Programador(Trabajador):

    def sueldo_final(self):

        return self.sueldo_base + 100000


class Vendedor(Trabajador):

    def __init__(self, nombre, sueldo_base, ventas):

        super().__init__(nombre, sueldo_base)

        self.ventas = ventas

    def sueldo_final(self):

        return self.sueldo_base + self.ventas * 0.1


equipo = [

    Trabajador("Pedro", 600000),
    Programador("José", 900000),
    Vendedor("Ana", 500000, 2000000)

]

print("\nSueldos:")

for trabajador in equipo:

    print(trabajador)