# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: modulos/05-2-miembros-privados-__all__/script.py


from modulo_A import *

print(var1)

try:
	print(var2)
except NameError as e:
	print(f"Exception caught: {e}")

# Pero se puede acceder a var2 con una importación explícita.

import modulo_A
print(modulo_A.var2)