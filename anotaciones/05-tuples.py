# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: anotaciones/05-tuples.py


def args_to_tuple(*args) -> tuple:
    return args

# Example uses of the args_to_tuple function

# Using the function with different numbers of arguments
tuple1 = args_to_tuple(1, 2, 3)
print(tuple1)  # Output: (1, 2, 3)
print(type(tuple1))

tuple2 = args_to_tuple('a', 'b', 'c', 'd')
print(tuple2)  # Output: ('a', 'b', 'c', 'd')
print(type(tuple2))

tuple3 = args_to_tuple(True, False, None)
print(tuple3)  # Output: (True, False, None)
print(type(tuple3))

# Using the function with no arguments
tuple4 = args_to_tuple()
print(tuple4)  # Output: ()
print(type(tuple4))


# Otro ejemplo
# Anotación de tupla con tipos específicos
def process_coordinates(coords: tuple[float, float]) -> str:
    x, y = coords
    return f"Coordinates are x: {x}, y: {y}"

# Example uses of the process_coordinates function
coord_result1 = process_coordinates((10.5, 20.3))
print(coord_result1)  # Output: Coordinates are x: 10.5, y: 20.3