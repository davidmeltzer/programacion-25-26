# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: modulos/01-importacion-de-OM/01-raiz.py


"""
01-raiz.py
Script that imports and uses functions from utilidades_matematicas.
"""

# Importación como "objeto módulo" con sus atributos
import utilidades_matematicas

def main():
    x, y = 5, 3
    print(f"The sum of {x} and {y} is {utilidades_matematicas.add(x, y)}")
    print(f"The product of {x} and {y} is {utilidades_matematicas.multiply(x, y)}")
    print(f"The value of pi is approximately {utilidades_matematicas.PI}")

if __name__ == "__main__":
    main()
