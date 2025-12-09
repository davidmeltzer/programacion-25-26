# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: pandas/10-df-columns-selection.py


# Para ejecutar esto desde vsc se recomienda configurarlo
# de tal manera que al ejecutarlo el directorio de trabajo sea
# el directorio del script:
# Extensions > Python > Terminal: Execute In File Dir (python.terminal.executeInFileDir).


from collections.abc import Iterable
import pandas as pd

def write_selected_columns(df, columns: Iterable[str] | str):
    selected_columns = df[columns]
    print("Columnas seleccionadas:\n", columns)
    print("Resultado de la selección:")
    print(selected_columns)
    print(f"Tipo de dato devuelto al extraer una o varias columnas: {type(selected_columns)}")
    print()

# Crear DataFrame a partir de los datos en un archivo csv
df_from_file = pd.read_csv('turismo-alojamientos-ocupados-por-ccaa.csv', sep=';')
print("\nDatos del fichero CSV:\n", df_from_file)
print()
print(df_from_file.dtypes)
print()

# Extraer varias columnas
columnas_a_seleccionar = ['Comunidad_autónoma', 'Año_2023', 'Año_2022']
write_selected_columns(df_from_file, columnas_a_seleccionar)

# Extraer una sola columna. Selección usando una cadena de texto
columnas_a_seleccionar = 'Año_2023'
write_selected_columns(df_from_file, columnas_a_seleccionar)

# Extraer una sola columna. Selección usando un iterable con un solo elemento
columnas_a_seleccionar = [ 'Año_2022' ]
write_selected_columns(df_from_file, columnas_a_seleccionar)


# Extraer una sola columna usando su nombre como un atributo del DataFrame
selected_columns = df_from_file.Año_2021
print("Resultado de la selección:")
print(selected_columns)
print(f"Tipo de dato devuelto al extraer una o varias columnas: {type(selected_columns)}")
