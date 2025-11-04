# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: modelo_datos/09-structural-subtyping.py


class Dog:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} is barking.")

class Cat:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} is meowing.")

for animal in [Cat("Tom"), Dog("Pluto")]:
    animal.make_sound()

# Verificación de disponibilidad de miembros necesarios
def is_animal(obj) -> bool:
    return hasattr(obj, 'make_sound') and callable(getattr(obj, 'make_sound'))

print(is_animal(Cat("Tom")))
print(is_animal(Dog("Pluto")))


# Verificación de cumplimiento de protocolo
from typing import Protocol # A partir de Python 3.8. Usar sólo Protocol.
from typing import runtime_checkable

@runtime_checkable
class AnimalProtocol(Protocol):
    def make_sound(self) -> None:
        pass

print(isinstance(Cat("Tom"), AnimalProtocol))  # ✅ True
print(isinstance(Dog("Pluto"), AnimalProtocol))  # ✅ True

def let_animal_sound(animal: AnimalProtocol): # Sirve para verificación estática de tipos
    animal.make_sound()

let_animal_sound(Cat("Tom"))
let_animal_sound(Dog("Pluto"))