# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: pandas/07-series-dict.py


import pandas as pd


# Serie a partir de diccionario
datos = {'a': 0.5, 'b': 2.0, 'c': 3.1415, 'd': -1.2}
s_floats = pd.Series(datos)
print("Float Series with custom index:")
print(s_floats)
print(s_floats.index)
print()

# Conversión a diccionario
diccionario = s_floats.to_dict()
print(diccionario)
