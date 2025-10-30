# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: funciones/01-funcion-retorno.py


def f(a, b, c):
    if(a + b + c) > 10:
        return a + b, b + c, a + c # Devuelve una tupla de 3 elementos.
    # Se termina sin return, lo que equivale a return None.


x, y, z = f(10, 20, 30)
print(x, y, z)

valor = f(1, 2, 3)
print(valor) # None

# Las funciones son objetos de tipo 'function'.
print(f"f es de tipo: {type(f)}")
print(f"f tiene los atributos: {dir(f)}")

import types # Se recomienda usar collection.ABC.Callable en lugar de types.FunctionType
print(f"f es instancia de 'types.FunctionType': {isinstance(f, types.FunctionType)}")
print(f"f es instancia de ABC.callable: {isinstance(f, callable)}")
print(f"f es una instancia callable: {callable(f)}")

import collections.abc
# Las funciones implementan el protocolo 'callable'.
# https://docs.python.org/3.13/library/collections.abc.html#collections-abstract-base-classes
print(f"f es una instancia de un objeto que implementa el protocolo callable: {isinstance(f, collections.abc.Callable)}")

print(f"f contiene el atributo (la función miembro) __call__: {'__call__' in dir(f)}")
print(f"f tiene el atributo __call__: {hasattr(f, '__call__')}")
