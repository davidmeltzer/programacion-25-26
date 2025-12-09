# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: pandas/06-head-tail.py


import pandas as pd


serie_datos = pd.Series(range(100,130))
print("Float Series with custom index:")
print(serie_datos)
print(serie_datos.index)
print()

print("Primeros 5 elementos (head)")
print(serie_datos.head())
print()

print("Últimos 5 elementos (tail)")
print(serie_datos.tail())