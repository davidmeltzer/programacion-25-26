# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: protocolos/06-objeto-iterable-iterador-externo.py


class IteradorExterno:
    def __init__(self, datos):
        self.datos = datos
        self.indice = 0
    
    def __next__(self):
        if self.indice < len(self.datos):
            valor = self.datos[self.indice]
            self.indice += 1
            return valor
        else:
            raise StopIteration

class SecuenciaIterable:
    def __init__(self, datos):
        self.datos = datos
    
    def __len__(self):
        return len(self.datos)

    def __iter__(self):
        return IteradorExterno(self.datos)


objeto_iterable = SecuenciaIterable([1, 2, 3, 4, 5])

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
print("\n\nFuncionamiento cuando el objeto iterable es capaz de devolver diferentes objetos iteradores")
iterador1 = iter(objeto_iterable)
print(f"Primer elemento extraido con iterador1: {next(iterador1)=}")
print(f"Segundo elemento extraido con iterador1: {next(iterador1)=}")
iterador2 = iter(objeto_iterable)
print(f"Primer elemento extraido con iterador2: {next(iterador2)=}")
print(f"Tercer elemento extraido con iterador1: {next(iterador1)=}")