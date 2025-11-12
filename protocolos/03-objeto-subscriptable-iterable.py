# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: protocolos/03-objeto-subscriptable-iterable.py


objeto_subscriptable = [ 1, 2, 3, 4, 5 ]
# objeto_subscriptable = ( 1, 2, 3, 4, 5 )
# objeto_subscriptable = range(10)

# ¿Por qué no es posible usar un índice en estos casos?
# objeto_subscriptable = { 1, 2, 3, 4, 5 }
# objeto_subscriptable = dict(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10)

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