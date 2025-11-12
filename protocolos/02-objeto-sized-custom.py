# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: protocolos/02-objeto-sized-custom.py


class ClaseSized:
    def __init__(self, datos):
        self.datos = datos

    def __len__(self):
        return len(self.datos)

objeto_sized = ClaseSized( [ 1, 2, 3, 4, 5 ] )


print(f"{objeto_sized=}")
print(f"type: {type(objeto_sized)}")

from collections.abc import Sized
print(f"{isinstance(objeto_sized, Sized)=}")

print(len(objeto_sized))