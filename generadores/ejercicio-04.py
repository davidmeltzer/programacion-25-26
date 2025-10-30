# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: generadores/ejercicio-04.py


# Build a small generator pipeline that:
#   1 .Generates numbers from 1 to 20.
#   2 .Filters out numbers not divisible by 3.
#   3 .Yields their squares.

def gen_numbers():
    # yields 1 to 20
    pass

def filter_div3(nums):
    # yields only numbers divisible by 3
    pass

def square(nums):
    # yields squares of input numbers
    pass

# Example:
result = square(filter_div3(gen_numbers()))
print(list(result))
# Expected: [9, 36, 81, 144, 225, 324, 441, 576, 729, 900]