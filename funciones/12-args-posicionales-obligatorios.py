# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: funciones/12-args-posicionales-obligatorios.py


def f(a, b, /, c):
    print(a, b, c)

f(1, 2, 3)
f(1, 2, c=3)
# f(a=1, 2, c=3)       # SyntaxError: argumento posicional después de un argumento con nombre
# f(1, b=2, c=3)       # TypeError
# f(a=1, b=2, c=3)     # TypeError

