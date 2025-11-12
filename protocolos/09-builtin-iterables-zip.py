# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: protocolos/09-builtin-iterables-zip.py


iterable_tuplas = zip( ('L', 'M', 'X', 'V', 'S', 'D'), ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo'] )

# Con un iterador explícito
print("\nUso con iterador explícito")
iterador = iter(iterable_tuplas)
terminado = False
while not terminado:
    try:
        elemento = next(iterador)
        print(elemento, " ", end='')
    except StopIteration:
        terminado = True

# Con un iterador implícito
print("\n\nUso con iterador implícito")
for elemento in iterable_tuplas:
    print(elemento, " ", end='')
print(f"¿Por qué no aparece la SECUENCIA ZIP en este caso?")

# ¿Qué ocurre aquí? ¿Por qué?
print("\n\nUn objeto iterable zip() devuelve siempre el mismo objeto iterador con cada invocación a iter()")
iterable_tuplas = zip( ('L', 'M', 'X', 'V', 'S', 'D'), ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo'] ) # Este es un nuevo objeto ZIP
print(f"{id(iterable_tuplas)=}")
iterador1 = iter(iterable_tuplas)
print(f"{id(iterador1)=}")
print(f"Primer elemento extraido con iterador1: {next(iterador1)=}")
print(f"Segundo elemento extraido con iterador1: {next(iterador1)=}")
iterador2 = iter(iterable_tuplas)
print(f"{id(iterador2)=}")
print(f"Primer elemento extraido con iterador2: {next(iterador2)=}")
print(f"Tercer elemento extraido con iterador1: {next(iterador1)=}")
print(f"{iterable_tuplas is iter(iterable_tuplas)=}")


# Hay constructores que admiten inicialización usando los elementos de un objeto iterable
lista = list( zip( ('L', 'M', 'X', 'V', 'S', 'D'), ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo'] ) )
print(f"\nLista inicializada con un objeto iterable zip(): {lista=}")
conjunto = set( zip( ('L', 'M', 'X', 'V', 'S', 'D'), ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo'] ) )
print(f"Conjunto inicializado con un objeto iterable ZIP(): {conjunto=}")
tupla = tuple( zip( ('L', 'M', 'X', 'V', 'S', 'D'), ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo'] ) )
print(f"Tupla inicializada con un objeto iterable ZIP(): {tupla=}")
diccionario = dict( zip( ('L', 'M', 'X', 'V', 'S', 'D'), ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo'] ) )
print(f"Diccionario inicializado con un objeto iterable ZIP(): {diccionario=}")