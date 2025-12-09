# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: numpy/04-cambio-tamano-transposicion.py


# See https://numpy.org/doc/stable/user/absolute_beginners.html

import numpy as np

def show_array_info(arr, name):
    print("name:", name)
    print("  Array:\n", arr)
    print("  Dimensions:", arr.ndim)
    print("  Shape:", arr.shape)
    print()

data = np.array([[1, 2], [3, 4]])
show_array_info(data, "Original array")

row_vector = data.reshape(1, -1) # -1 significa que se calcula automáticamente el tamaño de esa dimensión
show_array_info(row_vector, "Row vector")

# Remove singleton dimensions
row_vector_squeezed = np.squeeze(row_vector)
show_array_info(row_vector_squeezed, "Squeezed row vector")

column_vector = data.reshape(-1, 1)
show_array_info(column_vector, "Column vector")

matrix_from_squeezed_row_vector = np.expand_dims(row_vector_squeezed, axis=0)
show_array_info(matrix_from_squeezed_row_vector, "Matrix from squeezed row vector")

# Transposition
m = np.array([[1, 2, 3], [4, 5, 6]])
show_array_info(m, "Original matrix m")
m_transposed_1 = m.T
show_array_info(m_transposed_1, "Transposed matrix m.T")
m_transposed_2 = m.transpose()
show_array_info(m_transposed_2, "Transposed matrix m.transpose()")
