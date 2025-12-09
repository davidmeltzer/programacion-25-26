# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: numpy/01-creacion.py


import numpy as np

# Create numpy array from a list
list_data = [1, 2, 3, 4, 5]
array_from_list = np.array(list_data)

# Attributes of the numpy array
print("Array from list:", array_from_list)
print("Data type:", array_from_list.dtype)
print("Dimensions:", array_from_list.ndim)
print("Shape:", array_from_list.shape)
print("Size:", array_from_list.size)
print("Type of each cell:", array_from_list.dtype)

# Create numpy array from a tuple
tuple_data = (6, 7, 8, 9, 10)
array_from_tuple = np.array(tuple_data)
print("Array from tuple:", array_from_tuple)

# Create numpy array from a list with explicit type (float)
array_float = np.array(list_data, dtype=float)
print("Array from list with float type:", array_float)

# Create numpy array from a tuple with explicit type (complex)
array_complex = np.array(tuple_data, dtype=complex)
print("Array from tuple with complex type:", array_complex)

# Create 2D numpy array from nested list with explicit type (int32)
nested_list = [[1, 2], [3, 4]]
array_2d = np.array(nested_list, dtype=np.int32)
print("2D array from nested list with int32 type:\n", array_2d)

# Create a numpy array of zeros
zeros_array = np.zeros(5)
print("Array of zeros:", zeros_array)

# Create a numpy array of ones
ones_array = np.ones((2, 3))
print("2D array of ones:\n", ones_array)

# Create a diagonal array using diag
diag_array = np.diag([1, 2, 3, 4])
print("Diagonal array:\n", diag_array)

# Extract a diagonal array from matrix using diag
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
diag_array = np.diag(M)
print("Diagonal array:\n", diag_array)

# Create an identity array
identity_array = np.identity(4)
print("Identity array:\n", identity_array)

# Create an array using arange
arange_array = np.arange(0.5, 10, 2) # Se pueden usar valores en punto flotante
print("Array using arange:", arange_array)

# Create an array using linspace
linspace_array = np.linspace(0, 1, 5)  # 5 evenly spaced values from 0 to 1
print("Array using linspace:", linspace_array)