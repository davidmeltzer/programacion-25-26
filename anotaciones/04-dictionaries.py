# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: anotaciones/04-dictionaries.py


def kw_debug(**opts: int) -> dict[str, int]:
    return dict(opts)


# Example 1: Basic usage with keyword arguments
result1 = kw_debug(x=10, y=20, z=30)
print(f"Example 1: {result1}")

# Example 2: Single argument
result2 = kw_debug(count=42)
print(f"Example 2: {result2}")

# Example 3: Multiple arguments
d = {'width': 1920, 'height': 1080, 'depth': 24}
result3 = kw_debug(**d)
print(f"Example 3: {result3}")

# Example 4: No arguments
result4 = kw_debug()
print(f"Example 4: {result4}")


# Otro ejemplo
def invert(d: dict[str, int]) -> dict[int, str]:
    return {v: k for k, v in d.items()}

# Example 1: Basic inversion
original1 = {'a': 1, 'b': 2, 'c': 3}
inverted1 = invert(original1)
print(f"Original: {original1}, Inverted: {inverted1}")

# Example 2: Month numbers to names
months = {'January': 1, 'February': 2, 'March': 3}
month_lookup = invert(months)
print(f"Month lookup: {month_lookup}")

# Example 3: Single entry
single = {'first': 100}
inverted_single = invert(single)
print(f"Single entry: {inverted_single}")

# Example 4: Empty dictionary
empty = {}
inverted_empty = invert(empty)
print(f"Empty dict: {inverted_empty}")