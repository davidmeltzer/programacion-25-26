
# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: modelo_datos/07-user-types.py


# Protocolos estáticos

from typing import Protocol # A partir de Python 3.9 no usar para otros tipos
from typing import runtime_checkable

@runtime_checkable # para usar isinstance con tipos de usuario
class Saludador(Protocol):
    def saluda(self) -> str:
        pass

class Persona:
    def saluda(self) -> str:
        return "¡Hola!"

class Perro:
    def saluda(self) -> str:
        return "¡Guau!"

def di_hola(entity: Saludador):
    print(entity.saluda())

# Funciona para los dos tipos de objeto
print("Protocolos estáticos:")
di_hola(Persona())
di_hola(Perro())
print(isinstance(Persona(), Saludador))  # ✅ True
print(isinstance(Perro(), Saludador))  # ✅ True

# Protocolos dinámicos

@runtime_checkable # para usar isinstance con tipos de usuario
class Saludador_dinamico(Protocol):
    def saluda(self) -> str:
        pass

class Ingles:
    def saluda(self) -> str:
        return "Hi there!"

class Piedra:
    pass

p = Ingles()
r = Piedra()

print("Protocolos dinámicos:")
di_hola(Ingles())
print(isinstance(p, Saludador_dinamico))  # ✅ True
print(isinstance(r, Saludador_dinamico))  # ❌ False
