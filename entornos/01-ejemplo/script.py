import requests
from PIL import Image

# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: entornos/01-ejemplo.py


DOODLE_URL = "https://www.google.com/logos/doodles/2025/seasonal-holidays-2025-6753651837110711.2-law.gif"

# Descargar el doodle
response = requests.get(DOODLE_URL)
response.raise_for_status()

with open("doodle.gif", "wb") as file:
    file.write(response.content)

print("Doodle descargado correctamente como 'doodle.gif'")

# Visualizar el doodle con la aplicación por defecto del sistema
img = Image.open("doodle.gif")
img.show()