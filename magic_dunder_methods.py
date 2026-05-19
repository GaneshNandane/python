# Magic or dunder methods are special methods that use
# double underscores before and after their names.
# These methods allow objects to behave like built-in Python objects.
# These methods are predefined in Python.

class Character:
    
    # __init__() is a magic method used as a constructor
    # to initialize object attributes.
    def __init__(self, name, power):
        self.name = name
        self.power = power

    # __add__() is a magic method used for operator overloading.
    # It defines the behavior of the + operator for objects.
    def __add__(self, other):
        return self.power + other.power

    # __str__() is a magic method that defines
    # how the object is displayed when printed.
    def __str__(self):
        return f"{self.name} has power {self.power}"


p1 = Character("josef", 39)
p2 = Character("jax", 50)

print(p1)
print(p1 + p2)
