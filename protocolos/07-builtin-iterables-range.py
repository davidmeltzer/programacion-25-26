# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: protocolos/07-builtin-iterables-range.py


rango_valores = range(5)

# Con un iterador explícito
print("\nUso con iterador explícito")
iterador = iter(rango_valores)
terminado = False
while not terminado:
    try:
        elemento = next(iterador)
        print(elemento, " ", end='')
    except StopIteration:
        terminado = True

# Con un iterador implícito
print("\n\nUso con iterador implícito")
for elemento in rango_valores:
    print(elemento, " ", end='')

# ¿Qué ocurre aquí? ¿Por qué?
print("\n\nUn objeto iterable range() devuelve objeto iterador diferente con cada invocación a iter()")
iterador1 = iter(rango_valores)
print(f"Primer elemento extraido con iterador1: {next(iterador1)=}")
print(f"Segundo elemento extraido con iterador1: {next(iterador1)=}")
iterador2 = iter(rango_valores)
print(f"Primer elemento extraido con iterador2: {next(iterador2)=}")
print(f"Tercer elemento extraido con iterador1: {next(iterador1)=}")


# Hay constructores que admiten inicialización usando los elementos de un objeto iterable
lista = list(rango_valores)
print(f"\nLista inicializada con un objeto iterable range(): {lista=}")
conjunto = set(rango_valores)
print(f"Conjunto inicializado con un objeto iterable range(): {conjunto=}")
tupla = tuple(rango_valores)
print(f"Tupla inicializada con un objeto iterable range(): {tupla=}")