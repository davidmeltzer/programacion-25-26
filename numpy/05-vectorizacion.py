# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: numpy/05-vectorizacion.py


import numpy as np

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
print("x=\n",x,"\ny=\n",y)

# Suma, resta, multiplicación y división de matrices

r = x + y
print("x + y=\n",r)

r = x - y
print("x - y=\n",r)

r = x * y
print("x * y=\n",r)

r = y / x
print("y / x=\n",r)

