# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: funciones/02-funcion-tipos.py


def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print(f"El resultado de sumar(3, 5) es: {resultado}")

# Polimorfismo: la función 'sumar' funciona con distintos tipos de datos.
resultado = sumar(3+4j, 5-6j) # Los números complejos también funcionan.
print(f"El resultado de sumar(3+4j, 5-6j) es: {resultado}")

resultado = sumar("hola ", "mundo")
print(f"El resultado de sumar('hola ', 'mundo') es: {resultado}")

# La definión de tipos (type hinting) ES SÓLO INFORMATIVA.
def sumar_tipos(a: int, b: int) -> int:
    return a + b

resultado = sumar_tipos(3+4j, 5-6j) # Los números complejos siguen funcionando.
print(f"El resultado de sumar(3+4j, 5-6j) es: {resultado}")
