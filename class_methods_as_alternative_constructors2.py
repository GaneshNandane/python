# example of using a class method as an alternative constructor.
class Person:

    # Constructor to initialize the person's name and age.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Creating a Person object from a comma-separated string.
    @classmethod
    def from_string(cls, string):
        name, age = string.split(",")
        return cls(name.strip(), int(age))


# Creating a Person object using the class method.
person = Person.from_string("John Doe, 30")

print(person.name, person.age)
