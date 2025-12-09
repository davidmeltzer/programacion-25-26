# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: pandas/11-df-rows-selection-1.py


# Para ejecutar esto desde vsc se recomienda configurarlo
# de tal manera que al ejecutarlo el directorio de trabajo sea
# el directorio del script:
# Extensions > Python > Terminal: Execute In File Dir (python.terminal.executeInFileDir).


import pandas as pd

# Crear DataFrame a partir de los datos en un archivo csv
df_from_file = pd.read_csv('turismo-alojamientos-ocupados-por-ccaa.csv', sep=';')
print("\nDatos del fichero CSV:\n", df_from_file)
print()
print(df_from_file.dtypes)
print()

# Cambio del índice del DataFrame
df_from_file_changed_index = df_from_file.set_index('Comunidad_autónoma')
print(df_from_file_changed_index)
print()

# Selecciones usando .loc[]: selección por etiquetas de índice

# Selección de una fila usando .loc[] con una cadena de texto
rows_to_select = 'Andalucía'
selected_rows = df_from_file_changed_index.loc[rows_to_select]
print("Resultado de la selección:")
print(selected_rows)
print(f"Tipo de dato devuelto al extraer una o varias filas: {type(selected_rows)}")
print()

# Selección de una fila usando .loc[] con un iterable con un único valor de índice
rows_to_select = ['Andalucía']
selected_rows = df_from_file_changed_index.loc[rows_to_select]
print("Resultado de la selección:")
print(selected_rows)
print(f"Tipo de dato devuelto al extraer una o varias filas: {type(selected_rows)}")
print()

# Selección de varias filas usando .loc[] con un iterable de valores de índice
rows_to_select = ['Andalucía', 'Madrid, Comunidad de']
selected_rowss = df_from_file_changed_index.loc[rows_to_select]
print("Resultado de la selección:")
print(selected_rowss)
print(f"Tipo de dato devuelto al extraer una o varias filas: {type(selected_rowss)}")
print()


# Selecciones usando .iloc[]: selección por posición de índice

# Selección de una fila usando .iloc[] con un entero.
row_to_select = 3 # Cuarta fila (posición 3). Baleares.
selected_rows = df_from_file_changed_index.iloc[row_to_select]
print("Resultado de la selección:")
print(selected_rows)
print(f"Tipo de dato devuelto al extraer una o varias filas: {type(selected_rows)}")
print()

# # Selección de una fila usando .iloc[] con un iterable con un único valor de índice
row_to_select = [ 3 ] # Cuarta fila (posición 3). Baleares.
selected_rows = df_from_file_changed_index.iloc[row_to_select]
print("Resultado de la selección:")
print(selected_rows)
print(f"Tipo de dato devuelto al extraer una o varias filas: {type(selected_rows)}")
print()

# # Selección de varias filas usando .iloc[] con un iterable de valores de posición
row_to_select = [ 0, 1 ] # Primeras filas (posiciones 0 y 1). Andalucía y Aragón.
selected_rows = df_from_file_changed_index.iloc[row_to_select]
print("Resultado de la selección:")
print(selected_rows)
print(f"Tipo de dato devuelto al extraer una o varias filas: {type(selected_rows)}")
print()
