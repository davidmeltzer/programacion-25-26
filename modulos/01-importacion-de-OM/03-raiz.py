# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: modulos/01-importacion-de-OM/03-raiz.py


"""
03-raiz.py
Script that imports and uses functions from utilidades_matematicas.
"""

# Importación de atributos específicos del módulo al contexto global de este módulo.
from utilidades_matematicas import add, multiply, PI

# La importación de arriba es equivalente a:
# import utilidades_matematicas
# add  = utilidades_matematicas.add
# multiply = utilidades_matematicas.multiply
# PI = utilidades_matematicas.PI
# del utilidades_matematicas

def main():
    x, y = 5, 3
    print(f"The sum of {x} and {y} is {add(x, y)}")
    print(f"The product of {x} and {y} is {multiply(x, y)}")
    print(f"The value of pi is approximately {PI}")
if __name__ == "__main__":
    main()
