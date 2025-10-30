# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: funciones/03-args-posicion-nombre.py


def f(a, b, c):
    return a + b + c


print(f(1, 2, 3))           # Usando argumentos posicionales. Resultado: 6
print(f(a=1, b=2, c=3))     # Usando argumentos nombrados. Resultado: 6
print(f(1, c=3, b=2))       # Mezclando argumentos posicionales y nombrados. Resultado: 6
# print(f(a=1, 2, c=3))     # ¡Error! Los argumentos posicionales deben ir ANTES que los nombrados.