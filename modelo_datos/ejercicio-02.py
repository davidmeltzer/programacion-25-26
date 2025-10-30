# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: modelo_datos/ejercicio-02.py


# Dada la codificación incial de la clase Dato, 
# añada lo que sea necesario para que cada vez que se le el valor de
# 'valor' se incremente en uno un contador de lecturas.
# Ver: 
# https://docs.python.org/3.13/reference/datamodel.html#object.__getattribute__

class Dato:
    def __init__(self, valor):
        self.valor = valor
        self.contador = 0
        
    def __getattribute__(self, name):
        # 👉 your code here
        pass

un_dato = Dato('hola')

print(f"Valor inicial: '{un_dato.valor}', contador: {un_dato.contador}")
print(f"        Valor: '{un_dato.valor}', contador: {un_dato.contador}")
un_dato.valor = 'adios'
print(f"  Valor final: '{un_dato.valor}', contador: {un_dato.contador}")

