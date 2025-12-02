print("Hola desde paquete.__init__.py")

# Búsqueda SÓLO en el paquete actual.
from .modulo_A import * # Todos los atributos del objeto modulo_A
from .modulo_B import * # Todos los atributos del objeto modulo_B