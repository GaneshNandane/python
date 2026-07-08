class Person:
    """
    A class to represent a person.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        version (int): The version number of the object.
    """

    def __init__(self, name, age):
        """
        Initializes a Person object.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
        """
        self.name = name
        self.age = age
        self.version = 1


P = Person("John", 30)

print(P.__dict__)
help(Person)
