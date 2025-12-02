import sys

nombre_ejecutable = sys.executable

def saludo():
    print(f"Hola desde modulo_A.py!")
    print(f"Ejecutable: {nombre_ejecutable}")
    print(f"__name__ en modulo_A.py: {__name__}")
    print(f"__file__ en modulo_A.py: {__file__}")