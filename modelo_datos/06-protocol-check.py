# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: modelo_datos/06-protocol-check.py


class ExtractCharacters:
    def __init__(self, data: str):
        self.data = data

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.data):
            char = self.data[self.index]
            self.index += 1
            return char
        raise StopIteration

extractor = ExtractCharacters("Hello")
for char in extractor:
    print(char)

from collections.abc import Callable, Iterable, Iterator
print(f"ExtractCharacters cumple con protocolo Iterable: {isinstance(extractor, Iterable)}")
print(f"ExtractCharacters cumple con protocolo Iterator: {isinstance(extractor, Iterator)}")
print(f"ExtractCharacters cumple con protocolo Callable: {isinstance(extractor, Callable)}")
print(f"ExtractCharacters tiene atributos __iter__ y __next__: {hasattr(extractor, '__iter__') and hasattr(extractor, '__next__')}")
print(f"ExtractCharacters tiene atributos __iter__ y __next__: {all( (hasattr(extractor, '__iter__'), hasattr(extractor, '__next__')) )}") # all( iterable de booleanos )