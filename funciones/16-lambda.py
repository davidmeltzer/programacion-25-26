# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: funciones/16-lambda.py


# La definición de una función lleva asociada la instanciación de su objeto y
# la asignación de dicho objeto a una variable con el nombre de la función.
def f(a, b, c): 
    return a + b + c
print(f(1, 2, 3))
print()

# Al definir una función lambda, se crea un objeto función anónimo que se puede
# asignar a una variable.
g = lambda a, b, c: a + b + c
print(g(1, 2, 3))
print()

# Ejemplo de uso de lambda como función anónima.
var_iterable = [1, 2, 3, 4, 5]

# Uso de lambda como función anónima.
for elemento in map(lambda x: x * 2, var_iterable):
    print(elemento)
print()

resultado = list(map(lambda x: x * 2, var_iterable))
print(resultado)
print()

resultado = list(filter(lambda x: x % 2 != 0, var_iterable))
print(resultado)
print()

# Uso de lambda a traves de una variable.
f = lambda x: x ** 2
resultado = list(map(f, var_iterable))
print(resultado)
