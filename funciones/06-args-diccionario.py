# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: funciones/06-args-diccionario.py


def f(**kwargs): # diccionario
    print(f"type(kwargs) = {type(kwargs)}, {kwargs=}")
    for clave, valor in kwargs.items():
        print(f"  {clave}: {valor}")

# Llamadas con diferente cantidad de argumentos nombrados
f(nombre="Ana", edad=25, ciudad="Madrid")
f(producto="Laptop", precio=1200)
f(marca="Toyota", modelo="Corolla", año=2022, color="Azul")