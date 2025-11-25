# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: modulos/06-uso-dual-__name__/modulo.py


def hola():
    print("Hola. Este módulo se ejecuta como script raíz.")

print(f"__name__ en modulo.py: '{__name__}'")

if __name__ == "__main__":
    hola()