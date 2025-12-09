# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: pandas/12-df-rows-selection-2.py


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

# Selecciones usando .at[] y .iat[]
print(f".at['Aragón’, 'Año_2022']: {df_from_file_changed_index.at['Aragón', 'Año_2022']}")
print(f".iat[1, 2]: {df_from_file_changed_index.iat[1, 2]}")
print(f".at['Cantabria','Año_2021']: {df_from_file_changed_index.at['Cantabria', 'Año_2021']}")
print(f".iat[5, 3]: {df_from_file_changed_index.iat[5, 3]}")


