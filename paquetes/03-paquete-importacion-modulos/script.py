print(f"__name__ en script.py: {__name__}") # '__main__' por ser script raíz.
print(f"__file__ en script.py: {__file__}")

import paquete

paquete.get_nombre_ejecutable()
# Pero también se puede usar: paquete.modulo_A.get_nombre_ejecutable()
paquete.get_ssoo()
# Pero también se puede usar: paquete.modulo_B.get_ssoo()

print(f"Atributos de 'paquete':\n{ dir(paquete) }")
print(f"Atributos de script:\n{ dir() }")