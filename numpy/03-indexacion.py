# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: numpy/03-indexacion.py


import numpy as np

# Create a numpy array of integers
arr = np.array([10, 21, 32, 43, 54, 65, 76, 87, 98], dtype=int)
print("Original array:", arr)

# Indexing selected indexes with a list
selected_indexes = [1, 3, 5]
selected_elements = arr[selected_indexes]
print("Elements at indexes", selected_indexes, ":", selected_elements)

# Boolean indexing to show all odd numbers
array_of_booleans = arr % 2 == 1
print("Boolean array for odd numbers:", array_of_booleans)
odd_numbers = arr[array_of_booleans]
print("Odd numbers in the array:", odd_numbers)