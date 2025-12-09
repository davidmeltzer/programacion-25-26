# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: pandas/08-df-creation.py


import pandas as pd
import numpy as np


# list-of-lists (array-like)
data = [
    [1, 'Alice', 3.5],
    [2, 'Bob', 4.0],
    [3, 'Carol', 3.8],
]
df_from_list = pd.DataFrame(data, columns=['id', 'name', 'score'])
print("From list of lists:\n", df_from_list, "\n")

# dict of iterables (lists/tuples)
data_dict = {
    'id': [1, 2, 3],
    'name': ('Alice', 'Bob', 'Carol'),
    'score': [3.5, 4.0, 3.8],
}
df_from_dict = pd.DataFrame(data_dict)
print("From dict of iterables:\n", df_from_dict, "\n")

# numpy ndarray (array-like)
arr = np.array([[1, 10.0], [2, 20.0], [3, 30.0]])
df_from_ndarray = pd.DataFrame(arr, columns=['id', 'value'])
print("From numpy ndarray:\n", df_from_ndarray, "\n")

# generator (iterable)
gen = ({'id': i, 'square': i**2} for i in range(1, 4))
df_from_gen = pd.DataFrame(gen)
print("From generator:\n", df_from_gen)

# Pandas series
s_id = pd.Series([1, 2, 3], name='id')
s_value = pd.Series([100, 200, 300], name='value')
df_from_series = pd.DataFrame({ 'id': s_id, 'value': s_value })
print("\nFrom pandas Series:\n", df_from_series)
