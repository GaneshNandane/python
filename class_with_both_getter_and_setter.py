# Demonstrating the use of the @property and @property.setter decorators.These decorators provide controlled access to an object's attributes by
# allowing getter and setter methods to be accessed like normal attributes.

class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

obj = MyClass(10)

# Updating the object's attribute using the setter.
obj.value = 20

# Accessing the updated attribute using the getter.
print(obj.value)
