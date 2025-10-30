# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: modelo_datos/ejercicio-01.py


# Dada la codificación incial de la clase Complejo de un ejemplo anterior: 
# 1. añada los métodos __repr__ y __str__ para que las instancias de la clase
# tengan una representación adecuada tanto para desarrolladores como para 
# usuarios finales. 
# 2. Añada también el método que permita usar el operador de suma (+) 
# entre dos números complejos.


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

    def __repr__(self):
        # 👉 your code here
        pass

    def __str__(self):
        # 👉 your code here
        pass
    
    # Ver https://docs.python.org/es/3.13/reference/datamodel.html#emulating-numeric-types
    # para implementar el método que permite usar el operador de suma.
    # def ¿?(self, other):
    #     # 👉 your code here
    #     pass

a = NumeroComplejo( (1, 2) )
b = NumeroComplejo( (3, -4) )

c = a + b  # Implementa la suma de números complejos
print(f"a = {a}")  # Muestra el valor de a usando __str__
print(f"b = {b}")  # Muestra el valor de b usando __str__
print(f"a + b = {c}")  # Muestra el resultado de la suma usando __str__

d = eval( repr(c) ) # La representación devuelta por __repr__ debe permitir recrear el objeto.
print(f"d == c: {d == c}")  # Comprueba que d y c son iguales