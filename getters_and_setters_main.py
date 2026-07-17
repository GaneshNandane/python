# This class demonstrates the use of @property and @property.setter

class MyClass:

    # Constructor that initializes the object
    def __init__(self, value):
        self._value = value

    # Method to display the current value
    def show(self):
        print(f"Value is {self._value}")

    # Getter method for the property 'ten_value'
    @property
    def ten_value(self):
        # Returns 10 times the stored value
        return 10 * self._value

    # Setter method for the property 'ten_value'
    @ten_value.setter
    def ten_value(self, new_value):
        # Store one-tenth of the assigned value
        self._value = new_value / 10

# Create an object with initial value 10
obj = MyClass(10)

# Assign a value to the property
obj.ten_value = 67

# Print the property value
print(obj.ten_value)

# Display the stored value
obj.show()
