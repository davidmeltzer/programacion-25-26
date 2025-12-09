# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: pandas/16-df-statistics-visualization.py


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

# Informe general sobre los datos
print("\nInforme general sobre los datos del DataFrame:")
print(df_from_file_changed_index.describe(include='all'))
print()

# Visualización gráfica de los datos
import matplotlib.pyplot as plt
df_from_file_changed_index.plot(kind='bar', figsize=(10, 6))
plt.title('Alojamientos ocupados por Comunidad Autónoma (2018-2024)')
plt.xlabel('Comunidad Autónoma')
plt.ylabel('Número de Alojamientos Ocupados')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()