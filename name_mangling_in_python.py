# Define a class named MyClass
class MyClass:

    # Constructor that initializes the object's attributes
    def __init__(self):

        # Protected attribute (by convention)
        # A single underscore (_) indicates that this attribute is intended
        # for internal use, but it can still be accessed from outside the class.
        self._nonmangled_attribute = "I am a nonmangled attribute"

        # Private attribute using name mangling
        # A double underscore (__) tells Python to mangle the attribute name
        # to reduce the chance of accidental access or modification.
        self.__mangled_attribute = "I am a mangled attribute"

# Create an object of MyClass
my_object = MyClass()

# Access the protected attribute
# This works because protected attributes are only a naming convention.
print(my_object._nonmangled_attribute)
# Output: I am a nonmangled attribute

# Try to access the private (mangled) attribute directly
# This raises an AttributeError because Python changes its internal name.
print(my_object.__mangled_attribute)
# Output:
# AttributeError: 'MyClass' object has no attribute '__mangled_attribute'

# Access the mangled attribute using its internal name
# Python internally renames __mangled_attribute to _MyClass__mangled_attribute.
print(my_object._MyClass__mangled_attribute)
# Output: I am a mangled attribute
