# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: funciones/ejercicio-13.py


# Create a decorator 'twice' that runs the decorated function twice every time it’s called.


def twice(func):
    # 👉 Your code here
    pass

@twice
def say_hello(name):
    print(f"Hello {name}!")

say_hello("Pepe")