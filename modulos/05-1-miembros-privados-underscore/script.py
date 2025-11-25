# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: modulos/05-1-miembros-privados-underscore/script.py


from modulo_A import *

print(var1)

try:
	print(_var2)
except NameError as e:
	print(f"Exception caught: {e}")

# Pero se puede acceder a _var2 con una importación explícita.

import modulo_A
print(modulo_A._var2)