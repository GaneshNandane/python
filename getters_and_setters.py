# getters and setters are the two methods to get the values from the private variables of the class variables we can access this variables using getters and in setters we can modify that variables values 
# as you can see that we are defining the value at the object creation to the class's private variable and then imidiatelly printing that value to show the user that in the place of that variable there is this value that are present now 
# after that we are again defining the value at the same variable using setter 
# then we can access that value using getter using the @property decorator 
class value_operation:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
       
obj = value_operation(10)
print(obj.value)
obj.value = 20
print(obj.value)
