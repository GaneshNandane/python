# Defining the Student class
class Student:

    # Constructor used to initialize the object
    def __init__(self):
        # A single underscore indicates that this is a protected attribute
        self._name = "Harry"

    # A single underscore indicates that this is a protected method
    def _funName(self):
        return "CodeWithHarry"

# Defining the Subject class that inherits from the Student class
class Subject(Student):
    pass

# Creating an object of the Student class
obj = Student()

# Creating an object of the Subject class
obj1 = Subject()

# Accessing the protected attribute and method using the Student object
print(obj._name)
print(obj._funName())

# Accessing the inherited protected attribute and method using the Subject object
print(obj1._name)
print(obj1._funName())
