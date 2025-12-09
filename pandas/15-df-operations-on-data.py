# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: pandas/15-df-operations-on-data.py


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

# Inserción de nueva columna en el DataFrame con la media de las filas
serie = df_from_file_changed_index.mean(axis=1).round() # Media de las filas (axis=1) y redondeo
# df_from_file_changed_index['Media'] = serie
df_from_file_changed_index.insert(0, 'Media', serie) # Indice de inserción 0 (primera columna)
print(df_from_file_changed_index)
print()

# Inserción de nueva fila en el DataFrame con la media de las columnas
serie_fila = df_from_file_changed_index.mean(axis=0).round() # Media de las columnas (axis=0) y redondeo
dic = serie_fila.to_dict()
dic['Comunidad_autónoma'] = 'Media columnas'
df_from_file_changed_index.loc[len(df_from_file_changed_index)] = dic
print(df_from_file_changed_index)

