# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: protocolos/04-objeto-subscriptable-custom.py


class SecuenciaSubscriptable:
    def __init__(self, datos):
        self.datos = datos

    def __getitem__(self, indice):
        return self.datos[indice]

    def __len__(self):
        return len(self.datos)


objeto_subscriptable = SecuenciaSubscriptable([1, 2, 3, 4, 5])

print(f"{objeto_subscriptable=}")
print(f"type: {type(objeto_subscriptable)}")

from collections.abc import Sized, Sequence
print(f"{isinstance(objeto_subscriptable, Sized)=}")
print(f"{isinstance(objeto_subscriptable, Sequence)=}")

# Con un índice
print("\nUso con índice")
idx = 0
while idx < len(objeto_subscriptable):
    print(objeto_subscriptable[idx], " ", end='')
    idx += 1

# ¡También es iterable! Si admite índices empezando en 0 y arroja la excepción IndexError

# Con un iterador explícito
print("\n\nUso con iterador explícito")
iterador = iter(objeto_subscriptable)
terminado = False
while not terminado:
    try:
        elemento = next(iterador)
        print(elemento, " ", end='')
    except StopIteration:
        terminado = True

# Con un iterador implícito
print("\n\nUso con iterador implícito")
for elemento in objeto_subscriptable:
    print(elemento, " ", end='')