# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: funciones/11-kwargs-obligatorios.py


def f(a, b, *c, d):
    print(f"{a=}, {b=}, {c=}, {d=}")

f(1, 2, 3, 4, 5, d=6)  # a=1, b=2, c=(3, 4, 5), d=6
# f(3, 4, 5, d=6, a=1, b=2) # TypeError: f() got multiple values for argument 'a'
# f(1, 2, 3, 4, 5, 6)    # TypeError: falta el argumento obligatorio 'd' (argumento sin nombre)

def g(a, b, *, c, d):
    print(f"{a=}, {b=}, {c=}, {d=}")

g(1, 2, c=3, d=4)      # a=1, b=2, c=3, d=4
# g(1, 2, 3, 4)          # TypeError: faltan los argumentos nombrados 'c' y 'd'
# g(1, 2, c=3, 4)        # SyntaxError: argumento posicional después de un argumento nombrado
# g(1, 2, 3, d=4)        # SyntaxError: falta el argumento nombrado 'c'