# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: comprensiones/03-anidamiento.py


# Crear una nueva lista usando un bucle
nueva_lista_loop = []
for letra in 'abcde':
    for numero in range(1, 4):
        nueva_lista_loop.append(letra + str(numero))
print(nueva_lista_loop)

# Usando comprensión de listas
nueva_lista_comprehension = [letra + str(numero) for letra in 'abcde' for numero in range(1, 4)]
print(nueva_lista_comprehension)