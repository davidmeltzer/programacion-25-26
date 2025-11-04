# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: anotaciones/03-union.py


def raiz(numero: int) -> int | complex: # >= 3.10
    if numero >= 0:
        return int(numero ** 0.5)
    else:
        return complex(0, (-numero) ** 0.5)
    
# Ejemplo con resultado int
resultado_entero = raiz(16)
print(f"raiz(16) = {resultado_entero}, tipo: {type(resultado_entero)}")

# Ejemplo con resultado complex
resultado_complejo = raiz(-9)
print(f"raiz(-9) = {resultado_complejo}, tipo: {type(resultado_complejo)}")