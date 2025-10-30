# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: modelo_datos/02-repr-str.py


def mostrar_repr_str(obj):
    print(f"Objeto de tipo {type(obj).__name__}:")
    print(f"  repr(obj) = {repr(obj)}")
    print(f"  str(obj)  = {str(obj)}")
    print(f"  Valor: {obj}")
    print()

# Número decimal
from decimal import Decimal
num = Decimal('10.5')
mostrar_repr_str(num)

# Fracción
from fractions import Fraction
fraccion = Fraction(22, 7)
mostrar_repr_str(fraccion)

# Fecha y hora
from datetime import datetime
fecha_hora = datetime(2025, 10, 14, 15, 30)
mostrar_repr_str(fecha_hora)
