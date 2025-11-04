# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: funciones/07-args-kwargs.py


def f(a, *pargs, **kargs):
    print(f"{a=}, {pargs=}, {kargs=}")

f(1)
f(1, 2, 3)
f(1, 2, 3, x=4, y=5)

# Las siguientes llamadas generarán errores debido a la colocación incorrecta de argumentos nombrados

# Argumento nombrado antes de los argumentos posicionales (SyntaxError)
# f(a=1, 2, 3)

# Argumento posicional después de un argumento nombrado (SyntaxError)
# f(1, x=2, 3)

# Valor duplicado para el argumento 'a' (TypeError)
# f(1, a=2)
