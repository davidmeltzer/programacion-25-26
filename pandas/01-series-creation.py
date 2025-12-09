# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: pandas/01-series-creation.py


import pandas as pd
import numpy as np

# Examples of creating pandas.Series from lists of integers, floats, characters and strings.

# From a list of integers
ints1 = [10, 20, 30, 40]
s_ints1 = pd.Series(ints1)
print("Integer Series:")
print(s_ints1)
print()

# Demonstrate conversion between types if needed
# integer -> float
s_ints_as_float = s_ints1.astype(float)
print("Integers converted to floats:")
print(s_ints_as_float)
print()

# From a list of integers
ints2 = [10, 20, 30, 40]
s_ints2 = pd.Series(ints2, dtype=float)
print("Float Series:")
print(s_ints2)
print()

# From a generator of integers
ints3 = (x for x in range(10, 50, 10))
s_ints3 = pd.Series(ints3, name="integers")
print("Integer Series from generator:")
print(s_ints3)
print()

# From a list of floats
floats = [0.5, 2.0, 3.1415, -1.2]
index=["a", "b", "c", "d"]
s_floats = pd.Series(floats, index=index, name="floats")
print("Float Series with custom index:")
print(s_floats)
print(s_floats.index)
print()

# From a list of single characters (letters)
# chars = ["a", "b", "c", "d"]
chars = list("abcd")
# use pandas 'string' dtype (nullable string) or leave to default object
s_chars = pd.Series(chars, dtype="string", name="chars")
print("Character Series (string dtype):")
print(s_chars)
print()

# From a list of strings (including a missing value)
strings = ["apple", "banana", None, "cherry"]
# using nullable string dtype preserves <NA> for missing
s_strings = pd.Series(strings, dtype="string", name="fruits")
print("String Series with a missing value:")
print(s_strings)
print()

# From a numpy generator
np_floats = np.random.rand(5)
s_np_floats = pd.Series(np_floats, name="np_floats")
print("Float Series from numpy random generator:")
print(s_np_floats)
print()