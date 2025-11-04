# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: funciones/ejercicio-11.py


# Write a function calculate(operation="add", *args, **kwargs) that:
# 1. Accepts numbers as *args
# 2. Optionally takes operation="add" or "multiply"
# 3. Optionally prints result if verbose=True is in **kwargs
# 4 .returns the computed result

def calculate(operation="add", *args, **kwargs):
    # 👉 Your code here
    pass

number = calculate("multiply", 2, 3, 4, verbose=True)
# stdout output: Result = 24

number = calculate("multiply", 2, 3, 4)
# Shows no stdout output
