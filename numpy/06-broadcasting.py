# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: numpy/06-broadcasting.py


# See https://numpy.org/doc/stable/user/basics.broadcasting.html#broadcasting

import numpy as np

def show_array_info(arr, name):
    print(name)
    print("  Array:\n", arr)
    print("  Dimensions:", arr.ndim)
    print("  Shape:", arr.shape)
    print()

a = np.array([1.0, 2.0, 3.0])
show_array_info(a, "Array a")

b = 2.0
print("Scalar b = ", b)

# Producto de un array y un escalar (broadcasting)
# https://numpy.org/doc/stable/_images/broadcasting_1.png
r = a * b
show_array_info(r, "Result of a * b")

# Producto de una matriz por un vector fila (broadcasting)
# https://numpy.org/doc/stable/_images/broadcasting_2.png
a = np.array([[ 0.0,  0.0,  0.0],
              [10.0, 10.0, 10.0],
              [20.0, 20.0, 20.0],
              [30.0, 30.0, 30.0]])
show_array_info(a, "Matrix a")
b = np.array([1.0, 2.0, 3.0])
show_array_info(b, "Row vector b")

r = a + b
show_array_info(r, "Result of a + b (matrix + row vector)")

# Producto de un vector columna por un vector fila (broadcasting)
# https://numpy.org/doc/stable/_images/broadcasting_4.png
a = np.array([0.0, 10.0, 20.0, 30.0])
# show_array_info(a, "Column vector a")
a = np.expand_dims(a, axis=1)  # Hacer explícito que es un vector columna
show_array_info(a, "Column vector a")

b = np.array([1.0, 2.0, 3.0])
show_array_info(b, "Row vector b")

r = a + b
show_array_info(r, "Result of a + b (column vector + row vector)")
