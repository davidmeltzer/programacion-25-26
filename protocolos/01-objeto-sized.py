# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: protocolos/01-objeto-sized.py


objeto_sized = [ 1, 2, 3, 4, 5 ]
# objeto_sized = ( 1, 2, 3, 4, 5 )
# objeto_sized = { 1, 2, 3, 4, 5 }
# objeto_sized = dict(a=1, b=2, c=3, d=4, e=5)
# objeto_sized = range(10)

print(f"{objeto_sized=}")
print(f"type: {type(objeto_sized)}")

from collections.abc import Sized
print(f"{isinstance(objeto_sized, Sized)=}")

print(len(objeto_sized))