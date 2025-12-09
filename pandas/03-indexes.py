# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: pandas/03-indexes.py


import pandas as pd


# From a list of floats
floats = [0.5, 2.0, 3.1415, -1.2]
index=["a", "b", "c", "d"]
s_floats = pd.Series(floats, index=index, name="floats")
print("Float Series with custom index:")
print(s_floats)
print(s_floats.index)
print()

# Indexación con un único índice usando corchetes (desaconsejado usar .loc para evitar ambigüedades)
un_elemento = s_floats["b"] # Series es subscriptable
print( f"s_floats['b']: {un_elemento} de tipo {type(un_elemento)}" )
print( f"s_floats[1]: {un_elemento} de tipo {type(un_elemento)}" ) # Indexación por posición
print()

# Indexación con varios índices. Desaconsejado (usar .loc para evitar ambigüedades)
varios_elementos = ["b", "d"]
print( f"s_floats[ ['b', 'd'] ]:\n{s_floats[ varios_elementos ]}\nde tipo {type(s_floats[ varios_elementos])}" ) # Indexación con iterable, devuelve otra serie
print()

# Indexación por posición con .iloc (la primera posición es la 0)
print( f"s_floats.iloc[1]: {s_floats.iloc[1]}" )
print( f"s_floats.iloc[0, 2, 3]\n{s_floats.iloc[ [0, 2, 3] ]}" )
print()
print()

# Indexación por posición con .loc (usando etiquetas)
print( f"s_floats.loc[ 'b' ]: {s_floats.loc['b']}" )
print( f"s_floats.loc[ ['a', 'c', 'd'] ]:\n{s_floats.loc[ ['a', 'c', 'd'] ]}" )
print()
print()

# FILTRADO
# Obtención de un array booleano para filtrar
filtro = s_floats > 1.0 # Devuelve otra serie de booleanos
print( f"filtro es de tipo {type(filtro)}" )
print(filtro)
print()

datos_filtrados = s_floats[ filtro ] # Indexación con serie booleana. El resultado es una serie también
print(datos_filtrados)
print()

# Pertenencia de índice a la seria
print( f"'a' in s_floats.index: {'a' in s_floats.index}" )
print( f"'z' in s_floats.index: {'z' in s_floats.index}" )