# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: funciones/09-kwargs-unpacking.py


def mostrar_info(nombre, ciudad, edad=20):
    print(f"{nombre=}, {ciudad=}, {edad=}")

# Esto es un diccionario.
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}
print(f"type(persona): {type(persona)}")

mostrar_info(**persona)

persona = dict(nombre="Luis", ciudad="Barcelona")
print(f"type(persona): {type(persona)}")

mostrar_info(**persona)
