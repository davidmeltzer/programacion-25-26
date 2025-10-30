# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: modelo_datos/04-hash.py


class Persona:
    def __init__(self, nombre, direccion, edad):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad

    def __hash__(self):
        return hash((self.nombre, self.direccion, self.edad)) # Combina los hashes de los atributos relevantes
    
    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Persona):
            return NotImplemented
        return (self.nombre, self.direccion, self.edad) == (other.nombre, other.direccion, other.edad)
    
    def __repr__(self):
        return f"Persona(nombre={self.nombre}, direccion={self.direccion}, edad={self.edad})"
    
persona1 = Persona("Ana", "Calle Falsa 123", 30)
persona2 = Persona("Benito", "Calle Fake 456", 33)

print(f"Hash de persona1: {hash(persona1)}")
print(f"Hash de persona2: {hash(persona2)}")

persona3 = Persona("Ana", "Calle Falsa 123", 30)  # mismo contenido que persona1 -> mismo hash
print(f"Hash de persona3: {hash(persona3)}")

personas = {persona1, persona2, persona3}
print(f"Conjunto resultante: {personas}")