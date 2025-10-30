# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: modelo_datos/03-operadores-relacionales.py


from typing import Tuple
      
class NumeroComplejo:
    def __init__(self, complejo: Tuple[float, float]):
        real, imaginario = complejo
        self.real = real
        self.imaginario = imaginario

    def __eq__(self, other): # Se invoca con el operador ==. Ejemplo: x == x se invoca como x.__eq__(y)
        if not isinstance(other, NumeroComplejo):
            raise TypeError("Comparación no soportada entre instancias de diferentes tipos")
        return self.real == other.real and self.imaginario == other.imaginario

    def __ne__(self, other):
        return not self.__eq__(other)

a = NumeroComplejo( (1, 2) )
b = NumeroComplejo( (3, 4) )

print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a != 5: {a != 5}")# Probando con un tipo diferente