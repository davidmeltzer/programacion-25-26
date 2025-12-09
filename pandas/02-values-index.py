# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: pandas/02-values-index.py


import pandas as pd


# From a list of floats
floats = [0.5, 2.0, 3.1415, -1.2]
index=["a", "b", "c", "d"]
s_floats = pd.Series(floats, index=index, name="floats")
print("Float Series with custom index:")
print(s_floats)
print()

valores = s_floats.values # Array de Numpy
indices = s_floats.index # Index de pandas
longitud = len(s_floats)
shp = s_floats.shape

print(f"Valores: {valores}. Tipo: {type(valores)}")
print(f"Index: {indices}. Tipo: {type(indices)}")
print(f"Longitud: {longitud}")
print(f"Shape: {shp}")
