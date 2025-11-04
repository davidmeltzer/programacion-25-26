# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: anotaciones/02-basic-types.py


# Basic parameter and return annotations
def add(a: int, b: int) -> int:
    return a + b

# Positional-only parameters (PEP 570)
def ratio(n: float, d: float, /) -> float:
    return n / d

# Keyword-only parameters
def greet(*, name: str, times: int = 1) -> str:
    return " ".join([f"Hello, {name}!"] * times)

# Mixed: positional-only, normal, keyword-only
def format_point(x: float, /, y: float, *, sep: str = ", ") -> str:
    return f"{x}{sep}{y}"

# Default values with annotations
def repeat(s: str, n: int = 2) -> str:
    return s * n


# Usos con tipos compatibles de acuerdo a las anotaciones

print("Usos con tipos compatibles de acuerdo a las anotaciones")
# Using add()
result = add(5, 3)
print(f"add(5, 3) = {result}")

# Using ratio()
r = ratio(10.0, 2.5)
print(f"ratio(10.0, 2.5) = {r}")

# Using greet()
greeting = greet(name="Alice")
print(f"greet(name='Alice') = {greeting}")

greeting_multiple = greet(name="Bob", times=3)
print(f"greet(name='Bob', times=3) = {greeting_multiple}")

# Using format_point()
point = format_point(3.14, 2.71)
print(f"format_point(3.14, 2.71) = {point}")

point_custom = format_point(1.0, 2.0, sep=" | ")
print(f"format_point(1.0, 2.0, sep=' | ') = {point_custom}")

# Using repeat()
text = repeat("Hi!")
print(f"repeat('Hi!') = {text}")

text_custom = repeat("Python ", 4)
print(f"repeat('Python ', 4) = {text_custom}")


# Usos con tipos no compatibles (generan advertencias de tipo con mypy)
print("\nUsos con tipos no compatibles (generan advertencias de tipo con mypy)")

# add() expects int, but receiving strings
result_bad = add("5", "3")
print(f"add('5', '3') = {result_bad}")

# greet() expects str for name, but receiving int
greeting_bad = greet(name=123)
print(f"greet(name=123) = {greeting_bad}")

# format_point() expects float for x and y, but receiving strings
point_bad = format_point("3.14", "2.71")
print(f"format_point('3.14', '2.71') = {point_bad}")

# format_point() expects str for sep, but receiving int
point_bad2 = format_point(1.0, 2.0, sep=123)
print(f"format_point(1.0, 2.0, sep=123) = {point_bad2}")

# repeat() expects str for s, but receiving int
text_bad = repeat(42)
print(f"repeat(42) = {text_bad}")


#  Estos usos contienen errores que se producen en tiempo de ejecución.

# # greet() expects int for times, but receiving string
# greeting_bad2 = greet(name="Alice", times="3")
# print(f"greet(name='Alice', times='3') = {greeting_bad2}")

# # ratio() expects float, but receiving strings
# r_bad = ratio("10", "2.5")
# print(f"ratio('10', '2.5') = {r_bad}")

# # repeat() expects int for n, but receiving string
# text_bad2 = repeat("Hi!", "3")
# print(f"repeat('Hi!', '3') = {text_bad2}")