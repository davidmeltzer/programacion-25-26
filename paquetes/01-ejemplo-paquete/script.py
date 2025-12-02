print(f"__name__ en script.py: {__name__}") # '__main__' por ser script raíz.
print(f"__file__ en script.py: {__file__}")

import paquete.modulo_A

paquete.modulo_A.saludo()

print(f"Atributos de 'paquete':\n{ dir(paquete) }")
print(f"Atributos de script:\n{ dir() }")