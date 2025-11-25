# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: modulos/04-ejemplo-con-directorio/directorio/modulo_A.py


import sys

nombre_ejecutable = sys.executable

def saludo():
    print(f"Hola desde modulo_A.py!")
    print(f"Ejecutable: {nombre_ejecutable}")
    print(f"__name__ en modulo_A.py: {__name__}")
    print(f"__file__ en modulo_A.py: {__file__}")