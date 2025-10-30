# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: generadores/02-generadores-builtin.py


def mostrar_que_es(nombre, obj):
    print(f"Objeto: {nombre}")
    print(f"  Tipo: {type(obj)}")
    print(f"  Es iterable: {hasattr(obj, '__iter__')}")
    print(f"  Es un iterador: {hasattr(obj, '__next__')}")


mostrar_que_es('Una lista', [1, 2, 3])

un_rango = range(5)
mostrar_que_es('valor devuelto por range(5)', un_rango)

iterador = enumerate(['a', 'b', 'c'])
mostrar_que_es('valor devuelto por enumerate', iterador)
for indice, valor in iterador:
    print( (indice, valor))

iterador = zip(['a', 'b', 'c'], (1, 2, 3))
mostrar_que_es('valor devuelto por zip', iterador)
for tupla in iterador:
    print(tupla)