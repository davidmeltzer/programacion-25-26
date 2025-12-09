# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: numpy/08-funciones.py


import numpy as np

matrix = np.array([[1, 5],
                   [3, 2],
                   [7, 4]])

print("Matriz:\n", matrix)

# Funciones básicas
print("Max:", np.max(matrix))
print("Min:", np.min(matrix))
print("Sum:", np.sum(matrix))
print("Mean (axis=0):", np.mean(matrix, axis=0))
print("Mean (axis=1):", np.mean(matrix, axis=1))
print("Argmax:", np.argmax(matrix))
print("Argmax(axis=0):", np.argmax(matrix, axis=0))
print("Argmax(axis=1):", np.argmax(matrix, axis=1))
print("Argmin:", np.argmin(matrix))
print()

redundant_matrix = np.array([[1, 2, 2, 3],
                             [4, 5, 5, 6],
                             [4, 5, 5, 6],
                             [7, 8, 8, 9]])
print("Matriz con elementos redundantes:\n", redundant_matrix)

unique_elements = np.unique(redundant_matrix)
print("Elementos únicos:", unique_elements)

unique_elements, unique_indices, unique_counts = np.unique(redundant_matrix,
                                                           axis=0,
                                                           return_index=True,
                                                           return_counts=True)
print("Elementos únicos por filas:\n", unique_elements)
print("Índices de las filas únicas en la matriz original:", unique_indices)
print("Cuenta de apariciones de cada fila única:", unique_counts)

# ¿Y si queremos saber lo mismo para las columnas?
