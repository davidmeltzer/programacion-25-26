# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: pandas/13-df-rows-selection-boolean.py


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

# Selecciones booleanas
print("Selección de las filas donde el valor de la columna 'Año_2023' es mayor que 1000000")
boolean_selection = df_from_file_changed_index['Año_2023'] > 1000000
print("Serie booleana resultante de la comparación:")
print(boolean_selection)
print(f"Tipo de dato devuelto al realizar la comparación: {type(boolean_selection)}")
selected_rows = df_from_file_changed_index[boolean_selection]
print("Resultado de la selección:")
print(selected_rows)
print()

print("Selección de las filas donde el valor del año 2021 es menor que el del año 2018")
boolean_selection = df_from_file_changed_index['Año_2021'] < df_from_file_changed_index['Año_2018']
print("Serie booleana resultante de la comparación:")
print(boolean_selection)
print(f"Tipo de dato devuelto al realizar la comparación: {type(boolean_selection)}")
selected_rows = df_from_file_changed_index[boolean_selection]
print("Resultado de la selección:")
print(selected_rows)
