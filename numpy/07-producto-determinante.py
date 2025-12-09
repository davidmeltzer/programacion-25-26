# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: numpy/07-producto-determinante.py


import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])      # Shape: (2, 3)
B = np.array([[7, 8],
              [9, 10],
              [11, 12]])       # Shape: (3, 2)

# Matrix multiplication using @ operator
result_at = A @ B # Para matrices, este es el método recomendado

# Matrix multiplication using np.matmul
result_matmul = np.matmul(A, B) # Para matrices, este es el otro método recomendado

# Matrix multiplication using np.dot
# https://numpy.org/doc/stable/reference/generated/numpy.dot.html
result_dot = np.dot(A, B) # Para matrices, este no es el método recomendado (ver referencia).

print("Using @ operator:\n", result_at)
print("Using np.dot:\n", result_dot)
print("Using np.matmul:\n", result_matmul)

# Determinant of the resulting matrix
det_result_at = np.linalg.det(result_at)
print("Determinant of result_at:", det_result_at)