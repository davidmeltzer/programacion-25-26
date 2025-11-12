# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: protocolos/08-builtin-iterables-enumerate.py


enumeracion_valores = enumerate(['a', 'b', 'c', 'd', 'e']) # Este constructor acepta un iterable para su inicialización (ver documentación)

# Con un iterador explícito
print("\nUso con iterador explícito")
iterador = iter(enumeracion_valores)
terminado = False
while not terminado:
    try:
        elemento = next(iterador)
        print(elemento, " ", end='')
    except StopIteration:
        terminado = True

# Con un iterador implícito
print("\n\nUso con iterador implícito")
for elemento in enumeracion_valores:
    print(elemento, " ", end='')
print(f"¿Por qué no aparece la enumeración en este caso?")

# ¿Qué ocurre aquí? ¿Por qué?
print("\n\nUn objeto iterable enumerate() devuelve siempre el mismo objeto iterador con cada invocación a iter()")
enumeracion_valores = enumerate(['a', 'b', 'c', 'd', 'e']) # Este es un nuevo objeto enumerador
print(f"{id(enumeracion_valores)=}")
iterador1 = iter(enumeracion_valores)
print(f"{id(iterador1)=}")
print(f"Primer elemento extraido con iterador1: {next(iterador1)=}")
print(f"Segundo elemento extraido con iterador1: {next(iterador1)=}")
iterador2 = iter(enumeracion_valores)
print(f"{id(iterador2)=}")
print(f"Primer elemento extraido con iterador2: {next(iterador2)=}")
print(f"Tercer elemento extraido con iterador1: {next(iterador1)=}")
print(f"{enumeracion_valores is iter(enumeracion_valores)=}")


# Hay constructores que admiten inicialización usando los elementos de un objeto iterable
lista = list( enumerate(['a', 'b', 'c', 'd', 'e']) )
print(f"\nLista inicializada con un objeto iterable enumerate(): {lista=}")
conjunto = set( enumerate(['a', 'b', 'c', 'd', 'e']) )
print(f"Conjunto inicializado con un objeto iterable enumerate(): {conjunto=}")
tupla = tuple(enumerate( ['a', 'b', 'c', 'd', 'e']) )
print(f"Tupla inicializada con un objeto iterable enumerate(): {tupla=}")
diccionario = dict(enumerate( ['a', 'b', 'c', 'd', 'e']) )
print(f"Diccionario inicializado con un objeto iterable enumerate(): {diccionario=}")