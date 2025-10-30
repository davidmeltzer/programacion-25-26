# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: generadores/01-generador-uso.py


# Función que devuelve una lista de cuadrados
def cuadrados(n):
    return [i ** 2 for i in range(n)]

print(f"Función {cuadrados.__name__}")
print(f"Tipo: {type(cuadrados)}")

resultado = cuadrados(5)
print(f"Tipo del resultado: {type(resultado)}")
print(f"Resultado: {resultado}")


#  Generador que PRODUCE cuadrados de números
def cuadrados_generador(n):
    for i in range(n):
        yield i ** 2

print(f"Función {cuadrados_generador.__name__}")
print(f"Tipo: {type(cuadrados_generador)}")

iterador = cuadrados_generador(5) # El resultado de la invocación es un objeto iterador.
print(f"Tipo del resultado: {type(iterador)}")
print(f"Es iterable: {hasattr(iterador, '__iter__')}")
print(f"Es un iterador: {hasattr(iterador, '__next__')}")

# Uso del objeto iterador obtenido usando next()
terminado = False
while not terminado:
    try:
        valor = next(iterador)
        print(f"Valor generado: {valor}")
    except StopIteration:
        terminado = True

# Uso del generador en un bucle for
for valor in cuadrados_generador(5):
    print(f"Valor generado en bucle for: {valor}")


# Comparación de uso de memoria para función y generador
import sys
print(sys.getsizeof(cuadrados(1000000)))   # Tamaño de la lista devuelta por la función
print(sys.getsizeof(cuadrados_generador(1000000)))  # Tamaño del objeto iterable devuelto por el generador