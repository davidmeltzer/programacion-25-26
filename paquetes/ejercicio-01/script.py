# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: ejercicio-01/script.py


# Construya un paquete llamado 'trigonometria' que:
#
# 1 .contenga un módulo llamado 'funciones.py'. En este módulo, 
# implemente las funciones seno, coseno y tangente de un argumento 
# en ángulos sexagesimales. Las funciones deben usar la librería 'math' de Python.
#
# 2. Debe contener una función interna llamada '_grados_a_radianes' que convierta
# ángulos de grados sexagesimales a radianes. Esta función debe ser utilizada
# por las funciones seno, coseno y tangente para realizar los cálculos.
#
# 3. El paquete debe incluir un archivo '__init__.py' que importe las funciones
# seno, coseno y tangente del módulo 'funciones.py', de modo que puedan ser
# accedidas directamente desde el paquete 'trigonometria'.
# 4. Finalmente, incluya un archivo '__main__.py' en el paquete que permita
# al usuario ejecutarlo con la opción -m e interactuar con las funciones del 
# paquete desde la línea de comandos. Al hacerlo debe mostrar un menú que 
# permita al usuario elegir una de las tres funciones y proporcionar el valor 
# del ángulo en grados sexagesimales. El programa debe calcular y mostrar el 
# resultado de la función trigonométrica seleccionada.

def hacer_pruebas():
    """Función para probar las funciones trigonométricas."""
    from trigonometria import seno, coseno, tangente
    print("Pruebas de funciones trigonométricas:")
    angulo = 45
    print(f"Seno de {angulo}°: {seno(angulo)}") # Debe ser aproximadamente 0.7071
    print(f"Coseno de {angulo}°: {coseno(angulo)}") # Debe ser aproximadamente 0.7071
    print(f"Tangente de {angulo}°: {tangente(angulo)}") # Debe ser aproximadamente 1.0

if __name__ == "__main__":
    hacer_pruebas()