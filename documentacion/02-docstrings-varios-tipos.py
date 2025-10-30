# Programación - Doble Grado en Ingeniería y Sistemas de Datos e Ingeniería Telemática
# Programación Multiparadigma para Sistemas de Datos – Grados en Ingeniería de Telecomunicación
# 2025/2026
# Archivo: documentacion/02-docstrings-varios-tipos.py


def greet(name):
    """
    Greet a person by name.

    Parameters:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting message that includes the person's name.

    """
    return f"Hello, {name}!"

class Person:
    r'''
    A simple class to represent a person.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
    Esta es una raw string, por lo que las barras invertidas se interpretan literalmente.
    \Las \barras \invertidas \son \literales\
    '''
 
    def __init__(self, name, age):
        '''
        Initialize a new Person instance.

        Parameters:
            name (str): The person's name.
            age (int): The person's age.
        Esta es una cadena en la que las barras invertidas\nse interpretan como caracteres de escape.
        '''
        self.name = name
        self.age = age

    def introduce(self):
        """
        Return a short introduction message.

        Returns:
            str: A message introducing the person.
        """
        return f"My name is {self.name}, and I am {self.age} years old."
    
    def do_nothing(self):
        "This method does nothing and returns None." # Sólo para docstrings de una línea.
        pass

# Inspección de docstrings usando __doc__
# print(greet.__doc__)
# print(Person.__doc__)
# print(Person.__init__.__doc__)
# print(Person.introduce.__doc__)

# Inspección de docstrings usando help()
# help(greet)
# help(Person)
help(Person.__init__)
# help(Person.introduce)
