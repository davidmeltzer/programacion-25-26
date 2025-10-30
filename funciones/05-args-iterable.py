# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: funciones/05-args-iterable.py


# from collections.abc import Iterable

# def f(*args: Iterable) -> None:
def f(*args):
    print(f"type(args) = {type(args)}, valor = {args}")
    for elemento in args:
        print(f"- {elemento} ({type(elemento)})")


f()
f(1)
f(1, 2)
f(1, 2, 3)
f(1, 'hola', 3+4j)