# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: funciones/04-args-defecto.py


def f(a, b=1, c=3):
    return a + b + c


print(f(1))                 # Usando el valor por defecto de b y c. Resultado: 1 + 1 + 3 = 5
print(f(a=1))               # Usando el valor por defecto de b y c. Resultado: 1 + 1 + 3 = 5
print(f(a=1, c=3))          # Usando el valor por defecto de b. Resultado: 1 + 1 + 3 = 5
print(f(1, c=3))            # Usando el valor por defecto de b. Resultado: 1 + 1 + 3 = 5
print(f(1, 2))              # Usando el valor por defecto de c. Resultado: 1 + 2 + 3 = 6
print(f(b=2, a=1))          # Usando el valor por defecto de c. Resultado: 1 + 2 + 3 = 6
# print(f())                # ¡Error! Falta el argumento obligatorio 'a'.
