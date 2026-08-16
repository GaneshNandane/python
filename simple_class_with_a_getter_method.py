# Simple program to demonstrate the use of the @property decorator

# Define a class
class MyClass:

    # Initialize the object with a value
    def __init__(self, value):

        # Store the value in the _value attribute
        self._value = value

    # Use the @property decorator to access the value method like an attribute
    @property
    def value(self):

        # Return the value stored in the _value attribute
        return self._value

# Create an object of MyClass and pass 10 as the value
obj = MyClass(10)

# Access the value property and display the stored value
print(obj.value)
