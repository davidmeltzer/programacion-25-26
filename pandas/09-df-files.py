# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: pandas/09-df-files.py


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

# Datos del DataFrame
print(f"Número de filas: {len(df_from_file)}")
print(f"Forma del DataFrame: {df_from_file.shape}")
print(f"Número total de elementos: {df_from_file.size} (shape[0] * shape[1])")
print(f"Nombres de las columnas:\n {df_from_file.columns}")
print(f"Nombres de las columnas (como lista):\n {list(df_from_file.columns)}")
print(f"Indices de las filas:\n {df_from_file.index}")
print(f"Indices de las filas (como lista):\n {list(df_from_file.index)}")
print()

# Cambio del índice del DataFrame
df_from_file_changed_index = df_from_file.set_index('Comunidad_autónoma')
print(df_from_file_changed_index)
print()

# Eliminar las filas con elementos NaN
df_from_file = df_from_file.dropna()
print(df_from_file)
print()

# Convertir las columnas con tipo real a enteros (Int64)
años = [ "Año_" + str(año) for año in range(2018, 2025)]
df_from_file[años] = df_from_file[años].astype('Int64') # Se convierten varias columnas a la vez

print("\nTipos de las columnas después de la conversión:\n", df_from_file.dtypes)
print()
print(df_from_file)

# Guardar el DataFrame en un archivo csv
df_from_file.to_csv('turismo-alojamientos-ocupados-por-ccaa-modificado.csv', index=False)
