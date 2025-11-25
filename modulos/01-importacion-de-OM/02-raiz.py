# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: modulos/01-importacion-de-OM/02-raiz.py


"""
01-raiz.py
Script that imports and uses functions from utilidades_matematicas.
"""

# Importación como "objeto módulo" con sus atributos.
# Se usa un alias para el objeto módulo.
import utilidades_matematicas as um

def main():
    x, y = 5, 3
    print(f"The sum of {x} and {y} is {um.add(x, y)}")
    print(f"The product of {x} and {y} is {um.multiply(x, y)}")
    print(f"The value of pi is approximately {um.PI}")

if __name__ == "__main__":
    main()
