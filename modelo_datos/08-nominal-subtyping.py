# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: modelo_datos/08-nominal-subtyping.py


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def drink(self):
        print(f"{self.name} is drinking.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing.")

pluto = Dog("Pluto")
print(isinstance(pluto, Animal))

tom = Cat("Tom")
print(isinstance(tom, Animal))