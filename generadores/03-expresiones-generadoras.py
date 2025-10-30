# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: generadores/03-expresiones-generadoras.py


def mostrar_que_es(nombre, obj):
    print(f"Objeto: {nombre}")
    print(f"  Tipo: {type(obj)}")
    print(f"  Es iterable: {hasattr(obj, '__iter__')}")
    print(f"  Es un iterador: {hasattr(obj, '__next__')}")


expresion_generadora = (i ** 2 for i in range(5))

mostrar_que_es("Expresion generadora", expresion_generadora)

# Uso con iterador explícito

iterador = iter(expresion_generadora)
terminado = False
while not terminado:
    try:
        valor = next(iterador)
        print(f"Valor generado: {valor}")
    except StopIteration:
        terminado = True

print("La expresión generadora ha terminado su ejecución.")

# Uso con iterador implícito
for valor in expresion_generadora:
    print(f"Valor generado en bucle for: {valor}")

# Nota: En este caso, no se generarán más valores.
# ¿Por qué? Porque el iterador de una expresión generadora 
# es el propio objeto de la expresión generadora.

# Uso con iterador implícito con nuevo generador
for valor in (i ** 2 for i in range(5)):
    print(f"Valor generado en bucle for: {valor}")
