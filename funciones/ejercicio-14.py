# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: funciones/ejercicio-14.py


# Create a decorator 'show_arguments' that prints the arguments passed to a function before executing it.


def show_arguments(func):
    # 👉 Your code here
    pass

@show_arguments
def say_hello(*args, **kwargs):
    for name in args:
        print(f"Hello {name}!")
    for key, value in kwargs.items():
        for _ in range(value):
            print(f"Hello {key}!")

say_hello("Ana", "Benito", Carlos=2, Diana=3)