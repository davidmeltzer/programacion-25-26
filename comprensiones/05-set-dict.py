# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: comprensiones/05-set-dict.py


elementos = [ 1, 2, 3, 4, 5, 5 ]

# Crear un nuevo conjunto usando comprensión de conjuntos
nuevo_conjunto = { elemento + 100 for elemento in elementos }
print(nuevo_conjunto) # Es un CONJUNTO, no una LISTA.

# Crear un nuevo diccionario usando un bucle
nuevo_diccionario = {}
idx = 0
while idx < len(elementos):
    nuevo_diccionario[idx] = elementos[idx] + 100
    idx += 1 # idx = idx + 1
print(nuevo_diccionario)

# Crear un nuevo diccionario usando un bucle y enumerate()
nuevo_diccionario = {}
for indice, elemento in enumerate(elementos):
    nuevo_diccionario[indice] = elemento + 100
print(nuevo_diccionario)

# Usando comprensión de diccionarios
nuevo_diccionario_comprehension = {indice: elemento + 100 for indice, elemento in enumerate(elementos)}
print(nuevo_diccionario_comprehension)