# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: pandas/05-NaN.py


import pandas as pd


# https://es.wikipedia.org/wiki/Anexo:Municipios_de_España_por_población (datos 2024)
datos = {
    "Madrid": 3416771
    # ,"Barcelona": 1702547
    ,"Valencia": 825948
    ,"Sevilla": 687488
    # ,"Zaragoza": 686986
}

indices = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Zaragoza"]
serie_datos = pd.Series(datos, index=indices)
print("Float Series with custom index:")
print(serie_datos)
print(serie_datos.index)
print()

# Comprobar valores NaN
print("Comprobar valores NaN")
print(serie_datos.isna())  # Serie booleana

# Datos filtrados por para eliminar los faltantes
datos_filtrados1 = serie_datos[ serie_datos.isna() == False ] # datos_filtrados1 = serie_datos[ serie_datos.notna() ]
print("Datos filtrados (isna):")
print(datos_filtrados1)

