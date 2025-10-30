# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: funciones/15-decoradores.py


def funcion_decorador(func):
    """Un decorador que imprime las anotaciones de la función antes de llamarla."""
    def wrapper(*args, **kwargs):
        print("Antes de invocar a la función.")
        resultados = func(*args, **kwargs)
        print("Después de invocar a la función.")
        return resultados
    return wrapper
        
@funcion_decorador
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

print(sumar(1, 2, 3.5))