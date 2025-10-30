# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: modelo_datos/05-getattribute.py


class SecureData:
    def __init__(self):
        self.public = "Public Info"
        self._secret = "Sensitive Data"

    def __getattribute__(self, name): # Se ejecuta cada vez que se accede a un atributo
        if name.startswith("_"):
            raise AttributeError(f"Access to private attribute '{name}' is denied")
        return object.__getattribute__(self, name) # Equivalente a: return super().__getattribute__(name)
    
    def _do_something_private(self):
        return "Doing something private"

obj = SecureData()

print(obj.public)     # ✅ Se obtiene el valor del atributo
# print(obj._secret)    # ❌ Se deniega el acceso al atributo privado y se arroja AttributeError
# print(obj._do_something_private())  # ❌ Se deniega el acceso al método privado y se arroja AttributeError
