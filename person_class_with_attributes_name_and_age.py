# Class representing a person
class Person:

    # Parameterized constructor used to initialize the name and age of a Person object.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Class method used as an alternative constructor. It creates a Person object from a single formatted string.
    @classmethod
    def from_string(cls, string):

        # Split the string into name and age
        name, age = string.split(", ")

        # Create and return a new Person object
        return cls(name, int(age))

# Create a Person object using the class method instead of calling the constructor directly.
person = Person.from_string("John Doe, 30")

# Print the object's attributes
print(person.name)
print(person.age)
