# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: pandas/04-indexes-ambiguity.py


import pandas as pd


s = pd.Series(['a', 'b', 'c'], index=[10, 20, 30])
print(s)
print()

print( f"s[20]: {s[20]}" ) # Indexación por etiqueta numérica.
print( f"s[1]: {s[1]}" )   # Indexación por posición. Ambiguedad.
