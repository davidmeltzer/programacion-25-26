# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: funciones/13-args-kwargs-defaults.py


def f(a, /, b, c=3, *args, e=4, **kwargs):
    print(f'{a=}, {b=}, {c=}, {args=}, {e=}, {kwargs=}') #f-string debug


f(0, 1, 2, 3, 4, e=5, f=6, g=7)
# f(a=0, 1, 2, 3, 4, e=5, f=6, g=7) # SyntaxError: argumento posicional después de un argumento con nombre
# f(0, b=1, 2, 3, 4, e=5, f=6, g=7) # SyntaxError: argumento posicional después de un argumento con nombre


def g(a, /, b, c=3, *, e=4, **kwargs):
    print(f'{a=}, {b=}, {c=}, {e=}, {kwargs=}') #f-string debug


g(0, 1, 2, e=5, f=6, g=7)
# g(0, 1, 2, 3, 4, e=5, f=6, g=7) # TypeError: g() takes from 2 to 3 positional arguments but 5 positional arguments (and 1 keyword-only argument) were given
