# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: numpy/02-vistas-copias.py


import numpy as np

# Create a numpy array
arr = np.array([1, 2, 3, 4, 5])

# Create a view of the array
view_arr = arr[1:4]

print("Original array:", arr)
print("View before modification:", view_arr)

# Modify the original array
arr[2] = 99

print("Original array after modification:", arr)
print("View after modification:", view_arr)

# Create a copy of the slice
copy_arr = arr[1:4].copy()

# Modify the original array again
arr[3] = 77

print("Original array after second modification:", arr)
print("Copy of the slice after original modification:", copy_arr)