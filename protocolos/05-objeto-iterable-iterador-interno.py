# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: protocolos/05-objeto-iterable-iterador-interno.py


class SecuenciaIterable:
    def __init__(self, datos):
        self.datos = datos
    
    def __len__(self):
        return len(self.datos)

    def __iter__(self):
        self.indice = 0
        return self
    
    def __next__(self):
        if self.indice < len(self.datos):
            valor = self.datos[self.indice]
            self.indice += 1
            return valor
        else:
            raise StopIteration

objeto_iterable = SecuenciaIterable([1, 2, 3, 4, 5])

print(f"{objeto_iterable=}")
print(f"type: {type(objeto_iterable)}")

from collections.abc import Iterable, Sized, Sequence
print(f"{isinstance(objeto_iterable, Sized)=}")
print(f"{isinstance(objeto_iterable, Sequence)=}")
print(f"{isinstance(objeto_iterable, Iterable)=}")

# ¿Es subscriptable?
# idx = 0
# while idx < len(objeto_iterable):
#     print(objeto_iterable[idx])
#     idx += 1

# Con un iterador explícito
print("\nUso con iterador explícito")
iterador = iter(objeto_iterable)
terminado = False
while not terminado:
    try:
        elemento = next(iterador)
        print(elemento, " ", end='')
    except StopIteration:
        terminado = True

# Con un iterador implícito
print("\n\nUso con iterador implícito")
for elemento in objeto_iterable:
    print(elemento, " ", end='')

# ¿Qué ocurre aquí? ¿Por qué?
print("\n\nQué puede ocurrir cuando el iterador es el mismo objeto iterable")
iterador1 = iter(objeto_iterable)
print(f"Primer elemento extraido con iterador1: {next(iterador1)=}")
print(f"Segundo elemento extraido con iterador1: {next(iterador1)=}")
iterador2 = iter(objeto_iterable)
print(f"Primer elemento extraido con iterador2: {next(iterador2)=}")
print(f"Tercer elemento extraido con iterador1: {next(iterador1)=}")