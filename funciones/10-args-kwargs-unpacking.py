# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: funciones/10-args-kwargs-unpacking.py


def f(a, b, c, d):
    print(a, b, c, d)

f(*[1], *(2,), **dict(c=3), **{'d': 4})         # Equivalente a f(1, 2, c=3, d=4)
f(*[1], *(2,), *[3, 4])                         # Equivalente a f(1, 2, 3, 4)
f(**dict(a=1, b=2), **dict(c=3), **{'d': 4})    # Equivalente a f(a=1, b=2, c=3, d=4)
f(*[1], 2, **dict(c=3), d=4)            #       # Equivalente a f(1, 2, c=3, d=4)