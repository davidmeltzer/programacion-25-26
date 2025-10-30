# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: funciones/08-args-unpacking.py


def f(a, b, c, d):
    print(a, b, c, d)

args = (10, 20)
f(*args, 3, 4)            # Equivalente a f(10, 20, 3, 4)
f(1, *args, 4)            # Equivalente a f(1, 10, 20, 4)
f(1, 2, *args)            # Equivalente a f(1, 2, 10, 20)

# f(1, 2, 3, *args)       # TypeError: demasiados argumentos posicionales

iterable = range(4)
f(*iterable)              # Equivalente a f(0, 1, 2, 3)

f(*['este', 'es', 'un', 'test']) # Equivalente a f('este', 'es', 'un', 'test')
