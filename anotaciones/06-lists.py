# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: anotaciones/06-lists.py


def average(values: list[float] | None) -> float:
    return sum(values) / len(values) if values else 0.0

def unique(xs: list[int]) -> set[int]:
    return set(xs)

# Examples for average
float_lists = [
    [1.0, 2.0, 3.0, 4.0],
    [10.5, 3.5],
    [],
    None,
    [-1.0, 1.0],
]
for vals in float_lists:
    print(f"average({vals}) -> {average(vals)}")


# Examples for unique
int_lists = [
    [1, 2, 2, 3, 1],
    [],
    [42, 42, 42],
    [-3, -1, -3, 0, 1],
]
for xs in int_lists:
    s = unique(xs)
    print(f"unique({xs}) -> {s} (sorted: {sorted(s)})")