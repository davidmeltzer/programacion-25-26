# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: comprensiones/05-set-dict.py


elementos = [ 1, 2, 3, 4, 5 ]

# Crear un nuevo diccionario usando un bucle
nuevo_diccionario = {}
for indice, elemento in enumerate(elementos):
    nuevo_diccionario[indice] = elemento + 100
print(nuevo_diccionario)

# Usando comprensión de diccionarios
nuevo_diccionario_comprehension = {indice: elemento + 100 for indice, elemento in enumerate(elementos)}
print(nuevo_diccionario_comprehension)