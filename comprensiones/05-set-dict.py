# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: comprensiones/05-set-dict.py


elementos = [ 1, 2, 3, 4, 5 ]

# Crear una nueva lista usando un bucle
nueva_lista_comprehension = [elemento + 100 for elemento in elementos]
print(nueva_lista_comprehension)

# Usando comprensión de listas
nuevo_set_comprehension = {elemento + 100 for elemento in elementos}
print(nuevo_set_comprehension)

# Usando comprensión de diccionarios
nuevo_diccionario_comprehension = {x: elemento + 100 for x, elemento in enumerate(elementos)}
print(nuevo_diccionario_comprehension)