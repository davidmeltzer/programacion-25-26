# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: protocolos/ejercicio-02.py


# Create a class WordCollection that stores a list of words and behaves like a sequence.
# Requirements
# - Must implement __len__ and __getitem__.
# - len(obj) returns the number of words.
# - Iteration (for word in obj) must work.
# - Indexing (e.g., obj[0]) returns the word at that index.

from collections.abc import Sequence

class WordCollection(Sequence):
    def __init__(self, words):
        self.words = words
    # Implement __len__ and __getitem__
    # 👉 your code here

wc = WordCollection(["apple", "banana", "cherry"])
assert len(wc) == 3
assert wc[1] == "banana"
assert list(wc) == ["apple", "banana", "cherry"]
print("✅ Ejecución terminada.")