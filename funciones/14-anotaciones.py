# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: funciones/14-anotaciones.py


# Uso de anotaciones de manera arbitraria

def f(a: 'hack', b: (1, 10), c: float) -> int:
        return a + b + c

print(f(5, 3, 2.5))

# Una función es un objeto invocable (callable)
print(type(f))                          # Salida: <class 'function'>
print(callable(f))                      # Salida: True
print(hasattr(f, '__call__'))           # Salida: True
from collections.abc import Callable
print(isinstance(f, Callable))          # Salida: True

# Las anotaciones son un atributo del objeto función
print(f.__annotations__)
# print(dir(f))


# Uso de anotaciones para documentar tipos de argumentos y valor de retorno
def sumar(a: int, b: int, c: float) -> int:
    """Suma tres números.

    Args:
        a (int): El primer número entero.
        b (int): El segundo número entero.
        c (float): El tercer número real.

    Returns:
        int: La suma de los tres números.
    """
    return a + b + c

print(sumar(1, 2, 3.5))  # Salida: 6.5
print(sumar('¿hola ', 'que ', 'tal?'))  # Las anotaciones no imponen restricciones de tipo