# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: modulos/03-objeto-de-modulo/script.py


print(f"__name__ en script.py: {__name__}") # '__main__' por ser script raíz.
print(f"__file__ en script.py: {__file__}")

import modulo_A

modulo_A.saludo()

print(f"Atributos de módulo_A:\n{ dir(modulo_A) }")
print(f"Atributos de script:\n{ dir() }")
