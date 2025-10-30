# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: comprensiones/02-filtro.py


elementos = [ 1, 2, 3, 4, 5 ]

# Crear una nueva lista transformada usando un bucle
nueva_lista_loop = []
for elemento in elementos:
    if elemento % 2 == 0:
        nueva_lista_loop.append(elemento + 100)
print(nueva_lista_loop)

# Usando comprensión de listas
nueva_lista_comprehension = [elemento + 100 for elemento in elementos if elemento % 2 == 0]
print(nueva_lista_comprehension)